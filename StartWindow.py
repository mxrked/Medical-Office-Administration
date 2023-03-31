from PyQt5 import QtCore, QtGui, QtWidgets
from assets.qrc import app_bg, doctor, show, hide
from assets.files.GLOBALS import *
from assets.files import GLOBALS
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import urllib
import sqlalchemy

import SchedulingAppointmentsWindow


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        ''' FUNCTIONS '''
        def displayInfoDialog():
            ' This is used to display a dialog popup listing the different team members and their roles'

            infoDialog = QtWidgets.QDialog()
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
            infoDialogLayout = QtWidgets.QVBoxLayout()
            infoDialogCloseBtn = QtWidgets.QPushButton("CLOSE", infoDialog)
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
            infoDialogNames = QtWidgets.QFrame()
            infoDialogNamesLayout = QtWidgets.QVBoxLayout()


            for name in GLOBALS.teamMembers:

                infoDialogName = QtWidgets.QLabel(name)

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

        def connectToDB():
                ' This is used to connect to the DB '

                try:
                    import sqlalchemy as sql
                    import pyodbc
                    import urllib
                    from sqlalchemy.pool import QueuePool

                except ImportError as e:
                    print(f"LIBRARY MISSING: {e} \nMake sure your using the correct enviorment")
                    raise e

                params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 18 for SQL Server};SERVER=tcp:capstone2023.database.windows.net,1433;DATABASE=capstone2023;Trusted_Connection=no;Uid=MOAuser;Pwd=Password01!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
                engine = sql.create_engine(conn_str)

                engine.connect()

                # This is used to check if the database is connected
                if engine.connect():
                    print("Connected to database. . .")

                    return engine

                # with engine.connect() as conn:
                #     result = conn.execute(sql.text("SELECT * FROM Appointment"))
                #     for key in result.keys():
                #         print(key)
        def closeDBConnection():
                ' This is used to close the connection to the DB '

                try:
                    import sqlalchemy as sql
                    import pyodbc
                    import urllib
                    from sqlalchemy.pool import QueuePool

                except ImportError as e:
                    print(f"LIBRARY MISSING: {e} \nMake sure your using the correct enviorment")
                    raise e

                params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 18 for SQL Server};SERVER=tcp:capstone2023.database.windows.net,1433;DATABASE=capstone2023;Trusted_Connection=no;Uid=MOAuser;Pwd=Password01!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
                engine = sql.create_engine(conn_str)

                engine.dispose()

                if engine.dispose:
                        print("Closed database. . .")

        def closeApp():
            ' This is used to close the app... duh! '
            closeDBConnection()

            sys.exit()

        def enterSchedulingAppointmentsWindow():

            self.ui = SchedulingAppointmentsWindow.Ui_SchedulingAppointmentsWindow()
            self.window = QtWidgets.QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

            StartWindow.hide()

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
            self.startWindow_PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        def hidePassword():
            ' This is used to hide the password '

            # Hiding/Showing btns
            self.ShowPassword_Label.setFixedHeight(31)
            self.HidePassword_Label.setFixedHeight(0)

            # Changing echomode
            self.startWindow_PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        def loginUser():
            ' This is used to login the user '

            # Connecting to Database
            checkDBConnection = connectToDB()

            userName_Text = getUsername_Text()
            password_Text = getPassword_Text()

            # Declaring the login screen model
            Base = declarative_base()

            class UsersTable(Base):

                __tablename__ = "hold 5"
                Employee_ID = Column(Integer, primary_key=True)
                User_ID = Column(Integer)
                User_Name = Column(String)
                Email_Address = Column(String)
                Password = Column(String)

            # Connecting to database for data
            Session = sessionmaker(bind=checkDBConnection)
            session = Session()

            # Grabbing data entry
            user = session.query(UsersTable).filter(UsersTable.User_Name == userName_Text, UsersTable.Password == password_Text).first()

            # This is used to check if the user is available and will move the user to the scheduling window or not
            if user:

                # This is used to store certain values and make use of them later
                GLOBALS.currentEmployeeID.clear()
                GLOBALS.currentUserID.clear()
                GLOBALS.currentUsername.clear()

                GLOBALS.currentEmployeeID.append(user.Employee_ID)
                GLOBALS.currentUserID.append(user.User_ID)
                GLOBALS.currentUsername.append(user.User_Name)

                # Routing the user to the scheduling window
                print("Welcome, " + currentUsername[0])
                enterSchedulingAppointmentsWindow()

                # closeDBConnection() # Closes to prevent infinite connection/lag
            else:

                GLOBALS.currentEmployeeID.clear()
                GLOBALS.currentUserID.clear()
                GLOBALS.currentUsername.clear()

                print("That user does not exist..")

        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(900, 900)
        StartWindow.setMinimumSize(QtCore.QSize(900, 900))
        StartWindow.setMaximumSize(QtCore.QSize(900, 900))
        StartWindow.setStyleSheet("border-image: url(:/newPrefix/imgs/app-bg.png);")
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startWindow_Heading1 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_Heading1.setGeometry(QtCore.QRect(0, 20, 901, 181))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_Heading1.setFont(font)
        self.startWindow_Heading1.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_Heading1.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_Heading1.setObjectName("startWindow_Heading1")
        self.startWindow_Heading2 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_Heading2.setGeometry(QtCore.QRect(0, 100, 901, 121))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_Heading2.setFont(font)
        self.startWindow_Heading2.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_Heading2.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_Heading2.setObjectName("startWindow_Heading2")
        self.startWindow_SubHeading = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_SubHeading.setGeometry(QtCore.QRect(0, 380, 901, 91))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.startWindow_SubHeading.setFont(font)
        self.startWindow_SubHeading.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: white;\n"
