"""
check_in.py - A window to handle in checking in appointments for the clinic
UI Designed by: Jessica Weeks
Authors:
"""
from PyQt5.QtWidgets import QComboBox, QListWidget, QPushButton
from frontend.private.utility import Utility
from backend.data_handler import get_selected_combo_box_object, get_selected_list_object, \
      load_objects_to_list


class CheckIn(Utility):
    """
        Handles the Check In Page
        
        First initializes widgets

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
        self.check_in_providers = self.findChild(QComboBox, "CheckIn_Provider")
        self.check_ins_list = self.findChild(QListWidget, "CheckIn_ListWidget")

        # Load Buttons
        self.check_in_btn = self.findChild(QPushButton, "CheckIn_CheckIn")
        self.no_show_btn = self.findChild(QPushButton, "CheckIn_NoShow")
        self.refresh_btn = self.findChild(QPushButton, "CheckIn_Refresh")

        # Connect buttons
        self.check_in_btn.clicked.connect(self.check_in)
        self.no_show_btn.clicked.connect(self.no_show)
        self.refresh_btn.clicked.connect(self.check_in_refresh)

        # Populate Combo Boxes
        self.load_locations(self.check_in_location)
        self.load_physicians(self.check_in_providers)

        self.check_in_location.currentIndexChanged.connect(self.check_in_location_change)

    def check_in(self):
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

        getSelectedAppt = get_selected_list_object(self.check_ins_list)

        if not getSelectedAppt:
            self.load_error("Not selecting appointment.")
            return

        self.appointment_dm.set_appointment_in_progress(getSelectedAppt)

        self.check_in_refresh()

    def no_show(self):
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

        getSelectedAppt = get_selected_list_object(self.check_ins_list)

        if not getSelectedAppt:
            self.load_error("Not selecting appointment.")
            return

        self.appointment_dm.set_appointment_no_show(getSelectedAppt)
        
        self.check_in_refresh()

    def check_in_refresh(self):
        """
            Refreshes self.check_ins_list with appointments that can
                be checked in

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, self.check_ins_list) 
        """

        location = get_selected_combo_box_object(self.check_in_location)
        provider = get_selected_combo_box_object(self.check_in_providers)

        listOfAppointments = self.appointment_dm.get_todays_appointments(location, provider, self.todays_date)
        
        for appt in listOfAppointments:
            appt.Location = location
            appt.Employee = provider

        if len(listOfAppointments) < 0:
            self.load_error("No Available Appointments")
            return

        load_objects_to_list(listOfAppointments, self.check_ins_list, long_str=True)

    def check_in_location_change(self):
        location = get_selected_combo_box_object(self.check_in_location)
        self.load_physicians(self.check_in_providers, location=location)
