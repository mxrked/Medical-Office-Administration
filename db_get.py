"""
db_get.py - A set of functions that handle getting information from the database
Author: Jessica Weeks
"""
from db import *

def employee(conn, employee_id) -> Employee:
    stmt = sql.text(
        f""" 
    SELECT TOP 1 EmployeeTypeID, LastName, MiddleName, FirstName
    FROM Employee
    WHERE EmployeeID = {employee_id};
    """)

    results = conn.execute(stmt).fetchall()

    result = results[0]

    return Employee(employee_id, result[0], result[1], result[2], result[3])

def todays_appointments(conn) -> list[Appointment]:
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

def pending_appointments(conn) -> list[Appointment]:
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

def current_appointments(conn) -> list[Appointment]:
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