"}")
        self.startWindow_SubHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.startWindow_SubHeading.setObjectName("startWindow_SubHeading")
        self.startWindow_UsernameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.startWindow_UsernameLineEdit.setGeometry(QtCore.QRect(290, 490, 321, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.startWindow_UsernameLineEdit.setFont(font)
        self.startWindow_UsernameLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    min-width: 200px;\n"
"    height: 30px;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    paddding-right: 10px;\n"
"}")
        self.startWindow_UsernameLineEdit.setObjectName("startWindow_UsernameLineEdit")
        self.startWindow_PasswordLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.startWindow_PasswordLineEdit.setGeometry(QtCore.QRect(290, 570, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.startWindow_PasswordLineEdit.setFont(font)
        self.startWindow_PasswordLineEdit.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    min-width: 200px;\n"
"    height: 30px;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    paddding-right: 10px;\n"
"}")
        self.startWindow_PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.startWindow_PasswordLineEdit.setObjectName("startWindow_PasswordLineEdit")
        self.startWindow_LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_LoginBtn.clicked.connect(loginUser)
        self.startWindow_LoginBtn.setGeometry(QtCore.QRect(360, 680, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_LoginBtn.setFont(font)
        self.startWindow_LoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_LoginBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}")
        self.startWindow_LoginBtn.setObjectName("startWindow_LoginBtn")
        self.startWindow_ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_ExitBtn.clicked.connect(closeApp)
        self.startWindow_ExitBtn.setGeometry(QtCore.QRect(460, 680, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.startWindow_ExitBtn.setFont(font)
        self.startWindow_ExitBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_ExitBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: rgb(30, 147, 143);\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(14, 81, 85);\n"
"    color: white;\n"
"}")
        self.startWindow_ExitBtn.setObjectName("startWindow_ExitBtn")
        self.startWindow_InvalidUsernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_InvalidUsernameLabel.setGeometry(QtCore.QRect(290, 590, 0, 0))
        self.startWindow_InvalidUsernameLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setItalic(False)
        self.startWindow_InvalidUsernameLabel.setFont(font)
        self.startWindow_InvalidUsernameLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.startWindow_InvalidUsernameLabel.setObjectName("startWindow_InvalidUsernameLabel")
        self.startWindow_InvalidPasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_InvalidPasswordLabel.setGeometry(QtCore.QRect(290, 690, 0, 0))
        self.startWindow_InvalidPasswordLabel.setMaximumSize(QtCore.QSize(16777215, 0))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setItalic(False)
        self.startWindow_InvalidPasswordLabel.setFont(font)
        self.startWindow_InvalidPasswordLabel.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    color: rgb(0, 255, 127);\n"
"}")
        self.startWindow_InvalidPasswordLabel.setObjectName("startWindow_InvalidPasswordLabel")
        self.startWindow_InfoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_InfoBtn.clicked.connect(displayInfoDialog)
        self.startWindow_InfoBtn.setGeometry(QtCore.QRect(420, 820, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(28)
        self.startWindow_InfoBtn.setFont(font)
        self.startWindow_InfoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startWindow_InfoBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    color: #F3ECB0;\n"
"    background-color: transparent;\n"
"    padding-bottom: 3px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: rgb(241, 243, 103);\n"
"}")
        self.startWindow_InfoBtn.setObjectName("startWindow_InfoBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 190, 221, 211))
        self.label.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    background-color: none;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/doctor.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ShowPassword_Label = QtWidgets.QLabel(self.centralwidget)
        self.ShowPassword_Label.mousePressEvent = lambda event: showPassword()
        self.ShowPassword_Label.setGeometry(QtCore.QRect(580, 580, 31, 31))
        self.ShowPassword_Label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowPassword_Label.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"}")
        self.ShowPassword_Label.setText("")
        self.ShowPassword_Label.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/show.png"))
        self.ShowPassword_Label.setScaledContents(True)
        self.ShowPassword_Label.setObjectName("ShowPassword_Label")
        self.HidePassword_Label = QtWidgets.QLabel(self.centralwidget)
        self.HidePassword_Label.mousePressEvent = lambda event: hidePassword()
        self.HidePassword_Label.setGeometry(QtCore.QRect(580, 580, 31, 0))
        self.HidePassword_Label.setMinimumSize(QtCore.QSize(0, 0))
        self.HidePassword_Label.setMaximumSize(QtCore.QSize(16777215, 0))
        self.HidePassword_Label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HidePassword_Label.setStyleSheet("QLabel {\n"
"    border-image: none;\n"
"    border-radius: 5px;\n"
"    background-color: white;\n"
"}")
        self.HidePassword_Label.setText("")
        self.HidePassword_Label.setPixmap(QtGui.QPixmap(":/newPrefix/imgs/hide.png"))
        self.HidePassword_Label.setScaledContents(True)
        self.HidePassword_Label.setObjectName("HidePassword_Label")
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Forsyth Family Practice Center - MOA"))
        self.startWindow_Heading1.setText(_translate("StartWindow", "Medical Office"))
        self.startWindow_Heading2.setText(_translate("StartWindow", "Administration"))
        self.startWindow_SubHeading.setText(_translate("StartWindow", "Forsyth Family Practice Center"))
        self.startWindow_UsernameLineEdit.setPlaceholderText(_translate("StartWindow", "Enter Username"))
        self.startWindow_PasswordLineEdit.setPlaceholderText(_translate("StartWindow", "Enter Password"))
        self.startWindow_LoginBtn.setText(_translate("StartWindow", "LOGIN"))
        self.startWindow_ExitBtn.setText(_translate("StartWindow", "EXIT"))
        self.startWindow_InvalidUsernameLabel.setText(_translate("StartWindow", "INVALID USERNAME"))
        self.startWindow_InvalidPasswordLabel.setText(_translate("StartWindow", "INVALID PASSWORD"))
        self.startWindow_InfoBtn.setText(_translate("StartWindow", "🛈"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())
