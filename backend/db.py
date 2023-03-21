"""
db.py - A library for accessing the Office Administration Database
Author: Jessica Weeks
"""


try:
    import sqlalchemy as sql
    from sqlalchemy.pool import QueuePool
    import pyodbc

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
        # This must match ordering in the database
        appointment_id = row[0]
        appt_date = row[1].date()
        appt_time = row[2].time()
        appt_type_id = row[3]
        patient_id = row[4]
        appt_status = row[5]
        employee_id = row[6]
        visit_reason = row[7]
        location_id = row[8]
        appointment = Appointment(appointment_id=appointment_id,
                                  appt_date=appt_date,
                                  appt_time=appt_time,
                                  appt_type_id=appt_type_id,
                                  patient_id=patient_id,
                                  appt_status=appt_status,
                                  visit_reason=visit_reason,
                                  employee_id=employee_id, 
                                  location_id=location_id)

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


def create_refferal(conn, referral: Referral):
    """ 
    Add a referral to the database using the referral object.

    :param conn: The database connection object.
    :param referral: The referral object to add to the database.
    """

    formatted_date = referral.creation_date.strftime("%Y-%m-%d")
    stmt = sql.text(
        f""" 
    INSERT INTO Referral (ReferralReason, CreationDate, EmployeeID, PatientID)
    VALUES ('{referral.referral_reason}', '{formatted_date}', {referral.employee_id}, {referral.patient_id})
    """)

    conn.execute(stmt)


def create_lab_order(conn, lab_order: LabOrder):
    """ Add a lab order to the database using the lab_order object!
    the lab_order id should be handled by the Database
    """

    formatted_date = lab_order.lab_date.strftime("%Y-%m-%d")
    stmt = sql.text(
        f""" 
    INSERT INTO LabOrder (OrderName, EmployeeID, PatientID, LabDate, Results, LabID, LocationID)
    VALUES ('{lab_order.order_name}',
    {lab_order.employee_id},
    {lab_order.patient_id}
    '{formatted_date}',
    '{lab_order.results}',
    {lab_order.lab_id}, 
    {lab_order.location_id};)
    """)

    conn.execute(stmt)


### UNFINISHED: I WROTE THESE IN, THEY MUST BE DONE IN FUTURE ###


def find_avaliable_appointments(conn, date: date, for_appointment: Appointment) -> list[time]:
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

def find_all_doctors(conn) -> list[Employee]:
    """
    Here I just need a list of doctors, this is used for the dropdown box in the appointments
    screen
    """
    pass


def appointment_cancel(conn, appointment: Appointment):
    """ Here you are gonna remove an appointment, all you really need is the AppointmentID"""
    pass

def appointment_after_visit_summary(conn, appointment: Appointment) -> dict:
    """
    We need a bunch of information to print this out, all this will do is print out a object
    with a bunch of attirbutes
    
    UNFINISHED PENDING Database bening done
    """
    
    medical_record = {}

    provider = get.employee(conn, appointment.employee_id)

    name_of_provider = f"{provider.first_name} {provider.middle_name} {provider.last_name}"
    
    appt_date = appointment.appt_date.strftime("%B %d, %Y")
    appt_time = appointment.appt_time.strftime("%I:%M %p")
    appointment_time_date = f"{appt_date} {appt_time}"



    return medical_record


### MAIN ###

def main():
    with engine.connect() as conn:
        print(get.todays_appointments(conn))



if __name__ == "__main__":
    main()
