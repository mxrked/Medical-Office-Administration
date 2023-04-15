"""
Referrals.py - A window to submit referrals for a clinic
UI Designed by: Matthew Burrus
Authors:
"""

from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QPushButton
from frontend.main_nav import Nav
from backend.data_handler import set_objects_to_combo_box
from backend.user_dm import UserDM

class Referral(Nav):
    """
        Creates a referral using the Referral object

        Uses a the misc_dm & user_dm 

        Use the data handler 
            get_locations_into/get_physicians_into
        to load up combo_boxes by default
    """
    def __init__(self):
        super(Referral, self).__init__()

        Referral_Physicians = UserDM().get_physicians()

        # Initalized Input Widgets
        self.ref_fname = self.findChild(QLineEdit, "LineEdit_PatientFirstName")
        self.ref_lname = self.findChild(QLineEdit, "LineEdit_PatientLastName")
        self.dob = self.findChild(QDateEdit, "DateEdit_DOB")
        self.ref_practitioners = self.findChild(QComboBox, "Referral_Practitoner")
        self.ref_creation_date = self.findChild(QDateEdit, "DateEdit_CreationDate")
        self.ref_reason = self.findChild(QLineEdit, "LineEdit_Reason")

        # Initalized Buttons
        self.create_referral_btn = self.findChild(QPushButton, "Btn_CreateReferral")

        # Button Listeners
        self.create_referral_btn.clicked.connect(self.create_referral)

        set_objects_to_combo_box(Referral_Physicians, self.ref_practitioners)


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
        print(self.create_referral.__doc__)
