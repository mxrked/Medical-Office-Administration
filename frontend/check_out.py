"""
Checkout.py - A window to handle in checking out appointments for the clinic
UI Designed by: Jessica Weeks
Authors: Parker Phelps
"""
from PyQt5.QtWidgets import QListWidget, QComboBox, QPushButton
from frontend.main_nav import Nav
class CheckOut(Nav):
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
        self.locations_combobox = self.findChild(QComboBox, "comboBox_Locations")

        # Load button widgets
        self.check_out_btn = self.findChild(QPushButton, "Checkout_Btn_Checkout")
        self.check_out_refresh_btn = self.findChild(QPushButton, "Checkout_Btn_Refresh")
        self.download_summary_btn = self.findChild(QPushButton, "Checkout_Btn_Download")

        # Connect buttons
        self.check_out_btn.mousePressEvent = self.check_out
        self.check_out_refresh_btn.mousePressEvent = self.check_out_refresh
        self.download_summary_btn.mousePressEvent = self.download_summary

    def check_out(self, event):
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

    def check_out_refresh(self, event):
        """
            Refreshes self.checkOutListWidget with appointments that can
                be checked out

            Get list of appointments using Appointment_Data_Manager
            Then use the data handler to set_objects_to_list(appointments, QListWidget) 
        """
        print(self.check_out_refresh.__doc__)

    def download_summary(self, event):
        """
        I'm not sure what to do here.

        Something about views in the DB, I don't know
        """
        print(self.download_summary.__doc__)
