"""
NewPatient.py - A window to add a new patient to the database
UI Designed by: Destan Hutcherson
Authors: 
"""

from PyQt5.QtWidgets import QMainWindow
from frontend.schedule import Cancel

class Patient(Cancel):

    def __init__(self):
        super(Patient, self).__init__()

        # TODO: Load Buttons