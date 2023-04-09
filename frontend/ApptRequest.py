from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from abstract_main_window import AMainWindow
import sys

from backend.appointment_dm import AppointmentDM

class UI(AMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/apptrequest.ui", self)

        self.load_nav()

        

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
app.exec_()
