"""
scheduling_windows.py - A set of classes that all inherit eachother for
    the purpose of making different screens in the Appointment window easier
Authors: Parker Phelps, Jessica Weeks
"""
from PyQt5.QtWidgets import QDateEdit, QLineEdit, QComboBox, QListWidget, QTimeEdit, QPushButton
from PyQt5.QtCore import QDate
from frontend.abstract_main_window import AMainWindow
from frontend.ui.assets.files.STYLING import *
from backend.data_handler import get_selected_combo_box_object

class ScheduleAppt_AMW(AMainWindow):
    
    def __init__(self):
        super(ScheduleAppt_AMW, self).__init__()


    def load_SA(self):
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

        self.SA_PatientDOBDateEdit.setDate(QDate.currentDate())
        self.SA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.SA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.SA_ClearInputsPushButton.mousePressEvent = lambda event: self.clearInputs()
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.mousePressEvent = self.disableCustomTime
        self.SA_YesCustomTimePushButton.mousePressEvent = self.enableCustomTime
        self.SA_SearchPushButton.mousePressEvent = self.search_SA
        self.SA_ScheduleAppointmentPushButton.mousePressEvent = self.scheduleAppointment

    def disableCustomTime(self, event):
        
        # Appending false to customTime
        self.custom_time = False

        self.SA_YesCustomTimePushButton.setVisible(True)
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_CustomTimeTimeEdit.setEnabled(False)
        self.SA_CustomTimeTimeEdit.setStyleSheet(disableCustomTime_Style)

    def enableCustomTime(self, event):
        
        # Appending true to customTime
        self.custom_time = True

        self.SA_YesCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.setVisible(True)
        self.SA_CurrentAvailableTimesListWidget.clearSelection()
        self.SA_CustomTimeTimeEdit.setEnabled(True)
        self.SA_CustomTimeTimeEdit.setStyleSheet(enableCustomTime_Style)

    def search_SA(self, event):

        lines_to_check = [self.SA_PatientFNLineEdit,
            self.SA_PatientLNLineEdit,
            self.SA_PatientDOBDateEdit,
            self.SA_AppointmentReasonLineEdit]
        entered_inputs = self.checkInputs(lines_to_check)

        # Check if combo_boxes correspond to object:
        if (get_selected_combo_box_object(self.SA_OfficeLocationsComboBox) and
            get_selected_combo_box_object(self.SA_PhysicianNamesComboBox) and
            get_selected_combo_box_object(self.SA_AppointmentTypesComboBox)):

            combo_boxes_entered = True
        else:
            combo_boxes_entered = False

        if (not entered_inputs) or (not combo_boxes_entered):
            self.load_error("Please Enter in all inputs")
            return

    def scheduleAppointment(self, event):
        
        pass

class RescheduleAppt_AMW(ScheduleAppt_AMW):

    def __init__(self):
        super(ScheduleAppt_AMW, self).__init__()
        

    def load_RA(self):





class CancelAppt_AMW(RescheduleAppt_AMW):
    def __init__(self):
        super(CancelAppt_AMW, self).__init__()




class Appointments_AMW(CancelAppt_AMW):
    """
    The one to interface with and make a window out of,

    This initalized all the window specific nav stuff
    """
    def __init__(self):
        super(Appointments_AMW, self).__init__()
    
    def hideAllFrames(self):

        # All frames have a height of 681
        self.InputsFrame.setFixedHeight(0)
        self.CancelAppointment_Frame.setFixedHeight(0)
        self.RescheduleAppointment_Frame.setFixedHeight(0)

        # Re-enabling the frame btn togglers
        self.DisplaySchedule_Btn.setEnabled(True)
        self.DisplayCancel_Btn.setEnabled(True)
        self.DisplayReschedule_Btn.setEnabled(True)

        # Restyling frame btn togglers
        self.DisplaySchedule_Btn.setStyleSheet(enableFrameBtn_Style)
        self.DisplayCancel_Btn.setStyleSheet(enableFrameBtn_Style)
        self.DisplayReschedule_Btn.setStyleSheet(enableFrameBtn_Style)

    
    def displayInputsFrame(self):

        self.hideAllFrames()
        self.InputsFrame.setFixedHeight(681)

        # Disabling the toggler btn
        self.DisplaySchedule_Btn.setEnabled(False)
        self.DisplaySchedule_Btn.setStyleSheet(disableFrameBtn_Style)


    def displayCancelAppointmentFrame(self):

        self.hideAllFrames()
        self.CancelAppointment_Frame.setFixedHeight(681)

         # Disabling the toggler btn
        self.DisplayCancel_Btn.setEnabled(False)
        self.DisplayCancel_Btn.setStyleSheet(disableFrameBtn_Style)
        
        self.load_CA()


    def displayRescheduleAppointmentFrame(self):

        self.hideAllFrames()
        self.RescheduleAppointment_Frame.setFixedHeight(681)

        # Disabling the toggler btn
        self.DisplayReschedule_Btn.setEnabled(False)
        self.DisplayReschedule_Btn.setStyleSheet(disableFrameBtn_Style)

        self.load_RA()


    def load_appointment_nav(self):
        # Appiontment Nav 
        self.newPatientPushButton = self.findChild(QPushButton, "NewPatient_Btn")
        self.reschedulingPushButton = self.findChild(QPushButton, "DisplayReschedule_Btn")
        self.makeSchedulePushButton = self.findChild(QPushButton, "DisplaySchedule_Btn")
        self.cancelPushButton = self.findChild(QPushButton, "DisplayCancel_Btn")

                # Events for buttons
        self.newPatientPushButton.mousePressEvent = lambda event: self.enterNewPatientWindow()
        self.reschedulingPushButton.clicked.connect(self.displayRescheduleAppointmentFrame)
        self.makeSchedulePushButton.clicked.connect(self.displayInputsFrame)
        self.cancelPushButton.clicked.connect(self.displayCancelAppointmentFrame)
