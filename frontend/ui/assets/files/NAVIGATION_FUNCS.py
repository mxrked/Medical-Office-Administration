# import StartWindow, ApptRequest, NewPatient, Referrals, LabOrders, CheckIn, CheckOut

# import frontend.StartWindow
from frontend.ui.assets.files.GLOBALS import prevWindowCoords, isPhysician, currentUsername, currentUserID, currentEmployeeID
from backend.private.data_manager import DataManger

def greyOutReferralsAndLabOrdersForPhysicians(self):
    '''
        This will check if the isPhysician array is true and then it will
        grey out referrals and lab orders buttons
    '''

    if isPhysician:
        self.makeReferralPushButton.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgba(110, 204, 175, .2);\n"
"    color: rgba(0, 0, 0, .2);\n"
"    border: 2px solid rgba(0, 0, 0, .2);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.labOrdersPushButton.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgba(110, 204, 175, .2);\n"
"    color: rgba(0, 0, 0, .2);\n"
"    border: 2px solid rgba(0, 0, 0, .2);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")

def hideAllWindowsExceptForAppointments():
        '''

            This hides all of the current windows excluding the appointments window
            as it prevents duplication

        '''

        from frontend import StartWindow, ApptRequest, NewPatient, Referrals, LabOrders, CheckIn, CheckOut

        StartWindow.UIWindow.hide()
        NewPatient.UIWindow.hide()
        Referrals.UIWindow.hide()
        CheckIn.UIWindow.hide()
        CheckOut.UIWindow.hide()
        ApptRequest.UIWindow.hide()
        LabOrders.UIWindow.hide()

def changeTitleText(num, window):
        '''

            This changes the title to include both the window name
            and the current username that is logged in

        '''

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
        '''

            Similar for the title, instead this changes the bottom labels

        '''

        window.UIWindow.currentUserLabel.setText("Current User: " + currentUsername[0])

def enterStartWindow(self):
        '''

            This enters the StartWindow

        '''

        from frontend import StartWindow

        print("Routing to start screen")
        self.hide()

        StartWindow.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        StartWindow.UIWindow.show()

def enterSchedulingAppointmentsWindow():
        '''

            This enters the SchedulingAppointmentsWindow

        '''

        from frontend import SchedulingAppointmentsWindow


        print("Routing to scheduling appointments screen")
        hideAllWindowsExceptForAppointments()

        SchedulingAppointmentsWindow.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        SchedulingAppointmentsWindow.UIWindow.show()

        changeCurrentUserLabelText(SchedulingAppointmentsWindow)
        changeTitleText(1, SchedulingAppointmentsWindow)

def enterCheckInWindow(self):
        '''

            This enters the CheckInWindow

        '''

        from frontend import CheckIn
        print("Routing to check in screen")

        if len(currentUsername) == 0:
                print("There is nobody logged in..")
        if len(currentUsername) == 1:
                print("Current User: " + currentUsername[0])

                self.hide()
                CheckIn.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
                CheckIn.UIWindow.show()

                changeCurrentUserLabelText(CheckIn)
                changeTitleText(2, CheckIn)

def enterCheckOutWindow(self):
        '''

            This enters the CheckOutWindow

        '''

        from frontend import CheckOut

        print("Routing to check out screen")

        if len(currentUsername) == 0:
                print("There is nobody logged in..")
        if len(currentUsername) == 1:
                print("Current User: " + currentUsername[0])

                self.hide()
                CheckOut.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
                CheckOut.UIWindow.show()

                changeCurrentUserLabelText(CheckOut)
                changeTitleText(3, CheckOut)

def enterMakeReferralWindow(self):
        '''

            This enters the CheckInWindow

        '''

        from frontend import Referrals
        print("Routing to make referral screen")

        if len(currentUsername) == 0:
                print("There is nobody logged in..")
        if len(currentUsername) == 1:
                print("Current User: " + currentUsername[0])

                self.hide()
                Referrals.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
                Referrals.UIWindow.show()

                changeCurrentUserLabelText(Referrals)
                changeTitleText(4, Referrals)

def enterLabOrdersWindow(self):
        '''

            This enters the LabOrdersWindow

        '''

        from frontend import LabOrders
        print("Routing to lab orders screen")

        if len(currentUsername) == 0:
                print("There is nobody logged in..")
        if len(currentUsername) == 1:
                print("Current User: " + currentUsername[0])

                self.hide()
                LabOrders.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
                LabOrders.UIWindow.show()

                changeCurrentUserLabelText(LabOrders)
                changeTitleText(5, LabOrders)

def enterAppointmentApproveViaPortalWindow(self):
        '''

            This enters the ApptRequestWindow

        '''

        from frontend import ApptRequest
        print("Routing to appointment approve via portal screen")

        if len(currentUsername) == 0:
                print("There is nobody logged in..")
        if len(currentUsername) == 1:
                print("Current User: " + currentUsername[0])

                self.hide()
                ApptRequest.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
                ApptRequest.UIWindow.show()

                changeCurrentUserLabelText(ApptRequest)
                changeTitleText(6, ApptRequest)

def enterNewPatientWindow(self):
        '''

            This enters the NewPatientWindow

        '''


        from frontend import NewPatient
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
                NewPatient.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
                NewPatient.UIWindow.show()

                changeCurrentUserLabelText(NewPatient)
                changeTitleText(7, NewPatient)

def logoutUser(self):
        '''

            This is used to log out the user and sends them back to the login screen

        '''

        from frontend import SchedulingAppointmentsWindow

        # Clearing array values
        currentUsername.clear()
        currentUsername.append("Test")
        currentUserID.clear()
        currentEmployeeID.clear()

        print("LOGGED OUT")

        print("Resetted currentUsername: " + currentUsername[0])

        # Routing user back to the start window and resetting scheduling window and current username label
        SchedulingAppointmentsWindow.UIWindow.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments")
        self.currentUserLabel.setText("No User Logged In")

        enterStartWindow(self)
