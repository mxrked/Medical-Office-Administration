
from PyQt5.QtWidgets import QLineEdit, QDateEdit, QComboBox, QLabel, QListWidget, QTimeEdit, QPushButton, QCalendarWidget
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from frontend.ui.assets.files.STYLING import disableCustomTime_Style, enableCustomTime_Style
from backend.data_handler import load_objects_to_combo_box, get_selected_combo_box_object, get_selected_list_object, load_objects_to_list
from frontend.utility import Utility
from datetime import timedelta, datetime, date

class Schedule(Utility):
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
        

        load_objects_to_combo_box(self.appointment_dm.get_appointment_types(), self.SA_AppointmentTypesComboBox)

        self.load_locations(self.SA_OfficeLocationsComboBox)
        self.load_physicians(self.SA_PhysicianNamesComboBox)

        self.SA_OfficeLocationsComboBox.currentIndexChanged.connect(self.change_location_sa)

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
    
    def change_location_sa(self):
        location = get_selected_combo_box_object(self.SA_OfficeLocationsComboBox)
        self.load_physicians(self.SA_PhysicianNamesComboBox, location_id=location.LocationID)

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

        

        try:
            patient = self.get_verified_patient(SA_patientFN,
                                                SA_patientLN,
                                                SA_patientDOB)
            assert SA_appointmentReason != "", "No appointment Reason"
            assert SA_appointmentLength.isdigit(), "Invalid appointment Length"

        except AssertionError as error:
            self.load_error(str(error))
            return

        appt_length = timedelta(minutes=int(SA_appointmentLength))

        try:
            availableTimes = self.appointment_dm.get_avaliable_appointments(
                appt_date=SA_appointmentDate,
                provider=SA_physicianName,
                location=SA_officeLocation,
                appt_type=SA_appointmentType,
                appt_length=appt_length,
                patient=patient,
                appt_reason=SA_appointmentReason
                )
            
            assert len(availableTimes) > 0, "No Appointments Found"
        except AssertionError as error:
            self.load_error(str(error))
            return
        
        load_objects_to_list(availableTimes, self.SA_CurrentAvailableTimesListWidget)

    def scheduleAppointment(self):

        first_item = self.SA_CurrentAvailableTimesListWidget.item(0)
        
        if first_item is None:
            self.load_error("Please Search for Appointments First")
            return
        
        appt = get_selected_list_object(self.SA_CurrentAvailableTimesListWidget)

        # They dont have to select a time if custom tmie
        if (appt is None) and self.custom_time:
            # A reminder from data_handlers we store classes of objects to the list
            appt = first_item.obj

            # We pull the custom time, covnert it for adding later
            start_time = self.SA_CustomTimeTimeEdit.time().toPyTime()
            start_datetime = datetime.combine(date.today(), start_time)

            # Pull the length
            SA_appointmentLength = self.SA_AppointmentLengthLineEdit.text()
            length = timedelta(minutes=int(SA_appointmentLength))
            
            # Modify it with custom time
            appt.ApptTime = start_time
            appt.ApptEndTime = start_datetime + length
        
        elif appt is None:
            self.load_error("No Item Selected")
            return
        
        try:
            self.appointment_dm.add_appointment(appt, self.custom_time)
        except AssertionError as error:
            self.load_error(str(error))
            return

        self.clearInputs()
        self.SA_CurrentAvailableTimesListWidget.clear()


