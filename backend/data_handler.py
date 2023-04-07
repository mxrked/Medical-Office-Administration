"""
data_handler.py - A data handler for placing backend models into front end widgets for P
Authors: Jessica Weeks,
"""

from PyQt5.QtWidgets import QListWidget, QListWidgetItem

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


def place_objects_into_list(objects: list[object], list_widget: QListWidget) -> list[str]:
    
    list_widget.clear()
    object_strings = []

    for obj in objects:
        object_strings.append(str(obj))

    for object_str in object_strings:
        list_widget.addItem(QListWidgetItem(object_str))


    return object_strings

