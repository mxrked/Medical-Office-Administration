import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from frontend.schedule import Schedule, Reschedule, Cancel
from frontend.approve_appt import Approve
from frontend.check_in import CheckIn
from frontend.check_out import CheckOut
from frontend.referral import Referral
from frontend.lab import Lab
from frontend.patient import New_Patient

class MainWindow(Schedule, Reschedule, Cancel,
                 New_Patient,
                 CheckIn,
                 CheckOut,
                 Referral,
                 Lab,
                 Approve):
    """
    A QMainWindow for handeling all windows except StartWindow

    :param can_physician: bool, if they can use phsycian screens
    :param can_schedule: bool, if they can use scheduling screens

    Subclasses:

        Nav(QMainWindow)
        │ 
        ├───Schedule
        ├───Reschedule
        ├───Cancel 
        ├───Patient
        ├───CheckIn
        ├───CheckOut
        ├───Referral
        ├───Lab
        └───Approve

    Scope is a concern but this is inevitable because we have to load
        it all into one MainWindow

    Subclasses (All but Nav) are based on how our UI screens were originally made
        before we squeezed them into one big UI file

    None of these subclasses will run standalone, sorry! Run this instead
    """

    def __init__(self, can_physician:bool=True, can_schedule:bool=True):
        super(MainWindow, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


        self.can_physician = can_physician
        self.can_schedule = can_schedule

        # They will only be able to select btns they have access too
        self.disable_all_nav()
        self.enable_all_nav_with_access()

        # Sets Starting Window
        if self.can_schedule:

            self.enterSchedulingAppointmentsWindow()
        elif self.can_physician:
            self.enterMakeReferralWindow()
        else:
            self.load_error("No Permissions!")

            self.close()


#initializing app
app = QApplication(sys.argv)
UIWindow = MainWindow(True, True)
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
 