from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.NAVIGATION_FUNCS import *

import urllib
import sqlalchemy
import sys
import SchedulingAppointmentsWindow

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("ui/LabOrdersWindow.ui", self)

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
        self.appointmentsPushButton.mousePressEvent = lambda event: enterSchedulingAppointmentsWindow(self)
        self.checkinPushButton.mousePressEvent = lambda event: enterCheckInWindow(self)
        self.checkoutPushButton.mousePressEvent = lambda event: enterCheckOutWindow(self)
        self.makeReferralPushButton.mousePressEvent = lambda event: enterMakeReferralWindow(self)
        self.labOrdersPushButton.mousePressEvent = lambda event: enterLabOrdersWindow(self)
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: enterAppointmentApproveViaPortalWindow(self)

        # Hide the app
        self.hide()

        # Changing the title to show a user is logged in
        from frontend import SchedulingAppointmentsWindow
        if SchedulingAppointmentsWindow.UI.isHidden:
                print("Scheduling Appointments Window is hidden!")

                self.setWindowTitle("Forsyth Family Practice Center - Lab Orders") # Resetting the title
                currentTitle = self.windowTitle()
                self.setWindowTitle(currentTitle + " -|- User: " + currentUsername[0])

    # This will make it so when the user clicks the red x, it closes all windows
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()
        app.exit()


#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
# app.exec()
