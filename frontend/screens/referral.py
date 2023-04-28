"""
Referrals.py - A window to submit referrals for a clinic
UI Designed by: Matthew Burrus
Authors: Matthew Burrus
"""

from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QPushButton, QTextEdit
from PyQt5.QtCore import QDate
from frontend.private.utility import Utility
from backend.data_handler import load_objects_to_combo_box
from backend.data_handler import get_selected_combo_box_object
from backend.models import Referral

class ReferralScreen(Utility):
    """
        Creates a referral using the Referral object

        Uses a the misc_dm & user_dm 

        Use the data handler 
            get_locations_into/get_physicians_into
        to load up combo_boxes by default
    """
    def __init__(self):
        super(ReferralScreen, self).__init__()

        # Initalized Input Widgets
        self.ref_fname = self.findChild(QLineEdit, "Referral_Edit_Fname")
        self.ref_lname = self.findChild(QLineEdit, "Referral_Edit_Lname")
        self.ref_dob = self.findChild(QDateEdit, "Referral_DOB")
        self.ref_practitioners = self.findChild(QComboBox, "Referral_Practitoner")
        self.ref_creation_date = self.findChild(QDateEdit, "Referral_CreationDate")
        self.ref_reason = self.findChild(QTextEdit, "Referral_Reason")

        # Initalized Buttons
        self.create_referral_btn = self.findChild(QPushButton, "Btn_CreateReferral")
        self.ref_clear_input_btn = self.findChild(QPushButton, "Btn_RefClearInputs_2")

        # Button Listeners
        self.create_referral_btn.clicked.connect(self.create_referral)
        self.ref_clear_input_btn.clicked.connect(self.clear_inputs)

        # Load up values
        self.load_physicians(self.ref_practitioners, "All")
        self.ref_creation_date.setMinimumDate(QDate.currentDate())

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

        patient_fn = self.ref_fname.text()
        patient_ln = self.ref_lname.text()
        patient_dob = self.ref_dob.date().toPyDate()
        physician = get_selected_combo_box_object(self.ref_practitioners)
        creation_date = self.ref_creation_date.date().toPyDate()
        reason = self.ref_reason.toPlainText()

        try:
            patient = self.get_verified_patient(patient_fn, patient_ln, patient_dob)
            assert reason != "", "Please enter the reason for this referral."

        except AssertionError as error:
            self.load_error(str(error))
            return


        referral = self.misc_dm.create_referral(
            creation_date = creation_date,
            referral_reason = reason,
            patient = patient,
            employee = physician
        )

        self.misc_dm.add_referral(referral)

        self.clear_inputs()

