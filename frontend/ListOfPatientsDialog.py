

from PyQt5.QtWidgets import QDateEdit, QPushButton, QListWidget, QComboBox, QDialog, QApplication
from PyQt5 import uic
from backend.data_handler import load_objects_to_combo_box, get_selected_combo_box_object, get_selected_list_object, load_objects_to_list
from backend.misc_dm import MiscDM
from backend.models import Location
import sys
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo # pylint: disable=unused-import

class ListOfPatientsDialog(QDialog):
    def __init__(self):
        super(ListOfPatientsDialog, self).__init__()

        uic.loadUi("frontend/ui/ListOfPatientsDialog.ui", self)

        # Functions

        # Widgets
        self.listOfPatientsLW = self.findChild(QListWidget, "listOfPatientsListWidget")
        self.closeBtn = self.findChild(QPushButton, "closeListOfPatientsBtn")

