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

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("ui/SchedulingAppointmentsWindow.ui", self)

        # Functions
        def connectToDB():
                ' This is used to connect to the DB '

                try:
                    import sqlalchemy as sql
                    import pyodbc
                    import urllib.parse
                    from sqlalchemy.pool import QueuePool

                except ImportError as e:
                    print(f"LIBRARY MISSING: {e} \nMake sure your using the correct enviorment")
                    raise e

                params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 18 for SQL Server};SERVER=tcp:capstone2023.database.windows.net,1433;DATABASE=capstone2023;Trusted_Connection=no;Uid=MOAuser;Pwd=Password01!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
                engine = sql.create_engine(conn_str)

                engine.connect()

                # This is used to check if the database is connected
                if engine.connect():
                    print("Connected to database. . .")

                    return engine

                # with engine.connect() as conn:
                #     result = conn.execute(sql.text("SELECT * FROM Appointment"))
                #     for key in result.keys():
                #         print(key)
        def closeDBConnection():
                ' This is used to close the connection to the DB '

                try:
                    import sqlalchemy as sql
                    import pyodbc
                    import urllib.parse
                    from sqlalchemy.pool import QueuePool

                except ImportError as e:
                    print(f"LIBRARY MISSING: {e} \nMake sure your using the correct enviorment")
                    raise e

                params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 18 for SQL Server};SERVER=tcp:capstone2023.database.windows.net,1433;DATABASE=capstone2023;Trusted_Connection=no;Uid=MOAuser;Pwd=Password01!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
                engine = sql.create_engine(conn_str)

                engine.dispose()

                if engine.dispose:
                        print("Closed database. . .")

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

                # Display new window code here
        def enterCheckInWindow():
                print("Routing to check in screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                # Display new window code here
        def enterCheckOutWindow():
                print("Routing to check out screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                # Display new window code here
        def enterMakeReferralWindow():
                print("Routing to make referral screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                # Display new window code here
        def enterLabOrdersWindow():
                print("Routing to lab orders screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                # Display new window code here
        def enterAppointmentApproveViaPortalWindow():
                print("Routing to appointment approve via portal screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                # Display new window code here

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

                self.LineEdit_PatientFirstName_SA.setText("")
                self.LineEdit_PatientLastName_SA.setText("")
                self.dateEdit_DOB_SA.setDate(defaultDate)
                self.ComboBox_OfficeLocations_SA.setCurrentIndex(0)
                self.LineEdit_AppointmentReason_SA.setText("")
                self.LineEdit_AppointmentType_SA.setText("")
                self.ComboBox_PhysicianNames_SA.setCurrentIndex(0)
                self.DateEdit_AppDate_SA.setDate(defaultDate)

                self.ListWidget_AppointmentTypes_SA.clear()
                self.ListWidget_AvailableTimes_SA.clear()
        def scheduleAppointment_SA():
                print("Scheduling appointment.. (SA)")

        # Reschedule Appointment functions
        def displayCurrentAvailableTimesAndSearchedAppointments_RA():
                print("Displaying current available times and searched appointments.. (RA)")
        def rescheduleAppointment_RA():
                print("Rescheduling appointment.. (RA)")

        # Cancel Appointment functions
        def displaySearchedAppointments_CA():
                print("Displaying searched appointments.. (CA)")
        def cancelAppointment_CA():
                print("Cancelling appointment.. (CA)")

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

        #Hide the app
        self.hide()

    # This will make it so when the user clicks the red x, it closes all windows
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
# app.exec()