class Reschedule(Utility):
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
        self.RA_DisplayNewTimes = self.findChild(QPushButton, "DisplayNewTimes_Btn_RA")

        self.RA_AppointmentDateDateEdit.setDate(QDate.currentDate())
        self.RA_AppointmentDateDateEdit.setMinimumDate(QDate.currentDate())
        self.RA_RescheduleDateDateEdit.setDate(QDate.currentDate())
        self.RA_RescheduleDateDateEdit.setMinimumDate(QDate.currentDate())
        self.RA_ClearInputsPushButton.mousePressEvent = lambda event: self.clearInputs()
        self.RA_DisplayTimesAppointmentsPushButton.mousePressEvent = lambda event: self.displayTimesApps()
        self.RA_DisplayNewTimes.mousePressEvent = lambda event: self.displayRescheduleAppointment()
        self.RA_RescheduleAppointmentPushButton.mousePressEvent = lambda event: self.rescheduleAppointment()

        self.load_locations(self.RA_OfficeLocationsComboBox)
        self.load_physicians(self.RA_PhysicianNamesComboBox)

        self.RA_OfficeLocationsComboBox.currentIndexChanged.connect(self.ra_switch_locations)

    def ra_switch_locations(self):
        
        location = get_selected_combo_box_object(self.RA_OfficeLocationsComboBox) # Location ID starts with 1

        self.load_physicians(
            self.RA_PhysicianNamesComboBox,
            location_id = location.LocationID
        ) 

    def displayTimesApps(self):
        
        old_date = self.RA_AppointmentDateDateEdit.date().toPyDate()
        physician = get_selected_combo_box_object(self.RA_PhysicianNamesComboBox)

        old_appointments = self.appointment_dm.get_appointments_for_date(old_date, physician)

        try:
            assert len(old_appointments) > 0, "No Appointments Found"
        except AssertionError as error:
            self.load_error(str(error))

        load_objects_to_list(old_appointments, self.RA_SearchedAppointmentsListWidget)


    def displayRescheduleAppointment(self):

        new_date = self.RA_RescheduleDateDateEdit.date().toPyDate()

        appt = get_selected_list_object(self.RA_SearchedAppointmentsListWidget)

        try:
            assert appt is not None, "Appointment Not Selected"

        except AssertionError as error:
            self.load_error(str(error))
            return

        available_times = self.appointment_dm.get_appointments_for_reschedule(
            appt = appt,
            check_date = new_date
        )

        load_objects_to_list(available_times, self.RA_CurrentAvailableTimesListWidget)

        # Used so we could tell the old appointment time
        # The person is able to date the old appointment so we just 
        # Wanna make sure its the correct one
        self.ra_old_appointment = appt

    def rescheduleAppointment(self):

        appt = get_selected_list_object(self.RA_CurrentAvailableTimesListWidget)

        try:
            assert appt is not None, "No New Appointment Selected"
        except AssertionError as error:
            self.load_error(str(error))
            return

        self.appointment_dm.add_appointment(appt)
        self.appointment_dm.remove_appointment(self.ra_old_appointment)

        self.clearInputs()
        self.RA_CurrentAvailableTimesListWidget.clear()
        self.RA_SearchedAppointmentsListWidget.clear()


class Cancel(Utility):
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

        self.load_locations(self.CA_OfficeLocationsComboBox)
        self.load_physicians(self.CA_PhysicianNamesComboBox)

        self.CA_OfficeLocationsComboBox.currentIndexChanged.connect(self.ca_switch_location)

    def ca_switch_location(self):

        location = get_selected_combo_box_object(self.CA_OfficeLocationsComboBox)
        self.load_physicians(combo_box = self.CA_PhysicianNamesComboBox, location_id = location.LocationID)

    def search_CA(self):

        CA_physicianNames = get_selected_combo_box_object(self.CA_PhysicianNamesComboBox)
        CA_appointmentDate = self.CA_AppointmentDateDateEdit.date().toPyDate()

        appointments = self.appointment_dm.get_appointments_for_date(CA_appointmentDate, CA_physicianNames)

        try:
            assert len(appointments) > 0, "No Appointments Found"
        except AssertionError as error:
            self.load_error(str(error))

        load_objects_to_list(appointments, self.CA_SearchedAppointmentsListWidget)


    def cancelAppointment(self):

        appointment = get_selected_list_object(self.CA_SearchedAppointmentsListWidget)

        self.appointment_dm.set_appointment_canceled(appointment)

