import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication
from frontend.approve_appt import Approve
class MainWindow(Approve):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)






#initializing app
app = QApplication(sys.argv)
UIWindow = MainWindow()
if __name__ == "__main__":
    UIWindow.show()
    app.exec_()
 