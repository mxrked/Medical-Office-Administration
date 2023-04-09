'''

This will hold all of the different listeners for the scheduling/rescheduling/cancel module

'''

from frontend.ui.assets.files.GLOBALS import *
from PyQt5.QtCore import QDate


# Scheduling/Make
def clearInputs_SA(self):

                defaultDate = QDate().currentDate()

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


def checkValidValues_SA(self):
    patientFN = getPatientFN_SA(self)
    patientLN = getPatientLN_SA(self)
    patientDOB = getPatientDOB_SA(self)
    officeLocation = getOfficeLocation_SA(self)
    appointmentReason = getAppointmentReason_SA(self)
    appointmentType = getAppointmentType_SA(self)
    physicianName = getPhysicianName_SA(self)
    appointmentDate = getAppointmentDate_SA(self)

    # # Checking if inputs are empty
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

    # Office Location
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

def search_SA(self):

    patientFN = getPatientFN_SA(self)
    patientLN = getPatientLN_SA(self)
    patientDOB = getPatientDOB_SA(self)
    officeLocation = getOfficeLocation_SA(self)
    appointmentReason = getAppointmentReason_SA(self)
    appointmentType = getAppointmentType_SA(self)
    physicianName = getPhysicianName_SA(self)
    appointmentDate = getAppointmentDate_SA(self)

    checkValidValues_SA(self)

    # Appointment Date
def scheduleAppointment(self):

    checkValidValues_SA(self)


# Rescheduling
def clearInputs_RA(self):

                defaultDate = QDate().currentDate()

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
def checkValidValues_RA(self):
    officeLocation = getOfficeLocation_RA(self)
    physicianName = getPhysicianName_RA(self)
    appointmentDate = getAppointmentDate_RA(self)
    rescheduleDate = getRescheduleDate_RA(self)

    #Office Location
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
def displayTimesApps_RA(self):
    '''
        This is basically another search
    '''

    officeLocation = getOfficeLocation_RA(self)
    physicianName = getPhysicianName_RA(self)
    appointmentDate = getAppointmentDate_RA(self)
    rescheduleDate = getRescheduleDate_RA(self)

    checkValidValues_RA(self)


def rescheduleAppointment(self):

    checkValidValues_RA(self)

# Cancel
def clearInputs_CA(self):

                defaultDate = QDate().currentDate()

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
def checkValidValues_CA(self):
    officeLocation = getOfficeLocation_CA(self)
    physicianName = getPhysicianName_CA(self)
    appointmentDate = getAppointmentDate_CA(self)

    # Office Location
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
def search_CA(self):

    officeLocation = getOfficeLocation_CA(self)
    physicianName = getPhysicianName_CA(self)
    appointmentDate = getAppointmentDate_CA(self)

    checkValidValues_CA(self)



def cancelAppointment(self):

    checkValidValues_CA(self)

