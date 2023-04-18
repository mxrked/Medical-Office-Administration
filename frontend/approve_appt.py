"""
approve_appt.py - Window to handle appointment requests from the web portal.
UI Designed by: Christian Fortin
Authors: 
"""
from PyQt5.QtWidgets import QListWidget, QPushButton, QComboBox
from frontend.utility import Utility
from backend.data_handler import get_selected_combo_box_object, get_selected_list_object, set_objects_to_combo_box


class Approve(Utility):
    """
        Handles the Approve Appointment Buttons/Functions

        First initalizes widgets

        Uses The
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

        self.a_btn_approve.clicked.connect(self.approve)
        self.a_btn_deny.clicked.connect(self.deny)
        self.a_btn_refresh.clicked.connect(self.a_refresh)

        self.get_locations_into(self.a_location)
        self.get_physicians_into(self.a_provider)

        self.a_location.currentIndexChanged.connect(self.a_location_chagne)

    def approve(self):
        """
            Gets the selected item from self.approve_list
                Using the data_handler
        """

        getSelectedAppt = get_selected_list_object(self.a_list)

        if not getSelectedAppt:
            self.load_error("Not selecting appointment.")
            return

        try:
            self.appointment_dm.add_appointment(getSelectedAppt)
        except AssertionError as e:
            self.load_error(e)

        self.a_refresh() # Refreshes the list

    def deny(self):
        """
            Sets the status of the given appointment to deny

            Gets the selected item from self.approve_list
                Using the data_handler

            NOTE: Check if that data corresponds to data.
                If it doesn't use self.load_error()
            
            Then uses appointment_data_manager to set_appointment_canceled

            Then call self.a_refresh
        """
        getSelectedAppt = get_selected_list_object(self.a_list)

        if not getSelectedAppt:
            self.load_error("Not selecting appointment.")
            return

        self.appointment_dm.set_appointment_canceled(getSelectedAppt)

        self.a_refresh()

    def a_refresh(self):
        """
            Refreshes self.a_list with pending appointments

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, self.a_list) 
        """
        getLocations = get_selected_combo_box_object(self.a_location)
        getProviders = get_selected_combo_box_object(self.a_provider)

        listOfAppointments = self.appointment_dm.get_pending_appointments(getLocations, getProviders)
        set_objects_to_combo_box(listOfAppointments, self.a_list)

        print(self.a_refresh.__doc__)

    def a_location_chagne(self):
        location = get_selected_combo_box_object(self.a_location)
        self.get_physicians_into(self.a_provider, location_id=location.LocationID)