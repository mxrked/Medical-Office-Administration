from data_manager import *

class AppointmentStatusDataManger(DataManger):

    def __init__(self):
        super().__init__()

    def set_appointment_scheduled(self, appt: Appointment):
        self.__set_appointment_status(appt, "Scheduled")


    def set_appointment_in_progress(self, appt: Appointment):
        self.__set_appointment_status(appt, "In Progress")


    def set_appointment_no_show(self, appt: Appointment):
        self.__set_appointment_status(appt, "No Show")


    def set_appointment_canceled(self, appt: Appointment):
        self.__set_appointment_status(appt, "Canceled")

    def __set_appointment_status(self, appt: Appointment, status: String):
        pass
    
    def get_in_progress_appointments(self, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
        # Assume we are looking at today
        pass

    def get_pending_appointments(self, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
        pass

    def get_todays_appointments(self, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
        # We only want "Scheduled" or "Rescheduled" status
        pass