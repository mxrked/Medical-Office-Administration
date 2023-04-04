from frontend.ui.assets.files.GLOBALS import currentUsername, currentUserID, currentEmployeeID

def enterStartWindow(self):
                from frontend import StartWindow

                print("Routing to start screen")
                StartWindow.UIWindow.show()
                self.hide()
def enterSchedulingAppointmentsWindow(self):
                from frontend import SchedulingAppointmentsWindow

                print("Routing to scheduling appointments screen")
                SchedulingAppointmentsWindow.UIWindow.show()
                self.hide()
def enterNewPatientWindow(self):
                from frontend import NewPatient
                print("Routing to new patient screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        NewPatient.UIWindow.show()
                        self.hide()


                # Display new window code here
def enterCheckInWindow(self):
                from frontend import CheckIn
                print("Routing to check in screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        CheckIn.UIWindow.show()
                        self.hide()

                # Display new window code here
def enterCheckOutWindow(self):
                from frontend import CheckOut
                print("Routing to check out screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        CheckOut.UIWindow.show()
                        self.hide()

                # Display new window code here
def enterMakeReferralWindow(self):
                from frontend import Referrals
                print("Routing to make referral screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        Referrals.UIWindow.show()
                        self.hide()


                # Display new window code here
def enterLabOrdersWindow(self):
                from frontend import LabOrders
                print("Routing to lab orders screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        LabOrders.UIWindow.show()
                        self.hide()

                # Display new window code here
def enterAppointmentApproveViaPortalWindow(self):
                from frontend import ApptRequest
                print("Routing to appointment approve via portal screen")

                if len(currentUsername) == 0:
                        print("There is nobody logged in..")
                if len(currentUsername) == 1:
                        print("Current User: " + currentUsername[0])

                        ApptRequest.UIWindow.show()
                        self.hide()

def logoutUser(self):

                # Clearing array values
                # currentUsername.clear()

                currentUsername[0] = "Test"
                currentUserID.clear()
                currentEmployeeID.clear()

                print("LOGGED OUT")

                # Routing user back to the start window
                enterStartWindow(self)
