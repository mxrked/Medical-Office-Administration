"""
Checkout.py - A window to handle in checking out appointments for the clinic
UI Designed by: Jessica Weeks
Authors: Parker Phelps
"""
from PyQt5.QtWidgets import QListWidget, QComboBox, QPushButton
from frontend.check_in import CheckIn

class CheckOut(CheckIn):
    def __init__(self):
        super(CheckOut, self).__init__()

        # Load list widgets
        self.checkInsListWidget = self.findChild(QListWidget, "Checkout_List")

        # Load combo box widgets
        self.locationsComboBox = self.findChild(QComboBox, "comboBox_Locations")

        # Load button widgets
        self.checkOutPushButton = self.findChild(QPushButton, "Checkout_Btn_Checkout")
        self.refreshPushButton = self.findChild(QPushButton, "Checkout_Btn_Refresh")
        self.downloadSummaryPushButton = self.findChild(QPushButton, "Checkout_Btn_Download")

        # Connect buttons
        self.checkOutPushButton.mousePressEvent = self.checkOut
        self.refreshPushButton.mousePressEvent = self.refresh_checkOut
        self.downloadSummaryPushButton.mousePressEvent = self.downloadSummary

    def checkOut(self):
        pass
    
    def refresh_checkOut(self):
        pass

    def downloadSummary(self):
        pass
