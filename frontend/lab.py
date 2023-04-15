"""
LabOrders.py - A window to submit lab orders for a clinic
UI Designed by: Destan Hutcherson
Authors: 
"""
from PyQt5.QtWidgets import QPushButton, QLineEdit, QDateEdit, QComboBox

from backend.appointment_dm import AppointmentDM
from backend.misc_dm import MiscDM
from backend.user_dm import UserDM
from frontend.main_nav import Nav
from backend.data_handler import get_selected_combo_box_object, set_objects_to_combo_box


class Lab(Nav):
    """
    Creates a lab using Lab object
    
    Uses the misc_dm & user_dm
    """
    def __init__(self):
        super(Lab, self).__init__()

        self.lab_MainAppointmentDM = AppointmentDM()
        self.lab_MainMiscDM = MiscDM()
        self.lab_MainUserDM = UserDM()

        self.lab_Locations = self.RA_MainMiscDM.get_locations()
        self.lab_Labs = self.RA_MainMiscDM.get_lab_tests()


        # define widgets
        self.lab_submit_btn = self.findChild(QPushButton, "pushButton_SubmitLabOrder")
        self.lab_clear_btn = self.findChild(QPushButton, "pushButton_ClearLabOrder")
        self.lab_fname = self.findChild(QLineEdit, "Lab_Fname")
        self.lab_lname = self.findChild(QLineEdit, "Lab_Lname")
        self.lab_dob = self.findChild(QDateEdit, "Lab_DOB")
        self.lab_practitioner_combo = self.findChild(QComboBox, "Lab_Combo_Practitioner")
        self.lab_locations_combo = self.findChild(QComboBox, "Lab_Combo_Location")
        self.lab_lab_date_edit = self.findChild(QDateEdit, "Lab_Date")
        self.lab_lab_combo = self.findChild(QComboBox, "Lab_Combo_Labs")
        self.lab_order_name = self.findChild(QLineEdit, "Lab_Order")

        # Do something
        self.lab_submit_btn.clicked.connect(self.submit_information)
        self.lab_clear_btn.clicked.connect(self.clearInputs)

        self.get_physicians_into(self.lab_practitioner_combo)
        self.get_locations_into(self.lab_locations_combo)

        set_objects_to_combo_box(self.lab_Locations, self.lab_locations_combo)
        set_objects_to_combo_box(self.lab_Labs, self.lab_locations_combo)


    def submit_information(self):
        """
            First get the Patient from user_dm
                using the inputs
            
            Then creates Lab in the db
            using Lab([Data])
            
            Uses the misc_dm
            
            Then run self.clear_inputs()
        """
        #print(self.submit_information.__doc__)

        selected_emp = get_selected_combo_box_object(self.lab_practitioner_combo)

        print(" Selected Employee Is:", selected_emp)
        print(" We have the access to the whole object: ")
        print(" Position:", selected_emp.Position)
