"""
ApptRequest.py - Window to handle appointment requests from the web portal.
UI Designed by: Christian Fortin
Authors: 
"""
from PyQt5.QtWidgets import QListWidget, QPushButton, QComboBox
from frontend.lab import Lab

class Approve(Lab):
    def __init__(self):
        super(Approve, self).__init__()

        self.approve_list = self.findChild(QListWidget, "Approve_List")
        self.a_btn_approve = self.findChild(QPushButton, "Approve_Btn_Approve")
        self.a_btn_deny = self.findChild(QPushButton, "Approve_Btn_Deny")
        self.a_btn_refresh = self.findChild(QPushButton, "Approve_Btn_Refresh")
        self.a_location = self.findChild(QComboBox, "Approve_Combo_Location")
        self.a_provider = self.findChild(QComboBox, "Approve_Combo_Provider")

        self.a_btn_approve.mousePressEvent = self.approve
        self.a_btn_deny.mousePressEvent = self.deny
        self.a_btn_refresh.mousePressEvent = self.a_refresh

    
    def approve(self):
        pass

    def deny(self):
        pass

    def a_refresh(self):
        pass
