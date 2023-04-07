from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.NAVIGATION_FUNCS import *

import backend.private.data_manager
import urllib
import sqlalchemy
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/apptrequest.ui", self)

        # Session for connecting to the Database
        self.session = backend.private.data_manager.DataManger().session

        # Functions


        # Define widgets
        self.logoutPushButton = self.findChild(QPushButton, "Nav_LogoutBtn")
        self.appointmentsPushButton = self.findChild(QPushButton, "Nav_Appointments")
        self.checkinPushButton = self.findChild(QPushButton, "Nav_CheckinBtn")
        self.checkoutPushButton = self.findChild(QPushButton, "Nav_CheckoutBtn")
        self.makeReferralPushButton = self.findChild(QPushButton, "Nav_MakeReferralBtn")
        self.labOrdersPushButton = self.findChild(QPushButton, "Nav_LabOrdersBtn")
        self.approveAppointmentsPushButton = self.findChild(QPushButton, "Nav_ApproveAppointmentsBtn")
        self.currentUserLabel = self.findChild(QLabel, "currentUserLabel")

        self.list_widget = QListWidget()
        self.list_widget.setObjectName("listView_PendingAppts")

        # Do something (Use functions for buttons and stuff)
        self.logoutPushButton.mousePressEvent = lambda event: logoutUser(self)

        # self.appointmentsPushButton.clicked.connect(enterSchedulingAppointmentsWindow)
        self.appointmentsPushButton.mousePressEvent = lambda event: enterSchedulingAppointmentsWindow()
        self.checkinPushButton.mousePressEvent = lambda event: enterCheckInWindow(self)
        self.checkoutPushButton.mousePressEvent = lambda event: enterCheckOutWindow(self)
        self.makeReferralPushButton.mousePressEvent = lambda event: enterMakeReferralWindow(self)
        self.labOrdersPushButton.mousePressEvent = lambda event: enterLabOrdersWindow(self)
        self.approveAppointmentsPushButton.mousePressEvent = lambda event: enterAppointmentApproveViaPortalWindow(self)


        # Hide the app
        self.hide()

        example_objects = []

        class test_object():
            
            def __init__(self):
                self.name = "Name"
                self.description = "Description"

            def __str__(self):
                return f"My name is {self.name} and I am {self.description}"

        for i in range(0,10):
            example_objects.append(
                    test_object()
                )

        from backend.data_handler import place_objects_into_list

        
        place_objects_into_list(example_objects, self.list_view)
        
    # This will make it so when the user clicks the red x, it closes the app
    def closeEvent(self, event):
        sys.exit()


    def moveEvent(self, event):
        prevWindowCoords.clear()

        coords = self.pos()

        prevWindowCoords.append(coords.x())
        prevWindowCoords.append(coords.y())

        print(prevWindowCoords)

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
# app.exec()
