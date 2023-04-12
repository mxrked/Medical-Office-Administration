import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from frontend.main_nav import Nav
from frontend.lab_orders import Lab_Orders_Window
from frontend.check_in import CheckIn

class MainWindow(Nav):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.lab_orders = Lab_Orders_Window()



#initializing app
app = QApplication(sys.argv)
UIWindow = MainWindow()
if __name__ == "__main__":
    UIWindow.show()
app.exec_()
