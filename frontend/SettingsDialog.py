

from PyQt5.QtWidgets import QDateEdit, QComboBox, QDialog, QApplication,
from PyQt5 import uic
from backend.data_handler import load_objects_to_combo_box, get_selected_combo_box_object, get_selected_list_object, load_objects_to_list
from backend.misc_dm import MiscDM
from backend.models import Location
import sys
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo # pylint: disable=unused-import

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        uic.loadUi("frontend/ui/SettingsDialog.ui", self)

        # Functions

        # Widgets
        self.locationsCombobox = self.findChild(QComboBox, "settingsLocationsComboBox")
        self.todaysDateDateEdit = self.findChild(QDateEdit, "settingsTodaysDateDateEdit")

        self.todaysDate = self.todaysDateDateEdit.date().toPyDate()

        load_objects_to_combo_box(MiscDM().get_locations(), self.locationsCombobox)


        def selected_location(self) -> Location:
            pass

