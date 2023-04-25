"""
NewPatient.py - A window to add a new patient to the database
UI Designed by: Destan Hutcherson
Authors: Destan Hutcherson, Jessica Weeks
"""

from PyQt5.QtWidgets import QComboBox, QLineEdit, QRadioButton, QDateEdit, QPushButton
from backend.models import Patient
from frontend.private.utility import Utility
from backend.data_handler import get_selected_combo_box_object
class NewPatient(Utility):
    """
        Handes creating a new Patient using 
            a patient object

        Uses misc_dm
    """
    def __init__(self):
        super(NewPatient, self).__init__()

        self.p_appartment_num = self.findChild(QLineEdit,"Patient_appart_num")
        self.p_city = self.findChild(QLineEdit,"patient_city")
        self.p_state = self.findChild(QComboBox, "Patient_State_Combo")
        self.p_zip = self.findChild(QLineEdit, "patient_zipcode")
        self.p_phone_num = self.findChild(QLineEdit, "phone_number_lineEdit")
        self.p_email = self.findChild(QLineEdit, "email_lineEdit")
        self.p_dob = self.findChild(QDateEdit, "p_dob_dateEdit")
        self.p_snn = self.findChild(QLineEdit, "p_ssn")
        self.p_street = self.findChild(QLineEdit, "p_street_address")
        self.p_race = self.findChild(QComboBox, "p_race")

        # Name
        self.patient_fname = self.findChild(QLineEdit, "p_fname")
        self.patient_lname = self.findChild(QLineEdit, "p_lname")

        # Genders
        self.gender_male = self.findChild(QRadioButton, "radioButtonGenderM")
        self.gender_other = self.findChild(QRadioButton, "radioButtonOther")
        self.gender_female = self.findChild(QRadioButton, "radioButton_GenderF")

        # Buttons
        self.p_submit_btn = self.findChild(QPushButton, "btnSubmitNewPatient")

        # Connect buttons
        self.p_submit_btn.clicked.connect(self.submit_patient)


    def submit_patient(self):
        """
            Creates a patient and enters it into the database    
        """


        if self.gender_female.isChecked():
            gender = "Female"
        elif self.gender_male.isChecked():
            gender = "Male"
        elif self.gender_other.isChecked():
            gender = "Other"
        else:
            gender = False

        fname = self.patient_fname.text()
        lname = self.patient_lname.text()
        city = self.p_city.text()
        zipcode = self.p_zip.text()
        phone = self.p_phone_num.text()
        email = self.p_email.text()
        dob = self.p_dob.date().toPyDate()
        ssn = self.p_snn.text()
        street = self.p_street.text()
        state =  self.p_state.currentText()
        race = self.p_race.currentText()
     
        try:
            
            # If there are blank, they return False
            assert fname, "Please enter in a first name"
            assert lname, "Please enter in a last name"
            assert gender, "Please enter in a gender"
            assert city, "Please enter in a city"
            assert street, "Please enter in a street"
            assert zipcode, "Please enter in a zipcode"
                #email is not required

            # Special Cases with input masks
            assert ssn != "--", "Please enter in a Social Security Number"
            assert phone != "() -", "Please enter in a phone"

            assert len(zipcode) == 5, "Zipcode is invalid"
            assert len(phone) == 14, "Phone number is invalid"
            assert len(ssn) == 11, "SSN is invalid"

        except AssertionError as error:
            self.load_error(str(error))
            return

        
        patient = Patient(
            Last_Name = lname,
            First_Name = fname,
            Address = street,
            City = city,
            State = state,
            ZipCode = zipcode,
            Gender = gender,
            DateOfBirth = dob,
            Email = email,
            Phone = phone,
            Race = race
        )

        self.misc_dm.add_patient(patient)

        self.clear_inputs()


