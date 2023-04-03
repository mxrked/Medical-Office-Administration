from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg
from frontend.ui.assets.files.GLOBALS import *
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

import urllib
import sqlalchemy
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("ui/checkin.ui", self)

        # Functions


        # Define widgets


        # Do something (Use functions for buttons and stuff)


        # Hide the app
        self.hide()

    # This will make it so when the user clicks the red x, it closes all windows
    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()
        app.exit()


#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
# app.exec()
