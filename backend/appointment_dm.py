""" appointment_data_manager.py - A data manager for interacting with appointments
Author: Jessica Weeks
"""
from datetime import timedelta, date, time
import datetime
from sqlalchemy.orm import joinedload, object_session
import sqlalchemy as sa
from backend.models import HospitalHours, AppointmentType, Appointment,\
                    Employee, Location, Event, Patient
from backend.private.appointment_status_data_manger import AppointmentStatusDataManger


class AppointmentDM(AppointmentStatusDataManger):
    """
        A DataManager for modifying, adding and reading appointments. 

        • Get Avaliable Appointments
        • Set Appointment Time
        • Add Appointment
        • Get Appointment Types
        • Get Appointments for date
    """
    def __init__(self):
        super().__init__()

    def get_avaliable_appointments(self,
                               appt_date: date,
                               provider: Employee,
                               location: Location,
                               appt_type: AppointmentType,
                               appt_length: timedelta,
                               patient: Patient,
                               appt_reason: str) -> list[Appointment]:
        """
            Returns a list of available appointment times for the given 
            date, provider, location, appointment type, patient, and visit reason.

            :param appt_date: A date object from the datetime library represetning the appt date
            :param provider: A Employee object represetning the provider
            :param location: A Location object, where the appt will be
            :param appt_type: A AppointmentType object, what type of appointment
            :param appt_length: The Appointments Length
            :param patient: A Patient object, who will have the appointment
            :param visit_reason: A str representing the reason for the appointment.

            :return: A list of Appointment objects representing the available appointment times.
        """

        avaliable_appointments = []

        ### Make sure appt_date is not before today
        assert appt_date >= datetime.datetime.now().date(), ("Appoinment date cannot be before today's date")

        hours = self.__get_hours_for(appt_date, location)

        events = self.__get_events_for(provider, appt_date)

        ### Now we need to do some db queries ###

        with self.session_scope() as session:
                        
            ### First We Check if the Location is open ###

            session.add(hours)
            assert hours.OpenTime is not None, "Clinic is closed on this day"

            ### Then We check if the employee is out ###
            
            if object_session(provider) is None: # The provider is not in a session
                session.add(provider) # Sometimes when this is run the provider is already in a session

            if events:
                session.add(events)
                if events.EmployeeID == provider.EmployeeID: # The employee is out is out
                    raise AssertionError(f"This Physician is out for {events.EventName}")
                else: # Whole office is out
                    raise AssertionError(f"This clinic is closed for {events.EventName}")

            taken_appointment_statuses = ["Scheduled", "In Progress", "Rescheduled"]

            taken_appointments = session.query(Appointment)\
                .options(joinedload(Appointment.AppointmentType))\
                .filter(
                sa.and_(
                    Appointment.ApptDate == appt_date,
                    Appointment.PhysicianID == provider.EmployeeID,
                    Appointment.ApptStatus.in_(taken_appointment_statuses)
                    )
                ).all()
            session.expunge_all()

            # Will be appointment_start_time, appointment_length (time delta)
            taken_appointment_times_dict = {}

            for taken_appt in taken_appointments:

                taken_start = taken_appt.ApptTime
                
                start = taken_appt.ApptTime
                end = taken_appt.ApptEndtime
                
                # If goes over midnight
                if end < start:
                    end += timedelta(days=1)
                
                taken_appt_length = datetime.datetime.combine(datetime.datetime.min, end) -\
                datetime.datetime.combine(datetime.datetime.min, start)
                taken_appointment_times_dict[taken_start] = taken_appt_length



            ### Now we have everything we need ###



            # Ok, This is the hard part.
            # We use a counter (search_datetime) to loop through our start and end time
            # Think of search_datetime as a time, 9:00
            # First we check if a appointment intersects with our search_datetime and the end_time
            # Think of the search_datetime as a appointment, i.e 9:00 - 9:15
            # If thre is appointment intersects with that range, i.e 9:10-9:20, we can't use it
            # Our counter would then skip to 9:20, and check if we can make an appointment there
            # If we can make an appointment at 9:20, then we add that to our avaliable_appointments!
            # The counter would then skip from 9:20 to 9:35 (It would add the appt_length)

            # datetimes are required to add and subtract times
            search_datetime = datetime.datetime.combine(datetime.datetime.today(), hours.OpenTime)
            end_search_datetime = datetime.datetime.combine(datetime.datetime.today(), hours.CloseTime)

            avaliable_appointments_times = []

            while search_datetime < end_search_datetime:

                # For readability
                appt_start = search_datetime
                appt_end = appt_start + appt_length

                # We loop through our list of taken appointment times
                for taken_appointment, taken_appt_length in taken_appointment_times_dict.items():
                    # Converting appointment to datetime so we can compare using timedelta
                    taken_start = datetime.datetime.combine(datetime.datetime.today(), taken_appointment)
                    # Our discionary contains timedeltas as the apopintment length
                    taken_end = taken_start + taken_appt_length



                    # Check if there is a intersection
                    if ((appt_start < taken_end and appt_end > taken_start) or 
                        (taken_start < appt_end and taken_end > appt_start)):

                        # If it is in between it means we can't use this time!
                        # We must skip ahead to the end of this appointment to look for more times!
                        search_datetime = taken_end
                        break

                else:
                    # This activates if the for loop doesn't break!
                    # This means our search_datetime didn't interfer with any appointments!
                    avaliable_appointments_times.append(search_datetime)
                    # Now we must skip ahead to look for more times!
                    search_datetime += appt_length

            # Alrighty! Now we have a list of appointment times that are free!
            # Now to just make a bunch of objects using them
        with self.session_scope() as session:
            
            if object_session(provider) is None: # The provider is not in a session
                session.add(provider)
                session.add(location)
                session.add(patient)
                session.add(appt_type)
            
            for appt_time in avaliable_appointments_times:
                appt_endtime = (appt_time + appt_length).time()

                appt_time = appt_time.time()
                

                avaliable_appointments.append(Appointment(
                        ApptDate=appt_date,
                        ApptTime=appt_time,
                        PatientID=patient.PatientID,
                        ApptStatus="Scheduled",
                        ApptEndtime=appt_endtime,
                        PhysicianID=provider.EmployeeID,
                        ApptTypeID=appt_type.ApptTypeID,
                        LocationID = location.LocationID,
                        ApptReason=appt_reason,

                        Patient=patient,
                        AppointmentType=appt_type,
                        Employee=provider,
                        Location=location
                    )
                )

            patient_name = str(patient)

            for appt in avaliable_appointments:
                appt.patient_name = patient_name

            session.expunge_all()

            assert len(avaliable_appointments) > 0, "No appointments Avaliable on" + appt_date.strftime("%m/%d/%Y")

            return  avaliable_appointments


    def remove_appointment(self, appt:Appointment):
        """
            Removes a apopintment 

            :param appt: Appointment model to remove
        """
        with self.session_scope() as session:
            session.add(appt)
            session.delete(appt)

    def add_appointment(self, appt: Appointment, custom_time=None):
        """
            Adds an appointment to the database if the requested time is available

            :param appt: An Appointment object representing the appointment to add
            :param custom_time: A boolean flag if this was a user customized time

            :raises AssertionError: If appt not avaliable, display this to the user
        """
        self.check_appointment_available(appt, custom_time=custom_time)
        
        with self.session_scope() as session:
            session.merge(appt)
            session.commit()

    def get_appointment_types(self) -> list[AppointmentType]:
        """
            Returns a list of all appointment types

            :return: A list of AppointmentType objects representing all appointment types
        """
        with self.session_scope() as session:
            types = session.query(AppointmentType).all()
            session.expunge_all()
            return types

    def get_appointments_for_date(self, check_date: date, physician: Employee) -> list[Appointment]:
        """
            Returns a list of appointments scheduled for the given date.

            :param check_date: date object from the datetime library representing the date to check

            :return: A list of Appointment objects for the given date
        """
        with self.session_scope() as session:
            session.add(physician)
            appointments = session.query(Appointment)\
                .options(joinedload(Appointment.Patient))\
                .filter(Appointment.ApptDate == check_date,
                        Appointment.PhysicianID == physician.EmployeeID,
                        Appointment.ApptStatus.in_(["Scheduled", "Rescheduled"]))\
                .order_by(Appointment.ApptTime)\
                .all()
            
            for appt in appointments:
                appt.patient_name = str(appt.Patient)
                session.expunge(appt)
            return appointments

    def get_appointments_for_reschedule(self, appt: Appointment, check_date: date):
        with self.session_scope() as session:
            # We need to refresh our apopintment data
            session.add(appt)

            appt_start_datetime = datetime.datetime.combine(date.today(), appt.ApptTime)
            appt_end_datetime = datetime.datetime.combine(date.today(), appt.ApptEndtime)

            appt_length = appt_end_datetime - appt_start_datetime

            available_times = self.get_avaliable_appointments(
                appt_date = check_date,
                provider = appt.Employee,
                location = appt.Location,
                appt_type = appt.AppointmentType,
                appt_length = appt_length,
                appt_reason= appt.ApptReason,
                patient = appt.Patient
            )

            session.expunge_all()
            return available_times

    def check_appointment_available(self, appt: Appointment,
                                            new_time:time=None,
                                            new_date:date=None,
                                            custom_time:bool=None,
                                            length: timedelta=None) -> bool:
        """
            Check if a given appointment is available at a specific time and date.
            Will output a AssertionError if there is a issue with the check
            NOTE This function does 3 SQL queries in total. This function is not to be used on mass

            :param appt: The Appointment object to check availability for.
            :param new_time: The time to check availability for (by default its ApptTime)
            :param new_date: The date to check availability for (by default its ApptDate)
            :param custom_time: If True, the appointment time can be outside business hours

            :return: True if the appointment is available, raises AssertionError otherwise.
        """
        if new_time:
            appt.ApptTime = new_time
            
            new_time_delta = datetime.datetime.combine( date.today(), new_time)
            appt.ApptEndtime = new_time_delta + length

        if new_date:
            appt.ApptDate = new_date

        with self.session_scope() as session:
            session.add(appt)

            location = appt.Location
            employee = appt.Employee
            session.expunge_all()

        with self.session_scope() as session:
            ### First We check if there are any taken appointments ###

            taken_appointment_statuses = ["Scheduled", "In Progress", "Rescheduled"]
            taken_appointments = session.query(Appointment).\
                options(joinedload(Appointment.AppointmentType)).\
                filter(
                    sa.and_(
                        Appointment.ApptDate == appt.ApptDate,
                        Appointment.PhysicianID == appt.PhysicianID,
                        Appointment.ApptStatus.in_(taken_appointment_statuses),
                        sa.or_( 
                            # Check if the appointment start time is in between an existing appointment
                            sa.and_(Appointment.ApptTime <= appt.ApptTime,
                                    Appointment.ApptEndtime > appt.ApptTime),
                            # Check if the existing Boolean value of this clause is not definedappointment start time is in between the new appointment
                            sa.and_(Appointment.ApptTime >= appt.ApptTime,
                                    appt.ApptEndtime > Appointment.ApptTime)
                        )
                    )
                ).all()

            assert len(taken_appointments) == 0, "Appointment Already Taken!"

            ### Then We pull the hours for the location and day ###
            session.add(location)
            hours = self.__get_hours_for(appt.ApptDate, location)

            ### Then we tell if the location is closed ###

            assert hours.OpenTime is not None, "This Location is closed that day!"

            # Checks if its outside the hours of the location
            if (hours.OpenTime > appt.ApptTime or hours.CloseTime < appt.ApptTime):
                assert custom_time, "Outside this locations hours. Use custom time"

            ### Then we check if the physician is out, or if the entire clinic is out ###

            session.add(employee)
            events = self.__get_events_for(appt.Employee, appt.ApptDate)

            if events is not None:

                if events.EmployeeID == appt.PhysicianID: # The employee is out is out
                    raise AssertionError("This Physician is out on this day")
                else:
                    raise AssertionError("This clinic is closed for: ", events.EventName)


            # Everything above is asserted. We wont get here without errors unless its true
            return True

    def __get_hours_for(self, check_date: date, location: Location) -> HospitalHours:
        """ Gets hours for a given check_date & location object """
        # In the DB its either "Week1" or "Week2"
        week_number = self.__get_week_number(check_date)

        with self.session_scope() as session:
            if object_session(location) is None:
                session.add(location)
            hours =  session.query(HospitalHours).filter(
                sa.and_(
                    HospitalHours.LocationID == location.LocationID,

                    # Checks if Day of weeks Matches
                    HospitalHours.DayOfWeek == check_date.strftime("%A"),

                    # Check if the week_number matches, if needed
                    sa.or_(HospitalHours.WeekNumber == week_number,(HospitalHours.WeekNumber.is_(None)))
                )
            ).first()
            session.expunge_all()
            return hours

    def __get_events_for(self, employee: Employee, check_date: date) -> Event:
        """ Get if an employee has an event on a certain date """
        
        with self.session_scope() as session:
            if object_session(employee) is None:
                session.add(employee)
            events = session.query(Event)\
                        .filter(
                        sa.or_(Event.EmployeeID == employee.EmployeeID, Event.EmployeeID.is_(None)),
                        Event.StartDate <= check_date, # Check if its after start date
                        Event.EndDate >= check_date, # Check if its before end date
                        ).first()
            return events

    def __get_week_number(self, check_date:date):
        """ 
        A private method to get what week number it is for the db schedule
        
        It's a little jank.
        It checks how many weeks it has been since the first Sunday of 2015
        It then modulo's that number by 2, now each week will either be week 1 or week 2
        This insures no repeating weeks.

        If clinic ever chooses to add more weeks to their repeating schedule, chagne the constant
        """
        number_of_weeks = 2

        start_date = datetime.datetime(2015, 1, 4)
        end_date = datetime.datetime.combine(check_date, time(0,0,0))

        weeks_since_2015 = (end_date - start_date).days // 7

        week_number = weeks_since_2015 % number_of_weeks + 1

        return week_number

if __name__ == "__main__":
    # Used for debugging
    pass
