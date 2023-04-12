"""
StarWindow.py - Window for the login screen of the db
UI Designer: Parker Phelps
Authors: Parker Phelps, Jessica Weeks
"""
from PyQt5.QtWidgets import QApplication, QLineEdit, QLabel, QPushButton, QDialog, QVBoxLayout, QFrame, QMainWindow
from PyQt5 import uic, QtCore, QtGui

from frontend.ui.assets.qrc import app_bg, doctor, show, hide
from frontend.ui.assets.files.GLOBALS import teamMembers
from frontend.ui.assets.files.STYLING import *
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)

        #define widgets
        self.enterUsernameLineEdit = self.findChild(QLineEdit, "startWindow_UsernameLineEdit")
        self.enterPasswordLineEdit = self.findChild(QLineEdit, "startWindow_PasswordLineEdit")
        self.showPasswordLabel = self.findChild(QLabel, "ShowPassword_Label")
        self.hidePasswordLabel = self.findChild(QLabel, "HidePassword_Label")
        self.loginErrorLabel = self.findChild(QLabel, "loginErrorLabel")
        self.loginPushButton = self.findChild(QPushButton, "startWindow_LoginBtn")
        self.exitPushButton = self.findChild(QPushButton, "startWindow_ExitBtn")
        self.infoPushButton = self.findChild(QPushButton, "startWindow_InfoBtn")


        #Do something
        self.loginErrorLabel.hide()
        self.showPasswordLabel.mousePressEvent = lambda event: self.showPassword()
        self.hidePasswordLabel.mousePressEvent = lambda event: self.hidePassword()
        self.loginPushButton.clicked.connect(self.loginUser)
        self.exitPushButton.clicked.connect(self.closeEvent)
        self.infoPushButton.clicked.connect(self.displayInfoDialog)

        #Show the app
        self.show()

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

        user = True


        # This is used to check if the user is available and will move the user to the scheduling window or not
        if user:

            # Hiding login error label
            self.loginErrorLabel.hide()

            # Resetting inputs
            self.enterUsernameLineEdit.setText("")
            self.enterPasswordLineEdit.setText("")
            self.hidePassword()
            self.enterUsernameLineEdit.setStyleSheet(validEnterLE_Style)
            self.enterPasswordLineEdit.setStyleSheet(validEnterLE_Style)

            from frontend.main import MainWindow

            self.hide()

            self.main_window = MainWindow()
            self.main_window.show()

        else:

            # Displaying login error label
            self.loginErrorLabel.show()

            # Adding red border to invalid inputs
            self.enterUsernameLineEdit.setStyleSheet(invalidEnterLE_Style)
            self.enterPasswordLineEdit.setStyleSheet(invalidEnterLE_Style)

            print("That user does not exist..")


#initializing app


app = QApplication(sys.argv)
UIWindow = UI()

def main():
    UIWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()
