"""
Referrals.py - A window to submit referrals for a clinic
UI Designed by: Matthew Burrus
Authors:
"""

from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QPushButton
from frontend.main_nav import Nav
class Referral(Nav):
    """
        Creates a referral using the Referral object

        Uses a the misc_dm & user_dm 
    
    """
    def __init__(self):
        super(Referral, self).__init__()

        # Initalized Input Widgets
        self.ref_fname = self.findChild(QLineEdit, "LineEdit_PatientFirstName")
        self.ref_lname = self.findChild(QLineEdit, "LineEdit_PatientLastName")
        self.dob = self.findChild(QDateEdit, "DateEdit_DOB")
        self.ref_practitioners = self.findChild(QComboBox, "ComboBox_DoctorPractitioner")
        self.ref_creation_date = self.findChild(QDateEdit, "DateEdit_CreationDate")
        self.ref_reason = self.findChild(QLineEdit, "LineEdit_Reason")

        # Initalized Buttons
        self.create_referral_btn = self.findChild(QPushButton, "Btn_CreateReferral")

        # Button Listeners
        self.create_referral_btn.clicked.connect(self.create_referral)


    def create_referral(self):
        """
            Creates a referral and puts it into the db

            Makes sure all QLineEdits, RadioButtons and ComboBoxes are selected
                and corresponds to data

            First get the Patient from the relevant data using the 
                user_dm

            Then create a Referral([Data]) using the QLineEdits/QComboBoxes

            For the Comboboxes use a data_handler find the selected box
        """
        print(self.create_referral.__doc__)
