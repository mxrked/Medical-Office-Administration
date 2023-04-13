from datetime import date

from typing import List

from backend.private.data_manager import DataManager
from backend.models import AppointmentType, Employee, User, EmployeeType, Patient, EmpGroupCross, Group, Role, \
    GroupRoleCross
from sqlalchemy.orm import joinedload


class UserDM(DataManager):

    def __init__(self):
        super().__init__()

    def check_username_password(self, usertypeID: int, username: str, password: str) -> bool:

        validated = self.session.query(User) \
            .where(usertypeID == 1, username == User.Username, password == User.Password)

        # Besure to global the CURRENT_USER as a User Object
        # will need to validate group for screen access
        return validated

    def check_group_role(self, current_employee: Employee, search_role_id) -> bool:
        groups = self.check_user_group(current_employee)
        roles = []
        for group in groups:
            roles.extend(self.session.query(Role.RoleID)
                         .join(GroupRoleCross.RoleID)
                         .where(group == GroupRoleCross.GroupID)
                         )

        if search_role_id in roles:
            return True
        else:
            return False

    def check_user_group(self, current_employee: Employee) -> List[int]:
        # check if user type id is associated with a group
        groups = self.session.query(Group.GroupID) \
            .join(EmpGroupCross.GroupID) \
            .where(current_employee.EmployeeTypeID == EmpGroupCross.EmployeeTypeID)

        return groups

    def get_physicians(self) -> list[Employee]:
        valid_types = ["physcian"]
        physicians = self.session.query(Employee) \
            .join(EmployeeType) \
            .options(joinedload(Employee.EmployeeType)) \
            .filter(EmployeeType.TypeDescription.in_(valid_types)) \
            .order_by(Employee.LastName, Employee.FirstName) \
            .all()
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
            .where(dob == Patient.DateOfBirth, first_name == Patient.FirstName, last_name == Patient.LastName) \
            .all()

        return patients
