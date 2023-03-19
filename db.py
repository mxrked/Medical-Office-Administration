"""
db.py - A library for accessing the Office Administration Database
Author: Jessica Weeks
"""

try:
    import sqlalchemy as sql
    import pyodbc
    from sqlalchemy.pool import QueuePool

    from datetime import datetime

    from objects import Appointment, Patient

except ImportError as e:
    print(f"LIBRARY MISSING: {e} \nMake sure your using the correct enviorment")
    raise e

DB = "Driver={ODBC Driver 17 for SQL Server};" \
                 "Server=tcp:capstone2023.database.windows.net,1433;" \
                 "Database=capstone2023;" \
                 "Uid=MOAuser;" \
                 "Pwd=Password01!;" \
                 "Encrypt=yes;" \
                 "TrustServerCertificate=no;" \
                 "Connection Timeout=30;"

engine = sql.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}")
print("Connected to database. . .")


def get_todays_appointments(conn) -> list[Appointment]:
    """
    Returns a list of `Appointment` objects for all appointments that 
    occurred today and up to one hour ago.

    :param conn: A database connection object.
    :type conn: pyodbc.Connection
    :return: A list of `Appointment` objects.
    :rtype: list
    """

    stmt = sql.text(
        """
    SELECT * 
    FROM Appointment 
    WHERE ApptDate = Cast(GETDATE() AS DATE)
    AND ApptTime >= DATEADD(HOUR, -1, CAST(GETDATE() AS TIME));
    """)
    results = conn.execute(stmt).fetchall()

    return results_to_appointments(results)


def get_pending_appointments(conn) -> list[Appointment]:
    """
    Returns a list of pending appointments from the Appointment table.

    :param conn: A database connection object.
    :type conn: Connection
    :return: A list of Appointment objects.
    :rtype: list
    """

    stmt = sql.text(
        """
    SELECT *
    FROM Appointment
    WHERE ApptStatus = "pending";
    """)
    results = conn.execute(stmt).fetchall()

    return results_to_appointments(results)

def get_current_appointments(conn) -> list[Appointment]:
    """
    Returns a list of pending appointments from the Appointment table.

    :param conn: A database connection object.
    :type conn: Connection
    :return: A list of Appointment objects.
    :rtype: list
    """

    stmt = sql.text(
        """
    SELECT *
    FROM Appointment
    WHERE ApptStatus = "in progress";
    """)
    results = conn.execute(stmt).fetchall()

    return results_to_appointments(results)

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

def results_to_appointments(sql_results) -> list[Appointment]:
    """ Turns results from a SQL query into a list of Appointment objects"""
    appointments = []
    for row in sql_results:
        appointment_id = row[0]
        appt_date = row[1].date()
        appt_time = row[2].time()
        appt_type_id = row[3]
        patient_id = row[4]
        appt_status = row[5]
        visit_reason = row[6]
        appointment = Appointment(appointment_id,
                                  appt_date,
                                  appt_time,
                                  appt_type_id,
                                  patient_id,
                                  appt_status,
                                  visit_reason)

        appointments.append(appointment)

    return appointments



### UNFINISHED: I WROTE THESE IN, THEY MUST BE DONE IN FUTURE ###

def find_patients(conn, first_name, last_name, dob) -> list[Patient]:
    """ Returns a list of patient objects that match these attributes """
    pass



### MAIN ###

def main():
    with engine.connect() as conn:
        get_todays_appointments(conn)

main()
