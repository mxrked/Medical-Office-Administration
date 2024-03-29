"""
LabOrders.py - A window to submit lab orders for a clinic
UI Designed by: Destan Hutcherson
Authors: Destan Hutcherson, Jessica Weeks
"""
from PyQt5.QtWidgets import QPushButton, QLineEdit, QDateEdit, QComboBox
from frontend.private.utility import Utility
from backend.data_handler import get_selected_combo_box_object, load_objects_to_combo_box


class Lab(Utility):
    """
    Creates a lab using Lab object
    
    Uses the misc_dm & user_dm
    """
    def __init__(self):
        super(Lab, self).__init__()

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
        self.lab_clear_btn.clicked.connect(self.clear_inputs)

        # fill combo boxes
        self.load_physicians(self.lab_practitioner_combo)
        self.load_locations(self.lab_locations_combo)
        load_objects_to_combo_box(self.misc_dm.get_lab_tests(), self.lab_lab_combo)

        # Add listener for location change
        self.lab_locations_combo.currentIndexChanged.connect(self.change_lab_location)

    def change_lab_location(self):
        """
            Change the location of the lab
        """
        location = get_selected_combo_box_object(self.lab_locations_combo)
        self.load_physicians(self.lab_practitioner_combo, location=location)

    def submit_information(self):
        """
            First get the Patient from user_dm
                using the inputs
            
            Then creates Lab in the db
            using Lab([Data])
            
            Uses the misc_dm
            
            Then run self.clear_inputs()
        """

        patient_fn = self.lab_fname.text()
        patient_ln = self.lab_lname.text()
        patient_dob = self.lab_dob.date().toPyDate()
        physician = get_selected_combo_box_object(self.lab_practitioner_combo)
        location = get_selected_combo_box_object(self.lab_locations_combo)
        lab_date = self.lab_lab_date_edit.date().toPyDate()
        lab_lab = get_selected_combo_box_object(self.lab_lab_combo)
        lab_order = self.lab_order_name.text()

        try:
            patient = self.get_verified_patient(patient_fn,
                                                patient_ln,
                                                patient_dob)
        except AssertionError as error:
            self.load_error(str(error))
            return

        labToAdd = self.misc_dm.create_lab_order(order_name=lab_order,
                                                 patient=patient,
                                                 employee=physician,
                                                 lab_date=lab_date,
                                                 lab=lab_lab,
                                                 location=location)

        self.misc_dm.add_lab_order(labToAdd)

        self.clear_inputs()
