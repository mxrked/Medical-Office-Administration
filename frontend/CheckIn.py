from PyQt5.QtWidgets import QApplication, QComboBox, QListWidget, QPushButton
from PyQt5 import uic
from frontend.abstract_main_window import AMainWindow
from backend.appointment_dm import AppointmentDM
from backend.user_dm import UserDM
from backend.misc_dm import MiscDM
from backend.data_handler import get_selected_combo_box_object, set_objects_to_combo_box
import sys


class UI(AMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/checkin.ui", self)

        # Session for connecting to the Database
        self.load_nav()

        # Load Input Widgets
        self.location = self.findChild(QComboBox, "comboBox_Locations")
        self.providers = self.findChild(QComboBox, "comboBox_Doctors")
        self.check_ins_list = self.findChild(QListWidget, "listWidget_CheckIns")
        
        # Load Buttons
        self.check_in_btn = self.findChild(QPushButton, "Btn_CheckIn")
        self.no_show_btn = self.findChild(QPushButton, "Btn_CheckIn_2")
        self.refresh_btn = self.findChild(QPushButton, "Btn_Refresh")

        # Connect buttons
        self.check_in_btn.mousePressEvent = self.checkIn
        self.no_show_btn.mousePressEvent = self.noShow
        self.refresh_btn.mousePressEvent = self.refresh

        # Load db managers
        self.ApptDataManger = AppointmentDM()
        self.UserDataManager = UserDM()
        self.MiscDataManager = MiscDM()

        # Load Comobo Boxes
        physcians = self.UserDataManager.get_physicians()
        set_objects_to_combo_box(physcians, self.providers)
        
        locations = self.MiscDataManager.get_locations()
        set_objects_to_combo_box(locations, self.location)

    def checkIn(self, event):
        pass

    def noShow(self, event):
        pass

    def refresh(self, event):
        pass


#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
