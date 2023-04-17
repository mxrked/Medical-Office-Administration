"""
appointment_status_data_manager.py - A data manager for interacting with appointment status
Author: Jessica Weeks
"""
from datetime import date, datetime
import sqlalchemy as sa
from sqlalchemy.orm import make_transient
from backend.private.data_manager import DataManager
from backend.models import Appointment, Location, Employee


class AppointmentStatusDataManger(DataManager):
    """
        A DataManager for modifying and reading appointment status
        
            • Setting appointment status to
                • Scheduled
                • In Progress
                • No Show
                • Canceled
            
            • Get appointments by 
                • In Progress Status
                • Pending Status
                • Todays Appointments (For Checkin)

        It uses self.session for DB interactions
    """
    def __init__(self):
        """ Our superclass has self.session """
        super().__init__()

    def set_appointment_scheduled(self, appt: Appointment):
        """ Changes the appointment status of the given appointment to 'Scheduled' """
        self.__set_appointment_status(appt, "Scheduled")


    def set_appointment_in_progress(self, appt: Appointment):
        """ Changes the appointment status of the given appointment to 'In Progress' """
        self.__set_appointment_status(appt, "In Progress")


    def set_appointment_no_show(self, appt: Appointment):
        """ Changes the appointment status of the given appointment to 'No Show' """
        self.__set_appointment_status(appt, "No Show")


    def set_appointment_canceled(self, appt: Appointment):
        """ Changes the appointment status of the given appointment to 'Canceled' """
        self.__set_appointment_status(appt, "Canceled")

    def __set_appointment_status(self, appt: Appointment, status: str):
        """ A private method for setting appointment status directly """
        with self.session_scope() as session:
            stmt = sa.update(Appointment)\
                .where(Appointment.AppointmentID == appt.AppointmentID)\
                .values(ApptStatus=status)
            session.execute(stmt)
            session.commit()

    def get_in_progress_appointments(self,
                                     location: Location=None,
                                     provider: Employee=None) -> list[Appointment]:
        """
            Get appointments that are currently in progress, for today. 
            You can use either Location or Employee to search

            :param location: Use for searching this particular Location
            :param provider: Use for searching this particular Employee (Usually a provider)
            :return: A list of appointments that are currently in progress.
        """
        with self.session_scope() as session:
            in_progress = session.query(Appointment).filter(
                Appointment.ApptStatus == "In Progress",
                Appointment.ApptDate == date.today(),
                Appointment.LocationID == location.LocationID if location else True,
                Appointment.PhysicianID == provider.EmployeeID if provider else True,
            )

            [session.expunge(appt) for appt in in_progress]
            return in_progress

    def get_pending_appointments(self,
                                 location: Location=None,
                                 provider: Employee=None) -> list[Appointment]:
        """
            Get appointments that are currently pending.
            You can use either Location or Employee to search

            :param location: Use for searching this particular Location
            :param provider: Use for searching this particular Employee (Usually a provider)
            :return: A list of appointments that are currently pending.
        """
        with self.session_scope() as session:
            pending = session.query(Appointment).filter(
                Appointment.ApptStatus == "Pending",
                Appointment.LocationID == location.LocationID if location else True,
                Appointment.PhysicianID == provider.EmployeeID if provider else True,
            ).all()

            [session.expunge(appt) for appt in pending]
            return pending


    def get_todays_appointments(self,
                                location: Location=None,
                                provider: Employee=None,
                                check_date=date.today()) -> list[Appointment]:
        """
            Get appointments that are for today. 
            You can use either Location or Employee to search
            We search for the statuses "Scheduled" & "Rescheduled"

            :param location: Use for searching this particular Location
            :param provider: Use for searching this particular Employee (Usually a provider)
            :return: A list of appointments for today
        """


        with self.session_scope() as session:

            todays_appointments = session.query(Appointment).where(
                Appointment.ApptStatus.in_(["Scheduled", "Rescheduled"]),
                Appointment.ApptDate == check_date,
                Appointment.LocationID == location.LocationID,
                Appointment.PhysicianID == provider.EmployeeID
                ).all()
    
            for appt in todays_appointments:
                patient_name = str(appt.Patient)
                session.expunge(appt) # Detached Parent Tables
                appt.patient_name = patient_name


            #[session.expunge(today) for today in todays_appointments]
            return todays_appointments