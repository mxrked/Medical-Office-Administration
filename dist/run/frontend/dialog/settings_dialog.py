

from PyQt5.QtWidgets import QDateEdit, QComboBox, QDialog, QPushButton
from PyQt5 import uic, QtCore
from backend.data_handler import load_objects_to_combo_box, get_selected_combo_box_object
from backend.misc_dm import MiscDM
import json


class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        uic.loadUi("frontend/ui/SettingsDialog.ui", self)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Widgets
        self.save_btn = self.findChild(QPushButton, "settingsDialog_SaveBtn")
        self.locationsCombobox = self.findChild(QComboBox, "settingsLocationsComboBox")
        self.todays_date_edit = self.findChild(QDateEdit, "settingsTodaysDateDateEdit")

        self.todays_date = self.todays_date_edit.date().toPyDate()

        self.save_btn.clicked.connect(self.save_settigns)

        load_objects_to_combo_box(MiscDM().get_locations(), self.locationsCombobox)

        self.save_btn.clicked.connect(self.save_settigns)

        self.settings_json = ""

    def save_settigns(self):

        # We see if the file exists
        try:
            with open("frontend/ui/assets/files/Settings.json", "r",
                      encoding='UTF-8') as settings_file:
                file_contents = settings_file.read()
        
            settings_json = json.loads(file_contents)

        # if it doesn't exist, we create a settings_json
        except FileNotFoundError:
            print("Settings not found")
            settings_json = {
                "default_location_ID": "1",
                "last_entered_user": ""
            }

        # Make changes
        location = get_selected_combo_box_object(self.locationsCombobox)
        location_id = MiscDM().get_location_id(location)
        settings_json["default_location_ID"] = location_id[0]

        # Here we either create the file or modify the already existing file
        with open("frontend/ui/assets/files/Settings.json", "w",
                  encoding='UTF-8') as file:
            json.dump(settings_json, file)

        self.hide()
