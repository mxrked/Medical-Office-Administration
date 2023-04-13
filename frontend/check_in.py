"""
check_in.py - A window to handle in checking in appointments for the clinic
UI Designed by: Jessica Weeks
Authors: Jessica Weeks
"""
from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton
from frontend.main_nav import Nav
class CheckIn(Nav):
    """
        Handles the Check In Page
        
        First initalizes widgets

        Uses
            self.appointment_dm
            self.user_dm
            self.misc_dm

        Then grabs locations from the misc_dm 
        and providers from the user_dm
        and get_appointments_for_date from the appointment_dm

        then uses the data_handlers to 
            set_objects_to_combo_box(locations, self.check_in_location)
        does this for both
        
        lastly it runs self.check_in_refresh
    """
    def __init__(self):
        super(CheckIn, self).__init__()

        # Load Input Widgets
        self.check_in_location = self.findChild(QComboBox, "CheckIn_Location")
        self.providers = self.findChild(QComboBox, "CheckIn_Provider")
        self.check_ins_list = self.findChild(QListWidget, "CheckIn_ListWidget")

        # Load Buttons
        self.check_in_btn = self.findChild(QPushButton, "CheckIn_CheckIn")
        self.no_show_btn = self.findChild(QPushButton, "CheckIn_NoShow")
        self.refresh_btn = self.findChild(QPushButton, "CheckIn_Refresh")

        # Connect buttons
        self.check_in_btn.mousePressEvent = self.check_in
        self.no_show_btn.mousePressEvent = self.no_show
        self.refresh_btn.mousePressEvent = self.check_in_refresh

    def check_in(self, event):
        """
            Checks in the selected appointment    
        
            Gets the selected item from self.check_ins_list
                Using the data_handler

            NOTE: Check if that data corresponds to data.
                If it doesn't use self.load_error()

            Uses the appointment_data_manager to
                set_appointment_in_progress(appointment)

            Then calls self.check_in_refresh
        """
        print(self.check_in.__doc__)

    def no_show(self, event):
        """
            Marks selected appointment as "No Show"

            Gets the selected item from self.approve_list
                Using the data_handler

            NOTE: Check if that data corresponds to data.
                If it doesn't use self.load_error()

            Uses the appointment_data_manager to
                set_appointment_no_show(appointment)

            Then calls self.check_in_refresh
        """
        print(self.no_show.__doc__)

    def check_in_refresh(self, event):
        """
            Refreshes self.check_ins_list with appointments that can
                be checked in

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, self.check_ins_list) 
        """
        print(self.check_in_refresh.__doc__)
