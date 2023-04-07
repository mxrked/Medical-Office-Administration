from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.GLOBALS import *
from frontend.ui.assets.files.NAVIGATION_FUNCS import *
from frontend.ui.assets.files.SCHEDULING_LISTENERS import *

import urllib
import sqlalchemy
import backend.data_manager
import sys



class UI(QMainWindow):
    def __init__(self):


        super(UI, self).__init__()

        uic.loadUi("frontend/ui/SchedulingAppointmentsWindow.ui", self)

        # Session for connecting to the Database
        self.session = backend.data_manager.DataManger().session

        # Functions
        # Frame functions
        def hideAllFrames():

                # All frames have a height of 681
                self.InputsFrame.setFixedHeight(0)
                self.CancelAppointment_Frame.setFixedHeight(0)
                self.RescheduleAppointment_Frame.setFixedHeight(0)

                # Re-enabling the frame btn togglers
                self.DisplaySchedule_Btn.setEnabled(True)
                self.DisplayCancel_Btn.setEnabled(True)
                self.DisplayReschedule_Btn.setEnabled(True)

                # Restyling frame btn togglers
                self.DisplaySchedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
                self.DisplayCancel_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
                self.DisplayReschedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")

                # Clearing all the fields
                clearInputs_SA(self)
                clearInputs_RA(self)
                clearInputs_CA(self)

        def displayInputsFrame():

                hideAllFrames()
                self.InputsFrame.setFixedHeight(681)

                # Disabling the toggler btn
                self.DisplaySchedule_Btn.setEnabled(False)
                self.DisplaySchedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgba(110, 204, 175, .2);\n"
"    color: rgba(0, 0, 0, .2);\n"
"    border: 2px solid rgba(0, 0, 0, .2);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        def displayCancelAppointmentFrame():

                hideAllFrames()
                self.CancelAppointment_Frame.setFixedHeight(681)

                # Disabling the toggler btn
                self.DisplayCancel_Btn.setEnabled(False)
                self.DisplayCancel_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgba(110, 204, 175, .2);\n"
"    color: rgba(0, 0, 0, .2);\n"
"    border: 2px solid rgba(0, 0, 0, .2);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        def displayRescheduleAppointmentFrame():

                hideAllFrames()
                self.RescheduleAppointment_Frame.setFixedHeight(681)

                # Disabling the toggler btn
                self.DisplayReschedule_Btn.setEnabled(False)
                self.DisplayReschedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgba(110, 204, 175, .2);\n"
