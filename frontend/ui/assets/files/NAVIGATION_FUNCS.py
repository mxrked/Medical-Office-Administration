import SchedulingAppointmentsWindow, StartWindow, ApptRequest, NewPatient, Referrals, LabOrders, CheckIn, CheckOut

from frontend.ui.assets.files.GLOBALS import currentUsername, currentUserID, currentEmployeeID
from backend.data_manager import DataManger

def hideAllWindowsExceptForAppointments():
        from frontend import ApptRequest, NewPatient, Referrals, LabOrders, CheckIn, CheckOut

        StartWindow.UIWindow.hide()
        NewPatient.UIWindow.hide()
        Referrals.UIWindow.hide()
        CheckIn.UIWindow.hide()
        CheckOut.UIWindow.hide()
        ApptRequest.UIWindow.hide()
        LabOrders.UIWindow.hide()

def changeTitleText(num, window):
                # Title
                if num == 1:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments -|- User: " + currentUsername[0])
                if num == 2:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Check In -|- User: " + currentUsername[0])
                if num == 3:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Check Out -|- User: " + currentUsername[0])
                if num == 4:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Make Referral -|- User: " + currentUsername[0])
                if num == 5:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Lab Orders -|- User: " + currentUsername[0])
                if num == 6:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Approve Appointment via Portal -|- User: " + currentUsername[0])
                if num == 7:
                    window.UIWindow.setWindowTitle("Forsyth Family Practice Center - New Patient -|- User: " + currentUsername[0])

def changeCurrentUserLabelText(window):
                window.UIWindow.currentUserLabel.setText("Current User: " + currentUsername[0])


def enterStartWindow(self):
                from frontend import StartWindow

                print("Routing to start screen")
                self.hide()
                StartWindow.UIWindow.show()

def enterSchedulingAppointmentsWindow():
                from frontend import SchedulingAppointmentsWindow

                print("Routing to scheduling appointments screen")
                hideAllWindowsExceptForAppointments()
                SchedulingAppointmentsWindow.UIWindow.show()
                hideAllWindowsExceptForAppointments()

                changeCurrentUserLabelText(SchedulingAppointmentsWindow)
                changeTitleText(1, SchedulingAppointmentsWindow)

def enterCheckInWindow(self):
                from frontend import CheckIn
                print("Routing to check in screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        self.hide()
                        CheckIn.UIWindow.show()

                        changeCurrentUserLabelText(CheckIn)
                        changeTitleText(2, CheckIn)

def enterCheckOutWindow(self):
                from frontend import CheckOut
                print("Routing to check out screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        self.hide()
                        CheckOut.UIWindow.show()

                        changeCurrentUserLabelText(CheckOut)
                        changeTitleText(3, CheckOut)

def enterMakeReferralWindow(self):
                from frontend import Referrals
                print("Routing to make referral screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        self.hide()
                        Referrals.UIWindow.show()

                        changeCurrentUserLabelText(Referrals)
                        changeTitleText(4, Referrals)

def enterLabOrdersWindow(self):
                from frontend import LabOrders
                print("Routing to lab orders screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        self.hide()
                        LabOrders.UIWindow.show()

                        changeCurrentUserLabelText(LabOrders)
                        changeTitleText(5, LabOrders)

def enterAppointmentApproveViaPortalWindow(self):
                from frontend import ApptRequest
                print("Routing to appointment approve via portal screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        self.hide()
                        ApptRequest.UIWindow.show()

                        changeCurrentUserLabelText(ApptRequest)
                        changeTitleText(6, ApptRequest)

def enterNewPatientWindow(self):
                from frontend import NewPatient, SchedulingAppointmentsWindow
                print("Routing to new patient screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        # hideAllWindowsExceptForAppointments()
                        # SchedulingAppointmentsWindow.UIWindow.hide()
                        # NewPatient.UIWindow.show()
                        # SchedulingAppointmentsWindow.UIWindow.hide()

                        self.hide()
                        NewPatient.UIWindow.show()

                        changeCurrentUserLabelText(NewPatient)
                        changeTitleText(7, NewPatient)

def logoutUser(self):

                # Clearing array values
                currentUsername.clear()
                currentUsername.append("Test")
                currentUserID.clear()
                currentEmployeeID.clear()

                print("LOGGED OUT")

                print("Resetted currentUsername: " + currentUsername[0])

                # Routing user back to the start window
                self.currentUserLabel.setText("No User Logged In")

                enterStartWindow(self)
