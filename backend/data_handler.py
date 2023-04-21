"""
data_handler.py - A data handler for placing backend models into front end widgets for P
Authors: Jessica Weeks
"""
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QComboBox
from backend.misc_dm import MiscDM
from backend.user_dm import UserDM
class __QListWidgetObject(QListWidgetItem):
    """
        Used for ListWidgets to present a str to the GUI
        but when we call .selectedItems() we can get the data (the obj) back
    """
    def __init__(self, obj):
        super().__init__(str(obj))
        self.obj = obj

def load_objects_to_list(objects: list[object], list_widget: QListWidget):
    """
        Places a list of stringed objects into the list_widget
        i.e list[Appointments], appointments_list_widget
    
        :param objects: put the list of Object (Models) you want to enter in here
        :param list_widget: put the QListWidget you want to modify here

        We use the private class QListWidgetObject based off QlistWidgetItem to
        handle the relationship between data and string
    """
    list_widget.clear()
    for obj in objects:
        list_widget.addItem(__QListWidgetObject(obj))

def load_objects_to_combo_box(objects: list[object], combo_box: QComboBox):
    """
        Places a list of stringed objects into a combo_box
        i.e list[Physisicans], physiscans_comobo_box

        :param objects: put the list of Object (Models) you want to enter in here
        :param combo_box: put the QComboBox you want to modify here

        combo_boxes have a special feature that allows us to add data corresponding
        to the object_str
    """
    combo_box.clear()

    for obj in objects:
        combo_box.addItem(str(obj), obj)

def get_selected_list_object(list_widget: QListWidget) -> object:
    """
        Returns the object that corresponds to whatever is selected in
        list_widget

        :param list_widget: The QListWidget you wish to read from

        :returns: The relevant object placed using our object list setters
    """
    items = list_widget.selectedItems()
    if items:
        return items[0].obj

def get_selected_combo_box_object(combo_box: QComboBox) -> object:
    """
        Returns the object that corresponds to whatever is selected in
        combo_box

        :param combo_box: The QComboBox you wish to read from

        :returns: The relevant object placed using our object box setters
    """
    return combo_box.currentData()