"    color: rgba(0, 0, 0, .2);\n"
"    border: 2px solid rgba(0, 0, 0, .2);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")




        #define widgets
        self.logoutPushButton = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointmentsPushButton = self.findChild(QPushButton, "Nav_Appointments")
        self.checkinPushButton = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkoutPushButton = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.makeReferralPushButton = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.labOrdersPushButton = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approveAppointmentsPushButton = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")

        self.newPatientPushButton = self.findChild(QPushButton, "NewPatient_Btn")
        self.reschedulingPushButton = self.findChild(QPushButton, "DisplayReschedule_Btn")
        self.makeSchedulePushButton = self.findChild(QPushButton, "DisplaySchedule_Btn")
        self.cancelPushButton = self.findChild(QPushButton, "DisplayCancel_Btn")

        self.SA_PatientFNLineEdit = self.findChild(QLineEdit, "LineEdit_PatientFirstName_SA")
        self.SA_PatientLNLineEdit = self.findChild(QLineEdit, "LineEdit_PatientLastName_SA")
        self.SA_PatientDOBDateEdit = self.findChild(QDateEdit, "dateEdit_DOB_SA")
        self.SA_OfficeLocationsComboBox = self.findChild(QComboBox, "ComboBox_OfficeLocations_SA")
        self.SA_AppointmentReasonLineEdit = self.findChild(QLineEdit, "LineEdit_AppointmentReason_SA")
        self.SA_PhysicianNamesComboBox = self.findChild(QComboBox, "ComboBox_PhysicianNames_SA")
        self.SA_AppointmentTypesComboBox = self.findChild(QComboBox, "ComboBox_AppointmentTypes_SA")
        self.SA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_SA")
        self.SA_CurrentAvailableTimesListWidget = self.findChild(QListWidget, "ListWidget_AvailableTimes_SA")
        self.SA_CustomTimeTimeEdit = self.findChild(QTimeEdit, "timeEdit_CustomTime_SA")
        self.SA_YesCustomTimePushButton = self.findChild(QPushButton, "yesCustomTimePushButton_SA")
        self.SA_NoCustomTimePushButton = self.findChild(QPushButton, "noCustomTimePushButton_SA")

        self.SA_SearchPushButton = self.findChild(QPushButton, "Search_Btn_SA")
        self.SA_ClearInputsPushButton = self.findChild(QPushButton, "ClearInputsBtn")
        self.SA_ScheduleAppointmentPushButton = self.findChild(QPushButton, "ScheduleAppointmentBtn")

        self.RA_OfficeLocationsComboBox = self.findChild(QComboBox, "ComboBox_OfficeLocations_RA")
        self.RA_PhysicianNamesComboBox = self.findChild(QComboBox, "ComboBox_PhysicianNames_RA")
        self.RA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_RA")
        self.RA_RescheduleDateDateEdit = self.findChild(QDateEdit, "DateEdit_RescheduleDate_RA")
        self.RA_SearchedAppointmentsListWidget = self.findChild(QListWidget, "ListWidget_SearchedAppointments_RA")
        self.RA_CurrentAvailableTimesListWidget = self.findChild(QListWidget, "ListWidget_CurrentAvailableTimes_RA")
        self.RA_DisplayTimesAppointmentsPushButton = self.findChild(QPushButton, "DisplayCurrentTimes_Btn_RA")
        self.RA_RescheduleAppointmentPushButton = self.findChild(QPushButton, "RescheduleAppointment_Btn_RA")
        self.RA_ClearInputsPushButton = self.findChild(QPushButton, "RA_ClearInputsBtn")

        self.CA_OfficeLocationsComboBox = self.findChild(QComboBox, "ComboBox_OfficeLocations_CA")
        self.CA_PhysicianNamesComboBox = self.findChild(QComboBox, "ComboBox_PhysicianNames_CA")
        self.CA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_CA")
        self.CA_SearchedAppointmentsListWidget = self.findChild(QListWidget, "ListWidget_SearchedAppointments_CA")
        self.CA_SearchForAppointmentsPushButton = self.findChild(QPushButton, "SearchForAppointments_Btn_CA")
        self.CA_CancelAppointmentPushButton = self.findChild(QPushButton, "CancelAppointment_Btn_CA")
        self.CA_ClearInputsPushButton = self.findChild(QPushButton, "CA_ClearInputsBtn")
        self.currentUserLabel = self.findChild(QLabel, "currentUserLabel")

        # Displaying current user in label and title
        self.currentUserLabel.setText("")
        self.currentUserLabel.setText("Current User: " + currentUsername[0])
        self.setWindowTitle("")
        self.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments -|- User: " + currentUsername[0])

        #Do something
        self.logoutPushButton.mousePressEvent = lambda event: logoutUser(self)

        self.checkinPushButton.mousePressEvent = lambda event: enterCheckInWindow(self)
        self.checkoutPushButton.mousePressEvent = lambda event: enterCheckOutWindow(self)
        self.makeReferralPushButton.mousePressEvent = lambda event: enterMakeReferralWindow(self)
        self.labOrdersPushButton.mousePressEvent = lambda event: enterLabOrdersWindow(self)
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: enterAppointmentApproveViaPortalWindow(self)



        self.newPatientPushButton.mousePressEvent = lambda event: enterNewPatientWindow(self)
        self.reschedulingPushButton.clicked.connect(displayRescheduleAppointmentFrame)
        self.makeSchedulePushButton.clicked.connect(displayInputsFrame)
        self.cancelPushButton.clicked.connect(displayCancelAppointmentFrame)

        self.SA_ClearInputsPushButton.mousePressEvent = lambda event: clearInputs_SA(self)
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.mousePressEvent = lambda event: disableCustomTime(self)
        self.SA_YesCustomTimePushButton.mousePressEvent = lambda event: enableCustomTime(self)
        self.SA_SearchPushButton.mousePressEvent = lambda event: search_SA(self)

        self.RA_ClearInputsPushButton.mousePressEvent = lambda event: clearInputs_RA(self)

        self.CA_ClearInputsPushButton.mousePressEvent = lambda event: clearInputs_CA(self)


        #Hide the app
        # self.hide()




    # This will make it so when the user clicks the red x, it closes the app
    def closeEvent(self, event):
        sys.exit()

    def moveEvent(self, event):
        prevWindowCoords.clear()

        coords = self.pos()

        prevWindowCoords.append(coords.x())
        prevWindowCoords.append(coords.y())

        print(prevWindowCoords)


#initializing app
app = QApplication(sys.argv)
UIWindow = UI()


# app.exit()
