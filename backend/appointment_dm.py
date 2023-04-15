""" appointment_data_manager.py - A data manager for interacting with appointments
Author: Jessica Weeks
"""
from datetime import timedelta, date, time
import datetime
from sqlalchemy.orm import joinedload
import sqlalchemy as sa
from sqlalchemy.sql.expression import bindparam
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

        ### Make sure appt_date is not before today

        if appt_date < datetime.datetime.now().date():
            raise ValueError("Appoinment date cannot be before today's date")

        avaliable_appointments = []

        ### First We Check if the Location is open ###

        hours = self.__get_hours_for(appt_date, location)

        # This means they are closed
        if hours.OpenTime is None:
            return avaliable_appointments

        ### Then We check if the employee is out ###

        events = self.__get_events_for(provider, appt_date)

        # This means they are out!
        if events is not None:
            return avaliable_appointments


        ### Next we get every appointment and place them into a dictionary with their length ###

        taken_appointment_statuses = ["Scheduled", "In Progress"]

        taken_appointments = self.session.query(Appointment)\
            .options(joinedload(Appointment.AppointmentType))\
            .filter(
            sa.and_(
                Appointment.AppDate == appt_date,
                Appointment.ProviderID == provider,
                Appointment.ApptStatus.in_(taken_appointment_statuses)
                )
            ).all()

        # Will be appointment_start_time, appointment_length (time delta)
        taken_appointment_times_dict = {}

        for taken_appt in taken_appointments:

            taken_appt_start = taken_appt.ApptTime
            taken_appt_length = taken_appt.ApptLength

            taken_appointment_times_dict[
                datetime.time(taken_appt_start)] = timedelta(taken_appt_length)



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
                taken_appt_start = datetime.datetime.combine(
                    datetime.datetime.today(), taken_appointment)
                # Our discionary contains timedeltas as the apopintment length
                taken_appt_end = taken_appt_start + taken_appt_length


                # We first check if the appt_start is inbetween this taken_appointment
                # Then we check if the appt_end is inbetween this taken_appointment
                if (((appt_start >= taken_appt_start) and (appt_start < taken_appt_end)) or
                    ((appt_end > taken_appt_end) and (appt_end < taken_appt_end))):
                    # If it is in between it means we can't use this time!
                    # We must skip ahead to the end of this appointment to look for more times!
                    search_datetime = taken_appt_end
                    break

            else:
                # This activates if the for loop doesn't break!
                # This means our search_datetime didn't interfer with any appointments!
                avaliable_appointments_times.append(search_datetime)
                # Now we must skip ahead to look for more times!
                search_datetime += appt_length


        # Alrighty! Now we have a list of appointment times that are free!
        # Now to just make a bunch of objects using them

        for appt_time in avaliable_appointments_times:
            avaliable_appointments.append(
                Appointment(
                    ApptDate=appt_date,
                    ApptTime=appt_time,
                    PatientID=patient.PatientID,
                    ApptStatus="Scheduled",
                    ApptLength=appt_length,
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

        return avaliable_appointments


    def set_appointment_time(self, appt:Appointment,
                                   new_time:time,
                                   new_date:date,
                                   custom_time:bool=None):
        """
            Sets the appointment time and date to the given values if they are available.

            :param appt: An Appointment object representing the appointment to update.
            :param new_time: A time object from the datetime library representing the new appt time
            :param new_date: A date object from the datetime library represetning the new appt date
            :param custom_time: A boolean flag if this was a user customized time

            :raises AssertionError: If appt not avaliable, display this to the user

            :return: None
        """

        self.__check_appointment_available(appt, new_time, new_date, custom_time)

        stmt = sa.update(Appointment)\
            .where(Appointment.AppointmentID == appt.AppointmentID)\
            .values(ApptTime=new_time, ApptDate=new_date)
        self.session.execute(stmt)
        self.session.commit()

    def add_appointment(self, appt: Appointment, custom_time=None):
        """
            Adds an appointment to the database if the requested time is available

            :param appt: An Appointment object representing the appointment to add
            :param custom_time: A boolean flag if this was a user customized time

            :raises AssertionError: If appt not avaliable, display this to the user
        """
        self.__check_appointment_available(appt, custom_time=custom_time)

        self.session.add(appt)
        self.session.commit()

    def get_appointment_types(self) -> list[AppointmentType]:
        """
            Returns a list of all appointment types

            :return: A list of AppointmentType objects representing all appointment types
        """
        return self.session.query(AppointmentType).all()

    def get_appointments_for_date(self, check_date: date) -> list[Appointment]:
        """
            Returns a list of appointments scheduled for the given date.

            :param check_date: date object from the datetime library representing the date to check

            :return: A list of Appointment objects for the given date
        """
        return self.session.query(Appointment)\
            .filter_by(ApptDate = check_date)\
            .order_by(Appointment.ApptTime)\
            .all()

    def __check_appointment_available(self, appt: Appointment,
                                            new_time:time=None,
                                            new_date:date=None,
                                            custom_time:bool=None) -> bool:
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

        if new_date:
            appt.ApptDate = new_date



        ### First We check if there are any taken appointments ###

        appt_end_time = (datetime.datetime.combine(date=appt.ApptDate, time=appt.ApptTime) + timedelta(minutes= appt.ApptLength)).time()

        appt.ApptLength = time(0, appt.ApptLength)

        taken_appointment_statuses = ["Scheduled", "In Progress"]
        taken_appointments = self.session.query(Appointment).\
            options(joinedload(Appointment.AppointmentType)).\
            filter(
                sa.and_(
                    Appointment.ApptDate == appt.ApptDate,
                    Appointment.PhysicianID == appt.PhysicianID,
                    Appointment.ApptStatus.in_(taken_appointment_statuses),
                    sa.or_( 
                        # Check if the appointment start time is in between an existing appointment
                        sa.and_(Appointment.ApptTime <= appt.ApptTime, Appointment.EndTime(self=Appointment, date=Appointment.ApptDate, time=Appointment.ApptTime) > appt.ApptTime),
                        # Check if the existing Boolean value of this clause is not definedappointment start time is in between the new appointment
                        sa.and_(Appointment.ApptTime >= appt.ApptTime, appt_end_time > Appointment.ApptTime)
                    )
                )
            ).all()

        assert taken_appointments is None, "Appointment Already Taken!"
        print("No Taken Appointments")

        ### Then We pull the hours for the location and day ###

        hours = self.__get_hours_for(appt.ApptDate, appt.Location)

        ### Then we tell if the location is closed ###

        assert hours.OpenTime is not None, "This Location is closed that day!"

        # Checks if its outside the hours of the location
        if (hours.OpenTime > appt.ApptTime or hours.CloseTime < appt.ApptTime):
            assert custom_time, "Outside this locations hours. Use custom time"

        ### Then we check if the physician is out, or if the entire clinic is out ###
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

        print(week_number)
        hours =  self.session.query(HospitalHours).filter(
            sa.and_(
                HospitalHours.LocationID == location.LocationID,

                # Checks if Day of weeks Matches
                HospitalHours.DayOfWeek == check_date.strftime("%A"),

                # Check if the week_number matches, if needed
                (HospitalHours.WeekNumber == week_number | (HospitalHours.WeekNumber.is_(None)))
            )
        ).first()

        return hours

    def __get_events_for(self, employee: Employee, check_date: date) -> Event:
        """ Get if an employee has an event on a certain date """
        events = self.session.query(Event)\
                    .filter(
                       sa.or_(Event.EmployeeID == employee.EmployeeID, Event.EmployeeID.is_(None)),
                       Event.StartDate <= check_date, # Check if its after start date
                       Event.EndDate >= check_date, # Check if its before end date
                    ).first()
        return events

    def __get_week_number(self, check_date:date):
        """ 
        A private method to get what week number it is 
        
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
    from backend.user_dm import UserDM
    from backend.misc_dm import MiscDM

    appt_dm = AppointmentDM()
    user_dm = UserDM()
    misc_dm = MiscDM()

    me = user_dm.get_patient("Jessica", "Weeks", date(2000,2,17))
    my_physician = user_dm.get_physicians()
    my_appointment_type = appt_dm.get_appointment_types()
    my_location = misc_dm.get_locations()

    me = me[0]
    my_physician= my_physician[0]
    my_appointment_type = my_appointment_type[0]
    my_location = my_location[0]

    appt = Appointment(
        ApptDate=datetime.datetime.now().date(),
        ApptTime=time(13,30),
        PatientID=me.PatientID,
        ApptStatus="Scheduled",
        ApptLength=15,
        PhysicianID = my_physician.EmployeeID,
        ApptTypeID=my_appointment_type.ApptTypeID,
        LocationID=my_location.LocationID,
        ApptReason="Can't Stop Dancing!",

        Patient = me,
        Employee = my_physician,
        AppointmentType = my_appointment_type,
        Location = my_location
    )
    
    appt_dm.add_appointment(
        appt
    )

    list_of_obj = appt_dm.get_appointments_for_date(datetime.datetime.now().date())
    
    for i in list_of_obj:
        print(i)

