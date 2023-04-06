from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import uic
# from ui.assets.qrc import app_bg
# from ui.assets.files.GLOBALS import *
#from ui.assets.files.NAVIGATION_FUNCS import enterSchedulingAppointmentsWindow, logoutUser, enterStartWindow, enterCheckInWindow, enterCheckOutWindow, enterNewPatientWindow, enterLabOrdersWindow, enterMakeReferralWindow, enterAppointmentApproveViaPortalWindow
from ui.assets.files.NAVIGATION_FUNCS import *
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base


# import urllib
# import sqlalchemy
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("ui/checkin.ui", self)

        # Functions


        # Define widgets
        self.logoutPushButton = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointmentsPushButton = self.findChild(QPushButton, "Nav_Appointments")
        self.checkinPushButton = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkoutPushButton = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.makeReferralPushButton = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.labOrdersPushButton = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approveAppointmentsPushButton = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")

        # Do something (Use functions for buttons and stuff)
        self.logoutPushButton.mousePressEvent = lambda event: logoutUser(self)
        self.appointmentsPushButton.clicked.connect(enterSchedulingAppointmentsWindow)
        # self.appointmentsPushButton.mousePressEvent = lambda event: enterSchedulingAppointmentsWindow()
        self.checkinPushButton.mousePressEvent = lambda event: enterCheckInWindow(self)
        self.checkoutPushButton.mousePressEvent = lambda event: enterCheckOutWindow(self)
        self.makeReferralPushButton.mousePressEvent = lambda event: enterMakeReferralWindow(self)
        self.labOrdersPushButton.mousePressEvent = lambda event: enterLabOrdersWindow(self)
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: enterAppointmentApproveViaPortalWindow(self)


        # Hide the app
        self.hide()



    # This will make it so when the user clicks the red x, it closes the app
    def closeEvent(self, event):
        sys.exit()


    def moveEvent(self, event):
        prevWindowCoords.clear()

        coords = self.pos()

        prevWindowCoords.append(coords.x())
        prevWindowCoords.append(coords.y())

        print(prevWindowCoords)

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
# app.exec()
