
import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QDialog, QPushButton, QFileDialog
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
        self.summary_btn = self.findChild(QPushButton, "file_select")

        self.save_btn.clicked.connect(self.save_location)

        load_objects_to_combo_box(MiscDM().get_locations(), self.locationsCombobox)

        self.save_btn.clicked.connect(self.save_location)
        self.summary_btn.clicked.connect(self.summary_dialog)

        # We need to see if the file exists to create self.settings_json
        try:
            with open("frontend/ui/assets/files/Settings.json", "r",
                      encoding='UTF-8') as settings_file:
                file_contents = settings_file.read()
        
            self.settings_json = json.loads(file_contents)

        # if it doesn't exist, we create a settings_json
        except FileNotFoundError:
            print("Settings not found")
            self.settings_json = {
                "default_location_ID": "1",
                "last_entered_user": "",
                "summary_filepath": "C:/Users/Public/Desktop",
            }


    def save_location(self):


        # Make changes
        location = get_selected_combo_box_object(self.locationsCombobox)
        location_id = MiscDM().get_location_id(location)
        self.settings_json["default_location_ID"] = str(location_id[0])

        # Here we either create the file or modify the already existing file
        with open("frontend/ui/assets/files/Settings.json", "w",
                  encoding='UTF-8') as file:
            json.dump(self.settings_json, file)

        self.hide()

    def summary_dialog(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setDirectory(self.settings_json["summary_filepath"])
        dialog.setOption(QFileDialog.ShowDirsOnly, True)

        if dialog.exec() == QFileDialog.Accepted:
            directory = dialog.selectedFiles()[0]
            self.settings_json["summary_filepath"] = directory

            with open("frontend/ui/assets/files/Settings.json", "w", encoding='UTF-8') as file:
                json.dump(self.settings_json, file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsDialog()
    window.show()
    sys.exit(app.exec_())
