"""
main_nav - Handles Main Window Navigation
Author: Jessica Weeks, Parker Phelps
"""
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget,\
    QLineEdit, QStackedWidget, QFrame, QDialog, QVBoxLayout, QLabel, QDateEdit, QTimeEdit
from PyQt5 import QtCore, QtGui, uic
from frontend.ui.assets.files.STYLING import disableFrameBtn_Style, infoDialog_Style, \
    infoDialogCloseBtn_Style, infoDialogName_Style, enableFrameBtn_Style
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo
from backend.private.data_manager import DataManager
from frontend.StartWindow import UI

class Nav(QMainWindow):
    """
    Handles Navigation for all windows but StartWindow

    Also has some basic helper functions like self.clearInputs
    """
    def __init__(self):
        super(Nav, self).__init__()

        uic.loadUi("frontend/ui/mainWindow.ui", self)

        self.main_stacked_widget = self.findChild(QStackedWidget, "main_stacked_widget")

        # Define Main Nav
        self.logout_btn = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointments_btn = self.findChild(QPushButton, "Nav_Appointments")
        self.checkin_btn = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkout_btn = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.referral_btn = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.lab_orders_btn = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approve_appointment_btn = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")

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
        self.appointments_btn.mousePressEvent = lambda event: \
            self.enterSchedulingAppointmentsWindow()
        self.checkin_btn.mousePressEvent = lambda event: self.enterCheckInWindow()
        self.checkout_btn.mousePressEvent = lambda event: self.enterCheckOutWindow()
        self.referral_btn.mousePressEvent = lambda event: self.enterMakeReferralWindow()
        self.lab_orders_btn.mousePressEvent = lambda event: self.enterLabOrdersWindow()
        self.approve_appointment_btn.mousePressEvent = lambda event: \
            self.enterAppointmentApproveViaPortalWindow()
        self.logout_btn.mousePressEvent = lambda event: self.logout()

        # Appointment Nav
        self.new_patient_btn = self.findChild(QPushButton, "NewPatient_Btn")
        self.rescheduling_btn = self.findChild(QPushButton, "DisplayReschedule_Btn")
        self.make_schedule_btn = self.findChild(QPushButton, "DisplaySchedule_Btn")
        self.cancel_btn = self.findChild(QPushButton, "DisplayCancel_Btn")

        # Nav Frames

        self.inputs_frame = self.findChild(QFrame, "InputsFrame")
        self.cancel_appt_frame = self.findChild(QFrame, "CancelAppointment_Frame")
        self.reschedule_appt_frame = self.findChild(QFrame, "RescheduleAppointment_Frame")
        self.patient_frame = self.findChild(QFrame, "PatientFrame")

        # Events for buttons
        self.new_patient_btn.mousePressEvent = lambda event: self.display_patient_frame()
        self.rescheduling_btn.clicked.connect(self.display_reschedule_frame)
        self.make_schedule_btn.clicked.connect(self.display_inputs_frame)
        self.cancel_btn.clicked.connect(self.display_canceled_frame)


    def logout(self):
        # UI from frontend
        new_window = UI()

        new_window.show()

        self.hide()

    def hide_all_frames(self):

        # All frames have a height of 681
        self.inputs_frame.setFixedHeight(0)
        self.cancel_appt_frame.setFixedHeight(0)
        self.reschedule_appt_frame.setFixedHeight(0)
        self.patient_frame.setFixedHeight(0)

        # Re-enabling the frame btn togglers
        self.enable_nav(self.DisplaySchedule_Btn)
        self.enable_nav(self.DisplayCancel_Btn)
        self.enable_nav(self.DisplayReschedule_Btn)
        self.enable_nav(self.new_patient_btn)


    def display_inputs_frame(self):

        self.hide_all_frames()
        self.inputs_frame.setFixedHeight(681)
        self.inputs_frame.setFixedWidth(1171)

        # Disabling the toggler btn
        self.disable_nav(self.DisplaySchedule_Btn)


    def display_canceled_frame(self):

        self.hide_all_frames()
        self.cancel_appt_frame.setFixedHeight(681)
        self.cancel_appt_frame.setFixedWidth(1171)

         # Disabling the toggler btn
        self.disable_nav(self.DisplayCancel_Btn)



    def display_reschedule_frame(self):

        self.hide_all_frames()
        self.reschedule_appt_frame.setFixedHeight(681)
        self.reschedule_appt_frame.setFixedWidth(1171)

        # Disabling the toggler btn
        self.disable_nav(self.DisplayReschedule_Btn)

    def display_patient_frame(self):
        self.hide_all_frames()
        self.patient_frame.setFixedHeight(681)
        self.patient_frame.setFixedWidth(1171)

        self.disable_nav(self.new_patient_btn)




    def disable_nav(self, btn):
        btn.setStyleSheet(disableFrameBtn_Style)
        btn.setEnabled(False)

    def disable_all_nav(self):
        nav_buttons = [
            self.appointments_btn,
            self.checkin_btn,
            self.checkout_btn,
            self.referral_btn,
            self.lab_orders_btn,
            self.approve_appointment_btn
        ]

        for btn in nav_buttons:
            self.disable_nav(btn)

    def enable_all_nav_with_access(self):
        """
        Enables all buttons in which the user has permission for
        """
        # Somehow get permissions info

        scheduling_nav =[
            self.appointments_btn,
            self.checkin_btn,
            self.checkout_btn,
            self.approve_appointment_btn
        ]

        physician_nav =[
            self.referral_btn,
            self.lab_orders_btn,
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
        self.disable_nav(self.appointments_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments")


    def enterCheckInWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["CheckIn"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.checkin_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Check In")

    def enterCheckOutWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["CheckOut"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.checkout_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Check Out")

    
    def enterMakeReferralWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Referral"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.referral_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Referrals")

    def enterLabOrdersWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Lab"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.lab_orders_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Lab Orders")

    def enterAppointmentApproveViaPortalWindow(self):
        self.main_stacked_widget.setCurrentIndex(
            self.windows_indexes["Approve"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.approve_appointment_btn)

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
