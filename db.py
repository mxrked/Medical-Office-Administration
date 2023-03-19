"""
db.py - A library for accessing the Office Administration Database
Author: Jessica Weeks
"""


try:
    import sqlalchemy as sql
    import pyodbc
    from sqlalchemy.pool import QueuePool

    from datetime import datetime, time, date

    from objects import *

    import db_get as get
    import db_appointment as appt

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



def check_username(conn, user_name, password) -> User:
    stmt = sql.text(
        f""" 
    SELECT TOP 1 *
    FROM Users
    WHERE user_name = {user_name};
    """)

    results = conn.execute(stmt).fetchall()

    assert len(results) > 0, "No Users Found!"

    result = results[0]

    user_id = result[0]
    user_name = result[1]
    assert password == result[2], "Password Does not match!"
    employee_id = result[3]

    employee = get.employee(conn, employee_id)

    current_user = User(user_id, user_name, employee)

    return current_user





### UNFINISHED: I WROTE THESE IN, THEY MUST BE DONE IN FUTURE ###

def find_patients(conn, first_name, last_name, dob) -> list[Patient]:
    """ Returns a list of patient objects that match these attributes """
    pass

def find_avaliable_appointments(conn, date) -> list[time]:
    """ 
    This will be one of the hardest parts of the backend.

    You will need to create a list of avaliable appointment times for a given date. 
    They need to be in increments of (probably) 15 minutes. You need to check each doesn't interfer with
    any other appointment times.

    You also need to check if the doctor is avaliable for that time (be sure to check their leave times)

    Also check if the practice is open etc.

    You also need to check location stuff! This is big.

    Godspeed - Jessica
    """
    pass

def find_all_doctors(conn) -> list[Employee]:
    """
    Here I just need a list of doctors, this is used for the dropdown box in the appointments
    screen
    """
    pass


def appointment_create(conn, appointment: Appointment):
    """ 
    We want you to add a appointment entry using our Appointment Object 
    Remember to ignore setting appointmentID, that should be handled Automatticaly by our database
    """
    pass

def appointment_cancel(conn, appointment: Appointment):
    """ Here you are gonna remove an appointment, all you really need is the AppointmentID"""
    pass

def create_refferal(conn, referral: Referral):
    """ Add a refferal to the database using the referral object!
    Refferal id should be handled by the Database"""
    pass

def create_lab_order(conn, lab_order: LabOrder):
    """ Add a lab order to the database using the lab_order object!
    the lab_order id should be handled by the Database
    """
    pass



### MAIN ###

def main():
    with engine.connect() as conn:
        get.todays_appointments(conn)


if __name__ == "__main__":
    main()
