from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from frontend.ui.assets.files.NAVIGATION_FUNCS import logoutUser, enterSchedulingAppointmentsWindow, enterCheckInWindow,\
enterCheckInWindow, enterMakeReferralWindow, enterCheckOutWindow, enterLabOrdersWindow, enterAppointmentApproveViaPortalWindow
from frontend.ui.assets.files.SCHEDULING_LISTENERS import clearInputs_SA, clearInputs_RA, clearInputs_CA
from sys import exit
from frontend.ui.assets.qrc import app_bg, doctor, show, hide
from frontend.ui.assets.files.GLOBALS import prevWindowCoords

class AMainWindow(QMainWindow):

    def __init__(self):
        super(AMainWindow, self).__init__()

    def load_nav(self):
        # Nav widgets
        self.logoutPushButton = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointmentsPushButton = self.findChild(QPushButton, "Nav_Appointments")
        self.checkinPushButton = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkoutPushButton = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.makeReferralPushButton = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.labOrdersPushButton = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approveAppointmentsPushButton = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")
        self.currentUserLabel = self.findChild(QLabel, "currentUserLabel")

        # Do something (Use functions for buttons and stuff)
        self.logoutPushButton.mousePressEvent = lambda event: logoutUser(self)

        # self.appointmentsPushButton.clicked.connect(enterSchedulingAppointmentsWindow)
        self.appointmentsPushButton.mousePressEvent = lambda event: enterSchedulingAppointmentsWindow()
        self.checkinPushButton.mousePressEvent = lambda event: enterCheckInWindow(self)
        self.checkoutPushButton.mousePressEvent = lambda event: enterCheckOutWindow(self)
        self.makeReferralPushButton.mousePressEvent = lambda event: enterMakeReferralWindow(self)
        self.labOrdersPushButton.mousePressEvent = lambda event: enterLabOrdersWindow(self)
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: enterAppointmentApproveViaPortalWindow(self)


        self.currentUserLabel.setText("")
        self.currentUserLabel.setText("Current User: " + "USERNAME")
        self.setWindowTitle("")
        self.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments -|- User: " + "USERNAME")

    def closeEvent(self, event):
        exit()
    
    def moveEvent(self, event):
        prevWindowCoords.clear()

        coords = self.pos()

        prevWindowCoords.append(coords.x())
        prevWindowCoords.append(coords.y())


class AppointmentMainWindow(AMainWindow):
    def __init__(self):
        super(AppointmentMainWindow, self).__init__()
        
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

        # Clearing all the fields
        clearInputs_SA(self)
        clearInputs_RA(self)
        clearInputs_CA(self)
    
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
