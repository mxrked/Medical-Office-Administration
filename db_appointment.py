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

