"""
data_handler.py - A data handler for placing backend models into front end widgets for P
Authors: Jessica Weeks,
"""

from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from datetime import date, time

example_objects = []

class test_object():
    
    def __init__(self):
        self.name = "Name"
        self.description = "Description"

    def __str__(self):
        return f"My name is {self.name} and I am {self.description}"

for i in range(0,10):
    example_objects.append(
            test_object()
        )



def place_objects_into_list(objects: list[object], list_widget: QListWidget):
    

    for object in objects:
        
        dictionary = {
            str(object) : object
        }

    for object_str in list(dictionary.keys()):

        list_widget.addItem(QListWidgetItem(
            object_str
        ))

list_widget = QListWidget()

place_objects_into_list(test_object, list_widget)