"""
utility.py - A bunch of utlity functions that are used by every screen.
Author: Jessica Weeks
"""
import sys 
from datetime import date
from PyQt5.QtWidgets import QWidget, QLineEdit, QDateEdit, QTimeEdit, QDialog, \
    QVBoxLayout, QLabel, QDateEdit, QTimeEdit, QComboBox, QPushButton
from PyQt5.QtCore import QDate, Qt
from PyQt5 import QtGui
from backend.user_dm import UserDM
from backend.misc_dm import MiscDM
from backend.appointment_dm import AppointmentDM
from backend.data_handler import load_objects_to_combo_box
from backend.models import Patient
from frontend.main_nav import Nav
from frontend.ui.assets.files.STYLING import infoDialog_Style, infoDialogCloseBtn_Style, infoDialogName_Style
from frontend.ListOfPatientsDialog import ListOfPatientsDialog
class Utility(Nav):
    """
        Handles general utility that all screens use

        • Initalizing data handlers
        • clearInputs (Clears ALL inputs)
        • closeEvent (What happens when program closes)
        • 
    
    """
    def __init__(self):
        super(Utility, self).__init__()

        # Data Managers
        self.user_dm = UserDM()
        self.misc_dm = MiscDM()
        self.appointment_dm = AppointmentDM()

    
    def clear_inputs(self):
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
                widget.setDate(QDate.currentDate())
        
    
    def closeEvent(self, event): # Do not change name, needs to be the same as QMainWindow's
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
                load_error(error_text = str(e))
                return
            
            :param error_text: str to be displayed as errors 
        """
        info_dialog = QDialog()
        info_dialog.setStyleSheet(infoDialog_Style)

        # Dialog settings
        info_dialog.setWindowFlags(Qt.FramelessWindowHint) # Hides the title bar
        info_dialog.setFixedSize(400, 400)

        info_layout = QVBoxLayout()
        info_close_btn = QPushButton("CLOSE", info_dialog)
        info_close_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))

        info_close_btn.setStyleSheet(infoDialogCloseBtn_Style)
        info_close_btn.setFont(QtGui.QFont("Lato", 12))
        info_close_btn.clicked.connect(info_dialog.close) # Closes the dialog box

        info_label = QLabel(error_text)
        info_label.setStyleSheet(infoDialogName_Style)
        info_label.setFont(QtGui.QFont("Lato", 13))
        info_layout.addWidget(info_label, alignment=Qt.AlignmentFlag.AlignCenter)
        info_layout.addWidget(info_close_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        info_dialog.setLayout(info_layout)

        # Displaying the dialog
        info_dialog.exec_()


    def load_locations(self, combo_box: QComboBox):
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
        load_objects_to_combo_box(locations, combo_box)
        combo_box.setCurrentIndex(int(default_location))


    def load_physicians(self, combo_box: QComboBox, location_id=None):
        """
            Loads all physicians into the combo_box,
                just provide the relevant data_manager

            :param combo_box: The combo box you wanna add stuff too
            :param location_id: The location ID. Can be "All"

            We do this several times in the frontend. 
                This prevents duplicate code
        """

        if location_id is None:
            location_id = int(self.settings_json["default_location_ID"])
        elif location_id == "All":
            location_id = None

        physicians = self.user_dm.get_physicians(location_id)
        load_objects_to_combo_box(physicians, combo_box)

    def get_verified_patient(self, f_name: str, l_name: str, dob: date) -> Patient:
        """
            In multiple sections we need to get a patient and verify (with a assert)
                that one was found. This handles that

            This also handles if more than 2 patients are found

            :param f_name: Patients first name
            :param l_name: Patients last name
            :param dob: Patients dob using a datatime date object
        """
        
        patients = self.user_dm.get_patients(first_name=f_name,
                                                    last_name=l_name,
                                                    dob=dob)

        assert len(patients) != 0 , "No Patients Found"
        if len(patients) > 1:
            # Removes all but the selected item from the dialog
            patients = [self.display_settings_dialog(patients)]
        
        assert patients[0] is not None, "No Patient Selected"

        return patients[0]


    def display_settings_dialog(self, patients: list[Patient]):
        """
            Pops up a dialog window for the soul purpose of resolving mutltiple patients
                User not allowed to leave until a patient is selected

            :param patients: list of Patient Objects

            :returns patient: The resolved patient
        """

        subwindow = ListOfPatientsDialog(patients)
        subwindow.setWindowModality(Qt.ApplicationModal)

        if subwindow.exec_() == QDialog.Accepted:
            return subwindow.get_patient()
