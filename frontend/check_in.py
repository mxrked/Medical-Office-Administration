"""
CheckIn.py - A window to handle in checking in appointments for the clinic
UI Designed by: Jessica Weeks
Authors: Jessica Weeks
"""
from PyQt5.QtWidgets import QApplication, QComboBox, QListWidget, QPushButton, QMainWindow
from PyQt5 import uic
#from backend.appointment_dm import AppointmentDM
#from backend.user_dm import UserDM
#from backend.misc_dm import MiscDM
#from backend.data_handler import get_selected_combo_box_object, set_objects_to_combo_box
import sys


class CheckIn(QMainWindow):
    def __init__(self):
        super(CheckIn, self).__init__()

        uic.loadUi("frontend/ui/mainWindow.ui", self)



        # Load Input Widgets
        self.location = self.findChild(QComboBox, "CheckIn_Location")
        self.providers = self.findChild(QComboBox, "CheckIn_Provider")
        self.check_ins_list = self.findChild(QListWidget, "CheckIn_ListWidget")
        
        # Load Buttons
        self.check_in_btn = self.findChild(QPushButton, "CheckIn_CheckIn")
        self.no_show_btn = self.findChild(QPushButton, "CheckIn_NoShow")
        self.refresh_btn = self.findChild(QPushButton, "CheckIn_Refresh")

        # Connect buttons
        self.check_in_btn.mousePressEvent = self.checkIn
        self.no_show_btn.mousePressEvent = self.noShow
        self.refresh_btn.mousePressEvent = self.refresh

        # Load db managers
        #self.ApptDataManger = AppointmentDM()
        #self.UserDataManager = UserDM()
        #self.MiscDataManager = MiscDM()

        # Load Comobo Boxes
        #physcians = self.UserDataManager.get_physicians()
        #set_objects_to_combo_box(physcians, self.providers)
        
        #locations = self.MiscDataManager.get_locations()
        #set_objects_to_combo_box(locations, self.location)

    def checkIn(self, event):
        pass

    def noShow(self, event):
        pass

    def refresh(self, event):
        pass


#initializing app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = CheckIn()
    UIWindow.show()
    app.exec_()
