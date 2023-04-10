"""
LabOrders.py - A window to submit lab orders for a clinic
UI Designed by: Destan Hutcherson
Authors: 
"""
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QDateEdit, QComboBox
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg

from frontend.abstract_main_window import AMainWindow
import sys

class UI(AMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/LabOrdersWindow.ui", self)

        # define widgets
        self.submitPushButton = self.findChild(QPushButton, "pushButton_ClearLabOrders")
        self.clearPushbutton = self.findChild(QPushButton, "pushButton_SubmitLabOrder")
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



        self.load_nav()





        def submitInformation(self):
            ""





#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
