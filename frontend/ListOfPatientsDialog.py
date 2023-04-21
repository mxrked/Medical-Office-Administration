

from PyQt5.QtWidgets import QPushButton, QListWidget, QListWidgetItem, QDialog
from PyQt5 import uic
from backend.data_handler import get_selected_list_object, load_objects_to_list
from backend.misc_dm import MiscDM
from backend.models import Location
import sys
from frontend.ui.assets.qrc import app_bg, doctor, show, hide, logo # pylint: disable=unused-import

class ListOfPatientsDialog(QDialog):
    """
        A dialog to solve the soul issue of having multiple patients
            with the same name
    """
    def __init__(self, patients):
        super(ListOfPatientsDialog, self).__init__()

        uic.loadUi("frontend/ui/ListOfPatientsDialog.ui", self)

        # Functions
        
        # Widgets
        self.listOfPatientsLW = self.findChild(QListWidget, "listOfPatientsListWidget")
        self.closeBtn = self.findChild(QPushButton, "closeListOfPatientsBtn")

        # Since we need more information than the usual str, we have to recreate
        # What backend/data_handler.py does in load_objects_to_list
        for patient in patients:
            patient_str = str(patient)
            patient_str += f", DOB: {patient.DateOfBirth} \n"
            patient_str += f" Address: {patient.Address}"
            patient_str += f", Phone: {patient.Phone}"

            self.listOfPatientsLW.addItem(
                QLongListWidgtObject(patient, patient_str))


        self.closeBtn.clicked.connect(self.close)

    def close(self):
        patient = get_selected_list_object(self.listOfPatientsLW)

        if patient:
            self.accept()
    
    def get_patient(self):
        self.listOfPatientsLW = self.findChild(QListWidget, "listOfPatientsListWidget")

        return get_selected_list_object(self.listOfPatientsLW)



class QLongListWidgtObject(QListWidgetItem):
    """
        Like the one in backend/data_handler.py but we want our str to be inputed
        So our .selectedItems() returns the object
    """
    def __init__(self, obj, string):
        super().__init__(string)
        self.obj = obj
