

from PyQt5 import QtCore, QtGui, QtWidgets
from assets.qrc import app_bg
from assets.files.GLOBALS import *

import urllib
import sqlalchemy

class Ui_SchedulingAppointmentsWindow(object):
    def setupUi(self, SchedulingAppointmentsWindow):
        ' FUNCTIONS '
        def clearInputs():
                ' This is used to clear/reset the inputs '
                self.LineEdit_PatientFirstName_2.setText("")
                self.LineEdit_PatientLastName_2.setText("")
                self.LineEdit_AppointmentReason.setText("")
                self.LineEdit_MeetDateTime.setText("")

                defaultDate = QtCore.QDate(2000, 1, 1)
                self.dateEdit_DOB_2.setDate(defaultDate)

                self.ComboBox_AppointmentType.setCurrentIndex(0)

                self.ListWidget_MeetDateTimes.clearSelection()

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

                params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:capstone2023.database.windows.net,1433;DATABASE=capstone2023;Trusted_Connection=no;Uid=MOAuser;Pwd=Password01!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
                engine = sql.create_engine(conn_str)

                engine.dispose()

                if engine.dispose:
                        print("Closed database. . .")

        def hideAllFrames():
                ' This is used to hide the different frames '

                self.InputsFrame.setVisible(False)
                self.RescheduleAppointment_Frame.setVisible(False)
                self.CancelAppointment_Frame.setVisible(False)

                self.DisplaySchedule_Btn.setEnabled(True)
                self.DisplayReschedule_Btn.setEnabled(True)
                self.DisplayCancel_Btn.setEnabled(True)

                # Resetting styles for buttons
                self.DisplaySchedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
                self.DisplayReschedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
                self.DisplayCancel_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")

        def checkAvailableTimes():
                ' This is used to display/filter the possible available times '
        def checkCurrentAppointments():
                ' This is used to check the current appointments '

        def displayScheduling():
                ' This is used to display the scheduling module '

                hideAllFrames()

                self.InputsFrame.setVisible(True)
                self.DisplaySchedule_Btn.setEnabled(False)

                self.DisplaySchedule_Btn.setStyleSheet("QPushButton {\n"
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
        def displayReschedule():
                ' This is used to display the rescheduling module '

                hideAllFrames()

                self.RescheduleAppointment_Frame.setVisible(True)
                self.DisplayReschedule_Btn.setEnabled(False)

                # Refreshes the available times and appointments
                checkAvailableTimes()
                checkCurrentAppointments()

                self.DisplayReschedule_Btn.setStyleSheet("QPushButton {\n"
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
        def displayCancel():
                ' This is used to display the cancel module '

                hideAllFrames()

                self.CancelAppointment_Frame.setVisible(True)
                self.DisplayCancel_Btn.setEnabled(False)

                self.DisplayCancel_Btn.setStyleSheet("QPushButton {\n"
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

        def getPatientFN():
                ' This is used to get the patients first name in the DB '

                # Connecting to Database
                checkDBConnection = connectToDB()
        def getPatientLN():
                ' This is used to get the patients last name in the DB '

                # Connecting to Database
                checkDBConnection = connectToDB()
        def getPatientDOB():
                ' This is used to get the patients DOB in the DB '
                print()
        def getAppointmentType():
                ' This is used to get the Appointment Type in the DB '
                print()
        def getAppointmentReason():
                ' This is used to get the Appointment Reason in the DB '
                print()
        def getAppointmentDate():
                ' This is used to get the Appointment Date in the DB '
                print()
        def getAppointmentTime():
                ' This is used to get the Appointment Time in the DB '
                print()

        def scheduleAppointment():
                ' This is used to schedule an appointment '
        def rescheduleAppointment():
                ' This is used to reschedule an appointment '
        def cancelAppointment():
                ' This is used to cancel an appointment '


        connectToDB()
        # closeDBConnection()

        SchedulingAppointmentsWindow.setObjectName("SchedulingAppointmentsWindow")
        SchedulingAppointmentsWindow.resize(1430, 925)
        SchedulingAppointmentsWindow.setMinimumSize(QtCore.QSize(1420, 925))
        SchedulingAppointmentsWindow.setMaximumSize(QtCore.QSize(1430, 925))
        self.centralwidget = QtWidgets.QWidget(SchedulingAppointmentsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(0, -1, 1500, 941))
        self.MainFrame.setStyleSheet("QFrame {\n"
"    border-image: url(:/newPrefix/imgs/app-bg.png);\n"
"}")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.layoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 41, 1181, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Layout_NavBar = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Layout_NavBar.setContentsMargins(0, 0, 0, 0)
        self.Layout_NavBar.setSpacing(20)
        self.Layout_NavBar.setObjectName("Layout_NavBar")
        self.Nav_LogoutBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_LogoutBtn.setMinimumSize(QtCore.QSize(80, 40))
        self.Nav_LogoutBtn.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_LogoutBtn.setFont(font)
        self.Nav_LogoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_LogoutBtn.setStyleSheet("QPushButton {\n"
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
        self.Nav_LogoutBtn.setObjectName("Nav_LogoutBtn")
        self.Layout_NavBar.addWidget(self.Nav_LogoutBtn)
        self.Nav_Appointments = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_Appointments.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Nav_Appointments.sizePolicy().hasHeightForWidth())
        self.Nav_Appointments.setSizePolicy(sizePolicy)
        self.Nav_Appointments.setMinimumSize(QtCore.QSize(160, 40))
        self.Nav_Appointments.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_Appointments.setFont(font)
        self.Nav_Appointments.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_Appointments.setAutoFillBackground(False)
        self.Nav_Appointments.setStyleSheet("QPushButton {\n"
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
        self.Nav_Appointments.setObjectName("Nav_Appointments")
        self.Layout_NavBar.addWidget(self.Nav_Appointments)
        self.Nav_CheckinBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_CheckinBtn.setMinimumSize(QtCore.QSize(110, 40))
        self.Nav_CheckinBtn.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_CheckinBtn.setFont(font)
        self.Nav_CheckinBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_CheckinBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.Nav_CheckinBtn.setObjectName("Nav_CheckinBtn")
        self.Layout_NavBar.addWidget(self.Nav_CheckinBtn)
        self.Nav_CheckoutBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_CheckoutBtn.setMinimumSize(QtCore.QSize(110, 40))
        self.Nav_CheckoutBtn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_CheckoutBtn.setFont(font)
        self.Nav_CheckoutBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_CheckoutBtn.setStyleSheet("QPushButton {\n"
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
        self.Nav_CheckoutBtn.setObjectName("Nav_CheckoutBtn")
        self.Layout_NavBar.addWidget(self.Nav_CheckoutBtn)
        self.Nav_MakeReferralBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_MakeReferralBtn.setMinimumSize(QtCore.QSize(150, 40))
        self.Nav_MakeReferralBtn.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_MakeReferralBtn.setFont(font)
        self.Nav_MakeReferralBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_MakeReferralBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"")
        self.Nav_MakeReferralBtn.setObjectName("Nav_MakeReferralBtn")
        self.Layout_NavBar.addWidget(self.Nav_MakeReferralBtn)
        self.Nav_LabOrdersBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_LabOrdersBtn.setMinimumSize(QtCore.QSize(120, 40))
        self.Nav_LabOrdersBtn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_LabOrdersBtn.setFont(font)
        self.Nav_LabOrdersBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_LabOrdersBtn.setStyleSheet("QPushButton {\n"
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
        self.Nav_LabOrdersBtn.setObjectName("Nav_LabOrdersBtn")
        self.Layout_NavBar.addWidget(self.Nav_LabOrdersBtn)
        self.Nav_ApproveAppointmentsBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.Nav_ApproveAppointmentsBtn.setMinimumSize(QtCore.QSize(240, 40))
        self.Nav_ApproveAppointmentsBtn.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Nav_ApproveAppointmentsBtn.setFont(font)
        self.Nav_ApproveAppointmentsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nav_ApproveAppointmentsBtn.setStyleSheet("QPushButton {\n"
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
        self.Nav_ApproveAppointmentsBtn.setObjectName("Nav_ApproveAppointmentsBtn")
        self.Layout_NavBar.addWidget(self.Nav_ApproveAppointmentsBtn)
        self.InputsFrame = QtWidgets.QFrame(self.MainFrame)
        self.InputsFrame.setGeometry(QtCore.QRect(110, 200, 1181, 681))
        self.InputsFrame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.InputsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InputsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputsFrame.setObjectName("InputsFrame")
        self.HeadingLabel = QtWidgets.QLabel(self.InputsFrame)
        self.HeadingLabel.setGeometry(QtCore.QRect(0, 0, 1181, 150))
        self.HeadingLabel.setMinimumSize(QtCore.QSize(0, 150))
        self.HeadingLabel.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.HeadingLabel.setFont(font)
        self.HeadingLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HeadingLabel.setObjectName("HeadingLabel")
        self.UnderHeadingTextLabel = QtWidgets.QLabel(self.InputsFrame)
        self.UnderHeadingTextLabel.setGeometry(QtCore.QRect(0, 110, 1181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel.setFont(font)
        self.UnderHeadingTextLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel.setObjectName("UnderHeadingTextLabel")
        self.InputsInnerFrame = QtWidgets.QFrame(self.InputsFrame)
        self.InputsInnerFrame.setGeometry(QtCore.QRect(100, 220, 591, 341))
        self.InputsInnerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InputsInnerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputsInnerFrame.setObjectName("InputsInnerFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.InputsInnerFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InputsInnerVLayout = QtWidgets.QVBoxLayout()
        self.InputsInnerVLayout.setObjectName("InputsInnerVLayout")
        self.InputsRowHLayout_1 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_1.setObjectName("InputsRowHLayout_1")
        self.Label_PatientFirstName_2 = QtWidgets.QLabel(self.InputsInnerFrame)
        self.Label_PatientFirstName_2.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_PatientFirstName_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_PatientFirstName_2.setFont(font)
        self.Label_PatientFirstName_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_PatientFirstName_2.setObjectName("Label_PatientFirstName_2")
        self.InputsRowHLayout_1.addWidget(self.Label_PatientFirstName_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_1.addItem(spacerItem)
        self.LineEdit_PatientFirstName_2 = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_PatientFirstName_2.setMinimumSize(QtCore.QSize(350, 40))
        self.LineEdit_PatientFirstName_2.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_PatientFirstName_2.setFont(font)
        self.LineEdit_PatientFirstName_2.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_PatientFirstName_2.setText("")
        self.LineEdit_PatientFirstName_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineEdit_PatientFirstName_2.setObjectName("LineEdit_PatientFirstName_2")
        self.InputsRowHLayout_1.addWidget(self.LineEdit_PatientFirstName_2)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem1)
        self.InputsRowHLayout_2 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_2.setObjectName("InputsRowHLayout_2")
        self.Layout_PatientLastName_2 = QtWidgets.QHBoxLayout()
        self.Layout_PatientLastName_2.setObjectName("Layout_PatientLastName_2")
        self.Label_PatientLastName_2 = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_PatientLastName_2.setFont(font)
        self.Label_PatientLastName_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_PatientLastName_2.setObjectName("Label_PatientLastName_2")
        self.Layout_PatientLastName_2.addWidget(self.Label_PatientLastName_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_PatientLastName_2.addItem(spacerItem2)
        self.LineEdit_PatientLastName_2 = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_PatientLastName_2.setMinimumSize(QtCore.QSize(350, 40))
        self.LineEdit_PatientLastName_2.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_PatientLastName_2.setFont(font)
        self.LineEdit_PatientLastName_2.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_PatientLastName_2.setText("")
        self.LineEdit_PatientLastName_2.setObjectName("LineEdit_PatientLastName_2")
        self.Layout_PatientLastName_2.addWidget(self.LineEdit_PatientLastName_2)
        self.InputsRowHLayout_2.addLayout(self.Layout_PatientLastName_2)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem3)
        self.InputsRowHLayout_3 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_3.setObjectName("InputsRowHLayout_3")
        self.Layout_DOB_2 = QtWidgets.QHBoxLayout()
        self.Layout_DOB_2.setObjectName("Layout_DOB_2")
        self.Label_DOB_2 = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_DOB_2.setFont(font)
        self.Label_DOB_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_DOB_2.setObjectName("Label_DOB_2")
        self.Layout_DOB_2.addWidget(self.Label_DOB_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_DOB_2.addItem(spacerItem4)
        self.dateEdit_DOB_2 = QtWidgets.QDateEdit(self.InputsInnerFrame)
        self.dateEdit_DOB_2.setMinimumSize(QtCore.QSize(350, 40))
        self.dateEdit_DOB_2.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.dateEdit_DOB_2.setFont(font)
        self.dateEdit_DOB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_DOB_2.setStyleSheet("QDateEdit {\n"
"    QLineEdit \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"\n"
"/** \n"
"    QDateEdit QAbstractItemView:enabled {\n"
"    color: black;\n"
"    background-color: ghostwhite;\n"
"    selection-background-color: rgb(0, 177, 171);\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QCalendarWidget QTableView QLabel {\n"
"    color: white;\n"
"}\n"
"*/")
        self.dateEdit_DOB_2.setCalendarPopup(False)
        self.dateEdit_DOB_2.setObjectName("dateEdit_DOB_2")
        self.Layout_DOB_2.addWidget(self.dateEdit_DOB_2)
        self.InputsRowHLayout_3.addLayout(self.Layout_DOB_2)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem5)
        self.InputsRowHLayout_6 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_6.setObjectName("InputsRowHLayout_6")
        self.Label_AppointmentType = QtWidgets.QLabel(self.InputsInnerFrame)
        self.Label_AppointmentType.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_AppointmentType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_AppointmentType.setFont(font)
        self.Label_AppointmentType.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_AppointmentType.setObjectName("Label_AppointmentType")
        self.InputsRowHLayout_6.addWidget(self.Label_AppointmentType)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_6.addItem(spacerItem6)
        self.ComboBox_AppointmentType = QtWidgets.QComboBox(self.InputsInnerFrame)
        self.ComboBox_AppointmentType.setMinimumSize(QtCore.QSize(350, 40))
        self.ComboBox_AppointmentType.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_AppointmentType.setFont(font)
        self.ComboBox_AppointmentType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboBox_AppointmentType.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_AppointmentType.setObjectName("ComboBox_AppointmentType")
        self.ComboBox_AppointmentType.addItem("")
        self.InputsRowHLayout_6.addWidget(self.ComboBox_AppointmentType)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem7)
        self.InputsRowHLayout_4 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_4.setObjectName("InputsRowHLayout_4")
        self.Label_AppointmentReason = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_AppointmentReason.setFont(font)
        self.Label_AppointmentReason.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_AppointmentReason.setObjectName("Label_AppointmentReason")
        self.InputsRowHLayout_4.addWidget(self.Label_AppointmentReason)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_4.addItem(spacerItem8)
        self.LineEdit_AppointmentReason = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_AppointmentReason.setMinimumSize(QtCore.QSize(350, 40))
        self.LineEdit_AppointmentReason.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_AppointmentReason.setFont(font)
        self.LineEdit_AppointmentReason.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_AppointmentReason.setObjectName("LineEdit_AppointmentReason")
        self.InputsRowHLayout_4.addWidget(self.LineEdit_AppointmentReason)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem9)
        self.InputsRowHLayout_5 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_5.setObjectName("InputsRowHLayout_5")
        self.Label_AppointmentReason_2 = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_AppointmentReason_2.setFont(font)
        self.Label_AppointmentReason_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_AppointmentReason_2.setObjectName("Label_AppointmentReason_2")
        self.InputsRowHLayout_5.addWidget(self.Label_AppointmentReason_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_5.addItem(spacerItem10)
        self.LineEdit_MeetDateTime = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_MeetDateTime.setEnabled(False)
        self.LineEdit_MeetDateTime.setMinimumSize(QtCore.QSize(350, 40))
        self.LineEdit_MeetDateTime.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_MeetDateTime.setFont(font)
        self.LineEdit_MeetDateTime.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_MeetDateTime.setText("")
        self.LineEdit_MeetDateTime.setObjectName("LineEdit_MeetDateTime")
        self.InputsRowHLayout_5.addWidget(self.LineEdit_MeetDateTime)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_5)
        self.verticalLayout_3.addLayout(self.InputsInnerVLayout)
        self.TimesHolderFrame = QtWidgets.QFrame(self.InputsFrame)
        self.TimesHolderFrame.setGeometry(QtCore.QRect(730, 220, 341, 331))
        self.TimesHolderFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimesHolderFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimesHolderFrame.setObjectName("TimesHolderFrame")
        self.ListWidget_MeetDateTimes = QtWidgets.QListWidget(self.TimesHolderFrame)
        self.ListWidget_MeetDateTimes.setGeometry(QtCore.QRect(0, 10, 341, 321))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_MeetDateTimes.setFont(font)
        self.ListWidget_MeetDateTimes.setStyleSheet("QListWidget {\n"
"    background-color:#F3ECB0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(186, 186, 186);\n"
"    height: 40px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(0, 177, 171);\n"
"    color: black;\n"
"}")
        self.ListWidget_MeetDateTimes.setObjectName("ListWidget_MeetDateTimes")
        self.CheckAvailableTimesBtn = QtWidgets.QPushButton(self.InputsFrame)
        self.CheckAvailableTimesBtn.setGeometry(QtCore.QRect(780, 580, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CheckAvailableTimesBtn.setFont(font)
        self.CheckAvailableTimesBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CheckAvailableTimesBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.CheckAvailableTimesBtn.setObjectName("CheckAvailableTimesBtn")
        self.ScheduleAppointmentBtn = QtWidgets.QPushButton(self.InputsFrame)
        self.ScheduleAppointmentBtn.setEnabled(True)
        self.ScheduleAppointmentBtn.setGeometry(QtCore.QRect(110, 580, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ScheduleAppointmentBtn.setFont(font)
        self.ScheduleAppointmentBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScheduleAppointmentBtn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.ScheduleAppointmentBtn.setObjectName("ScheduleAppointmentBtn")
        self.ClearInputsBtn = QtWidgets.QPushButton(self.InputsFrame)
        self.ClearInputsBtn.clicked.connect(clearInputs)
        self.ClearInputsBtn.setGeometry(QtCore.QRect(360, 580, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ClearInputsBtn.setFont(font)
        self.ClearInputsBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ClearInputsBtn.setStyleSheet("QPushButton {\n"
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
        self.ClearInputsBtn.setObjectName("ClearInputsBtn")
        self.CurrentAvailableTimes_Label = QtWidgets.QLabel(self.InputsFrame)
        self.CurrentAvailableTimes_Label.setGeometry(QtCore.QRect(730, 195, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAvailableTimes_Label.setFont(font)
        self.CurrentAvailableTimes_Label.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAvailableTimes_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAvailableTimes_Label.setObjectName("CurrentAvailableTimes_Label")
        self.CancelAppointment_Frame = QtWidgets.QFrame(self.MainFrame)
        self.CancelAppointment_Frame.setVisible(False)
        self.CancelAppointment_Frame.setGeometry(QtCore.QRect(340, 200, 721, 681))
        self.CancelAppointment_Frame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.CancelAppointment_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CancelAppointment_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CancelAppointment_Frame.setObjectName("CancelAppointment_Frame")
        self.CancelAppointment_HeadingLabel = QtWidgets.QLabel(self.CancelAppointment_Frame)
        self.CancelAppointment_HeadingLabel.setGeometry(QtCore.QRect(0, 0, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.CancelAppointment_HeadingLabel.setFont(font)
        self.CancelAppointment_HeadingLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CancelAppointment_HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CancelAppointment_HeadingLabel.setObjectName("CancelAppointment_HeadingLabel")
        self.CurrentAppointments_Frame_3 = QtWidgets.QFrame(self.CancelAppointment_Frame)
        self.CurrentAppointments_Frame_3.setGeometry(QtCore.QRect(140, 250, 451, 281))
        self.CurrentAppointments_Frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CurrentAppointments_Frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CurrentAppointments_Frame_3.setObjectName("CurrentAppointments_Frame_3")
        self.ListWidget_CurrentAppointments_3 = QtWidgets.QListWidget(self.CurrentAppointments_Frame_3)
        self.ListWidget_CurrentAppointments_3.setGeometry(QtCore.QRect(0, 0, 451, 281))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_CurrentAppointments_3.setFont(font)
        self.ListWidget_CurrentAppointments_3.setStyleSheet("QListWidget {\n"
"    background-color:#F3ECB0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(186, 186, 186);\n"
"    height: 40px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(0, 177, 171);\n"
"    color: black;\n"
"}")
        self.ListWidget_CurrentAppointments_3.setObjectName("ListWidget_CurrentAppointments_3")
        self.UnderHeadingTextLabel_4 = QtWidgets.QLabel(self.CancelAppointment_Frame)
        self.UnderHeadingTextLabel_4.setGeometry(QtCore.QRect(90, 100, 541, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_4.setFont(font)
        self.UnderHeadingTextLabel_4.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_4.setWordWrap(True)
        self.UnderHeadingTextLabel_4.setObjectName("UnderHeadingTextLabel_4")
        self.CurrentAppointments_Label_5 = QtWidgets.QLabel(self.CancelAppointment_Frame)
        self.CurrentAppointments_Label_5.setGeometry(QtCore.QRect(140, 200, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAppointments_Label_5.setFont(font)
        self.CurrentAppointments_Label_5.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAppointments_Label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAppointments_Label_5.setObjectName("CurrentAppointments_Label_5")
        self.CancelAppointment_Btn = QtWidgets.QPushButton(self.CancelAppointment_Frame)
        self.CancelAppointment_Btn.clicked.connect(cancelAppointment)
        self.CancelAppointment_Btn.setEnabled(True)
        self.CancelAppointment_Btn.setGeometry(QtCore.QRect(250, 580, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CancelAppointment_Btn.setFont(font)
        self.CancelAppointment_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CancelAppointment_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.CancelAppointment_Btn.setObjectName("CancelAppointment_Btn")
        self.RescheduleAppointment_Frame = QtWidgets.QFrame(self.MainFrame)
        self.RescheduleAppointment_Frame.setVisible(False)
        self.RescheduleAppointment_Frame.setGeometry(QtCore.QRect(340, 200, 721, 681))
        self.RescheduleAppointment_Frame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.RescheduleAppointment_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RescheduleAppointment_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RescheduleAppointment_Frame.setObjectName("RescheduleAppointment_Frame")
        self.RescheduleAppointment_HeadingLabel_3 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.RescheduleAppointment_HeadingLabel_3.setGeometry(QtCore.QRect(0, 0, 701, 151))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.RescheduleAppointment_HeadingLabel_3.setFont(font)
        self.RescheduleAppointment_HeadingLabel_3.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.RescheduleAppointment_HeadingLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.RescheduleAppointment_HeadingLabel_3.setObjectName("RescheduleAppointment_HeadingLabel_3")
        self.CurrentAppointments_Frame_4 = QtWidgets.QFrame(self.RescheduleAppointment_Frame)
        self.CurrentAppointments_Frame_4.setGeometry(QtCore.QRect(120, 250, 451, 121))
        self.CurrentAppointments_Frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CurrentAppointments_Frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CurrentAppointments_Frame_4.setObjectName("CurrentAppointments_Frame_4")
        self.ListWidget_CurrentAppointments_4 = QtWidgets.QListWidget(self.CurrentAppointments_Frame_4)
        self.ListWidget_CurrentAppointments_4.setGeometry(QtCore.QRect(0, 0, 451, 171))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_CurrentAppointments_4.setFont(font)
        self.ListWidget_CurrentAppointments_4.setStyleSheet("QListWidget {\n"
"    background-color:#F3ECB0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(186, 186, 186);\n"
"    height: 40px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(0, 177, 171);\n"
"    color: black;\n"
"}")
        self.ListWidget_CurrentAppointments_4.setObjectName("ListWidget_CurrentAppointments_4")
        self.TimesHolderFrame_4 = QtWidgets.QFrame(self.RescheduleAppointment_Frame)
        self.TimesHolderFrame_4.setGeometry(QtCore.QRect(120, 440, 451, 121))
        self.TimesHolderFrame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimesHolderFrame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimesHolderFrame_4.setObjectName("TimesHolderFrame_4")
        self.ListWidget_MeetDateTimes_4 = QtWidgets.QListWidget(self.TimesHolderFrame_4)
        self.ListWidget_MeetDateTimes_4.setGeometry(QtCore.QRect(0, 0, 451, 121))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_MeetDateTimes_4.setFont(font)
        self.ListWidget_MeetDateTimes_4.setStyleSheet("QListWidget {\n"
"    background-color:#F3ECB0;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    border: 1px solid rgb(186, 186, 186);\n"
"    height: 40px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgb(0, 177, 171);\n"
"    color: black;\n"
"}")
        self.ListWidget_MeetDateTimes_4.setObjectName("ListWidget_MeetDateTimes_4")
        self.CurrentAppointments_Label_6 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.CurrentAppointments_Label_6.setGeometry(QtCore.QRect(120, 410, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAppointments_Label_6.setFont(font)
        self.CurrentAppointments_Label_6.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAppointments_Label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAppointments_Label_6.setObjectName("CurrentAppointments_Label_6")
        self.UnderHeadingTextLabel_5 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.UnderHeadingTextLabel_5.setGeometry(QtCore.QRect(30, 110, 661, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_5.setFont(font)
        self.UnderHeadingTextLabel_5.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_5.setWordWrap(True)
        self.UnderHeadingTextLabel_5.setObjectName("UnderHeadingTextLabel_5")
        self.CurrentAppointments_Label_7 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.CurrentAppointments_Label_7.setGeometry(QtCore.QRect(120, 210, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAppointments_Label_7.setFont(font)
        self.CurrentAppointments_Label_7.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAppointments_Label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAppointments_Label_7.setObjectName("CurrentAppointments_Label_7")
        self.RescheduleAppointment_Btn_3 = QtWidgets.QPushButton(self.RescheduleAppointment_Frame)
        self.RescheduleAppointment_Btn_3.clicked.connect(rescheduleAppointment)
        self.RescheduleAppointment_Btn_3.setGeometry(QtCore.QRect(200, 590, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.RescheduleAppointment_Btn_3.setFont(font)
        self.RescheduleAppointment_Btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RescheduleAppointment_Btn_3.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.RescheduleAppointment_Btn_3.setObjectName("RescheduleAppointment_Btn_3")
        self.ViewBtns_Frame = QtWidgets.QFrame(self.MainFrame)
        self.ViewBtns_Frame.setGeometry(QtCore.QRect(380, 110, 641, 91))
        self.ViewBtns_Frame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: none;\n"
"}")
        self.ViewBtns_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ViewBtns_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ViewBtns_Frame.setObjectName("ViewBtns_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ViewBtns_Frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DisplayReschedule_Btn = QtWidgets.QPushButton(self.ViewBtns_Frame)
        self.DisplayReschedule_Btn.clicked.connect(displayReschedule)
        self.DisplayReschedule_Btn.setEnabled(True)
        self.DisplayReschedule_Btn.setMinimumSize(QtCore.QSize(170, 40))
        self.DisplayReschedule_Btn.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DisplayReschedule_Btn.setFont(font)
        self.DisplayReschedule_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DisplayReschedule_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.DisplayReschedule_Btn.setObjectName("DisplayReschedule_Btn")
        self.horizontalLayout.addWidget(self.DisplayReschedule_Btn)
        self.DisplaySchedule_Btn = QtWidgets.QPushButton(self.ViewBtns_Frame)
        self.DisplaySchedule_Btn.clicked.connect(displayScheduling)
        self.DisplaySchedule_Btn.setEnabled(False)
        self.DisplaySchedule_Btn.setMinimumSize(QtCore.QSize(200, 40))
        self.DisplaySchedule_Btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DisplaySchedule_Btn.setFont(font)
        self.DisplaySchedule_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DisplaySchedule_Btn.setStyleSheet("QPushButton {\n"
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
        self.DisplaySchedule_Btn.setObjectName("DisplaySchedule_Btn")
        self.horizontalLayout.addWidget(self.DisplaySchedule_Btn)
        self.DisplayCancel_Btn = QtWidgets.QPushButton(self.ViewBtns_Frame)
        self.DisplayCancel_Btn.clicked.connect(displayCancel)
        self.DisplayCancel_Btn.setEnabled(True)
        self.DisplayCancel_Btn.setMinimumSize(QtCore.QSize(100, 40))
        self.DisplayCancel_Btn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DisplayCancel_Btn.setFont(font)
        self.DisplayCancel_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DisplayCancel_Btn.setStyleSheet("QPushButton {\n"
"    border-image: none;\n"
"    background-color: #6ECCAF;\n"
"    color: black;\n"
"    border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(139, 231, 100);\n"
"    color: white;\n"
"}\n"
"\n"
"")
        self.DisplayCancel_Btn.setObjectName("DisplayCancel_Btn")
        self.horizontalLayout.addWidget(self.DisplayCancel_Btn)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.layoutWidget.raise_()
        self.InputsFrame.raise_()
        self.RescheduleAppointment_Frame.raise_()
        self.CancelAppointment_Frame.raise_()
        self.ViewBtns_Frame.raise_()
        SchedulingAppointmentsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SchedulingAppointmentsWindow)
        QtCore.QMetaObject.connectSlotsByName(SchedulingAppointmentsWindow)

    def retranslateUi(self, SchedulingAppointmentsWindow):
        _translate = QtCore.QCoreApplication.translate
        SchedulingAppointmentsWindow.setWindowTitle(_translate("SchedulingAppointmentsWindow", "Forsyth Family Practice Center - Scheduling Appointments"))
        self.Nav_LogoutBtn.setText(_translate("SchedulingAppointmentsWindow", "Logout"))
        self.Nav_Appointments.setText(_translate("SchedulingAppointmentsWindow", "Appointments"))
        self.Nav_CheckinBtn.setText(_translate("SchedulingAppointmentsWindow", "Check-in"))
        self.Nav_CheckoutBtn.setText(_translate("SchedulingAppointmentsWindow", "Check-out"))
        self.Nav_MakeReferralBtn.setText(_translate("SchedulingAppointmentsWindow", "Make Referral"))
        self.Nav_LabOrdersBtn.setText(_translate("SchedulingAppointmentsWindow", "Lab Orders"))
        self.Nav_ApproveAppointmentsBtn.setText(_translate("SchedulingAppointmentsWindow", "App. Approve via Portal"))
        self.HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Schedule Appointment"))
        self.UnderHeadingTextLabel.setText(_translate("SchedulingAppointmentsWindow", "This window is where you can input information related to scheduling and booking an appointment with a patient."))
        self.Label_PatientFirstName_2.setText(_translate("SchedulingAppointmentsWindow", "Patient First Name:"))
        self.LineEdit_PatientFirstName_2.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Enter First Name"))
        self.Label_PatientLastName_2.setText(_translate("SchedulingAppointmentsWindow", "Patient Last Name:"))
        self.LineEdit_PatientLastName_2.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Enter Last Name"))
        self.Label_DOB_2.setText(_translate("SchedulingAppointmentsWindow", "Patient\'s DOB:"))
        self.Label_AppointmentType.setText(_translate("SchedulingAppointmentsWindow", "Appointment Type:"))
        self.ComboBox_AppointmentType.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A TYPE --"))
        self.Label_AppointmentReason.setText(_translate("SchedulingAppointmentsWindow", "Appointment Reason:"))
        self.LineEdit_AppointmentReason.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Patient has the chills"))
        self.Label_AppointmentReason_2.setText(_translate("SchedulingAppointmentsWindow", "Meet Date/Time:"))
        self.LineEdit_MeetDateTime.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Select an available date and time on the right    ->"))
        self.CheckAvailableTimesBtn.setText(_translate("SchedulingAppointmentsWindow", "Check Available Times"))
        self.ScheduleAppointmentBtn.setText(_translate("SchedulingAppointmentsWindow", "Schedule Appointment"))
        self.ClearInputsBtn.setText(_translate("SchedulingAppointmentsWindow", "Clear Inputs"))
        self.CurrentAvailableTimes_Label.setText(_translate("SchedulingAppointmentsWindow", "Current Available Times"))
        self.CancelAppointment_HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Cancel Appointment"))
        self.UnderHeadingTextLabel_4.setText(_translate("SchedulingAppointmentsWindow", "To cancel an appointment, just click on one of the appointments you would like to cancel."))
        self.CurrentAppointments_Label_5.setText(_translate("SchedulingAppointmentsWindow", "Current Appointments"))
        self.CancelAppointment_Btn.setText(_translate("SchedulingAppointmentsWindow", "Cancel Appointment"))
        self.RescheduleAppointment_HeadingLabel_3.setText(_translate("SchedulingAppointmentsWindow", "Reschedule Appointment"))
        self.CurrentAppointments_Label_6.setText(_translate("SchedulingAppointmentsWindow", "Current Available Times"))
        self.UnderHeadingTextLabel_5.setText(_translate("SchedulingAppointmentsWindow", "To reschedule an appointment, click on one of your current appointments and a different available time that you would like to have."))
        self.CurrentAppointments_Label_7.setText(_translate("SchedulingAppointmentsWindow", "Current Appointments"))
        self.RescheduleAppointment_Btn_3.setText(_translate("SchedulingAppointmentsWindow", "Reschedule Appointment"))
        self.DisplayReschedule_Btn.setText(_translate("SchedulingAppointmentsWindow", "Rescheduling"))
        self.DisplaySchedule_Btn.setText(_translate("SchedulingAppointmentsWindow", "Make/Schedule"))
        self.DisplayCancel_Btn.setText(_translate("SchedulingAppointmentsWindow", "Cancel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SchedulingAppointmentsWindow = QtWidgets.QMainWindow()
    ui = Ui_SchedulingAppointmentsWindow()
    ui.setupUi(SchedulingAppointmentsWindow)
    SchedulingAppointmentsWindow.show()
    sys.exit(app.exec_())
