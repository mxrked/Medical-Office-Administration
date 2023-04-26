

from PyQt5.QtWidgets import QDateEdit, QComboBox, QDialog, QPushButton
from PyQt5 import uic, QtCore
from backend.data_handler import load_objects_to_combo_box
from backend.misc_dm import MiscDM
from backend.models import Location
import sys
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo # pylint: disable=unused-import

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        uic.loadUi("frontend/ui/SettingsDialog.ui", self)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        def closeSettings():
            self.hide()

        # Widgets
        self.saveBtn = self.findChild(QPushButton, "settingsDialog_SaveBtn")
        self.locationsCombobox = self.findChild(QComboBox, "settingsLocationsComboBox")
        self.todaysDateDateEdit = self.findChild(QDateEdit, "settingsTodaysDateDateEdit")

        self.todaysDate = self.todaysDateDateEdit.date().toPyDate()

        self.saveBtn.clicked.connect(closeSettings)

        load_objects_to_combo_box(MiscDM().get_locations(), self.locationsCombobox)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Hides the title bar


    def selected_location(self) -> Location:
        pass

