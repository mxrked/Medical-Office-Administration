from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor
from frontend.ui.assets.qrc import app_bg, doctor, show, hide
from frontend.ui.assets.files.GLOBALS import *
from frontend.ui.assets.files import GLOBALS
from sqlalchemy import BLOB, Column, Table, Integer, String, VARCHAR, Date, Time, ForeignKey, Numeric, NVARCHAR, Float, NCHAR
from sqlalchemy.orm import sessionmaker, declarative_base

import temp_classes
import backend.db
import sys
import SchedulingAppointmentsWindow

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("ui/StartWindow.ui", self)

<<<<<<< HEAD
        # Session for connecting to the Database
        session = backend.db.get_session()

=======
>>>>>>> 27c856e01ce4d214ce2525371f2191e63e2773fc
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

<<<<<<< HEAD
=======
        def connectToDB():
                ' This is used to connect to the DB '

                try:
                    import sqlalchemy as sql
                    import pyodbc
                    import urllib.parse
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
                    import urllib.parse
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

>>>>>>> 27c856e01ce4d214ce2525371f2191e63e2773fc
        def closeApp():
            ' This is used to close the app... duh! '
            closeDBConnection()
            app.exit()
<<<<<<< HEAD
            backend.db.close_session(session)
=======
>>>>>>> 27c856e01ce4d214ce2525371f2191e63e2773fc

        def enterSchedulingAppointmentsWindow():
            self.hide()
            print(SchedulingAppointmentsWindow)
            SchedulingAppointmentsWindow.UIWindow.show()

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
<<<<<<< HEAD
=======

            # Connecting to Database
            checkDBConnection = connectToDB()

>>>>>>> 27c856e01ce4d214ce2525371f2191e63e2773fc
            userName_Text = getUsername_Text()
            password_Text = getPassword_Text()

            from temp_classes import TempUser

<<<<<<< HEAD
=======
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

>>>>>>> 27c856e01ce4d214ce2525371f2191e63e2773fc
            # Grabbing data entry
            user = session.query(TempUser).filter(TempUser.User_Name == userName_Text, TempUser.Password == password_Text).first()

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

            else:

                GLOBALS.currentEmployeeID.clear()
                GLOBALS.currentUserID.clear()
                GLOBALS.currentUsername.clear()

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
app.exec()
