"""
Checkout.py - A window to handle in checking out appointments for the clinic
UI Designed by: Jessica Weeks
Authors: Parker Phelps
"""
from PyQt5.QtWidgets import QApplication, QListWidget, QComboBox, QPushButton
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg
from frontend.abstract_main_window import AMainWindow
from backend.appointment_dm import AppointmentDM
from backend.user_dm import UserDM
from backend.misc_dm import MiscDM
from backend.data_handler import set_objects_to_combo_box, set_objects_to_list
import sys


class UI(AMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/checkout.ui", self)

        self.load_nav()


        # Load list widgets
        self.checkInsListWidget = self.findChild(QListWidget, "listWidget_Check_ins")

        # Load combo box widgets
        self.locationsComboBox = self.findChild(QComboBox, "comboBox_Locations")

        # Load button widgets
        self.checkOutPushButton = self.findChild(QPushButton, "Btn_CheckOut")
        self.refreshPushButton = self.findChild(QPushButton, "Btn_Refresh")
        self.downloadSummaryPushButton = self.findChild(QPushButton, "Btn_CheckOutSummary")

        # Connect buttons
        self.checkOutPushButton.mousePressEvent = self.checkOut
        self.refreshPushButton.mousePressEvent = self.refresh
        self.downloadSummaryPushButton.mousePressEvent = self.downloadSummary

        # Load db managers
        self.ApptDataManger = AppointmentDM()
        self.UserDataManager = UserDM()
        self.MiscDataManager = MiscDM()

        # Load Combo boxes and list widgets
        inProgressAppointments = self.ApptDataManger.get_in_progress_appointments()
        set_objects_to_list(inProgressAppointments, self.checkInsListWidget)

        locations = self.MiscDataManager.get_locations()
        set_objects_to_combo_box(locations, self.locationsComboBox)


    def checkOut(self, event):
        pass

    def refresh(self, event):
        '''

            This is used to refresh the checkins list widget with
            the current/new in progress appointments

        '''

        refreshInProgressAppointments = self.ApptDataManger.get_in_progress_appointments()
        set_objects_to_list(refreshInProgressAppointments, self.checkInsListWidget)

    def downloadSummary(self, event):
        '''

            This is used to download the result of an appointment and when
            it checks out

        '''

        pass

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
