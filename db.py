"""
db.py - A library for accessing the Office Administration Database
Author: Jessica Weeks
"""

try: 
    import sqlalchemy as sql
    import pyodbc
    from sqlalchemy.pool import QueuePool
    
    from datetime import datetime

    from objects import Appointment

except ImportError as e:
    print(f"LIBRARY MISSING: {e} \nMake sure your using the correct enviorment")
    raise e

db = "Driver={ODBC Driver 17 for SQL Server};" \
                 "Server=tcp:capstone2023.database.windows.net,1433;" \
                 "Database=capstone2023;" \
                 "Uid=MOAuser;" \
                 "Pwd=Password01!;" \
                 "Encrypt=yes;" \
                 "TrustServerCertificate=no;" \
                 "Connection Timeout=30;"

engine = sql.create_engine(f"mssql+pyodbc:///?odbc_connect={db}")
print("Connected to database. . .")


def get_todays_appointments(conn) -> list:
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


def get_pending_appointments(conn) -> list:
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


def find_patients(conn, first_name, last_name, DOB) -> list:
    """ Returns a list of patient objects that match these attributes """
    pass



def main():
    with engine.connect() as conn:
        get_todays_appointments(conn)

main()