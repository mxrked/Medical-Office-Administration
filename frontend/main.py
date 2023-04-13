import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication
from frontend.approve_appt import Approve
class MainWindow(Approve):
    def __init__(self, can_physician: bool, can_schedule: bool):
        super(MainWindow, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)


        self.can_physician = can_physician
        self.can_schedule = can_schedule

        self.disable_all_nav()

        self.enable_all_nav_with_access()

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
 