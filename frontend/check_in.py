"""
CheckIn.py - A window to handle in checking in appointments for the clinic
UI Designed by: Jessica Weeks
Authors: Jessica Weeks
"""
from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton
from frontend.patient import Patient

class CheckIn(Patient):
    def __init__(self):
        super(CheckIn, self).__init__()

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

    def checkIn(self, event):
        pass

    def noShow(self, event):
        pass

    def refresh(self, event):
        pass