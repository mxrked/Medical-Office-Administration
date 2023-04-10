from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QDialog
from sys import exit
from PyQt5 import QtCore, QtGui
from frontend.ui.assets.qrc import app_bg, doctor, show, hide
from frontend.ui.assets.files.GLOBALS import prevWindowCoords


class AMainWindow(QMainWindow):

    def __init__(self):
        super(AMainWindow, self).__init__()

    def load_nav(self):
        """
        Loads all navigation widgets.
        Use if you are on one of the screens with a nav bar right after init
        """

        # Declare widgets
        self.logoutPushButton = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointmentsPushButton = self.findChild(QPushButton, "Nav_Appointments")
        self.checkinPushButton = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkoutPushButton = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.makeReferralPushButton = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.labOrdersPushButton = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approveAppointmentsPushButton = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")
        self.currentUserLabel = self.findChild(QLabel, "currentUserLabel")

        # Do something (Use functions for buttons and stuff)
        self.logoutPushButton.mousePressEvent = lambda event: self.logoutUser()

        # self.appointmentsPushButton.clicked.connect(enterSchedulingAppointmentsWindow)
        self.appointmentsPushButton.mousePressEvent = lambda event: self.enterSchedulingAppointmentsWindow()
        self.checkinPushButton.mousePressEvent = lambda event: self.enterCheckInWindow()
        self.checkoutPushButton.mousePressEvent = lambda event: self.enterCheckOutWindow()
        self.makeReferralPushButton.mousePressEvent = lambda event: self.enterMakeReferralWindow()
        self.labOrdersPushButton.mousePressEvent = lambda event: self.enterLabOrdersWindow()
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: self.enterAppointmentApproveViaPortalWindow()


        self.currentUserLabel.setText("")
        self.currentUserLabel.setText("Current User: " + "USERNAME")
        self.setWindowTitle("")
        self.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments -|- User: " + "USERNAME")

    def load_error(self, error_text: str):
        """
        Loads simple error text box popup with the error_text and a
        close button

        This can be used for db calls that may return error:
        try: 
            add_appointment(appointment)
        except AssertionError as e: 
            load_error(error_text=e)
            return
        
        :param error_text: str to be displayed as errors 
        """
        infoDialog = QDialog()
        infoDialog.setStyleSheet("QDialog {background-color: #344D67}")

        # Dialog settings
        infoDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        infoDialog.setFixedSize(400, 400)

        infoDialogLayout = QVBoxLayout()
        infoDialogCloseBtn = QPushButton("CLOSE", infoDialog)
        infoDialogCloseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        infoDialogCloseBtn.setStyleSheet("""
        QPushButton {
            background-color: #ADE792; 
            border: none; 
            color: #344D67; 
            height: 44px; 
            width: 69px; 
            margin-bottom: 20px;
            font-weight: bold;
        }

        QPushButton::hover {
            color: white;
            background-color: rgb(139, 231, 100);
        }

        """)
        infoDialogCloseBtn.setFont(QtGui.QFont("Lato", 12))
        infoDialogCloseBtn.clicked.connect(infoDialog.close) # Closes the dialog box

        infoDialogName = QLabel(error_text)
        infoDialogName.setStyleSheet("QLabel {color: white}")
        infoDialogName.setFont(QtGui.QFont("Lato", 13))
        infoDialogLayout.addWidget(infoDialogName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        infoDialogLayout.addWidget(infoDialogCloseBtn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        infoDialog.setLayout(infoDialogLayout)

        # Displaying the dialog
        infoDialog.exec_()


    def clearInputs(self):
        for widget in self.findChildren(QLineEdit):
            widget.clear()

    def checkInputs(self, list_of_QLineEdit: list[QLineEdit]) -> bool:
        for widget in list_of_QLineEdit:
            if widget.text() == "":
                return False
        return True

    def closeEvent(self, event):
        exit()
    
    def moveEvent(self, event):
        prevWindowCoords.clear()

        coords = self.pos()

        prevWindowCoords.append(coords.x())
        prevWindowCoords.append(coords.y())


    def changeTitleText(self, num, window):
        '''

            This changes the title to include both the window name
            and the current username that is logged in

        '''
        username = "USERNAME"
        # Title
        if num == 1:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments -|- User: " + username)
        if num == 2:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Check In -|- User: " + username)
        if num == 3:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Check Out -|- User: " + username)
        if num == 4:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Make Referral -|- User: " + username)
        if num == 5:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Lab Orders -|- User: " + username)
        if num == 6:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - Approve Appointment via Portal -|- User: " + username)
        if num == 7:
            window.UIWindow.setWindowTitle("Forsyth Family Practice Center - New Patient -|- User: " + username)


    def greyOutReferralsAndLabOrdersForPhysicians(self):
        '''
            This will check if the isPhysician array is true and then it will
            grey out referrals and lab orders buttons
        '''

        if False == True:
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

    def hideAllWindowsExceptForAppointments(self):
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



    def changeCurrentUserLabelText(self, window):
        '''

            Similar for the title, instead this changes the bottom labels

        '''

        window.UIWindow.currentUserLabel.setText("Current User: " + "User")

    def enterStartWindow(self):
        '''

            This enters the StartWindow

        '''

        from frontend import StartWindow

        print("Routing to start screen")
        self.hide()

        StartWindow.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        StartWindow.UIWindow.show()

    def enterSchedulingAppointmentsWindow(self):
        '''

            This enters the SchedulingAppointmentsWindow

        '''

        from frontend import SchedulingAppointmentsWindow


        print("Routing to scheduling appointments screen")
        self.hideAllWindowsExceptForAppointments()

        SchedulingAppointmentsWindow.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        SchedulingAppointmentsWindow.UIWindow.show()

        self.changeCurrentUserLabelText(SchedulingAppointmentsWindow)
        self.changeTitleText(1, SchedulingAppointmentsWindow)

    def enterCheckInWindow(self):
        '''

            This enters the CheckInWindow

        '''

        from frontend import CheckIn
        print("Routing to check in screen")

        self.hide()
        CheckIn.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        CheckIn.UIWindow.show()

        self.changeCurrentUserLabelText(CheckIn)
        self.changeTitleText(2, CheckIn)

    def enterCheckOutWindow(self):
        '''

        This enters the CheckOutWindow

        '''

        from frontend import CheckOut

        print("Routing to check out screen")

        self.hide()
        CheckOut.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        CheckOut.UIWindow.show()

        self.changeCurrentUserLabelText(CheckOut)
        self.changeTitleText(3, CheckOut)

    def enterMakeReferralWindow(self):
        '''

            This enters the CheckInWindow

        '''

        from frontend import Referrals
        print("Routing to make referral screen")


        self.hide()
        Referrals.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        Referrals.UIWindow.show()

        self.changeCurrentUserLabelText(Referrals)
        self.changeTitleText(4, Referrals)

    def enterLabOrdersWindow(self):
        '''

            This enters the LabOrdersWindow

        '''

        from frontend import LabOrders
        print("Routing to lab orders screen")



        self.hide()
        LabOrders.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        LabOrders.UIWindow.show()

        self.changeCurrentUserLabelText(LabOrders)
        self.changeTitleText(5, LabOrders)

    def enterAppointmentApproveViaPortalWindow(self):
        '''

            This enters the ApptRequestWindow

        '''

        from frontend import ApptRequest
        print("Routing to appointment approve via portal screen")

        self.hide()
        ApptRequest.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        ApptRequest.UIWindow.show()

        self.changeCurrentUserLabelText(ApptRequest)
        self.changeTitleText(6, ApptRequest)

    def enterNewPatientWindow(self):
        '''

            This enters the NewPatientWindow

        '''

        from frontend import NewPatient

        print("Routing to new patient screen")

        self.hide()
        NewPatient.UIWindow.move(prevWindowCoords[0], prevWindowCoords[1])
        NewPatient.UIWindow.show()

        self.changeCurrentUserLabelText(NewPatient)
        self.changeTitleText(7, NewPatient)

    def logoutUser(self):
        '''

            This is used to log out the user and sends them back to the login screen

        '''

        from frontend import SchedulingAppointmentsWindow

        # Routing user back to the start window and resetting scheduling window and current username label
        SchedulingAppointmentsWindow.UIWindow.setWindowTitle("Forsyth Family Practice Center - Scheduling Appointments")
        self.currentUserLabel.setText("No User Logged In")

        self.enterStartWindow()





    