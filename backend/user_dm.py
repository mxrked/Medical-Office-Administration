from datetime import date

from typing import List

from backend.private.data_manager import DataManager

from backend.models import AppointmentType, Employee, User, EmployeeType, Patient, EmpGroupCross, Group, Role, \
    GroupRoleCross
from sqlalchemy.orm import joinedload
import sqlalchemy as sa

class UserDM(DataManager):
    """
        A Data Manager for managing users and employees

        • Check Username Password
        • Check Employee Role
        • Get Physicians
        • Get Patient

        NOTE: We did not design the DB and we couldn't get everything how we wanted
        We wanted a User-Group-Role System but we got a
        Employee-Group-Role System with Users addtionally
    """
    def __init__(self):
        super().__init__()

    def check_username_password(self, username: str, password: str) -> Employee:

        employee = self.session.query(Employee) \
            .join(User) \
            .filter(User.UserTypeID == 1, User.UserName == username, User.Password == password) \
            .first()

        if (employee is None):
            return False

        return employee

    def check_employee_role(self, current_employee: Employee, search_role_id) -> bool:
        
        groups = self.session.query(EmpGroupCross)\
            .filter_by(EmployeeID = current_employee.EmployeeID).all()
        
        roles = []
        for group in groups:
            roles = self.session.query(Role.RoleID)\
                    .join(GroupRoleCross)\
                    .where(sa.text(f"GroupRoleCross.GroupID = {group.GroupID}")
                ).all()
            
            for role in roles: # Roles are returned as a tuple
                if search_role_id in role:
                    return True

        return False


    def get_physicians(self) -> list[Employee]:
        valid_types = ["General Practitioner", "Internal Medicine", "Ear, Nose & Throat", "Womens Medicine"]

        physicians = self.session.query(Employee) \
            .where(Employee.Position.in_(valid_types)) \
            .order_by(Employee.Position.asc(), Employee.FirstName.asc()) \
            .all()
        print
        return physicians

    def get_patient(self, first_name: str, last_name: str, dob: date) -> list[Patient]:
        """
        Returns a list of patients whose name contains the search text.
        NOTE TO FRONTEND: THERE CAN BE MULTIPLE PATIENTS THAT ARE RETURNED. BE SURE TO HANDLE THIS.

        :param dob: a date selected by user
        :param first_name: a String representing a FirstName
        :param last_name: a String representing a LastName
        :return: A list of Patient objects.
        """


        patients = self.session.query(Patient) \
            .where(dob == Patient.DateOfBirth, first_name == Patient.First_Name, last_name == Patient.Last_Name) \
            .all()

        return patients
