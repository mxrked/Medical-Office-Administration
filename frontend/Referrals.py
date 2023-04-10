from PyQt5.QtWidgets import QApplication, QLineEdit, QDateEdit, QComboBox, QPushButton
from PyQt5 import uic
from datetime import date
from frontend.ui.assets.qrc import app_bg
from backend.data_handler import get_selected_combo_box_object, set_objects_to_combo_box
from backend.misc_dm import MiscDM
from backend.user_dm import UserDM
from backend.models import Referrals, Patient, Employee
from frontend.abstract_main_window import AMainWindow
import sys

class UI(AMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/Referrals.ui", self)

        self.load_nav()

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

        # Load relevant data_manager
        self.Mdm = MiscDM()
        self.Udm = UserDM()

        # Populate Practitioner comobo box
        physcians = self.Udm.get_physicians()
        set_objects_to_combo_box(physcians, self.Practitioner)

    def create_referral(self, event):
        
        entered_inputs = self.checkInputs([self.FName, self.LName, self.Reason])

        if (get_selected_combo_box_object(self.Practitioner)):

            combo_boxes_entered = True
        else:
            combo_boxes_entered = True

        if (not entered_inputs) or (not combo_boxes_entered):
            return

        # All inputs are there!

        # Resolve Patient
        """
        patients = self.Udm.get_patient(
            first_name=self.Fname.text(),
            last_name=self.LName.text(),
            dob=self.dob.date().toPyDate()
        )
        

        if len(patients) > 1:
            # Do Error handeling stuff
            return
            pass
        elif len(patients) == 0:
            # No patient found, do error handeling
            return
            pass
        
        patient = patients[0]

        employee = get_selected_combo_box_object(self.Practitioner)
        """

        da = date(2000,2,17)

        patient = Patient(
            PatientID=1,
            LastName="Weeks",
            FirstName = "Jessica",
            DateOfBirth = da,
        )

        employee = Employee(
            EmployeeID=1,
            LastName="Fortin",
            FirstName="Christina",
            DateOfBirth=date(2000,3,20),
            StartDate=date(2010,1,1),
            EmployeeTypeID=1
        )

        referral = Referrals(
            PatientID = patient.PatientID,
            EmployeeID = employee.EmployeeID,
            DateofReferal = self.CreationDate.date().toPyDate(),
            ReferralReason = self.Reason.text(),

            Patient=patient,
            Employee=employee
        )

        print(referral)

        #self.dm.add_referral(referral)
        

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
