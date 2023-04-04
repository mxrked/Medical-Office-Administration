from data_manager import *
from data_manager import HospitalHours, AppointmentType, Appointment
from sqlalchemy.orm import joinedload
from datetime import timedelta

class AppointmentDataManger(DataManger):

    def __init__(self):
        super().__init__()

    def get_avaliable_appointments(self,
                               date: date,
                               provider: Employee,
                               location: HospitalLocation,
                               appointment_length: timedelta) -> list[Appointment]:
    # Be sure to check if the provider is on Vacation (in event table)
    # Be sure to check if the Location is closed (Check event table & HospitalHours table)
    # Be Sure to check if its the weekend (might be in HospitalHours?)
    # CHECK EVERYTHING
    # Also when generating a list of taken_appointments, be SURE not to include "pending", "no show" & "canceled" appointments
    # Also times should incriment by appointment_length.
    # I have a demo here on how to find possible times https://pastebin.com/vfvF0KD6 - Jess
        pass

    def set_appointment_time(self, appt: Appointment, new_time:time, new_date:date, custom_time:bool):
        
        assert self.__check_appointment_available(appt, new_time, new_date, custom_time), "Appointment time not available"

        stmt = sa.update(Appointment)\
            .where(Appointment.AppointmentID == appt.AppointmentID)\
            .values(ApptTime=new_time, ApptDate=new_date)
        self.session.execute(stmt)
        self.session.commit()

    def add_appointment(self, appt: Appointment, custom_time):

        assert self.__check_appointment_available(appt, custom_time=custom_time), "Appointment time not available"
        self.session.add(appt)
        self.session.commit()

    def get_appointment_types(self, search_text: String) -> list[AppointmentType]:
        return self.session.query(AppointmentType)\
            .filter(AppointmentType.ApptName\
            .like(f'%{search_text}%'))\
            .all()

    def get_appointments_for_date(self, date: date) -> list[Appointment]: # Check Reschedule/Canceling appointment screen first
        return self.session.query(Appointment)\
            .filter_by(ApptDate = date)\
            .order_by(Appointment.ApptTime)\
            .all()

    def __check_appointment_available(self, appt: Appointment, new_time:time=None, new_date:date=None, custom_time:bool=None) -> bool:
        
        appt.ApptDate = new_date
        appt.ApptTime = new_time
        

        ### First We check if there are any taken appointments ### 

        appt_end_time = appt.ApptTime + timedelta(minutes= appt.AppointmentType.ApptLength)
        
        # Used to finding the end time of a appointment in the DB
        appointment_end_time = Appointment.ApptTime + timedelta(minutes=Appointment.AppointmentType.ApptLength)
        
        is_appointment_time_conflicted = (
             # Check if the appointment start time is in between an existing appointment
            (Appointment.ApptTime <= appt.ApptTime and appointment_end_time > appt.ApptTime) or 
            # Check if the existing appointment start time is in between the new appointment
            (Appointment.ApptTime >= appt.ApptTime and appt_end_time > Appointment.ApptTime)
        )

        taken_appointments = self.session.query(Appointment).\
            options(joinedload(Appointment.AppointmentType)).\
            filter(
                sa.and_(
                    Appointment.ApptDate == appt.ApptDate,
                    Appointment.Physician == appt.EmployeeID,
                    is_appointment_time_conflicted
                )
            ).first()

        assert taken_appointments is None, "Appointment Already Taken!"


        ### Then We pull the hours for the location and day ###
        
        # In the DB its either "Week1" or "Week2"
        week_number = "Week"
        week_number += self.__get_week_number(appt.ApptDate) 

        hours =  self.session.query(HospitalHours).filter(
            sa.and_(
                HospitalHours.LocationID == Appointment.LocationID,

                # Checks if Day of weeks Matches
                HospitalHours.DayOfWeek == Appointment.ApptDate.strftime("%A"),

                # Check if the week_number matches, if needed
                (HospitalHours.WeekNumber == week_number | (HospitalHours.WeekNumber is None)) 
            )
        ).first()

        ### Then we tell if the location is closed ###

        assert hours.OpenTime is not None, "This Location is closed that day!"

        # Checks if its outside the hours of the location
        if (hours.OpenTime > appt.ApptTime or hours.CloseTime < appt.ApptTime):
            assert custom_time, "Outside this locations hours. Use custom time"


        ### Then we check if the physician is out, or if the entire clinic is out ###
        events = self.session.query(Event)\
                     .filter(
                        sa.or_(Event.EmployeeID == appt.EmployeeID, Event.EmployeeID is None),
                        Event.StartDate <= appt.ApptDate, # Check if its after start date
                        Event.EndDate >= appt.ApptDate, # Check if its before end date
                     ).first()
        
        if events is not None:
            
            if events.EmployeeID == appt.EmployeeID: # The employee is out is out
                raise AssertionError("This Physician is out on this day")
            else:
                raise AssertionError("This clinic is closed for: ", events.EventName)



        # Everything above is asserted. We wont get here without errors unless its true
        return True

    def __get_week_number(self, check_date=datetime.now()):
        """ 
        A private method to get what week number it is 
        
        It's a little jank.
        It checks how many weeks it has been since the first Sunday of 2015
        It then modulo's that number by 2, now each week will either be week 1 or week 2
        This insures no repeating weeks.

        If the clinic ever chooses to add more weeks to their repeating schedule, chagne the constant
        """

        number_of_weeks = 2

        start_date = datetime(2015, 1, 4)
        end_date = check_date

        weeks_since_2015 = (end_date - start_date).days // 7

        week_number = weeks_since_2015 % number_of_weeks + 1

        return week_number
