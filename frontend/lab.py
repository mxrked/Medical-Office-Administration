"""
LabOrders.py - A window to submit lab orders for a clinic
UI Designed by: Destan Hutcherson
Authors: Destan Hutcherson, 
"""
from PyQt5.QtWidgets import QPushButton, QLineEdit, QDateEdit, QComboBox

from backend.models import LabOrder
from frontend.main_nav import Nav
from backend.data_handler import get_selected_combo_box_object, set_objects_to_combo_box


class Lab(Nav):
    """
    Creates a lab using Lab object
    
    Uses the misc_dm & user_dm
    """
    def __init__(self):
        super(Lab, self).__init__()



        # define widgets
        self.lab_submit_btn = self.findChild(QPushButton, "pushButton_SubmitLabOrder")
        self.lab_clear_btn = self.findChild(QPushButton, "pushButton_ClearLabOrder")
        self.lab_fname = self.findChild(QLineEdit, "Lab_Fname")
        self.lab_lname = self.findChild(QLineEdit, "Lab_Lname")
        self.lab_dob = self.findChild(QDateEdit, "Lab_DOB")
        self.lab_practitioner_combo = self.findChild(QComboBox, "Lab_Combo_Practitioner")
        self.lab_locations_combo = self.findChild(QComboBox, "Lab_Combo_Location")
        self.lab_lab_date_edit = self.findChild(QDateEdit, "Lab_Date")
        self.lab_lab_combo = self.findChild(QComboBox, "Lab_Combo_Labs")
        self.lab_order_name = self.findChild(QLineEdit, "Lab_Order")

        # Do something
        self.lab_submit_btn.clicked.connect(self.submit_information)
        self.lab_clear_btn.clicked.connect(self.clearInputs)

        # fill combo boxes
        self.get_physicians_into(self.lab_practitioner_combo)
        self.get_locations_into(self.lab_locations_combo)
        set_objects_to_combo_box(self.misc_dm.get_lab_tests(), self.lab_lab_combo)





    def submit_information(self):
        """
            First get the Patient from user_dm
                using the inputs
            
            Then creates Lab in the db
            using Lab([Data])
            
            Uses the misc_dm
            
            Then run self.clear_inputs()
        """


        patient_fn = self.lab_fname.text()
        patient_ln = self.lab_lname.text()
        patient_dob = self.lab_dob.date().toPyDate()
        physician = get_selected_combo_box_object(self.lab_practitioner_combo)
        location = get_selected_combo_box_object(self.lab_locations_combo)
        lab_date = self.lab_lab_date_edit.date().toPyDate()
        lab_lab = get_selected_combo_box_object(self.lab_lab_combo)
        lab_order = self.lab_order_name.text()
        patients = self.user_dm.get_patients(first_name=patient_fn,
                                            last_name=patient_ln,
                                            dob=patient_dob)
        if len(patients) == 0:
            self.load_error("No Patients")
            return
        if len(patients) > 1:
            self.load_error("More than one patient")
            return

        patient = patients[0]


        labToAdd = LabOrder(
            OrderName = lab_order,
            PatientID =  patient.PatientID,
            PhysicianID = physician.EmployeeID,
            LabDate = lab_date,
            LabID = lab_lab.LabID,
            LocationID = location.LocationID,
            Employee = physician,
            Patient = patient,
            Location = location
        )


        self.misc_dm.add_lab_order(labToAdd)

