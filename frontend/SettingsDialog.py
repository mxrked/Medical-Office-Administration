from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        uic.loadUi("frontend/ui/SettingsDialog.ui", self)

        # Functions

        # Widgets






def main():
    app = QApplication(sys.argv)
    UIWindow = SettingsDialog()
    UIWindow.show()
    app.exec()



if __name__ == "__main__":
    main()
