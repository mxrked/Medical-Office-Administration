"""
approve_appt.py - Window to handle appointment requests from the web portal.
UI Designed by: Christian Fortin
Authors: 
"""
from PyQt5.QtWidgets import QListWidget, QPushButton, QComboBox
from frontend.lab import Lab

class Approve(Lab):
    """
        Handles the Approve Appointment Buttons/Functions

        First initalizes widgets

        Then loads the
            self.appointment_dm
            self.user_dm
            self.misc_dm

        Then grabs locations from the misc_dm 
        and providers from the user_dm

        then uses the data_handlers to 
            set_objects_to_combo_box(locations, self.a_location)
        does this for both
        
        lastly it runs self.a_refresh to fill up list
    """
    def __init__(self):
        super(Approve, self).__init__()

        self.a_list = self.findChild(QListWidget, "Approve_List")
        self.a_btn_approve = self.findChild(QPushButton, "Approve_Btn_Approve")
        self.a_btn_deny = self.findChild(QPushButton, "Approve_Btn_Deny")
        self.a_btn_refresh = self.findChild(QPushButton, "Approve_Btn_Refresh")
        self.a_location = self.findChild(QComboBox, "Approve_Combo_Location")
        self.a_provider = self.findChild(QComboBox, "Approve_Combo_Provider")

        self.a_btn_approve.mousePressEvent = self.approve
        self.a_btn_deny.mousePressEvent = self.deny
        self.a_btn_refresh.mousePressEvent = self.a_refresh

    
    def approve(self, event):
        """
            Gets the selected item from self.approve_list
                Using the data_handler

            NOTE: Check if that data corresponds to data.
                If it doesn't use self.load_error()
            
            Then uses the Appointment_Data_Manager To add_appointment

            NOTE: Put this in a try catch, if the appointment is taken
                it will give you a Assertion error

            try:
                add_appointment()
            catch AssertionError as e:
                self.load_error(e)

            Then call self.a_refresh
        """
        print(self.approve.__doc__)

    def deny(self, event):
        """
            Sets the status of the given appointment to deny

            Gets the selected item from self.approve_list
                Using the data_handler

            NOTE: Check if that data corresponds to data.
                If it doesn't use self.load_error()
            
            Then uses appointment_data_manager to set_appointment_canceled

            Then call self.a_refresh
        """
        print(self.deny.__doc__)

    def a_refresh(self, event):
        """
            Refreshes self.a_list with pending appointments

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, self.a_list) 
        """
        print(self.a_refresh.__doc__)
