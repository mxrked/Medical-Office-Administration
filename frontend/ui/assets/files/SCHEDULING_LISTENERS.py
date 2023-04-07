'''

This will hold all of the different listeners for the scheduling/rescheduling/cancel module

'''

from frontend.ui.assets.files.GLOBALS import customTime

from PyQt5.QtCore import QDate


# Scheduling/Make
def clearInputs_SA(self):

                defaultDate = QDate(2000, 1, 1)

                self.SA_PatientFNLineEdit.setText("")
                self.SA_PatientLNLineEdit.setText("")
                self.SA_PatientDOBDateEdit.setDate(defaultDate)
                self.SA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.SA_AppointmentReasonLineEdit.setText("")
                self.SA_AppointmentTypesComboBox.setCurrentIndex(0)
                self.SA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.SA_AppointmentDateDateEdit.setDate(defaultDate)

                self.SA_CurrentAvailableTimesListWidget.clear()
def getPatientFN_SA(self):
    return self.SA_PatientFNLineEdit.text()
def getPatientLN_SA(self):
    return self.SA_PatientLNLineEdit.text()
def getPatientDOB_SA(self):
    return self.SA_PatientDOBDateEdit.date()
def getOfficeLocation_SA(self):
    return self.SA_OfficeLocationsComboBox.currentIndex()
def getAppointmentReason_SA(self):
    return self.SA_AppointmentReasonLineEdit.text()
def getAppointmentType_SA(self):
    return self.SA_AppointmentTypesComboBox.currentIndex()
def getPhysicianName_SA(self):
    return self.SA_PhysicianNamesComboBox.currentIndex()
def getAppointmentDate_SA(self):
    return self.SA_AppointmentDateDateEdit.date()
def getAvailableTime_SA(self):
    return self.SA_CurrentAvailableTimesListWidget.currentRow()
def enableCustomTime(self):

        # Appending true to customTime
        customTime.clear()
        customTime.append(True)

        self.SA_YesCustomTimePushButton.setVisible(False)
        self.SA_NoCustomTimePushButton.setVisible(True)
        self.SA_CurrentAvailableTimesListWidget.clearSelection()
        self.SA_CustomTimeTimeEdit.setEnabled(True)
        self.SA_CustomTimeTimeEdit.setStyleSheet("QTimeEdit {\n"
"    border-image: none;\n"
"    background-color: rgb(243, 236, 176);\n"
"    font-family: 'MS Shell Dlg 2';\n"
"    color: #344D67;;\n"
"    border: none;\n"
"    font-size: 15;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n")
        print("Enabled Custom Time")
def disableCustomTime(self):

        # Appending false to customTime
        customTime.clear()
        customTime.append(False)

        self.SA_YesCustomTimePushButton.setVisible(True)
        self.SA_NoCustomTimePushButton.setVisible(False)
        self.SA_CustomTimeTimeEdit.setEnabled(False)
        self.SA_CustomTimeTimeEdit.setStyleSheet("QTimeEdit {\n"
"    border-image: none;\n"
"    background-color: rgba(243, 236, 176, 133);\n"
"    font-family: 'MS Shell Dlg 2';\n"
"    color: #344D67;;\n"
"    border: none;\n"
"    font-size: 15;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n")
        print("Disabled Custom Time")





def search_SA(self):
    pass

# Rescheduling
def clearInputs_RA(self):

                defaultDate = QDate(2000, 1, 1)

                self.RA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.RA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.RA_AppointmentDateDateEdit.setDate(defaultDate)
                self.RA_RescheduleDateDateEdit.setDate(defaultDate)

                self.RA_SearchedAppointmentsListWidget.clear()
                self.RA_CurrentAvailableTimesListWidget.clear()


# Cancel
def clearInputs_CA(self):

                defaultDate = QDate(2000, 1, 1)

                self.CA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.CA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.CA_AppointmentDateDateEdit.setDate(defaultDate)

                self.CA_SearchedAppointmentsListWidget.clear()
