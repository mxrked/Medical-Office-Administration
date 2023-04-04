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
        stmt = sa.update(Appointment)\
            .where(Appointment.AppointmentID == appt.AppointmentID)\
            .values(ApptStatus=status)
        self.session.execute(stmt)
        self.session.commit()
    
    def get_in_progress_appointments(self, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
        return self.session.query(Appointment).filter(
            Appointment.ApptStatus == "In Progress",
            Appointment.ApptDate == date.today(),
            Appointment.LocationID == location.LocationID if location else True,
            Appointment.EmployeeID == provider.EmployeeID if provider else True,
        )

    def get_pending_appointments(self, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
        return self.session.query(Appointment).filter(
            Appointment.ApptStatus == "Pending",
            Appointment.ApptDate == date.today(),
            Appointment.LocationID == location.LocationID if location else True,
            Appointment.EmployeeID == provider.EmployeeID if provider else True,
        )

    def get_todays_appointments(self, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
        return self.session.query(Appointment).filter(
            Appointment.ApptStatus.in_(["Scheduled", "Rescheduled"]),
            Appointment.ApptDate == datetime.date.today(),
            Appointment.LocationID == location.LocationID if location else True,
            Appointment.EmployeeID == provider.EmployeeID if provider else True
            ).all()