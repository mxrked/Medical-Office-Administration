"""
db_appointment.py - A set of functions for handling appointments in the database
Author: Jessica Weeks
"""
from db import *

def check_in(conn, appointment):
    """
    Update the status of an appointment to 'checked in' in the database.

    :param conn: Connection object to the database.
    :param appointment: Appointment object to be checked in.
    """

    stmt = sql.text(
        f""" 
    UPDATE appointments
    SET appt_status = 'checked in'
    WHERE appointment_id = {appointment.id}
    """)
    conn.execute(stmt)

def check_out(conn, appointment):
    """
    Update the status of an appointment to 'completed' in the database.

    :param conn: Connection object to the database.
    :param appointment: Appointment object to be completed.
    """

    stmt = sql.text(
        f""" 
    UPDATE appointments
    SET appt_status = 'completed'
    WHERE appointment_id = {appointment.id}
    """)
    conn.execute(stmt)

def start(conn, appointment):
    """
    Update the status of an appointment to 'in progress' in the database.

    :param conn: Connection object to the database.
    :param appointment: Appointment object to be in progress.
    """

    stmt = sql.text(
        f""" 
    UPDATE appointments
    SET appt_status = 'in progress'
    WHERE appointment_id = {appointment.id}
    """)
    conn.execute(stmt)

def schedule_pending(conn, appointment: Appointment):
    """
    Update the status of an appointment to 'pending' in the database.

    :param conn: Connection object to the database.
    :param appointment: Appointment object to be pending.
    """
    stmt = sql.text(
        f""" 
    UPDATE appointments
    SET appt_status = 'scheduled'
    WHERE appointment_id = {appointment.id}
    """)
    conn.execute(stmt)


def appointment_create(conn, appointment: Appointment):
    """ 
    We want you to add a appointment entry using our Appointment Object 
    Remember to ignore setting appointmentID, that should be handled Automatticaly by our database
    """

    appt_time = appointment.appt_time.strftime("%H:%M:%S")
    appt_date = appointment.appt_date.strftime("%Y-%m-%d")

    stmt = sql.text(
        f""" 
    INSERT INTO 
    Appointment (ApptDate, ApptTime, ApptTypeID, PatientID,ApptStatus, EmployeeID, VisitReason, LocationID)
    VALUES ('{appt_date}',
    '{appt_time}',
    {appointment.appt_type_id}, 
    {appointment.patient_id},
    {appointment.appt_status},
    {appointment.employee_id},
    {appointment.visit_reason},
    {appointment.location_id})
    """)

    conn.execute(stmt)
