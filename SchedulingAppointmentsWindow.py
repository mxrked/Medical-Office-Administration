

from PyQt5 import QtCore, QtGui, QtWidgets
from assets.qrc import app_bg
from assets.files.GLOBALS import *


class Ui_SchedulingAppointmentsWindow(object):
    def setupUi(self, SchedulingAppointmentsWindow):

        ''' FUNCTIONS '''
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

        def getPatientFN():
                ' This is used to get the patients first name in the DB '
                print()
        def getPatientLN():
                ' This is used to get the patients last name in the DB '
                print()
        def getPatientDOB():
                ' This is used to get the patients DOB in the DB '
                print()

        def connectToDB():
                ' This is used to connect to the database '
                print()

        def checkAvailableTimes():
                ' This is used to display/filter the possible available times '

        def scheduleAppointment():
                print()

        SchedulingAppointmentsWindow.setObjectName("SchedulingAppointmentsWindow")
        SchedulingAppointmentsWindow.resize(1400, 900)
        SchedulingAppointmentsWindow.setMinimumSize(QtCore.QSize(1400, 900))
        SchedulingAppointmentsWindow.setMaximumSize(QtCore.QSize(1400, 900))
        self.centralwidget = QtWidgets.QWidget(SchedulingAppointmentsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(0, -1, 1411, 901))
        self.MainFrame.setStyleSheet("QFrame {\n"
"    border-image: url(:/newPrefix/imgs/app-bg.png);\n"
"}")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.layoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 40, 1181, 42))
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
        self.InputsFrame.setGeometry(QtCore.QRect(110, 130, 1181, 721))
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
        font.setFamily("Lato")
        font.setPointSize(14)
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
        self.CheckAvailableTimesBtn.setGeometry(QtCore.QRect(810, 580, 181, 51))
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
        self.ScheduleAppointmentBtn.clicked.connect(scheduleAppointment)
        self.ScheduleAppointmentBtn.setEnabled(True)
        self.ScheduleAppointmentBtn.setGeometry(QtCore.QRect(110, 580, 181, 51))
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
        self.ClearInputsBtn.setGeometry(QtCore.QRect(310, 580, 111, 51))
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
        self.HeadingLabel.setText(_translate("SchedulingAppointmentsWindow", "Scheduling Appointments Window"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SchedulingAppointmentsWindow = QtWidgets.QMainWindow()
    ui = Ui_SchedulingAppointmentsWindow()
    ui.setupUi(SchedulingAppointmentsWindow)
    SchedulingAppointmentsWindow.show()
    sys.exit(app.exec_())
