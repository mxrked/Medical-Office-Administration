"""
NewPatient.py - A window to add a new patient to the database
UI Designed by: Destan Hutcherson
Authors: 
"""
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg

from frontend.abstract_main_window import AMainWindow
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/NewPatient.ui", self)

        self.appointmentsPushButton.mousePressEvent = lambda event: self.enterSchedulingAppointmentsWindow()
        self.checkinPushButton.mousePressEvent = lambda event: self.enterCheckInWindow()
        self.checkoutPushButton.mousePressEvent = lambda event: self.enterCheckOutWindow()
        self.makeReferralPushButton.mousePressEvent = lambda event: self.enterMakeReferralWindow()
        self.labOrdersPushButton.mousePressEvent = lambda event: self.enterLabOrdersWindow()
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: self.enterAppointmentApproveViaPortalWindow()

        

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
