from PyQt5.QtWidgets import QDateEdit, QLineEdit, QComboBox, QListWidget, QTimeEdit, QPushButton, QWidget
from PyQt5.QtCore import QDate
from frontend.abstract_main_window import AMainWindow


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
        self.SA_NoCustomTimePushButton.mousePressEvent = lambda event: self.disableCustomTime()
        self.SA_YesCustomTimePushButton.mousePressEvent = lambda event: self.enableCustomTime()
        self.SA_SearchPushButton.mousePressEvent = lambda event: self.search()
        self.SA_ScheduleAppointmentPushButton.mousePressEvent = lambda event: self.scheduleAppointment()

    def disableCustomTime(self):
        pass

    def enableCustomTime(self):
        pass

    def search(self):
        entered_inputs = self.checkInputs(self, [
            self.SA_PatientFNLineEdit,
            self.SA_PatientLNLineEdit,
            self.SA_PatientDOBDateEdit,
            self.SA_AppointmentReasonLineEdit,
        ])

        if not entered_inputs:
            # Error Box Stuff
            return False
        
        # Do searching stuff

    def scheduleAppointment(self):
        pass

class RescheduleAppt_AMW(ScheduleAppt_AMW):

    def __init__(self):
        super(ScheduleAppt_AMW, self).__init__()
        

    def load_RA(self):
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
        pass

    def rescheduleAppointment(self):
        pass

class CancelAppt_AMW(RescheduleAppt_AMW):
    def __init__(self):
        super(CancelAppt_AMW, self).__init__()


    def load_CA(self):  
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
        self.CA_SearchForAppointmentsPushButton.mousePressEvent = lambda event: self.search()
        self.CA_CancelAppointmentPushButton.mousePressEvent = lambda event: self.cancelAppointment()

    def search(self):
        pass

    def cancelAppointment(self):
        pass

class Appointments_AMW(CancelAppt_AMW):
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

    
    def displayInputsFrame(self):

        self.hideAllFrames()
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
    
    def displayCancelAppointmentFrame(self):

        self.hideAllFrames()
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
        
        self.load_CA()
        
    def displayRescheduleAppointmentFrame(self):

        self.hideAllFrames()
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

