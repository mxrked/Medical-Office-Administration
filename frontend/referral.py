"""
Referrals.py - A window to submit referrals for a clinic
UI Designed by: Matthew Burrus
Authors: Jessica Weeks
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
        self.FName = self.findChild(QLineEdit, "LineEdit_PatientFirstName")
        self.LName = self.findChild(QLineEdit, "LineEdit_PatientLastName")
        self.dob = self.findChild(QDateEdit, "DateEdit_DOB")
        self.Practitioner = self.findChild(QComboBox, "ComboBox_DoctorPractitioner")
        self.CreationDate = self.findChild(QDateEdit, "DateEdit_CreationDate")
        self.Reason = self.findChild(QLineEdit, "LineEdit_Reason")

        # Initalized Buttons
        self.CreateReferral = self.findChild(QPushButton, "Btn_CreateReferral")

        # Button Listeners
        self.CreateReferral.mousePressEvent = self.create_referral


    def create_referral(self, event):
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
