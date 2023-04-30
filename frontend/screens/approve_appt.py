"""
approve_appt.py - Window to handle appointment requests from the web portal.
UI Designed by: Christian Fortin
Authors: 
"""
from PyQt5.QtWidgets import QListWidget, QPushButton, QComboBox
from frontend.private.utility import Utility
from backend.data_handler import get_selected_combo_box_object, get_selected_list_object, load_pending_appts_to_list
from frontend.ui.assets.files import styling

class Approve(Utility):
    """
        Handles the Approve Appointment Buttons/Functions
        
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

        self.load_locations(self.a_location)
        self.load_physicians(self.a_provider)

        self.a_location.currentIndexChanged.connect(self.a_location_change)

    def approve(self):
        """
            Gets the selected item from self.approve_list
                Using the data_handler
        """

        selected_appointment = get_selected_list_object(self.a_list)

        if not selected_appointment:
            self.load_error("Not selecting appointment.")
            return

        self.appointment_dm.set_appointment_scheduled(selected_appointment)

        self.a_refresh() # Refreshes the list

    def deny(self):
        """
            Sets the status of the given appointment to deny
            Then call self.a_refresh
        """
        selected_appointment = get_selected_list_object(self.a_list)

        if not selected_appointment:
            self.load_error("Not selecting appointment.")
            return

        self.appointment_dm.set_appointment_canceled(selected_appointment)

        self.a_refresh()

    def a_refresh(self):
        """
            Refreshes self.a_list with pending appointments

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, self.a_list) 
        """
        providers = get_selected_combo_box_object(self.a_provider)

        appointments = self.appointment_dm.get_pending_appointments(providers)

        load_pending_appts_to_list(appointments, self.a_list)


    def a_location_change(self):
        location = get_selected_combo_box_object(self.a_location)
        self.load_physicians(self.a_provider, location)
