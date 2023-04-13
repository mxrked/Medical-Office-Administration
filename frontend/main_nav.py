from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget,\
    QLineEdit, QStackedWidget, QFrame, QDialog, QVBoxLayout, QLabel, QDateEdit, QTimeEdit
from PyQt5 import QtCore, QtGui, uic
import sys
from frontend.ui.assets.files.STYLING import *
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo
from backend.private.data_manager import DataManager


class Nav(QMainWindow):
    def __init__(self):
        super(Nav, self).__init__()

        uic.loadUi("frontend/ui/mainWindow.ui", self)

        self.main_stacked_widget = self.findChild(QStackedWidget, "main_stacked_widget")

        # Define Main Nav
        self.logoutPushButton = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointmentsPushButton = self.findChild(QPushButton, "Nav_Appointments")
        self.checkinPushButton = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkoutPushButton = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.makeReferralPushButton = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.labOrdersPushButton = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approveAppointmentsPushButton = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")
        
        # Define needed labels
        #self.currentUserLabel = self.findChild(QLabel, "currentUserLabel")

        # Corresponds to QStackedWidget's pages
        self.windows_indexes = {

            "Appointment" : 0,
            "CheckIn" : 1,
            "CheckOut" : 2,
            "Referral" : 3,
            "Lab" : 4,
            "Approve" : 5
        }

        # For Navigation Permissions
        self.can_schedule = True
        self.can_physician = True

        # Connect Nav Buttons
        self.appointmentsPushButton.mousePressEvent = lambda event: self.enterSchedulingAppointmentsWindow()
        self.checkinPushButton.mousePressEvent = lambda event: self.enterCheckInWindow()
        self.checkoutPushButton.mousePressEvent = lambda event: self.enterCheckOutWindow()
        self.makeReferralPushButton.mousePressEvent = lambda event: self.enterMakeReferralWindow()
        self.labOrdersPushButton.mousePressEvent = lambda event: self.enterLabOrdersWindow()
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: self.enterAppointmentApproveViaPortalWindow()
        self.logoutPushButton.mousePressEvent = lambda event: self.logout()

        # Appointment Nav
        self.newPatientPushButton = self.findChild(QPushButton, "NewPatient_Btn")
        self.reschedulingPushButton = self.findChild(QPushButton, "DisplayReschedule_Btn")
        self.makeSchedulePushButton = self.findChild(QPushButton, "DisplaySchedule_Btn")
        self.cancelPushButton = self.findChild(QPushButton, "DisplayCancel_Btn")
        
        # Nav Frames

        self.InputsFrame = self.findChild(QFrame, "InputsFrame")
        self.CancelAppointment_Frame = self.findChild(QFrame, "CancelAppointment_Frame")
        self.RescheduleAppointment_Frame = self.findChild(QFrame, "RescheduleAppointment_Frame")
        self.PatientFrame = self.findChild(QFrame, "PatientFrame")

        # Events for buttons
        self.newPatientPushButton.mousePressEvent = lambda event: self.enterNewPatientWindow()
        self.reschedulingPushButton.clicked.connect(self.displayRescheduleAppointmentFrame)
        self.makeSchedulePushButton.clicked.connect(self.displayInputsFrame)
        self.cancelPushButton.clicked.connect(self.displayCancelAppointmentFrame)

    
    def logout(self):
        from frontend.StartWindow import UI
        
        new_window = UI()

        new_window.show()

        self.hide()

    def hideAllFrames(self):

        # All frames have a height of 681
        self.InputsFrame.setFixedHeight(0)
        self.CancelAppointment_Frame.setFixedHeight(0)
        self.RescheduleAppointment_Frame.setFixedHeight(0)
        self.PatientFrame.setFixedHeight(0)

        # Re-enabling the frame btn togglers
        self.enable_nav(self.DisplaySchedule_Btn)
        self.enable_nav(self.DisplayCancel_Btn)
        self.enable_nav(self.DisplayReschedule_Btn)
        self.enable_nav(self.newPatientPushButton)

    
    def displayInputsFrame(self):

        self.hideAllFrames()
        self.InputsFrame.setFixedHeight(681)
        self.InputsFrame.setFixedWidth(1171)

        # Disabling the toggler btn
        self.disable_nav(self.DisplaySchedule_Btn)


    def displayCancelAppointmentFrame(self):

        self.hideAllFrames()
        self.CancelAppointment_Frame.setFixedHeight(681)
        self.CancelAppointment_Frame.setFixedWidth(1171)

         # Disabling the toggler btn
        self.disable_nav(self.DisplayCancel_Btn)



    def displayRescheduleAppointmentFrame(self):

        self.hideAllFrames()
        self.RescheduleAppointment_Frame.setFixedHeight(681)
        self.RescheduleAppointment_Frame.setFixedWidth(1171)

        # Disabling the toggler btn
        self.disable_nav(self.DisplayReschedule_Btn)

    def enterNewPatientWindow(self):
        self.hideAllFrames()
        self.PatientFrame.setFixedHeight(681)
        self.PatientFrame.setFixedWidth(1171)

        self.disable_nav(self.newPatientPushButton)



        
    def disable_nav(self, btn):
        btn.setStyleSheet(disableFrameBtn_Style)
        btn.setEnabled(False)

    def disable_all_nav(self):
        nav_buttons = [
            self.appointmentsPushButton,
            self.checkinPushButton,
            self.checkoutPushButton,
            self.makeReferralPushButton,
            self.labOrdersPushButton,
            self.approveAppointmentsPushButton
        ]

        for btn in nav_buttons:
            self.disable_nav(btn)

    def enable_all_nav_with_access(self):
        """
        Enables all buttons in which the user has permission for
        """
        # Somehow get permissions info

        scheduling_nav =[
            self.appointmentsPushButton,
            self.checkinPushButton,
            self.checkoutPushButton,
            self.approveAppointmentsPushButton
        ]

        physician_nav =[
            self.makeReferralPushButton,
            self.labOrdersPushButton,
        ]

        nav_buttons = []

        if self.can_schedule:
            nav_buttons.extend(scheduling_nav)

        if self.can_physician:
            nav_buttons.extend(physician_nav)

        for btn in nav_buttons:
            self.enable_nav(btn)

    def enable_nav(self, btn):
        btn.setStyleSheet(enableFrameBtn_Style)
        btn.setEnabled(True)

    def enterSchedulingAppointmentsWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Appointment"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.appointmentsPushButton)

        self.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments")


    def enterCheckInWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["CheckIn"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.checkinPushButton)

        self.setWindowTitle("Forsyth Family Practice Center - Check In")

    def enterCheckOutWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["CheckOut"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.checkoutPushButton)

        self.setWindowTitle("Forsyth Family Practice Center - Check Out")

    
    def enterMakeReferralWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Referral"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.makeReferralPushButton)

        self.setWindowTitle("Forsyth Family Practice Center - Referrals")

    def enterLabOrdersWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Lab"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.labOrdersPushButton)

        self.setWindowTitle("Forsyth Family Practice Center - Lab Orders")

    def enterAppointmentApproveViaPortalWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Approve"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.approveAppointmentsPushButton)

        self.setWindowTitle("Forsyth Family Practice Center - Approve Appointments")

    def clearInputs(self):
        """
            Resets all widgets everywhere!
            Use with caution
        """
        for widget in self.findChildren(QWidget):
            # Clears Line Edits
            if isinstance(widget, QLineEdit) and not isinstance(widget, (QDateEdit, QTimeEdit)):
                widget.clear()
                # Otherwise Certain widgets are selected, for some reason
                widget.selectAll()
                widget.deselect()

            # Clears DateEdits
            if isinstance(widget, QDateEdit) and not isinstance(widget, (QTimeEdit, QLineEdit)):
                widget.setDate(QtCore.QDate.currentDate())
    
    def closeEvent(self, event):
        """
            Closes all data managers before exiting the program
        """

        for var_name in vars(self):

            if isinstance( getattr(self, var_name), DataManager):
                delattr(self, var_name)

        sys.exit()
    
    def load_error(self, error_text: str):
        """
            Loads simple error text box popup with the error_text and a
            close button

            This can be used for db calls that may return error:
            try: 
                add_appointment(appointment)
            except AssertionError as e: 
                load_error(error_text=e)
                return
            
            :param error_text: str to be displayed as errors 
        """
        infoDialog = QDialog()
        infoDialog.setStyleSheet(infoDialog_Style)

        # Dialog settings
        infoDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        infoDialog.setFixedSize(400, 400)

        infoDialogLayout = QVBoxLayout()
        infoDialogCloseBtn = QPushButton("CLOSE", infoDialog)
        infoDialogCloseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        infoDialogCloseBtn.setStyleSheet(infoDialogCloseBtn_Style)
        infoDialogCloseBtn.setFont(QtGui.QFont("Lato", 12))
        infoDialogCloseBtn.clicked.connect(infoDialog.close) # Closes the dialog box

        infoDialogName = QLabel(error_text)
        infoDialogName.setStyleSheet(infoDialogName_Style)
        infoDialogName.setFont(QtGui.QFont("Lato", 13))
        infoDialogLayout.addWidget(infoDialogName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        infoDialogLayout.addWidget(infoDialogCloseBtn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        infoDialog.setLayout(infoDialogLayout)

        # Displaying the dialog
        infoDialog.exec_()

#initializing app
app = QApplication(sys.argv)
UIWindow = Nav()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
