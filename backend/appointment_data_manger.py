from data_manager import *

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

    def set_appointment_time(self, appt: Appointment, new_time: time, new_date: date):

        assert self.__check_appointment_available(appt, new_time, new_date), "Appointment time not available"
    
        # Now we can set the correct time

    def add_appointment(self, appt: Appointment):

        assert self.__check_appointment_available(appt), "Appointment time not available"

    # Now we can add the appointment

    def get_appointment_types(self, search_text: String) -> list[AppointmentType]:
        appointment_types = []
        return appointment_types
    
    def get_appointments_for_date(self, date: date) -> list[Appointment]: # Check Reschedule/Canceling appointment screen first
        pass

    def __check_appointment_available(self, appt: Appointment, new_time=None, new_date=None) -> bool:

        new_time = new_time or appt.ApptTime
        new_date = new_date or appt.ApptDate

