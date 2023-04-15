"""
main_nav - Handles Main Window Navigation
Author: Jessica Weeks, Parker Phelps
"""
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget,\
    QLineEdit, QStackedWidget, QFrame, QDialog, QVBoxLayout, QLabel, QDateEdit, QTimeEdit, QComboBox
from PyQt5 import QtCore, QtGui, uic
import datetime

from frontend.ui.assets.files.STYLING import disableFrameBtn_Style, infoDialog_Style, \
    infoDialogCloseBtn_Style, infoDialogName_Style, enableFrameBtn_Style

from frontend.StartWindow import Start

# These qrc are used by pyqt 5
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo # pylint: disable=unused-import
from backend.user_dm import UserDM, DataManager
from backend.misc_dm import MiscDM
from backend.appointment_dm import AppointmentDM
from backend.data_handler import set_objects_to_combo_box
import json

class Nav(QMainWindow):
    """
    Handles Navigation for all windows but StartWindow

    Also has some basic helper functions like self.clearInputs
    """
    def __init__(self):
        super(Nav, self).__init__()

        uic.loadUi("frontend/ui/mainWindow.ui", self)

        # Data Managers
        self.user_dm = UserDM()
        self.misc_dm = MiscDM()
        self.appointment_dm = AppointmentDM()

        # Load Settings
        try:
            with open("frontend/ui/assets/files/Settings.json", "r",
                      encoding='UTF-8') as settings_file:
                file_contents = settings_file.read()
        
            self.settings_json = json.loads(file_contents)

        except FileNotFoundError:
            print("Settings not found")
            self.settings_json = {
                "default_location_ID" : "1",
                "last_entered_user" : ""
            }
            with open("frontend/ui/assets/files/Settings.json", "w",
                      encoding='UTF-8') as file:
                json.dump(self.settings_json, file)

        # Used for debugging certain dates
        self.todays_date = datetime.datetime.now().date()

        self.stacked_widget = self.findChild(QStackedWidget, "main_stacked_widget")

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
        self.new_patient_btn.clicked.connect(self.display_patient_frame)
        self.rescheduling_btn.clicked.connect(self.display_reschedule_frame)
        self.make_schedule_btn.clicked.connect(self.display_inputs_frame)
        self.cancel_btn.clicked.connect(self.display_canceled_frame)

    
    def logout(self):
        """
            Shows the start window and closes the current one
        """
        # From the frontend
        new_window = Start()

        print(self.todays_date)

        new_window.show()

        self.hide()

    def hide_all_frames(self):
        """
            We used QStacked Widget for most our nav

            But, the Appointments window was build differently so we
                must modify the hights, this clears the screen 
                for moving to another screen
        """
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
        """ Opens 'Scheduling' Screen """
        self.hide_all_frames()
        self.inputs_frame.setFixedHeight(681)
        self.inputs_frame.setFixedWidth(1171)

        # Disabling the toggler btn
        self.disable_nav(self.DisplaySchedule_Btn)


    def display_canceled_frame(self):
        """ Opens 'Cancel' Screen """
        self.hide_all_frames()
        self.cancel_appt_frame.setFixedHeight(681)
        self.cancel_appt_frame.setFixedWidth(1171)

         # Disabling the toggler btn
        self.disable_nav(self.DisplayCancel_Btn)



    def display_reschedule_frame(self):
        """ Opens 'Reschedule' Screen """ 
        self.hide_all_frames()
        self.reschedule_appt_frame.setFixedHeight(681)
        self.reschedule_appt_frame.setFixedWidth(1171)

        # Disabling the toggler btn
        self.disable_nav(self.DisplayReschedule_Btn)

    def display_patient_frame(self):
        """ Opens 'New Patient' Screen """
        self.hide_all_frames()
        self.patient_frame.setFixedHeight(681)
        self.patient_frame.setFixedWidth(1171)

        self.disable_nav(self.new_patient_btn)


    def disable_nav(self, btn: QPushButton):
        """ Disables & Grey's out a particular nav button """
        btn.setStyleSheet(disableFrameBtn_Style)
        btn.setEnabled(False)

    def disable_all_nav(self):
        """
            Disables all navigation

            This is used at the start of the program so
                we can enable only those we have access to
                (Access is determined by superclasses params)
        """
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

            All others are left disabled
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
        """ Enables & ungreys a particular nav button """
        btn.setStyleSheet(enableFrameBtn_Style)
        btn.setEnabled(True)

    def enterSchedulingAppointmentsWindow(self):
        """
            Enters the scheduling appointment screen

            By default on Schedule appointment screen, but
                if window changed this persists
        """
        self.stacked_widget.setCurrentIndex(
            self.windows_indexes["Appointment"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.appointments_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments")


    def enterCheckInWindow(self):
        """ Enters the checkin screen """
        self.stacked_widget.setCurrentIndex(
            self.windows_indexes["CheckIn"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.checkin_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Check In")

    def enterCheckOutWindow(self):
        """ Eneters the check out screen """
        self.stacked_widget.setCurrentIndex(
            self.windows_indexes["CheckOut"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.checkout_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Check Out")

    
    def enterMakeReferralWindow(self):
        """ Enters the refferal screen """
        self.stacked_widget.setCurrentIndex(
            self.windows_indexes["Referral"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.referral_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Referrals")

    def enterLabOrdersWindow(self):
        """ Enters the Lab Order Screen """
        self.stacked_widget.setCurrentIndex(
            self.windows_indexes["Lab"]
        )
        self.enable_all_nav_with_access()
        self.disable_nav(self.lab_orders_btn)

        self.setWindowTitle("Forsyth Family Practice Center - Lab Orders")

    def enterAppointmentApproveViaPortalWindow(self):
        """ Enters the Approve Appointment Screen """
        self.stacked_widget.setCurrentIndex(
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

        data_managers = [self.user_dm, self.appointment_dm, self.misc_dm]

        for dm in data_managers:
            dm.close()

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
        info_dialog = QDialog()
        info_dialog.setStyleSheet(infoDialog_Style)

        # Dialog settings
        info_dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        info_dialog.setFixedSize(400, 400)

        info_layout = QVBoxLayout()
        info_close_btn = QPushButton("CLOSE", info_dialog)
        info_close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        info_close_btn.setStyleSheet(infoDialogCloseBtn_Style)
        info_close_btn.setFont(QtGui.QFont("Lato", 12))
        info_close_btn.clicked.connect(info_dialog.close) # Closes the dialog box

        info_label = QLabel(error_text)
        info_label.setStyleSheet(infoDialogName_Style)
        info_label.setFont(QtGui.QFont("Lato", 13))
        info_layout.addWidget(info_label, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        info_layout.addWidget(info_close_btn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        info_dialog.setLayout(info_layout)

        # Displaying the dialog
        info_dialog.exec_()

    def get_locations_into(self, combo_box: QComboBox):
        """
            Loads all locations into the combo_box,
                just provide the elevant data_manager

            :param misc_dm: use self.misc_dm
            :param combo_box: The combo box you wanna add stuff too
            
            We do this several times in the frontend. 
                This prevents duplicate code
        """
        
        default_location = self.settings_json["default_location_ID"]

        locations = self.misc_dm.get_locations()
        set_objects_to_combo_box(locations, combo_box)
        combo_box.setCurrentIndex(int(default_location))


    def get_physicians_into(self, combo_box: QComboBox):
        """
            Loads all physicians into the combo_box,
                just provide the elevant data_manager

            :param misc_dm: use self.misc_dm
            :param combo_box: The combo box you wanna add stuff too
            
            We do this several times in the frontend. 
                This prevents duplicate code
        """
        physicians = self.user_dm.get_physicians()
        set_objects_to_combo_box(physicians, combo_box)



#initializing app
app = QApplication(sys.argv)
UIWindow = Nav()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
