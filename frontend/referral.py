"""
Referrals.py - A window to submit referrals for a clinic
UI Designed by: Matthew Burrus
Authors:
"""

from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QPushButton
from frontend.main_nav import Nav
from backend.data_handler import set_objects_to_combo_box
from backend.data_handler import get_selected_combo_box_object
from backend.appointment_dm import AppointmentDM
from frontend.utility import Utility
class Referral_Screen(Utility):
    """
        Creates a referral using the Referral object

        Uses a the misc_dm & user_dm 

        Use the data handler 
            get_locations_into/get_physicians_into
        to load up combo_boxes by default
    """
    def __init__(self):
        super(Referral_Screen, self).__init__()

        # Initalized Input Widgets
        self.ref_fname = self.findChild(QLineEdit, "LineEdit_PatientFirstName")
        self.ref_lname = self.findChild(QLineEdit, "LineEdit_PatientLastName")
        self.ref_dob = self.findChild(QDateEdit, "DateEdit_DOB")
        self.ref_practitioners = self.findChild(QComboBox, "ComboBox_DoctorPractitioner")
        self.ref_creation_date = self.findChild(QDateEdit, "DateEdit_CreationDate")
        self.ref_reason = self.findChild(QLineEdit, "LineEdit_Reason")

        # Initalized Buttons
        self.create_referral_btn = self.findChild(QPushButton, "Btn_CreateReferral")

        # Button Listeners
        self.create_referral_btn.clicked.connect(self.create_referral)

    def create_referral(self):
        """
            Creates a referral and adds it into the db

            Makes sure all QLineEdits, RadioButtons and ComboBoxes are selected
                and corresponds to data (with data handlers)

            First get the Patient from the relevant data using the 
                user_dm

            Then create a Referral([Data]) using the QLineEdits/QComboBoxes

            For the Comboboxes use a data_handler find the selected box
        """

        REF_patientFN = self.ref_fname.text()
        REF_patientLN = self.ref_lname.text()
        REF_patientDOB = self.ref_dob.date().toPyDate()
        REF_practitioner = get_selected_combo_box_object(self.ref_practitioners)
        REF_creation_date = self.ref_creation_date
        REF_reason = self.ref_reason.text()

        patients = self.user_dm.get_patients(first_name=REF_patientFN,
                                                    last_name=REF_patientLN,
                                                    dob=REF_patientDOB)

        if len(patients) == 0:
            self.load_error("No Patients")
            return


        try:
            assert REF_patientFN != "", "Please enter patients' first name."
            assert REF_patientLN != "", "Please enter patients' last name."
            assert REF_reason != "", "Please enter the reason for this referral."

        except AssertionError as error:
            self.load_error(str(error))
            return



