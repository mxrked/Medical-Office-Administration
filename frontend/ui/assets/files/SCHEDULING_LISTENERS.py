'''

This will hold all of the different listeners for the scheduling/rescheduling/cancel module

'''

from frontend.ui.assets.files.GLOBALS import *

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

                self.SA_PatientFNLineEdit.setStyleSheet("""
                
                    QLineEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
                self.SA_PatientLNLineEdit.setStyleSheet("""
                
                    QLineEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
                self.SA_PatientDOBDateEdit.setStyleSheet("""
                
                    QDateEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
                self.SA_OfficeLocationsComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.SA_AppointmentReasonLineEdit.setStyleSheet("""
                
                    QLineEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
                self.SA_AppointmentTypesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.SA_PhysicianNamesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.SA_AppointmentDateDateEdit.setStyleSheet("""
                
                    QDateEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
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
def getCustomTime_SA(self):
    if customTime[0] == True:
        return self.SA_CustomTimeTimeEdit.time()
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

    patientFN = getPatientFN_SA(self)
    patientLN = getPatientLN_SA(self)
    patientDOB = getPatientDOB_SA(self)
    officeLocation = getOfficeLocation_SA(self)
    appointmentReason = getAppointmentReason_SA(self)
    appointmentType = getAppointmentType_SA(self)
    physicianName = getPhysicianName_SA(self)
    appointmentDate = getAppointmentDate_SA(self)

    # Checking if inputs are/are not empty
    if patientFN != "" and patientFN != None:
        print() # Check if is valid and in db
    if patientFN == "" or patientFN == None:
        validPatientFN_SA.clear()
        validPatientFN_SA.append(False)

        self.SA_PatientFNLineEdit.setStyleSheet("""
                
                    QLineEdit {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    if patientLN != "" and patientLN != None:
        print() # Check if is valid and in db
    if patientLN == "" or patientLN == None:
        validPatientLN_SA.clear()
        validPatientLN_SA.append(False)

        self.SA_PatientLNLineEdit.setStyleSheet("""
                
                    QLineEdit {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Patient DOB

    # Office Location
    if officeLocation != 0:
        print() # Check if is valid
    if officeLocation == 0:
        validOfficeLocation_SA.clear()
        validOfficeLocation_SA.append(False)

        self.SA_OfficeLocationsComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    if appointmentReason != "" and appointmentReason != None:
        print() # Check if is valid and in db
    if appointmentReason == "" or appointmentReason == None:

        validAppointmentReason_SA.clear()
        validAppointmentReason_SA.append(False)

        self.SA_AppointmentReasonLineEdit.setStyleSheet("""

                        QLineEdit {
                            border-image: none;
                            border: 2px solid red;
                            background-color: #F3ECB0;
                            color: #344D67;
                            font-family: "MS Shell Dlg 2";
                            font-size: 11;
                            padding-left: 10px;
                            padding-right: 10px;
                        }

            """)

    # Appointment Type
    if appointmentType != 0:
        print() # Check if is valid
    if appointmentType == 0:
        validAppointmentType_SA.clear()
        validAppointmentType_SA.append(False)

        self.SA_AppointmentTypesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Physician Name
    if physicianName != 0:
        print() # Check if is valid
    if physicianName == 0:
        validPhysicianName_SA.clear()
        validPhysicianName_SA.append(False)

        self.SA_PhysicianNamesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Appointment Date
def scheduleAppointment(self):

    if validPatientFN_SA[0] == True and validPatientLN_SA[0] == True and validPatientDOB_SA[0] == True and validOfficeLocation_SA[0] == True and validAppointmentReason_SA[0] == True and validAppointmentType_SA[0] == True and validPhysicianName_SA[0] == True and validAppointmentDate_SA[0] == True:
        print()

    # Checking for invalids
    if validPatientFN_SA[0] != True:
        print("Patient FN value is invalid (SA)")
    if validPatientLN_SA[0] != True:
        print("Patient LN value is invalid (SA)")
    if validPatientDOB_SA[0] != True:
        print("Patient DOB value is invalid (SA)")
    if validOfficeLocation_SA[0] != True:
        print("Office Location value is invalid (SA)")
    if validAppointmentReason_SA[0] != True:
        print("Appointment Reason value is invalid (SA)")
    if validAppointmentType_SA[0] != True:
        print("Appointment Type value is invalid (SA)")
    if validPhysicianName_SA[0] != True:
        print("Physician Name value is invalid (SA)")
    if validAppointmentDate_SA[0] != True:
        print("Appointment Date value is invalid (SA)")

# Rescheduling
def clearInputs_RA(self):

                defaultDate = QDate(2000, 1, 1)

                self.RA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.RA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.RA_AppointmentDateDateEdit.setDate(defaultDate)
                self.RA_RescheduleDateDateEdit.setDate(defaultDate)

                self.RA_SearchedAppointmentsListWidget.clear()
                self.RA_CurrentAvailableTimesListWidget.clear()

                self.RA_OfficeLocationsComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.RA_PhysicianNamesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.RA_AppointmentDateDateEdit.setStyleSheet("""
                
                    QDateEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
                self.RA_RescheduleDateDateEdit.setStyleSheet("""
                
                    QDateEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
def getOfficeLocation_RA(self):
    return self.RA_OfficeLocationsComboBox.currentIndex()
def getPhysicianName_RA(self):
    return self.RA_PhysicianNamesComboBox.currentIndex()
def getAppointmentDate_RA(self):
    return self.RA_AppointmentDateDateEdit.date()
def getRescheduleDate_RA(self):
    return self.RA_RescheduleDateDateEdit.date()
def displayTimesApps_RA(self):
    '''
        This is basically another search
    '''

    officeLocation = getOfficeLocation_RA(self)
    physicianName = getPhysicianName_RA(self)
    appointmentDate = getAppointmentDate_RA(self)
    rescheduleDate = getRescheduleDate_RA(self)

    # Office Location
    if officeLocation != 0:
        print() # Check if is valid
    if officeLocation == 0:
        validOfficeLocation_SA.clear()
        validOfficeLocation_SA.append(False)

        self.RA_OfficeLocationsComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Physician Name
    if physicianName != 0:
        print() # Check if is valid
    if physicianName == 0:
        validPhysicianName_SA.clear()
        validPhysicianName_SA.append(False)

        self.RA_PhysicianNamesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Appointment Date

    # Reschedule Date

def rescheduleAppointment(self):

    if validOfficeLocation_RA[0] == True and validPhysicianName_RA[0] == True and validAppointmentDate_RA[0] == True and validRescheduleDate_RA[0] == True:
        print()

    # Checking for invalids
    if validOfficeLocation_RA[0] != True:
        print("Office Location value is invalid (RA)")
    if validPhysicianName_RA[0] != True:
        print("Physician Name value is invalid (RA)")
    if validAppointmentDate_RA[0] != True:
        print("Appointment Date value is invalid (RA)")
    if validRescheduleDate_RA[0] != True:
        print("Reschedule Appointment Date value is invalid (RA)")

# Cancel
def clearInputs_CA(self):

                defaultDate = QDate(2000, 1, 1)

                self.CA_OfficeLocationsComboBox.setCurrentIndex(0)
                self.CA_PhysicianNamesComboBox.setCurrentIndex(0)
                self.CA_AppointmentDateDateEdit.setDate(defaultDate)

                self.CA_SearchedAppointmentsListWidget.clear()

                self.CA_OfficeLocationsComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.CA_PhysicianNamesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                    }
                
        """)
                self.CA_AppointmentDateDateEdit.setStyleSheet("""
                
                    QDateEdit {
                        border-image: none;
                        border: none;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)
def getOfficeLocation_CA(self):
    return self.CA_OfficeLocationsComboBox.currentIndex()
def getPhysicianName_CA(self):
    return self.CA_PhysicianNamesComboBox.currentIndex()
def getAppointmentDate_CA(self):
    return self.CA_AppointmentDateDateEdit.date()
def search_CA(self):

    officeLocation = getOfficeLocation_CA(self)
    physicianName = getPhysicianName_CA(self)
    appointmentDate = getAppointmentDate_CA(self)

    # Office Location
    if officeLocation != 0:
        print() # Check if is valid
    if officeLocation == 0:
        validOfficeLocation_SA.clear()
        validOfficeLocation_SA.append(False)

        self.CA_OfficeLocationsComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Physician Name
    if physicianName != 0:
        print() # Check if is valid
    if physicianName == 0:
        validPhysicianName_SA.clear()
        validPhysicianName_SA.append(False)

        self.CA_PhysicianNamesComboBox.setStyleSheet("""
                
                    QComboBox {
                        border-image: none;
                        border: 2px solid red;
                        background-color: #F3ECB0;
                        color: #344D67;
                        font-family: "MS Shell Dlg 2";
                        font-size: 11;
                        padding-left: 10px;
                        padding-right: 10px;
                    }
                
        """)

    # Appointment Date

def cancelAppointment(self):

    if validOfficeLocation_CA[0] == True and validPhysicianName_CA[0] == True and validAppointmentDate_CA[0] == True:
        print()

    # Checking for invalids
    if validOfficeLocation_CA[0] != True:
        print("Office Location value is invalid (CA)")
    if validPhysicianName_CA[0] != True:
        print("Physician Name value is invalid (CA)")
    if validAppointmentDate_CA[0] != True:
        print("Appointment Date value is invalid (CA)")
