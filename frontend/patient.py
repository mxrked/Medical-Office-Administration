"""
NewPatient.py - A window to add a new patient to the database
UI Designed by: Destan Hutcherson
Authors: 
"""

from PyQt5.QtWidgets import QComboBox, QLineEdit, QRadioButton
from frontend.schedule import Cancel

class Patient(Cancel):

    def __init__(self):
        super(Patient, self).__init__()

        self.appartment_num = self.findChild(QLineEdit,"Patient_appart_num")
        self.city = self.findChild(QLineEdit,"city_lineEdit")
        self.state = self.findChild(QComboBox, "Patient_State_Combo")
        self.zip = self.findChild(QLineEdit, "zip_code_lineEdit")
        self.phone_number = self.findChild(QLineEdit, "phone_number_lineEdit")
        self.email = self.findChild(QLineEdit, "email_lineEdit")
        
        # Name
        self.patient_fname = self.findChild(QLineEdit, "p_fname")
        self.patient_mname = self.findChild(QLineEdit, "p_mname")
        self.patient_lname = self.findChild(QLineEdit, "p_lname")

        # Genders
        self.gender_male = self.findChild(QRadioButton, "radioButtonGenderM")
        self.gender_other = self.findChild(QRadioButton, "radioButtonOther")
        self.gender_female = self.findChild(QRadioButton, "radioButtonGenderF")

        # Suffixes
        self.iii_radioButton = self.findChild(QRadioButton, "III_radioButton_5")
        self.ii_radioButton = self.findChild(QRadioButton, "II_radioButton_5")
        self.i_radioButton = self.findChild(QRadioButton, "I_radioButton_5")
        self.jr_radioButton = self.findChild(QRadioButton, "jr_radioButton_5")
        self.na_radioButton = self.findChild(QRadioButton, "radioButton_10")
        self.sr_radioButton = self.findChild(QRadioButton, "sr_radioButton_5")
        