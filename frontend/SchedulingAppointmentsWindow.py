from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.GLOBALS import *
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

import urllib
import sqlalchemy
import sys
import Referrals, LabOrders, NewPatient, CheckIn, CheckOut, ApptRequest
import backend.db

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("ui/SchedulingAppointmentsWindow.ui", self)

        # Session for connecting to the Database
        session = backend.db.get_session()

        # Functions
        # Window Functions
        def enterStartWindow():
                from frontend import StartWindow

                print("Routing to start screen")
                StartWindow.UIWindow.show()
                self.hide()
        def enterNewPatientWindow():
                print("Routing to new patient screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        NewPatient.UIWindow.show()
                        self.hide()


                # Display new window code here
        def enterCheckInWindow():
                print("Routing to check in screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        CheckIn.UIWindow.show()
                        self.hide()

                # Display new window code here
        def enterCheckOutWindow():
                print("Routing to check out screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        CheckOut.UIWindow.show()
                        self.hide()

                # Display new window code here
        def enterMakeReferralWindow():
                print("Routing to make referral screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        Referrals.UIWindow.show()
                        self.hide()

                        Referrals.UIWindow.show()
                        self.hide()

                # Display new window code here
        def enterLabOrdersWindow():
                print("Routing to lab orders screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        LabOrders.UIWindow.show()
                        self.hide()

                # Display new window code here
        def enterAppointmentApproveViaPortalWindow():
                print("Routing to appointment approve via portal screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        ApptRequest.UIWindow.show()
                        self.hide()


        def logoutUser():

                # Clearing array values
                currentUsername.clear()
                currentUserID.clear()
                currentEmployeeID.clear()

                print("LOGGED OUT")

                # Routing user back to the start window
                enterStartWindow()

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
                clearInputs_SA()
                clearInputs_RA()
                clearInputs_CA()

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

        # Getting widget values
        def getLineEditValue(widget):
                return widget.text()
        def getDateEditValue(widget):
                return widget.date()
        def getComboBoxValue(widget):
                return widget.currentIndex()
        def getListWidgetValue(widget, type):
                if type == "Text": # This will get the text of the item and not its index
                        return widget.currentItem()
                if type == "Index": # This will get the index of the item and not its text
                        return widget.currentRow()

        # Schedule Appointment functions
        def displayAppointmentTypes_SA():
                print("Displaying appointment types.. (SA)")
        def displayCurrentAvailableTimes_SA():
                print("Displaying current available times.. (SA)")
        def search_SA():
                print("Searching.. (SA)")
        def clearInputs_SA():

                defaultDate = QDate(2000, 1, 1)

                self.SA_PatientFNLineEdit.setText("")
                self.SA_PatientLNLineEdit.setText("")
                self.SA_PatientDOBDateEdit.setDate(defaultDate)
                self.SA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.SA_AppointmentReasonLineEdit.setText("")
                self.SA_AppointmentTypeLineEdit.setText("")
                self.SA_AppointmentLengthLineEdit.setText("")
                self.SA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.SA_AppointmentDateDateEdit.setDate(defaultDate)

                self.SA_AppointmentTypesListWidget.clear()
                self.SA_CurrentAvailableTimesListWidget.clear()
        def scheduleAppointment_SA():
                print("Scheduling appointment.. (SA)")

        # Reschedule Appointment functions
        def displayCurrentAvailableTimesAndSearchedAppointments_RA():
                print("Displaying current available times and searched appointments.. (RA)")
        def rescheduleAppointment_RA():
                print("Rescheduling appointment.. (RA)")
        def clearInputs_RA():

                defaultDate = QDate(2000, 1, 1)

                self.RA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.RA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.RA_AppointmentDateDateEdit.setDate(defaultDate)
                self.RA_RescheduleDateDateEdit.setDate(defaultDate)

                self.RA_SearchedAppointmentsListWidget.clear()
                self.RA_CurrentAvailableTimesListWidget.clear()

        # Cancel Appointment functions
        def displaySearchedAppointments_CA():
                print("Displaying searched appointments.. (CA)")
        def cancelAppointment_CA():
                print("Cancelling appointment.. (CA)")
        def clearInputs_CA():

                defaultDate = QDate(2000, 1, 1)

                self.CA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.CA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.CA_AppointmentDateDateEdit.setDate(defaultDate)

                self.CA_SearchedAppointmentsListWidget.clear()


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
        self.SA_AppointmentTypeLineEdit = self.findChild(QLineEdit, "LineEdit_AppointmentType_SA")
        self.SA_AppointmentLengthLineEdit = self.findChild(QLineEdit, "LineEdit_AppointmentLength_SA")
        self.SA_PhysicianNamesComboBox = self.findChild(QComboBox, "ComboBox_PhysicianNames_SA")
        self.SA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_SA")
        self.SA_AppointmentTypesListWidget = self.findChild(QListWidget, "ListWidget_AppointmentTypes_SA")
        self.SA_CurrentAvailableTimesListWidget = self.findChild(QListWidget, "ListWidget_AvailableTimes_SA")
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

        #Do something
        self.logoutPushButton.clicked.connect(logoutUser)
        self.checkinPushButton.clicked.connect(enterCheckInWindow)
        self.checkoutPushButton.clicked.connect(enterCheckOutWindow)
        self.makeReferralPushButton.clicked.connect(enterMakeReferralWindow)
        self.labOrdersPushButton.clicked.connect(enterLabOrdersWindow)
        self.approveAppointmentsPushButton.clicked.connect(enterAppointmentApproveViaPortalWindow)

        self.newPatientPushButton.clicked.connect(enterNewPatientWindow)
        self.reschedulingPushButton.clicked.connect(displayRescheduleAppointmentFrame)
        self.makeSchedulePushButton.clicked.connect(displayInputsFrame)
        self.cancelPushButton.clicked.connect(displayCancelAppointmentFrame)

        self.SA_ClearInputsPushButton.clicked.connect(clearInputs_SA)

        self.RA_ClearInputsPushButton.clicked.connect(clearInputs_RA)

        self.CA_ClearInputsPushButton.clicked.connect(clearInputs_CA)

        #Hide the app
        self.hide()

    # This will make it so when the user clicks the red x, it closes all windows
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()
        app.exit()


#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
# app.exec()
