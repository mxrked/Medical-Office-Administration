
from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QLabel, QListWidget, QTimeEdit, QPushButton, QCalendarWidget
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from frontend.main_nav import Nav
from frontend.ui.assets.files.STYLING import disableCustomTime_Style, enableCustomTime_Style
from backend.data_handler import set_objects_to_combo_box, get_selected_combo_box_object, get_selected_list_object, set_objects_to_list
from backend.appointment_dm import AppointmentDM
from backend.misc_dm import MiscDM
from backend.user_dm import UserDM
from datetime import timedelta

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
        self.SA_AppointmentLengthLineEdit = self.findChild(QLineEdit, "LineEdit_ApptLength_SA")
        self.SA_AppointmentDateDateEdit = self.findChild(QDateEdit, "DateEdit_AppDate_SA")
        self.SA_CurrentAvailableTimesListWidget = self.findChild(QListWidget, "ListWidget_AvailableTimes_SA")
        self.SA_CustomTimeTimeEdit = self.findChild(QTimeEdit, "timeEdit_CustomTime_SA")
        self.SA_YesCustomTimePushButton = self.findChild(QPushButton, "yesCustomTimePushButton_SA")
        self.SA_NoCustomTimePushButton = self.findChild(QPushButton, "noCustomTimePushButton_SA")
        

        # Calanders
        self.SA_AppDate_cal = self.findChild(QCalendarWidget, "SA_AppDate_Cal")
        self.SA_App_Date_Label = self.findChild(QLabel, "SA_App_Date_Cal")
        self.SA_DOB_Cal = self.findChild(QCalendarWidget, "SA_DOB_Cal")
        self.SA_Patient_DOB_Cal = self.findChild(QLabel, "SA_Patient_DOB_Cal")

        self.SA_App_Date_Label.mousePressEvent = lambda event: \
            self.toggle_widget(self.SA_AppDate_cal)

        self.SA_Patient_DOB_Cal.mousePressEvent = lambda event: \
            self.toggle_widget(self.SA_DOB_Cal)
        
        self.SA_AppDate_cal.setVisible(False)
        self.SA_DOB_Cal.setVisible(False)

        # Making the appointment lenght be only numbers
        self.SA_ApptLengthValidator = QIntValidator()

        self.SA_AppointmentLengthLineEdit.setValidator(self.SA_ApptLengthValidator)

        self.SA_SearchPushButton = self.findChild(QPushButton, "Search_Btn_SA")
        self.SA_ClearInputsPushButton = self.findChild(QPushButton, "ClearInputsBtn")
        self.SA_ScheduleAppointmentPushButton = self.findChild(QPushButton, "ScheduleAppointmentBtn")

        self.SA_PatientDOBDateEdit.setDate(QDate.currentDate())
        self.SA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.SA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.SA_ClearInputsPushButton.mousePressEvent = lambda event: self.clearInputs()
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.clicked.connect(self.disableCustomTime)
        self.SA_YesCustomTimePushButton.clicked.connect(self.enableCustomTime)
        self.SA_SearchPushButton.clicked.connect(self.search_SA)
        self.SA_ScheduleAppointmentPushButton.clicked.connect(self.scheduleAppointment)

        

        set_objects_to_combo_box(self.appointment_dm.get_appointment_types(), self.SA_AppointmentTypesComboBox)

        self.get_locations_into(self.SA_OfficeLocationsComboBox)
        self.get_physicians_into(self.SA_PhysicianNamesComboBox)

        self.custom_time = False


    def disableCustomTime(self):
        # Appending false to customTime
        self.custom_time = False

        self.SA_YesCustomTimePushButton.setVisible(True)
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_CustomTimeTimeEdit.setEnabled(False)
        self.SA_CustomTimeTimeEdit.setStyleSheet(disableCustomTime_Style)

    def enableCustomTime(self):

        # Appending true to customTime
        self.custom_time = True

        self.SA_YesCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.setVisible(True)
        self.SA_CurrentAvailableTimesListWidget.clearSelection()
        self.SA_CustomTimeTimeEdit.setEnabled(True)
        self.SA_CustomTimeTimeEdit.setStyleSheet(enableCustomTime_Style)

    def search_SA(self):
        
        SA_patientFN = self.SA_PatientFNLineEdit.text()
        SA_patientLN = self.SA_PatientLNLineEdit.text()
        SA_patientDOB = self.SA_PatientDOBDateEdit.date().toPyDate()
        SA_officeLocation = get_selected_combo_box_object(self.SA_OfficeLocationsComboBox)
        SA_appointmentReason = self.SA_AppointmentReasonLineEdit.text()
        SA_appointmentType = get_selected_combo_box_object(self.SA_AppointmentTypesComboBox)
        SA_appointmentLength = self.SA_AppointmentLengthLineEdit.text()
        SA_physicianName = get_selected_combo_box_object(self.SA_PhysicianNamesComboBox)
        SA_appointmentDate = self.SA_AppointmentDateDateEdit.date().toPyDate()

        patients = self.user_dm.get_patient(first_name=SA_patientFN,
                                                    last_name=SA_patientLN,
                                                    dob=SA_patientDOB)

        if len(patients) == 0:
            self.load_error("No Patients")
            return
        if len(patients) > 1:
            self.load_error("More than one patient")
            return

        patient = patients[0]

        try:
            assert SA_appointmentReason != "", "Appointment Reason"
            assert SA_appointmentLength.isdigit(), "Appointment Length"

        except AssertionError as error:
            self.load_error("Invalid:" + str(error))
            return

        appt_length = timedelta(minutes=int(SA_appointmentLength))
        availableTimes = self.appointment_dm.get_avaliable_appointments(
            appt_date=SA_appointmentDate,
            provider=SA_physicianName,
            location=SA_officeLocation,
            appt_type=SA_appointmentType,
            appt_length=appt_length,
            patient=patient,
            appt_reason=SA_appointmentReason
            )
        
        set_objects_to_list(availableTimes, self.SA_CurrentAvailableTimesListWidget)

    def scheduleAppointment(self):

        SA_availableTime = get_selected_list_object(self.SA_CurrentAvailableTimesListWidget)
        print("Schedule Appointment")



class Reschedule(Nav):
    def __init__(self):
        super(Reschedule, self).__init__()

        RA_Locations = MiscDM().get_locations()
        RA_Physicians = UserDM().get_physicians()

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

        set_objects_to_combo_box(RA_Locations, self.RA_OfficeLocationsComboBox)
        set_objects_to_combo_box(RA_Physicians, self.RA_PhysicianNamesComboBox)

    def displayTimesApps(self):
        print("DisplayTimesApps")
        

    def rescheduleAppointment(self):
        print("RescheduleAppointments")
        

class Cancel(Nav):
    def __init__(self):
        super(Cancel, self).__init__()

        CA_Locations = MiscDM().get_locations()
        CA_Physicians = UserDM().get_physicians()

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

        set_objects_to_combo_box(CA_Locations, self.CA_OfficeLocationsComboBox)
        set_objects_to_combo_box(CA_Physicians, self.CA_PhysicianNamesComboBox)

    def search_CA(self):
        print("Search SA")
        

    def cancelAppointment(self):
        print("Cancel Appointment")
        
