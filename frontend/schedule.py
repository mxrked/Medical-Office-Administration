
from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QListWidget, QTimeEdit, QPushButton
from PyQt5.QtCore import QDate
from frontend.main_nav import Nav
from frontend.ui.assets.files.STYLING import disableCustomTime_Style, enableCustomTime_Style

class Schedule(Nav):
    def __init__(self):
        super(Schedule, self).__init__()

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
        print("Search_SA")
        return

    def scheduleAppointment(self, event):
        print("Schedule Appointment")
        pass

class Reschedule(Nav):
    def __init__(self):
        super(Reschedule, self).__init__()

        self.RA_OfficeLocationsComboBox = self.findChild(QComboBox, "ComboBox_OfficeLocations_RA")
        self.RA_PhysicianNamesComboBox = self.findChild(QComboBox, "ComboBox_PhysicianNames_RA")
        self.RA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_RA")
        self.RA_RescheduleDateDateEdit = self.findChild(QDateEdit, "DateEdit_RescheduleDate_RA")
        self.RA_SearchedAppointmentsListWidget = self.findChild(QListWidget, "ListWidget_SearchedAppointments_RA")
        self.RA_CurrentAvailableTimesListWidget = self.findChild(QListWidget, "ListWidget_CurrentAvailableTimes_RA")
        self.RA_DisplayTimesAppointmentsPushButton = self.findChild(QPushButton, "DisplayCurrentTimes_Btn_RA")
        self.RA_RescheduleAppointmentPushButton = self.findChild(QPushButton, "RescheduleAppointment_Btn_RA")
        self.RA_ClearInputsPushButton = self.findChild(QPushButton, "RA_ClearInputsBtn")

        self.RA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.RA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.RA_RescheduleDateDateEdit.setDate(QDate.currentDate())
        self.RA_RescheduleDateDateEdit.setMinimumDate(QDate.currentDate())
        self.RA_ClearInputsPushButton.mousePressEvent = lambda event: self.clearInputs()
        self.RA_DisplayTimesAppointmentsPushButton.mousePressEvent = lambda event: self.displayTimesApps()
        self.RA_RescheduleAppointmentPushButton.mousePressEvent = lambda event: self.rescheduleAppointment()

    def displayTimesApps(self):
        print("DisplayTimesApps")
        pass

    def rescheduleAppointment(self):
        print("RescheduleAppointments")
        pass

class Cancel(Nav):
    def __init__(self):
        super(Cancel, self).__init__()

        self.CA_OfficeLocationsComboBox = self.findChild(QComboBox, "ComboBox_OfficeLocations_CA")
        self.CA_PhysicianNamesComboBox = self.findChild(QComboBox, "ComboBox_PhysicianNames_CA")
        self.CA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_CA")
        self.CA_SearchedAppointmentsListWidget = self.findChild(QListWidget, "ListWidget_SearchedAppointments_CA")
        self.CA_SearchForAppointmentsPushButton = self.findChild(QPushButton, "SearchForAppointments_Btn_CA")
        self.CA_CancelAppointmentPushButton = self.findChild(QPushButton, "CancelAppointment_Btn_CA")
        self.CA_ClearInputsPushButton = self.findChild(QPushButton, "CA_ClearInputsBtn")


        self.CA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.CA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.CA_ClearInputsPushButton.mousePressEvent = lambda event: self.clearInputs()
        self.CA_SearchForAppointmentsPushButton.mousePressEvent = lambda event: self.search_CA()
        self.CA_CancelAppointmentPushButton.mousePressEvent = lambda event: self.cancelAppointment()

    def search_CA(self):
        print("Search SA")
        pass

    def cancelAppointment(self):
        print("Cancel Appointment")
        pass
