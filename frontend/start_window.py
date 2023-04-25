"""
StarWindow.py - Window for the login screen of the db
UI Designer: Parker Phelps
Authors: Parker Phelps, Jessica Weeks
"""
import sys
import json
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QDialog, \
    QVBoxLayout, QFrame, QMainWindow
from PyQt5 import uic, QtCore, QtGui

from frontend.ui.assets.qrc import app_bg, doctor, show, hide, gears, logo # pylint: disable=unused-import
from frontend.ui.assets.files.globals import teamMembers
from frontend.ui.assets.files.styling import infoDialog_Style, infoDialogCloseBtn_Style, infoDialogName_Style,\
    validEnterLE_Style, invalidEnterLE_Style
from frontend.dialog.settings_dialog import SettingsDialog
from backend.user_dm import UserDM
from backend.private.data_manager import DataManager


class Start(QMainWindow):
    def __init__(self, debug=False, today=datetime.today().date()):
        super(Start, self).__init__()

        # Used so program shuts down properly
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # used for Debugging
        self.debug = debug
        self.today= today

        # Datamanager
        self.user_dm = UserDM()

        uic.loadUi("frontend/ui/StartWindow.ui", self)

        #define widgets
        self.enterUsernameLineEdit = self.findChild(QLineEdit, "startWindow_UsernameLineEdit")
        self.enterPasswordLineEdit = self.findChild(QLineEdit, "startWindow_PasswordLineEdit")
        self.showPasswordLabel = self.findChild(QLabel, "ShowPassword_Label")
        self.hidePasswordLabel = self.findChild(QLabel, "HidePassword_Label")
        self.loginOutputLabel = self.findChild(QLabel, "loginErrorLabel")
        self.loginPushButton = self.findChild(QPushButton, "startWindow_LoginBtn")
        self.exitPushButton = self.findChild(QPushButton, "startWindow_ExitBtn")
        self.infoPushButton = self.findChild(QPushButton, "startWindow_InfoBtn")
        self.settingsPushButton = self.findChild(QLabel, "StartWindow_SettingsLabel")


        # Setting Events
        self.loginOutputLabel.hide()
        self.showPasswordLabel.mousePressEvent = lambda event: self.showPassword()
        self.hidePasswordLabel.mousePressEvent = lambda event: self.hidePassword()
        self.loginPushButton.clicked.connect(self.loginUser)
        self.exitPushButton.clicked.connect(self.closeEvent)
        self.infoPushButton.clicked.connect(self.displayInfoDialog)
        self.settingsPushButton.mousePressEvent = lambda event: self.displaySettingsDialog()

        # Makes It so we can hit enter to login instead
        self.enterUsernameLineEdit.returnPressed.connect(self.loginUser)
        self.enterPasswordLineEdit.returnPressed.connect(self.loginUser)

        # Load Last used Username
        try:
            with open("frontend/ui/assets/files/Settings.json", "r", 
                      encoding='UTF-8') as settings_file:
                file_contents = settings_file.read()
        
            self.settings_json = json.loads(file_contents)


            last_user = self.settings_json["last_entered_user"]
            if last_user != "":
                self.enterUsernameLineEdit.setText(last_user)
                self.enterPasswordLineEdit.setFocus()

        except FileNotFoundError:
            print("Settings not found")
            self.settings_json = {
                "default_location_ID" : "1",
                "last_entered_user" : ""
            }
            with open("frontend/ui/assets/files/Settings.json", "w",
                      encoding='UTF-8') as file:
                json.dump(self.settings_json, file)


    def displayInfoDialog(self):
        ' This is used to display a dialog popup listing the different team members and their roles'

        infoDialog = QDialog()
        infoDialog.setStyleSheet(infoDialog_Style)
  
        # Dialog settings
        infoDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
        infoDialog.setFixedSize(400, 400)

        # Dialog widgets
        infoDialogLayout = QVBoxLayout()
        infoDialogCloseBtn = QPushButton("CLOSE", infoDialog)
        infoDialogCloseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        infoDialogCloseBtn.setStyleSheet(infoDialogCloseBtn_Style)
        infoDialogCloseBtn.setFont(QtGui.QFont("Lato", 12))
        infoDialogCloseBtn.clicked.connect(infoDialog.close) # Closes the dialog box

        # Creating the team member names
        infoDialogNames = QFrame()
        infoDialogNamesLayout = QVBoxLayout()


        for name in teamMembers:

            infoDialogName = QLabel(name)

            infoDialogName.setStyleSheet(infoDialogName_Style)

            infoDialogName.setFont(QtGui.QFont("Lato", 13))
            infoDialogLayout.addWidget(infoDialogName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


        infoDialogNames.setLayout(infoDialogNamesLayout)

        infoDialogLayout.addWidget(infoDialogNames, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
        infoDialogLayout.addWidget(infoDialogCloseBtn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


        infoDialog.setLayout(infoDialogLayout)

        # Displaying the dialog
        infoDialog.exec_()

    def displaySettingsDialog(self):

        dialog = SettingsDialog()
        dialog.exec_()

        # Restart?

    def closeEvent(self, event): # pylint: disable=unused-argument
        """
            Closes all data managers before exiting the program
        """
        
        data_managers = [self.user_dm]

        for dm in data_managers:
            dm.__del__

        sys.exit()


    def showPassword(self):
        ' This is used to show the password '
        # Hiding/Showing btns
        self.ShowPassword_Label.setFixedHeight(0)
        self.HidePassword_Label.setFixedHeight(31)

        # Changing echomode
        self.startWindow_PasswordLineEdit.setEchoMode(QLineEdit.Normal)
    
    def hidePassword(self):
        ' This is used to hide the password '

        # Hiding/Showing btns
        self.ShowPassword_Label.setFixedHeight(31)
        self.HidePassword_Label.setFixedHeight(0)

        # Changing echomode
        self.startWindow_PasswordLineEdit.setEchoMode(QLineEdit.Password)


    def loginUser(self):
        """ This is used to login the user """

        userName_Text = self.startWindow_UsernameLineEdit.text()
        password_Text = self.startWindow_PasswordLineEdit.text()
        
        # Returns none if no employee
        employee = self.user_dm.check_username_password(userName_Text, password_Text)

        if employee or self.debug:
            
            if self.debug:
                can_login = True
                can_physician = True
                can_schedule = True
            else:
                # Get Permissions, with user_dm
                can_login = self.user_dm.check_employee_role(employee, 1)
                can_physician = self.user_dm.check_employee_role(employee, 2)
                can_schedule = self.user_dm.check_employee_role(employee, 3)
            
                if not can_login:
                    self.loginOutputLabel.show()
                    return None



            # Save Last User
            self.settings_json["last_entered_user"] = userName_Text
            with open("frontend/ui/assets/files/Settings.json", "w", encoding='UTF-8') as file:
                json.dump(self.settings_json, file)
    
            # Hiding login error label

            # Resetting inputs
            self.enterUsernameLineEdit.setText("")
            self.enterPasswordLineEdit.setText("")
            self.hidePassword()
            self.enterUsernameLineEdit.setStyleSheet(validEnterLE_Style)
            self.enterPasswordLineEdit.setStyleSheet(validEnterLE_Style)

            self.hide()

            # We must import here to avoid circular imports
            from frontend.main_window import MainWindow

            main_window = MainWindow(can_physician, can_schedule, self.debug, self.today)
            main_window.show()

        else:

            # Displaying login error label
            self.loginOutputLabel.show()

            # Adding red border to invalid inputs
            self.enterUsernameLineEdit.setStyleSheet(invalidEnterLE_Style)
            self.enterPasswordLineEdit.setStyleSheet(invalidEnterLE_Style)

            print("That user does not exist..")


#initializing app




def main(debug=False, today=datetime.today().date()):
    app = QApplication(sys.argv)
    UIWindow = Start(debug=debug, today=today)
    UIWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()
