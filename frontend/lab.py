"""
LabOrders.py - A window to submit lab orders for a clinic
UI Designed by: Destan Hutcherson
Authors: 
"""
from PyQt5.QtWidgets import QPushButton, QLineEdit, QDateEdit, QComboBox, QMainWindow
from frontend.referral import Referral

class Lab(Referral):
    def __init__(self):
        super(Lab, self).__init__()
        # define widgets
        self.submitPushButton = self.findChild(QPushButton, "pushButton_SubmitLabOrder")
        self.clearPushbutton = self.findChild(QPushButton, "pushButton_ClearLabOrder")
        self.enterFirstName = self.findChild(QLineEdit, "LineEdit_PatientFirstName")
        self.enterLastName = self.findChild(QLineEdit, "LineEdit_PatientLastName")
        self.selectDateOfBirth = self.findChild(QDateEdit, "dateEdit_DOB")
        self.selectPractitioner = self.findChild(QComboBox, "comboBox_Practitioner")
        self.selectLocation = self.findChild(QComboBox, "comboBox_LocationID")
        self.selectLabDate = self.findChild(QDateEdit, "dateEdit_LabDate")
        self.selectLab = self.findChild(QComboBox, "comboBox_PossibleLabs")
        self.enterOrderName = self.findChild(QLineEdit, "LineEdit_LabOrderName")

        # Do something
        self.submitPushButton.clicked.connect(self.submitInformation)
        

    def submitInformation(self):
        print("Submit Information")
        pass