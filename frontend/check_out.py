"""
Checkout.py - A window to handle in checking out appointments for the clinic
UI Designed by: Jessica Weeks
Authors:
"""
from PyQt5.QtWidgets import QListWidget, QComboBox, QPushButton
from frontend.utility import Utility
from backend.data_handler import get_selected_combo_box_object, get_selected_list_object, load_objects_to_list

class CheckOut(Utility):
    """
        Handles checkout page

        First initalizes widgets 

        Uses
            self.appointment_dm
            self.user_dm

        and providers from the user_dm
        and get_appointments_for_date from the appointment_dm

        then uses the data_handlers to 
            set_objects_to_combo_box(providers, self.checkoutListWidget)
       
        
        lastly it runs self.checkOut_refresh
    
    """
    def __init__(self):
        super(CheckOut, self).__init__()

        # Load list widgets
        self.check_out_list = self.findChild(QListWidget, "Checkout_List")

        # Load combo box widgets
        self.locations_combobox = self.findChild(QComboBox, "CheckOut_ComboBox_Location")

        # Load button widgets
        self.check_out_btn = self.findChild(QPushButton, "Checkout_Btn_Checkout")
        self.check_out_refresh_btn = self.findChild(QPushButton, "Checkout_Btn_Refresh")
        self.download_summary_btn = self.findChild(QPushButton, "Checkout_Btn_Download")

        # Connect buttons
        self.check_out_btn.clicked.connect(self.check_out)
        self.check_out_refresh_btn.clicked.connect(self.check_out_refresh)
        self.download_summary_btn.clicked.connect(self.download_summary)

        
        # Populate Combo Boxes
        self.load_locations(self.locations_combobox)

    def check_out(self):
        """
            Checks out the selected appointment    
        
            Gets the selected item from self.checkOutListWidget
                Using the data_handler

            NOTE: Check if that data corresponds to data.
                If it doesn't use self.load_error()

            Uses the appointment_data_manager to
                set_appointment_in_check_out(appointment)

            Then calls self.checkOut_refresh        
        """
        print(self.check_out.__doc__)

        getSelectedAppt = get_selected_list_object(self.check_out_list)

        if not getSelectedAppt:
            self.load_error("Not selecting appointment.")
            return

        self.appointment_dm.set_appointment_checked_out(getSelectedAppt)

        self.check_out_refresh() # Refreshes the list

    def check_out_refresh(self):
        """
            Refreshes self.checkOutListWidget with appointments that can
                be checked out

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, QListWidget) 
        """

        location = get_selected_combo_box_object(self.locations_combobox)

        listOfAppointments = self.appointment_dm.get_in_progress_appointments(location=location)
        load_objects_to_list(listOfAppointments, self.check_out_list)

    def download_summary(self):
        """
        I'm not sure what to do here.

        Something about views in the DB, I don't know
        """
        print(self.download_summary.__doc__)
