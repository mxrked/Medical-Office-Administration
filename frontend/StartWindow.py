from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from frontend.ui.assets.qrc import app_bg, doctor, show, hide
from frontend.ui.assets.files.GLOBALS import *
from frontend.ui.assets.files import GLOBALS

import temp_classes
import data_manager
import sys
import SchedulingAppointmentsWindow

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # print(currentUsername[0])
        uic.loadUi("ui/StartWindow.ui", self)


        # Session for connecting to the Database
        session = data_manager.DataManger().session

        # Functions
        def displayInfoDialog():
            ' This is used to display a dialog popup listing the different team members and their roles'

            infoDialog = QDialog()
            infoDialog.setStyleSheet("""
            
                QDialog {
                    background-color: #344D67;
                }
            
            """)

            # Dialog settings
            infoDialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar
            infoDialog.setWindowTitle("Meet the team.")
            infoDialog.setFixedSize(400, 400)

            # Dialog widgets
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

            # Creating the team member names
            infoDialogNames = QFrame()
            infoDialogNamesLayout = QVBoxLayout()


            for name in GLOBALS.teamMembers:

                infoDialogName = QLabel(name)

                infoDialogName.setStyleSheet("""
                
                    QLabel {
                        color: white;
                    }
                
                """)

                infoDialogName.setFont(QtGui.QFont("Lato", 13))
                infoDialogLayout.addWidget(infoDialogName, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


            infoDialogNames.setLayout(infoDialogNamesLayout)

            infoDialogLayout.addWidget(infoDialogNames, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
            infoDialogLayout.addWidget(infoDialogCloseBtn, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


            infoDialog.setLayout(infoDialogLayout)

            # Displaying the dialog
            infoDialog.exec_()

        def closeApp():
            ' This is used to close the app... duh! '
            app.exit()

        def getUsername_Text():
            return self.startWindow_UsernameLineEdit.text()
        def getPassword_Text():
            return self.startWindow_PasswordLineEdit.text()

        def showPassword():
            ' This is used to show the password '

            # Hiding/Showing btns
            self.ShowPassword_Label.setFixedHeight(0)
            self.HidePassword_Label.setFixedHeight(31)

            # Changing echomode
            self.startWindow_PasswordLineEdit.setEchoMode(QLineEdit.Normal)
        def hidePassword():
            ' This is used to hide the password '

            # Hiding/Showing btns
            self.ShowPassword_Label.setFixedHeight(31)
            self.HidePassword_Label.setFixedHeight(0)

            # Changing echomode
            self.startWindow_PasswordLineEdit.setEchoMode(QLineEdit.Password)

        def loginUser():
            ' This is used to login the user '

            userName_Text = getUsername_Text()
            password_Text = getPassword_Text()

            from temp_classes import TempUser

            # Grabbing data entry
            user = session.query(TempUser).filter(TempUser.User_Name == userName_Text, TempUser.Password == password_Text).first()
            currentUsername.clear()

            # This is used to check if the user is available and will move the user to the scheduling window or not
            if user:

                # This is used to store certain values and make use of them later
                GLOBALS.currentEmployeeID.clear()
                GLOBALS.currentUserID.clear()
                GLOBALS.currentUsername.clear()

                GLOBALS.currentEmployeeID.append(user.Employee_ID)
                GLOBALS.currentUserID.append(user.User_ID)

                # Routing the user to the scheduling window
                currentUsername.append(str(user.User_Name))


                # Resetting inputs
                self.enterUsernameLineEdit.setText("")
                self.enterPasswordLineEdit.setText("")
                hidePassword()

                from frontend.ui.assets.files.NAVIGATION_FUNCS import enterSchedulingAppointmentsWindow

                self.hide()

                enterSchedulingAppointmentsWindow(self)

            else:

                GLOBALS.currentEmployeeID.clear()
                GLOBALS.currentUserID.clear()
                GLOBALS.currentUsername.clear()
                GLOBALS.currentUsername.append("Test")

                print("That user does not exist..")


        #define widgets
        self.enterUsernameLineEdit = self.findChild(QLineEdit, "startWindow_UsernameLineEdit")
        self.enterPasswordLineEdit = self.findChild(QLineEdit, "startWindow_PasswordLineEdit")
        self.showPasswordLabel = self.findChild(QLabel, "ShowPassword_Label")
        self.hidePasswordLabel = self.findChild(QLabel, "HidePassword_Label")
        self.loginPushButton = self.findChild(QPushButton, "startWindow_LoginBtn")
        self.exitPushButton = self.findChild(QPushButton, "startWindow_ExitBtn")
        self.infoPushButton = self.findChild(QPushButton, "startWindow_InfoBtn")


        #Do something
        self.showPasswordLabel.mousePressEvent = lambda event: showPassword()
        self.hidePasswordLabel.mousePressEvent = lambda event: hidePassword()
        self.loginPushButton.clicked.connect(loginUser)
        self.exitPushButton.clicked.connect(closeApp)
        self.infoPushButton.clicked.connect(displayInfoDialog)


        #Show the app
        self.show()


    # This will make it so when the user clicks the red x, it closes all windows
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()
        app.exit()

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()

app.exec_()
