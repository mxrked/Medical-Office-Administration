from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.GLOBALS import *
from frontend.ui.assets.files.NAVIGATION_FUNCS import *
from frontend.ui.assets.files.SCHEDULING_LISTENERS import *

from abstract_main_window import AppointmentMainWindow
import sys



class UI(AppointmentMainWindow):
    def __init__(self):


        super(UI, self).__init__()

        uic.loadUi("frontend/ui/SchedulingAppointmentsWindow.ui", self)

        self.load_nav()


        #define widgets

        # Appiontment Nav 
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


        # Events for buttons
        self.newPatientPushButton.mousePressEvent = lambda event: enterNewPatientWindow(self)
        self.reschedulingPushButton.clicked.connect(self.displayRescheduleAppointmentFrame)
        self.makeSchedulePushButton.clicked.connect(self.displayInputsFrame)
        self.cancelPushButton.clicked.connect(self.displayCancelAppointmentFrame)

        self.SA_PatientDOBDateEdit.setDate(QDate.currentDate())
        self.SA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.SA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.SA_ClearInputsPushButton.mousePressEvent = lambda event: clearInputs_SA(self)
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.mousePressEvent = lambda event: disableCustomTime(self)
        self.SA_YesCustomTimePushButton.mousePressEvent = lambda event: enableCustomTime(self)
        self.SA_SearchPushButton.mousePressEvent = lambda event: search_SA(self)
        self.SA_ScheduleAppointmentPushButton.mousePressEvent = lambda event: scheduleAppointment(self)

        self.RA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.RA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.RA_RescheduleDateDateEdit.setDate(QDate.currentDate())
        self.RA_RescheduleDateDateEdit.setMinimumDate(QDate.currentDate())
        self.RA_ClearInputsPushButton.mousePressEvent = lambda event: clearInputs_RA(self)
        self.RA_DisplayTimesAppointmentsPushButton.mousePressEvent = lambda event: displayTimesApps_RA(self)
        self.RA_RescheduleAppointmentPushButton.mousePressEvent = lambda event: rescheduleAppointment(self)

        self.CA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.CA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.CA_ClearInputsPushButton.mousePressEvent = lambda event: clearInputs_CA(self)
        self.CA_SearchForAppointmentsPushButton.mousePressEvent = lambda event: search_CA(self)
        self.CA_CancelAppointmentPushButton.mousePressEvent = lambda event: cancelAppointment(self)



#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
