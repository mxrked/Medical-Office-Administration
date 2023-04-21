"""
main.py - Runs all the main windows except StartWindow
Author: Jessica Weeks
"""
import sys
from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from frontend.screens.schedule import Schedule, Reschedule, Cancel
from frontend.screens.approve_appt import Approve
from frontend.screens.check_in import CheckIn
from frontend.screens.check_out import CheckOut
from frontend.screens.referral import ReferralScreen
from frontend.screens.lab import Lab
from frontend.screens.patient import NewPatient

class MainWindow(Schedule, Reschedule, Cancel,
                 NewPatient,
                 CheckIn,
                 CheckOut,
                 ReferralScreen,
                 Lab,
                 Approve):
    """
    A QMainWindow for handeling all windows except StartWindow

    :param can_physician: bool, if they can use phsycian screens
    :param can_schedule: bool, if they can use scheduling screens
    :param debug: bool, makes it so no password is required
    :param today: date, sets todays date for debuggin purposes

    Subclasses:

    Nav(QMainWindow) (Navigation Functions)
    │ 
    └─── Utility ( Loads Datamangers & Useful functs for repeated code )
            │ 
            │   ( Screens )
            ├─── Schedule
            ├─── Reschedule
            ├─── Cancel 
            ├─── Patient
            ├─── CheckIn
            ├─── CheckOut
            ├─── Referral
            ├─── Lab
            └─── Approve

    Scope is a concern but this is inevitable because we have to load
        it all into one QMainWindow

    None of these subclasses will run standalone, sorry! Run this instead
    """

    def __init__(self,
                 can_physician:bool=True,
                 can_schedule:bool=True,
                 debug=False,
                 today=datetime.now().date()):

        super(MainWindow, self).__init__()

        # Stop QBasicTimer Spam
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.can_physician = can_physician
        self.can_schedule = can_schedule

        self.debug = debug

        # Used for tricking the program what day it is for testing purposes
        if self.debug:
            self.todays_date = today

        # They will only be able to select btns they have access too
        self.disable_all_nav()
        self.enable_all_nav_with_access()

        # Sets Starting Window
        if self.can_schedule:

            self.enter_appointments_window()
            self.display_inputs_frame() # Main Scheduling Window

        elif self.can_physician:
            self.enter_referral_window()
        else:
            self.load_error("No Permissions!")

            self.close()

        # Resets everything so no starting data
        # And everything is today
        self.clear_inputs()


#initializing app
app = QApplication(sys.argv)
UIWindow = MainWindow(True, True)
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
 