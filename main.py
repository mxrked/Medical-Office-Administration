from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
import sys
from frontend.StartWindow import UI

if __name__ == "__main__":

    app = QApplication(sys.argv)
    UIWindow = UI()

    app.exec_()
