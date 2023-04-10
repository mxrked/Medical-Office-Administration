from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QComboBox, QDateEdit, QListWidget, QTimeEdit
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.SCHEDULING_LISTENERS import *

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
