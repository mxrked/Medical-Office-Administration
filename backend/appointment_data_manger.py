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

        stmt = sa.update(Appointment)\
            .where(Appointment.AppointmentID == appt.AppointmentID)\
            .values(ApptTime=new_time, ApptDate=new_date)
        self.session.execute(stmt)
        self.session.commit()

    def add_appointment(self, appt: Appointment):

        assert self.__check_appointment_available(appt), "Appointment time not available"
        self.session.add(appt)
        self.session.commit()

    def get_appointment_types(self, search_text: String) -> list[AppointmentType]:
        return self.session.query(AppointmentType)\
            .filter(AppointmentType.ApptName\
            .like(f'%{search_text}%'))\
            .all()

    def get_appointments_for_date(self, date: date) -> list[Appointment]: # Check Reschedule/Canceling appointment screen first
        return self.session.query(Appointment)\
            .filter_by(date=date)\
            .order_by(Appointment.ApptTime)\
            .all()

    def __check_appointment_available(self, appt: Appointment, new_time=None, new_date=None) -> bool:

        appointment_not_taken = True

        taken_appointments = self.session.query(Appointment).filter(
            sa.and_(
                Appointment.ApptDate == new_date,
                Appointment.ApptTime == new_time,
                Appointment.Physician == appt.EmployeeID
            )
        ).first()

        # Check HospitalHours for hours

        # Check in the events table in the physisician is out
        
        if taken_appointments is None:
            appointment_not_taken = False

        return appointment_not_taken
