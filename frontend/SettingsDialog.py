

from PyQt5.QtWidgets import QDateEdit, QComboBox, QDialog, QApplication
from PyQt5 import uic
from frontend.main_nav import Nav
from backend.data_handler import set_objects_to_combo_box, get_selected_combo_box_object, get_selected_list_object, set_objects_to_list

import sys

class SettingsDialog(QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        uic.loadUi("frontend/ui/SettingsDialog.ui", self)

        # Functions

        # Widgets
        self.locationsCombobox = self.findChild(QComboBox, "settingsLocationsComboBox")
        self.todaysDateDateEdit = self.findChild(QDateEdit, "settingsTodaysDateDateEdit")

        self.todaysDate = self.todaysDateDateEdit.date().toPyDate()

        set_objects_to_combo_box(self.misc_dm.get_locations(), self.locationsCombobox) # This didnt work
        self.get_locations_into(self.locationsCombobox) # Nor did this .-. - I switched from Nav to QDialog again


def main():
    app = QApplication(sys.argv)
    UIWindow = SettingsDialog()
    UIWindow.show()
    app.exec()



if __name__ == "__main__":
    main()
