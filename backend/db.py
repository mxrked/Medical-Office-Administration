"""
db.py - A set of functions for working with the clinics database.
Author: Jessica Weeks, Christian Fortin
"""
from datetime import datetime, date, time, timedelta
from models import *
from sqlalchemy.orm import Session, sessionmaker, joinedload
import sqlalchemy as sa

def get_session() -> Session:
    """
    Be sure to close your sessions when the program is closed!

    :returns: A Sqlalchemy Session
    """

    with open("backend/connection_string.txt", "r", encoding="utf-8") as file:
        DB = file.read()

    engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}")

    session_maker = sessionmaker(bind=engine)
    return session_maker()

def close_session(session: Session):
    session.close()
    session.bind.dispose()

def get_locations(session) -> list[HospitalLocation]:
    locations = session.query(HospitalLocation).all()
    return locations


def get_physicians(session) -> list[Employee]:
    valid_types = ["physcian"]
    physicians = session.query(Employee)\
        .join(EmployeeType)\
        .options(joinedload(Employee.EmployeeType))\
        .filter(EmployeeType.TypeDescription.in_(valid_types))\
        .all()
    return physicians

def get_pending_appointments(session, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
    pass

def get_todays_appointments(session, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
    # We only want "Scheduled" or "Rescheduled" status
    pass

def get_in_progress_appointments(session, location: HospitalLocation=None, provider: Employee=None) -> list[Appointment]:
    # Assume we are looking at today
    pass

def get_lab_tests(session) -> list[Lab]:
    labs = []
    return labs


def get_appointment_types(session, search_text: String) -> list[AppointmentType]:
    appointment_types = []
    return appointment_types

def get_patient(session, first_name: String, last_name: String, dob: String) -> list[Patient]:
    """
    Returns a list of patients whose name contains the search text.
    NOTE TO FRONTEND: THERE CAN BE MULTIPLE PATIENTS THAT ARE RETURNED. BE SURE TO HANDLE THIS.

    :param session: A SQLAlchemy session object.
    :param search_text: A string representing the search text.
    :return: A list of Patient objects.
    """
    patients = []

    return patients

def get_appointments_for_date(session, date: date) -> list[Appointment]: # Check Reschedule/Canceling appointment screen first
    pass

def get_physicians_for_appointment_type(session, apptType: AppointmentType) -> list[Employee]:
    # I have no idea how this will get done
    pass

def get_avaliable_appointments(session,
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

def set_appointment_time(session, appt: Appointment, new_time: time, new_date: date):

    assert __check_appointment_available(session, Appointment, new_time=new_time, new_date=new_date), "Appointment time not available"
    
    # Now we can set the correct time

def check_username_password(session, username: String, password: String) -> bool:
    
    validated = False

    # Besure to global the CURRENT_USER as a User Object
    return validated

def check_user_role(session, current_user: User, role: String) -> bool:
    has_role = False
    # Check if their group has that role
    # Check if the user has that role
    return has_role

def set_appointment_scheduled(session, appt: Appointment):
    __set_appointment_status(session, appt, "Scheduled")


def set_appointment_in_progress(session, appt: Appointment):
    __set_appointment_status(session, appt, "In Progress")


def set_appointment_no_show(session, appt: Appointment):
    __set_appointment_status(session, appt, "No Show")


def set_appointment_canceled(session, appt: Appointment):
    __set_appointment_status(session, appt, "Canceled")

def add_refferal(session, referral: Referrals):
    pass

def add_lab_order(session, lab_order: LabOrder):
    pass

def add_patient(session, patient: Patient):
    pass

def add_appointment(session, appt: Appointment):

    assert __check_appointment_available(session, appt), "Appointment time not available"

    # Now we can add the appointment


def __check_appointment_available(session, appt: Appointment, new_time=None, new_date=None) -> bool:

    new_time = new_time or appt.ApptTime
    new_date = new_date or appt.ApptDate

def __set_appointment_status(session, appt: Appointment, status: String):
    pass

if __name__ == "__main__":
    # Add Some Test Functions

    session = get_session()
    print("Connected...")
    close_session(session)
