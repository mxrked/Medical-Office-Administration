from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from frontend.ui.assets.qrc import app_bg

from frontend.abstract_main_window import AMainWindow
import sys

class UI(AMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("frontend/ui/LabOrdersWindow.ui", self)

        self.load_nav()

#initializing app
app = QApplication(sys.argv)
UIWindow = UI()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
