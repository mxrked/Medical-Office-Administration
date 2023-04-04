from data_manager import *

class UserDataManager(DataManger):

    def __init__(self):
        super().__init__()

    def get_physicians_for_appointment_type(self, apptType: AppointmentType) -> list[Employee]:
        # I have no idea how this will get done
        pass

    def check_username_password(self, username: String, password: String) -> bool:
    
        validated = False

        # Besure to global the CURRENT_USER as a User Object
        return validated

    def check_user_role(self, current_user: User, role: String) -> bool:
        has_role = False
        # Check if their group has that role
        # Check if the user has that role
        return has_role

    def get_physicians(self) -> list[Employee]:
        valid_types = ["physcian"]
        physicians = self.session.query(Employee)\
            .join(EmployeeType)\
            .options(joinedload(Employee.EmployeeType))\
            .filter(EmployeeType.TypeDescription.in_(valid_types))\
            .order_by(Employee.LastName, Employee.FirstName)\
            .all()
        return physicians

    def get_patient(self, first_name: String, last_name: String, dob: String) -> list[Patient]:
        """
        Returns a list of patients whose name contains the search text.
        NOTE TO FRONTEND: THERE CAN BE MULTIPLE PATIENTS THAT ARE RETURNED. BE SURE TO HANDLE THIS.

        :param session: A SQLAlchemy session object.
        :param search_text: A string representing the search text.
        :return: A list of Patient objects.
        """
        patients = []

        return patients