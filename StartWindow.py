


from PyQt5 import QtCore, QtGui, QtWidgets
from assets.qrc import app_bg

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(900, 900)
        StartWindow.setMinimumSize(QtCore.QSize(900, 900))
        StartWindow.setMaximumSize(QtCore.QSize(900, 900))
        StartWindow.setStyleSheet("border-image: url(:/newPrefix/imgs/app-bg.png);")
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startWindow_Heading1 = QtWidgets.QLabel(self.centralwidget)
        self.startWindow_Heading1.setGeometry(QtCore.QRect(0, 120, 901, 181))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(48)
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
        self.startWindow_Heading2.setGeometry(QtCore.QRect(0, 220, 901, 121))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(48)
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
        self.startWindow_SubHeading.setGeometry(QtCore.QRect(0, 340, 901, 41))
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
        self.startWindow_UsernameLineEdit.setGeometry(QtCore.QRect(290, 460, 321, 51))
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
        self.startWindow_PasswordLineEdit.setGeometry(QtCore.QRect(290, 540, 321, 51))
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
        self.startWindow_PasswordLineEdit.setObjectName("startWindow_PasswordLineEdit")
        self.startWindow_LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startWindow_LoginBtn.setGeometry(QtCore.QRect(360, 650, 81, 51))
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
        self.startWindow_ExitBtn.setGeometry(QtCore.QRect(460, 650, 71, 51))
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
        self.startWindow_InvalidUsernameLabel.setGeometry(QtCore.QRect(290, 430, 321, 0))
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
        self.startWindow_InvalidPasswordLabel.setGeometry(QtCore.QRect(290, 530, 321, 0))
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
        self.startWindow_InfoBtn.setGeometry(QtCore.QRect(420, 840, 51, 51))
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
