"""
SchedulingAppointmentsWindow.py A window for scheduling/rescheduling and canceling appointments
UI Designed by: Parker Phelps
Author: Jessica Weeks
"""
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg

from frontend.scheduling_windows import Appointments_AMW
import sys



class UI(Appointments_AMW):
    def __init__(self):

        
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/SchedulingAppointmentsWindow.ui", self)

        self.load_nav()

        self.load_appointment_nav()

        self.load_SA()




#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
