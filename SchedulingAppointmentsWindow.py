
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
                self.LineEdit_PatientFirstName_SA.setText("")
                self.LineEdit_PatientLastName_SA.setText("")
                self.LineEdit_AppointmentReason_SA.setText("")
                self.LineEdit_MeetDateTime_SA.setText("")

                defaultDate = QtCore.QDate(2000, 1, 1)
                self.dateEdit_DOB_SA.setDate(defaultDate)
                self.ComboBox_AppointmentType_SA.setCurrentIndex(0)
                self.ListWidget_MeetDateTimes_SA.clearSelection()

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

                # Getting connection
                params = urllib.parse.quote_plus(r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:capstone2023.database.windows.net,1433;DATABASE=capstone2023;Trusted_Connection=no;Uid=MOAuser;Pwd=Password01!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
                conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
                engine = sql.create_engine(conn_str)

                # Closing the connection
                engine.dispose()

                if engine.dispose:
                        print("Closed database. . .")

        def hideAllFrames():
                ' This is used to hide the different frames '

                self.InputsFrame.setFixedHeight(0)
                self.CancelAppointment_Frame.setFixedHeight(0)
                self.RescheduleAppointment_Frame.setFixedHeight(0)

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
                self.InputsFrame.setFixedHeight(681)
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

                self.RescheduleAppointment_Frame.setFixedHeight(681)
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

                self.CancelAppointment_Frame.setFixedHeight(681)
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
                print()
        def getPatientLN():
                ' This is used to get the patients last name in the DB '
                print()
        def getPatientDOB():
                ' This is used to get the patients DOB in the DB '
                print()
        def getOfficeLocation():
                ' This is used to get the Office Location in the DB '
                print()
        def getDoctorName():
                ' This is used to get the Doctor Name in the DB '
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
                print()
        def rescheduleAppointment():
                ' This is used to reschedule an appointment '
                print()
        def cancelAppointment():
                ' This is used to cancel an appointment '
                print()


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
        self.InputsFrame.setGeometry(QtCore.QRect(110, 200, 1171, 681))
        self.InputsFrame.setMinimumSize(QtCore.QSize(0, 681))
        self.InputsFrame.setMaximumSize(QtCore.QSize(16777215, 630))
        self.InputsFrame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.InputsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InputsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputsFrame.setObjectName("InputsFrame")
        self.ScheduleAppointment_HeadingLabel = QtWidgets.QLabel(self.InputsFrame)
        self.ScheduleAppointment_HeadingLabel.setGeometry(QtCore.QRect(0, 0, 1181, 150))
        self.ScheduleAppointment_HeadingLabel.setMinimumSize(QtCore.QSize(0, 150))
        self.ScheduleAppointment_HeadingLabel.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ScheduleAppointment_HeadingLabel.setFont(font)
        self.ScheduleAppointment_HeadingLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.ScheduleAppointment_HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ScheduleAppointment_HeadingLabel.setObjectName("ScheduleAppointment_HeadingLabel")
        self.UnderHeadingTextLabel_SA = QtWidgets.QLabel(self.InputsFrame)
        self.UnderHeadingTextLabel_SA.setGeometry(QtCore.QRect(0, 110, 1181, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_SA.setFont(font)
        self.UnderHeadingTextLabel_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_SA.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_SA.setObjectName("UnderHeadingTextLabel_SA")
        self.InputsInnerFrame = QtWidgets.QFrame(self.InputsFrame)
        self.InputsInnerFrame.setGeometry(QtCore.QRect(100, 190, 591, 371))
        self.InputsInnerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InputsInnerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputsInnerFrame.setObjectName("InputsInnerFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.InputsInnerFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.InputsInnerVLayout = QtWidgets.QVBoxLayout()
        self.InputsInnerVLayout.setObjectName("InputsInnerVLayout")
        self.InputsRowHLayout_1 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_1.setObjectName("InputsRowHLayout_1")
        self.Label_PatientFirstName_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        self.Label_PatientFirstName_SA.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_PatientFirstName_SA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_PatientFirstName_SA.setFont(font)
        self.Label_PatientFirstName_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_PatientFirstName_SA.setObjectName("Label_PatientFirstName_SA")
        self.InputsRowHLayout_1.addWidget(self.Label_PatientFirstName_SA)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_1.addItem(spacerItem)
        self.LineEdit_PatientFirstName_SA = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_PatientFirstName_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.LineEdit_PatientFirstName_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_PatientFirstName_SA.setFont(font)
        self.LineEdit_PatientFirstName_SA.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_PatientFirstName_SA.setText("")
        self.LineEdit_PatientFirstName_SA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LineEdit_PatientFirstName_SA.setObjectName("LineEdit_PatientFirstName_SA")
        self.InputsRowHLayout_1.addWidget(self.LineEdit_PatientFirstName_SA)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem1)
        self.InputsRowHLayout_2 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_2.setObjectName("InputsRowHLayout_2")
        self.Layout_PatientLastName_2 = QtWidgets.QHBoxLayout()
        self.Layout_PatientLastName_2.setObjectName("Layout_PatientLastName_2")
        self.Label_PatientLastName_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_PatientLastName_SA.setFont(font)
        self.Label_PatientLastName_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_PatientLastName_SA.setObjectName("Label_PatientLastName_SA")
        self.Layout_PatientLastName_2.addWidget(self.Label_PatientLastName_SA)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_PatientLastName_2.addItem(spacerItem2)
        self.LineEdit_PatientLastName_SA = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_PatientLastName_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.LineEdit_PatientLastName_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_PatientLastName_SA.setFont(font)
        self.LineEdit_PatientLastName_SA.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_PatientLastName_SA.setText("")
        self.LineEdit_PatientLastName_SA.setObjectName("LineEdit_PatientLastName_SA")
        self.Layout_PatientLastName_2.addWidget(self.LineEdit_PatientLastName_SA)
        self.InputsRowHLayout_2.addLayout(self.Layout_PatientLastName_2)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem3)
        self.InputsRowHLayout_3 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_3.setObjectName("InputsRowHLayout_3")
        self.Layout_DOB_2 = QtWidgets.QHBoxLayout()
        self.Layout_DOB_2.setObjectName("Layout_DOB_2")
        self.Label_DOB_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_DOB_SA.setFont(font)
        self.Label_DOB_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_DOB_SA.setObjectName("Label_DOB_SA")
        self.Layout_DOB_2.addWidget(self.Label_DOB_SA)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Layout_DOB_2.addItem(spacerItem4)
        self.dateEdit_DOB_SA = QtWidgets.QDateEdit(self.InputsInnerFrame)
        self.dateEdit_DOB_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.dateEdit_DOB_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.dateEdit_DOB_SA.setFont(font)
        self.dateEdit_DOB_SA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_DOB_SA.setStyleSheet("QDateEdit {\n"
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
        self.dateEdit_DOB_SA.setCalendarPopup(False)
        self.dateEdit_DOB_SA.setObjectName("dateEdit_DOB_SA")
        self.Layout_DOB_2.addWidget(self.dateEdit_DOB_SA)
        self.InputsRowHLayout_3.addLayout(self.Layout_DOB_2)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem5)
        self.InputsRowHLayout_10 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_10.setObjectName("InputsRowHLayout_10")
        self.Label_OfficeLocation_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        self.Label_OfficeLocation_SA.setMinimumSize(QtCore.QSize(140, 0))
        self.Label_OfficeLocation_SA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_OfficeLocation_SA.setFont(font)
        self.Label_OfficeLocation_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_OfficeLocation_SA.setObjectName("Label_OfficeLocation_SA")
        self.InputsRowHLayout_10.addWidget(self.Label_OfficeLocation_SA)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_10.addItem(spacerItem6)
        self.ComboBox_OfficeLocations_SA = QtWidgets.QComboBox(self.InputsInnerFrame)
        self.ComboBox_OfficeLocations_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.ComboBox_OfficeLocations_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_OfficeLocations_SA.setFont(font)
        self.ComboBox_OfficeLocations_SA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboBox_OfficeLocations_SA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_OfficeLocations_SA.setObjectName("ComboBox_OfficeLocations_SA")
        self.ComboBox_OfficeLocations_SA.addItem("")
        self.InputsRowHLayout_10.addWidget(self.ComboBox_OfficeLocations_SA)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_10)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem7)
        self.InputsRowHLayout_6 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_6.setObjectName("InputsRowHLayout_6")
        self.Label_DoctorName_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        self.Label_DoctorName_SA.setMinimumSize(QtCore.QSize(140, 0))
        self.Label_DoctorName_SA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_DoctorName_SA.setFont(font)
        self.Label_DoctorName_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_DoctorName_SA.setObjectName("Label_DoctorName_SA")
        self.InputsRowHLayout_6.addWidget(self.Label_DoctorName_SA)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_6.addItem(spacerItem8)
        self.ComboBox_DoctorNames_SA = QtWidgets.QComboBox(self.InputsInnerFrame)
        self.ComboBox_DoctorNames_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.ComboBox_DoctorNames_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_DoctorNames_SA.setFont(font)
        self.ComboBox_DoctorNames_SA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboBox_DoctorNames_SA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_DoctorNames_SA.setObjectName("ComboBox_DoctorNames_SA")
        self.ComboBox_DoctorNames_SA.addItem("")
        self.InputsRowHLayout_6.addWidget(self.ComboBox_DoctorNames_SA)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem9)
        self.InputsRowHLayout_4 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_4.setObjectName("InputsRowHLayout_4")
        self.Label_AppointmentReason_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_AppointmentReason_SA.setFont(font)
        self.Label_AppointmentReason_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_AppointmentReason_SA.setObjectName("Label_AppointmentReason_SA")
        self.InputsRowHLayout_4.addWidget(self.Label_AppointmentReason_SA)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_4.addItem(spacerItem10)
        self.LineEdit_AppointmentReason_SA = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_AppointmentReason_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.LineEdit_AppointmentReason_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_AppointmentReason_SA.setFont(font)
        self.LineEdit_AppointmentReason_SA.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_AppointmentReason_SA.setObjectName("LineEdit_AppointmentReason_SA")
        self.InputsRowHLayout_4.addWidget(self.LineEdit_AppointmentReason_SA)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_4)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem11)
        self.InputsRowHLayout_9 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_9.setObjectName("InputsRowHLayout_9")
        self.Label_AppointmentType_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        self.Label_AppointmentType_SA.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_AppointmentType_SA.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_AppointmentType_SA.setFont(font)
        self.Label_AppointmentType_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_AppointmentType_SA.setObjectName("Label_AppointmentType_SA")
        self.InputsRowHLayout_9.addWidget(self.Label_AppointmentType_SA)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_9.addItem(spacerItem12)
        self.ComboBox_AppointmentType_SA = QtWidgets.QComboBox(self.InputsInnerFrame)
        self.ComboBox_AppointmentType_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.ComboBox_AppointmentType_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_AppointmentType_SA.setFont(font)
        self.ComboBox_AppointmentType_SA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ComboBox_AppointmentType_SA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_AppointmentType_SA.setObjectName("ComboBox_AppointmentType_SA")
        self.ComboBox_AppointmentType_SA.addItem("")
        self.InputsRowHLayout_9.addWidget(self.ComboBox_AppointmentType_SA)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_9)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.InputsInnerVLayout.addItem(spacerItem13)
        self.InputsRowHLayout_5 = QtWidgets.QHBoxLayout()
        self.InputsRowHLayout_5.setObjectName("InputsRowHLayout_5")
        self.Label_MeetDateTime_SA = QtWidgets.QLabel(self.InputsInnerFrame)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_MeetDateTime_SA.setFont(font)
        self.Label_MeetDateTime_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_MeetDateTime_SA.setObjectName("Label_MeetDateTime_SA")
        self.InputsRowHLayout_5.addWidget(self.Label_MeetDateTime_SA)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputsRowHLayout_5.addItem(spacerItem14)
        self.LineEdit_MeetDateTime_SA = QtWidgets.QLineEdit(self.InputsInnerFrame)
        self.LineEdit_MeetDateTime_SA.setEnabled(False)
        self.LineEdit_MeetDateTime_SA.setMinimumSize(QtCore.QSize(350, 30))
        self.LineEdit_MeetDateTime_SA.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.LineEdit_MeetDateTime_SA.setFont(font)
        self.LineEdit_MeetDateTime_SA.setStyleSheet("QLineEdit {\n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}")
        self.LineEdit_MeetDateTime_SA.setText("")
        self.LineEdit_MeetDateTime_SA.setObjectName("LineEdit_MeetDateTime_SA")
        self.InputsRowHLayout_5.addWidget(self.LineEdit_MeetDateTime_SA)
        self.InputsInnerVLayout.addLayout(self.InputsRowHLayout_5)
        self.verticalLayout_3.addLayout(self.InputsInnerVLayout)
        self.TimesHolderFrame_SA = QtWidgets.QFrame(self.InputsFrame)
        self.TimesHolderFrame_SA.setGeometry(QtCore.QRect(730, 200, 341, 351))
        self.TimesHolderFrame_SA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimesHolderFrame_SA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimesHolderFrame_SA.setObjectName("TimesHolderFrame_SA")
        self.ListWidget_MeetDateTimes_SA = QtWidgets.QListWidget(self.TimesHolderFrame_SA)
        self.ListWidget_MeetDateTimes_SA.setGeometry(QtCore.QRect(0, 40, 341, 311))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_MeetDateTimes_SA.setFont(font)
        self.ListWidget_MeetDateTimes_SA.setStyleSheet("QListWidget {\n"
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
        self.ListWidget_MeetDateTimes_SA.setObjectName("ListWidget_MeetDateTimes_SA")
        self.CurrentAvailableTimes_Label_SA = QtWidgets.QLabel(self.TimesHolderFrame_SA)
        self.CurrentAvailableTimes_Label_SA.setGeometry(QtCore.QRect(0, -10, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAvailableTimes_Label_SA.setFont(font)
        self.CurrentAvailableTimes_Label_SA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAvailableTimes_Label_SA.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAvailableTimes_Label_SA.setObjectName("CurrentAvailableTimes_Label_SA")
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
        self.ViewBtns_Frame = QtWidgets.QFrame(self.MainFrame)
        self.ViewBtns_Frame.setGeometry(QtCore.QRect(420, 110, 541, 91))
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
        self.CancelAppointment_Frame = QtWidgets.QFrame(self.MainFrame)
        self.CancelAppointment_Frame.setGeometry(QtCore.QRect(110, 200, 1171, 0))
        self.CancelAppointment_Frame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.CancelAppointment_Frame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.CancelAppointment_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CancelAppointment_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CancelAppointment_Frame.setObjectName("CancelAppointment_Frame")
        self.CancelAppointment_HeadingLabel = QtWidgets.QLabel(self.CancelAppointment_Frame)
        self.CancelAppointment_HeadingLabel.setGeometry(QtCore.QRect(0, 10, 1181, 121))
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
        self.UnderHeadingTextLabel_CA = QtWidgets.QLabel(self.CancelAppointment_Frame)
        self.UnderHeadingTextLabel_CA.setGeometry(QtCore.QRect(0, 100, 1181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_CA.setFont(font)
        self.UnderHeadingTextLabel_CA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_CA.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_CA.setWordWrap(True)
        self.UnderHeadingTextLabel_CA.setObjectName("UnderHeadingTextLabel_CA")
        self.Frame_SelectDoctor_CA = QtWidgets.QFrame(self.CancelAppointment_Frame)
        self.Frame_SelectDoctor_CA.setGeometry(QtCore.QRect(100, 320, 441, 61))
        self.Frame_SelectDoctor_CA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_SelectDoctor_CA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_SelectDoctor_CA.setObjectName("Frame_SelectDoctor_CA")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.Frame_SelectDoctor_CA)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.Label_SelectDoctor_CA = QtWidgets.QLabel(self.Frame_SelectDoctor_CA)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_SelectDoctor_CA.setFont(font)
        self.Label_SelectDoctor_CA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_SelectDoctor_CA.setObjectName("Label_SelectDoctor_CA")
        self.horizontalLayout_20.addWidget(self.Label_SelectDoctor_CA)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem15)
        self.ComboBox_DoctorNames_CA = QtWidgets.QComboBox(self.Frame_SelectDoctor_CA)
        self.ComboBox_DoctorNames_CA.setMinimumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_DoctorNames_CA.setFont(font)
        self.ComboBox_DoctorNames_CA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_DoctorNames_CA.setObjectName("ComboBox_DoctorNames_CA")
        self.ComboBox_DoctorNames_CA.addItem("")
        self.horizontalLayout_20.addWidget(self.ComboBox_DoctorNames_CA)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        self.Frame_SelectDoctor_CA_2 = QtWidgets.QFrame(self.CancelAppointment_Frame)
        self.Frame_SelectDoctor_CA_2.setGeometry(QtCore.QRect(100, 260, 441, 61))
        self.Frame_SelectDoctor_CA_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_SelectDoctor_CA_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_SelectDoctor_CA_2.setObjectName("Frame_SelectDoctor_CA_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.Frame_SelectDoctor_CA_2)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.Label_OfficeLocation_CA = QtWidgets.QLabel(self.Frame_SelectDoctor_CA_2)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_OfficeLocation_CA.setFont(font)
        self.Label_OfficeLocation_CA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_OfficeLocation_CA.setObjectName("Label_OfficeLocation_CA")
        self.horizontalLayout_22.addWidget(self.Label_OfficeLocation_CA)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem16)
        self.ComboBox_OfficeLocations_CA = QtWidgets.QComboBox(self.Frame_SelectDoctor_CA_2)
        self.ComboBox_OfficeLocations_CA.setMinimumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_OfficeLocations_CA.setFont(font)
        self.ComboBox_OfficeLocations_CA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_OfficeLocations_CA.setObjectName("ComboBox_OfficeLocations_CA")
        self.ComboBox_OfficeLocations_CA.addItem("")
        self.horizontalLayout_22.addWidget(self.ComboBox_OfficeLocations_CA)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)
        self.CurrentAppointments_Frame_CA = QtWidgets.QFrame(self.CancelAppointment_Frame)
        self.CurrentAppointments_Frame_CA.setGeometry(QtCore.QRect(660, 220, 391, 361))
        self.CurrentAppointments_Frame_CA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CurrentAppointments_Frame_CA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CurrentAppointments_Frame_CA.setObjectName("CurrentAppointments_Frame_CA")
        self.ListWidget_CurrentAppointments_CA = QtWidgets.QListWidget(self.CurrentAppointments_Frame_CA)
        self.ListWidget_CurrentAppointments_CA.setGeometry(QtCore.QRect(0, 50, 391, 311))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_CurrentAppointments_CA.setFont(font)
        self.ListWidget_CurrentAppointments_CA.setStyleSheet("QListWidget {\n"
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
        self.ListWidget_CurrentAppointments_CA.setObjectName("ListWidget_CurrentAppointments_CA")
        self.CurrentAppointments_Label_CA = QtWidgets.QLabel(self.CurrentAppointments_Frame_CA)
        self.CurrentAppointments_Label_CA.setGeometry(QtCore.QRect(0, -10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAppointments_Label_CA.setFont(font)
        self.CurrentAppointments_Label_CA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAppointments_Label_CA.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAppointments_Label_CA.setObjectName("CurrentAppointments_Label_CA")
        self.CancelAppointment_Btn = QtWidgets.QPushButton(self.CancelAppointment_Frame)
        self.CancelAppointment_Btn.setEnabled(True)
        self.CancelAppointment_Btn.setGeometry(QtCore.QRect(100, 450, 181, 51))
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
        self.UnderHeadingTextLabel_CA_2 = QtWidgets.QLabel(self.CancelAppointment_Frame)
        self.UnderHeadingTextLabel_CA_2.setGeometry(QtCore.QRect(100, 390, 481, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_CA_2.setFont(font)
        self.UnderHeadingTextLabel_CA_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_CA_2.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_CA_2.setWordWrap(True)
        self.UnderHeadingTextLabel_CA_2.setObjectName("UnderHeadingTextLabel_CA_2")
        self.RescheduleAppointment_Frame = QtWidgets.QFrame(self.MainFrame)
        self.RescheduleAppointment_Frame.setGeometry(QtCore.QRect(110, 200, 1171, 0))
        self.RescheduleAppointment_Frame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.RescheduleAppointment_Frame.setStyleSheet("QFrame {\n"
"    border-image: none;\n"
"    background-color: rgb(52, 77, 103);\n"
"}")
        self.RescheduleAppointment_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RescheduleAppointment_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RescheduleAppointment_Frame.setObjectName("RescheduleAppointment_Frame")
        self.RescheduleAppointment_HeadingLabel = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.RescheduleAppointment_HeadingLabel.setGeometry(QtCore.QRect(0, 10, 1181, 121))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.RescheduleAppointment_HeadingLabel.setFont(font)
        self.RescheduleAppointment_HeadingLabel.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.RescheduleAppointment_HeadingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RescheduleAppointment_HeadingLabel.setObjectName("RescheduleAppointment_HeadingLabel")
        self.UnderHeadingTextLabel_RA_2 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.UnderHeadingTextLabel_RA_2.setGeometry(QtCore.QRect(0, 100, 1181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_RA_2.setFont(font)
        self.UnderHeadingTextLabel_RA_2.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_RA_2.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_RA_2.setWordWrap(True)
        self.UnderHeadingTextLabel_RA_2.setObjectName("UnderHeadingTextLabel_RA_2")
        self.Frame_SelectDoctor_RA = QtWidgets.QFrame(self.RescheduleAppointment_Frame)
        self.Frame_SelectDoctor_RA.setGeometry(QtCore.QRect(160, 320, 471, 61))
        self.Frame_SelectDoctor_RA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_SelectDoctor_RA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_SelectDoctor_RA.setObjectName("Frame_SelectDoctor_RA")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.Frame_SelectDoctor_RA)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.Label_SelectDoctor_RA = QtWidgets.QLabel(self.Frame_SelectDoctor_RA)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_SelectDoctor_RA.setFont(font)
        self.Label_SelectDoctor_RA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_SelectDoctor_RA.setObjectName("Label_SelectDoctor_RA")
        self.horizontalLayout_24.addWidget(self.Label_SelectDoctor_RA)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem17)
        self.ComboBox_DoctorNames_RA = QtWidgets.QComboBox(self.Frame_SelectDoctor_RA)
        self.ComboBox_DoctorNames_RA.setMinimumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_DoctorNames_RA.setFont(font)
        self.ComboBox_DoctorNames_RA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_DoctorNames_RA.setObjectName("ComboBox_DoctorNames_RA")
        self.ComboBox_DoctorNames_RA.addItem("")
        self.horizontalLayout_24.addWidget(self.ComboBox_DoctorNames_RA)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_24)
        self.Frame_SelectOfficeLocation_RA = QtWidgets.QFrame(self.RescheduleAppointment_Frame)
        self.Frame_SelectOfficeLocation_RA.setGeometry(QtCore.QRect(160, 260, 471, 61))
        self.Frame_SelectOfficeLocation_RA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_SelectOfficeLocation_RA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_SelectOfficeLocation_RA.setObjectName("Frame_SelectOfficeLocation_RA")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.Frame_SelectOfficeLocation_RA)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.Label_OfficeLocation_RA = QtWidgets.QLabel(self.Frame_SelectOfficeLocation_RA)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_OfficeLocation_RA.setFont(font)
        self.Label_OfficeLocation_RA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.Label_OfficeLocation_RA.setObjectName("Label_OfficeLocation_RA")
        self.horizontalLayout_26.addWidget(self.Label_OfficeLocation_RA)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem18)
        self.ComboBox_OfficeLocations_RA = QtWidgets.QComboBox(self.Frame_SelectOfficeLocation_RA)
        self.ComboBox_OfficeLocations_RA.setMinimumSize(QtCore.QSize(280, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.ComboBox_OfficeLocations_RA.setFont(font)
        self.ComboBox_OfficeLocations_RA.setStyleSheet("QComboBox {    \n"
"    border-image: none;\n"
"    border: none;\n"
"    background-color: #F3ECB0;\n"
"    color: #344D67;\n"
"    font-family: \"MS Shell Dlg 2\";\n"
"    font-size: 11;\n"
"}")
        self.ComboBox_OfficeLocations_RA.setObjectName("ComboBox_OfficeLocations_RA")
        self.ComboBox_OfficeLocations_RA.addItem("")
        self.horizontalLayout_26.addWidget(self.ComboBox_OfficeLocations_RA)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.UnderHeadingTextLabel_RA_1 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.UnderHeadingTextLabel_RA_1.setGeometry(QtCore.QRect(160, 390, 431, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_RA_1.setFont(font)
        self.UnderHeadingTextLabel_RA_1.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_RA_1.setAlignment(QtCore.Qt.AlignCenter)
        self.UnderHeadingTextLabel_RA_1.setWordWrap(True)
        self.UnderHeadingTextLabel_RA_1.setObjectName("UnderHeadingTextLabel_RA_1")
        self.UnderHeadingTextLabel_RA_3 = QtWidgets.QLabel(self.RescheduleAppointment_Frame)
        self.UnderHeadingTextLabel_RA_3.setGeometry(QtCore.QRect(170, 430, 421, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.UnderHeadingTextLabel_RA_3.setFont(font)
        self.UnderHeadingTextLabel_RA_3.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.UnderHeadingTextLabel_RA_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UnderHeadingTextLabel_RA_3.setWordWrap(True)
        self.UnderHeadingTextLabel_RA_3.setObjectName("UnderHeadingTextLabel_RA_3")
        self.RescheduleAppointment_Btn = QtWidgets.QPushButton(self.RescheduleAppointment_Frame)
        self.RescheduleAppointment_Btn.setGeometry(QtCore.QRect(170, 500, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.RescheduleAppointment_Btn.setFont(font)
        self.RescheduleAppointment_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RescheduleAppointment_Btn.setStyleSheet("QPushButton {\n"
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
        self.RescheduleAppointment_Btn.setObjectName("RescheduleAppointment_Btn")
        self.CurrentAppointments_Frame_RA = QtWidgets.QFrame(self.RescheduleAppointment_Frame)
        self.CurrentAppointments_Frame_RA.setGeometry(QtCore.QRect(720, 190, 331, 201))
        self.CurrentAppointments_Frame_RA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CurrentAppointments_Frame_RA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CurrentAppointments_Frame_RA.setObjectName("CurrentAppointments_Frame_RA")
        self.ListWidget_CurrentAppointments_RA = QtWidgets.QListWidget(self.CurrentAppointments_Frame_RA)
        self.ListWidget_CurrentAppointments_RA.setGeometry(QtCore.QRect(0, 40, 331, 161))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_CurrentAppointments_RA.setFont(font)
        self.ListWidget_CurrentAppointments_RA.setStyleSheet("QListWidget {\n"
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
        self.ListWidget_CurrentAppointments_RA.setObjectName("ListWidget_CurrentAppointments_RA")
        self.CurrentAppointments_Label_RA = QtWidgets.QLabel(self.CurrentAppointments_Frame_RA)
        self.CurrentAppointments_Label_RA.setGeometry(QtCore.QRect(0, 0, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAppointments_Label_RA.setFont(font)
        self.CurrentAppointments_Label_RA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAppointments_Label_RA.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAppointments_Label_RA.setObjectName("CurrentAppointments_Label_RA")
        self.TimesHolderFrame_RA = QtWidgets.QFrame(self.RescheduleAppointment_Frame)
        self.TimesHolderFrame_RA.setGeometry(QtCore.QRect(720, 420, 331, 191))
        self.TimesHolderFrame_RA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimesHolderFrame_RA.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimesHolderFrame_RA.setObjectName("TimesHolderFrame_RA")
        self.ListWidget_MeetDateTimes_RA = QtWidgets.QListWidget(self.TimesHolderFrame_RA)
        self.ListWidget_MeetDateTimes_RA.setGeometry(QtCore.QRect(0, 30, 331, 161))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.ListWidget_MeetDateTimes_RA.setFont(font)
        self.ListWidget_MeetDateTimes_RA.setStyleSheet("QListWidget {\n"
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
        self.ListWidget_MeetDateTimes_RA.setObjectName("ListWidget_MeetDateTimes_RA")
        self.CurrentAvailableTimes_Label_RA = QtWidgets.QLabel(self.TimesHolderFrame_RA)
        self.CurrentAvailableTimes_Label_RA.setGeometry(QtCore.QRect(0, -10, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        self.CurrentAvailableTimes_Label_RA.setFont(font)
        self.CurrentAvailableTimes_Label_RA.setStyleSheet("QLabel {\n"
"    color: white;\n"
"}")
        self.CurrentAvailableTimes_Label_RA.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentAvailableTimes_Label_RA.setObjectName("CurrentAvailableTimes_Label_RA")
        self.layoutWidget.raise_()
        self.ViewBtns_Frame.raise_()
        self.InputsFrame.raise_()
        self.CancelAppointment_Frame.raise_()
        self.RescheduleAppointment_Frame.raise_()
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
        self.ScheduleAppointment_HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Schedule Appointment"))
        self.UnderHeadingTextLabel_SA.setText(_translate("SchedulingAppointmentsWindow", "This window is where you can input information related to scheduling and booking an appointment with a patient."))
        self.Label_PatientFirstName_SA.setText(_translate("SchedulingAppointmentsWindow", "Patient First Name:"))
        self.LineEdit_PatientFirstName_SA.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Enter First Name"))
        self.Label_PatientLastName_SA.setText(_translate("SchedulingAppointmentsWindow", "Patient Last Name:"))
        self.LineEdit_PatientLastName_SA.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Enter Last Name"))
        self.Label_DOB_SA.setText(_translate("SchedulingAppointmentsWindow", "Patient\'s DOB:"))
        self.Label_OfficeLocation_SA.setText(_translate("SchedulingAppointmentsWindow", "Office Location:"))
        self.ComboBox_OfficeLocations_SA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A LOCATION --"))
        self.Label_DoctorName_SA.setText(_translate("SchedulingAppointmentsWindow", "Doctor Name:"))
        self.ComboBox_DoctorNames_SA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A DOCTOR --"))
        self.Label_AppointmentReason_SA.setText(_translate("SchedulingAppointmentsWindow", "Appointment Reason:"))
        self.LineEdit_AppointmentReason_SA.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Patient has the chills"))
        self.Label_AppointmentType_SA.setText(_translate("SchedulingAppointmentsWindow", "Appointment Type:"))
        self.ComboBox_AppointmentType_SA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A TYPE --"))
        self.Label_MeetDateTime_SA.setText(_translate("SchedulingAppointmentsWindow", "Meet Date/Time:"))
        self.LineEdit_MeetDateTime_SA.setPlaceholderText(_translate("SchedulingAppointmentsWindow", "Select an available date and time on the right    ->"))
        self.CurrentAvailableTimes_Label_SA.setText(_translate("SchedulingAppointmentsWindow", "Current Available Times"))
        self.ScheduleAppointmentBtn.setText(_translate("SchedulingAppointmentsWindow", "Schedule Appointment"))
        self.ClearInputsBtn.setText(_translate("SchedulingAppointmentsWindow", "Clear Inputs"))
        self.DisplayReschedule_Btn.setText(_translate("SchedulingAppointmentsWindow", "Rescheduling"))
        self.DisplaySchedule_Btn.setText(_translate("SchedulingAppointmentsWindow", "Make/Schedule"))
        self.DisplayCancel_Btn.setText(_translate("SchedulingAppointmentsWindow", "Cancel"))
        self.CancelAppointment_HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Cancel Appointment"))
        self.UnderHeadingTextLabel_CA.setText(_translate("SchedulingAppointmentsWindow", "To cancel an appointment, just click on one of the appointments you would like to cancel."))
        self.Label_SelectDoctor_CA.setText(_translate("SchedulingAppointmentsWindow", "Doctor Name:"))
        self.ComboBox_DoctorNames_CA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A DOCTOR --"))
        self.Label_OfficeLocation_CA.setText(_translate("SchedulingAppointmentsWindow", "Office Location:"))
        self.ComboBox_OfficeLocations_CA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A LOCATION --"))
        self.CurrentAppointments_Label_CA.setText(_translate("SchedulingAppointmentsWindow", "Current Appointments"))
        self.CancelAppointment_Btn.setText(_translate("SchedulingAppointmentsWindow", "Cancel Appointment"))
        self.UnderHeadingTextLabel_CA_2.setText(_translate("SchedulingAppointmentsWindow", "Click on an appointment on the right that you would like to cancel."))
        self.RescheduleAppointment_HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Reschedule Appointment"))
        self.UnderHeadingTextLabel_RA_2.setText(_translate("SchedulingAppointmentsWindow", "To reschedule an appointment, click on one of your current appointments and a different available time that you would like to have."))
        self.Label_SelectDoctor_RA.setText(_translate("SchedulingAppointmentsWindow", "Doctor Name:"))
        self.ComboBox_DoctorNames_RA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A DOCTOR --"))
        self.Label_OfficeLocation_RA.setText(_translate("SchedulingAppointmentsWindow", "Office Location:"))
        self.ComboBox_OfficeLocations_RA.setItemText(0, _translate("SchedulingAppointmentsWindow", "-- SELECT A LOCATION --"))
        self.UnderHeadingTextLabel_RA_1.setText(_translate("SchedulingAppointmentsWindow", "Click on an appointment you want to change on the right."))
        self.UnderHeadingTextLabel_RA_3.setText(_translate("SchedulingAppointmentsWindow", "Click on an time you want to reschedule the appointment to on the right."))
        self.RescheduleAppointment_Btn.setText(_translate("SchedulingAppointmentsWindow", "Reschedule Appointment"))
        self.CurrentAppointments_Label_RA.setText(_translate("SchedulingAppointmentsWindow", "Current Appointments"))
        self.CurrentAvailableTimes_Label_RA.setText(_translate("SchedulingAppointmentsWindow", "Current Available Times"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SchedulingAppointmentsWindow = QtWidgets.QMainWindow()
    ui = Ui_SchedulingAppointmentsWindow()
    ui.setupUi(SchedulingAppointmentsWindow)
    SchedulingAppointmentsWindow.show()
    sys.exit(app.exec_())