from datetime import date
import sqlalchemy as sa
from fpdf.fpdf import FPDF
from backend.private.data_manager import DataManager

from backend.models import Location, Employee, User, Patient, EmpGroupCross, Role, \
    GroupRoleCross, Appointment


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

        # Used for very basic cacheing
        self.physicians_dict = {}

    def check_username_password(self, username: str, password: str) -> Employee:
        """
            Checks if username and password are valid and returns
             the employee if they are valid

            :param username: str, The username to check
            :param password: str, The password to check

            returns: Employee, SQL ORM object
        """
        with self.session_scope() as session:
            employee = session.query(Employee) \
                .join(User) \
                .filter(User.UserTypeID == 1,
                        User.UserName == username,
                        User.Password == password) \
                .first()

            if (employee is None):
                return False

            session.expunge(employee)
            return employee

    def check_employee_role(self, current_employee: Employee, search_role_id) -> bool:
        """
            Checks db if a employee's group or themselves has a given role id

            :param current_employee: Employee, SQL ORM object
            :param search_role_id: int, The role id to check

            :returns: bool, True if the employee has the role, False otherwise        
        """
        with self.session_scope() as session:
            session.add(current_employee)
            groups = session.query(EmpGroupCross)\
                .filter_by(EmployeeID=current_employee.EmployeeID).all()
            
            roles = []
            for group in groups:
                roles = session.query(Role.RoleID)\
                        .join(GroupRoleCross)\
                        .where(sa.text(f"GroupRoleCross.GroupID = {group.GroupID}")).all()
                
                for role in roles:  # Roles are returned as a tuple
                    if search_role_id in role:
                        return True

            return False

    def get_physicians(self, location: Location = None) -> list[Employee]:
        """
        
        :param: location_id : Corresponds to a LocationID (So it matches up with JSON)
            Certain physicians only work at certain locations
            if location is None, it will search all locations

        """
        valid_types = ["General Practitioner", "Internal Medicine", "Ear, Nose & Throat", "Womens Medicine"]

        with self.session_scope() as session:
            
            if location is None:
                # Search all locations instead
                physicians = session.query(Employee) \
                    .where(Employee.Position.in_(valid_types)) \
                    .order_by(Employee.Position.asc(), Employee.FirstName.asc()) \
                    .all()
            else:
                session.add(location)
                physicians = session.query(Employee) \
                    .where(Employee.Position.in_(valid_types),
                           Employee.LocationID == location.LocationID) \
                    .order_by(Employee.Position.asc(), Employee.FirstName.asc()) \
                    .all()

            session.expunge_all()

            return physicians

    def get_patients(self, first_name: str, last_name: str, dob: date) -> list[Patient]:
        """
        Returns a list of patients whose name contains the search text.
        NOTE TO FRONTEND: THERE CAN BE MULTIPLE PATIENTS THAT ARE RETURNED. BE SURE TO HANDLE THIS.

        :param dob: a date selected by user
        :param first_name: a String representing a FirstName
        :param last_name: a String representing a LastName
        :return: A list of Patient objects.
        """

        with self.session_scope() as session:
        
            patients = session.query(Patient) \
                .where(dob == Patient.DateOfBirth, first_name == Patient.First_Name, last_name == Patient.Last_Name) \
                .all()
            
            session.expunge_all()
            return patients


    def get_summary_info(self, appt: Appointment) -> FPDF:
        with self.session_scope() as session:
            session.add(appt)

            pdf = FPDF()
            pdf.add_page()
            pdf.image("frontend/ui/assets/imgs/logo.png", 170, 8, 33)
            pdf.set_font('Arial', 'B', 12)
            formated_time = appt.ApptTime.strftime("%I:%M:%S %p")
            formated_endtime = appt.ApptEndtime.strftime("%I:%M:%S %p")
            formated_date = appt.ApptDate.strftime("%m/%d/%Y")

            text = \
            f"""
Appointment Summary:
    Patient: {appt.Patient}
    Physician: {appt.Employee}
    Date: {formated_date}
    Time: {formated_time} till {formated_endtime}
    Apppointment Type: {appt.AppointmentType}
    Appointment Reason: {appt.ApptReason}
"""
            pdf.multi_cell(200, 10, txt=text, align='L')
            session.expunge_all()

            return pdf

