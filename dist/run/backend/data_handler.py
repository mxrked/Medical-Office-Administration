"""
data_handler.py - A data handler for placing backend models into front end widgets for P
Authors: Jessica Weeks
"""
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QComboBox
from PyQt5.QtGui import QBrush, QColor
from backend.appointment_dm import AppointmentDM
from backend.models import Appointment


class __QListWidgetObject(QListWidgetItem):
    """
        Used for ListWidgets to present a str to the GUI
        but when we call .selectedItems() we can get the data (the obj) back

        :param obj: any stringable object
        :param long_str: if the object has a long string you want to use. This is a 
            little jank, but the object is supposed to have a method called "long_str"
    """
    def __init__(self, obj, long_str: bool = False, extra_info: str = ""):
        if long_str and hasattr(obj, "long_str"):
            super().__init__(str(obj.long_str() + extra_info))
        else:
            super().__init__(str(obj) + extra_info)
        self.obj = obj


def load_objects_to_list(objects: list[object], list_widget: QListWidget, long_str: bool = False):
    """
        Places a list of stringed objects into the list_widget
        ie list[Appointments], appointments_list_widget
    
        :param objects: put the list of Object (Models) you want to enter in here
        :param list_widget: put the QListWidget you want to modify here
        :param long_str: if the object has a long string you want to use. This is a 
            little jank, but the object is supposed to have a method called "long_str"

        We use the private class QListWidgetObject based off QlistWidgetItem to
        handle the relationship between data and string
    """
    list_widget.clear()
    for obj in objects:
        list_widget.addItem(__QListWidgetObject(obj, long_str))


def load_objects_to_combo_box(objects: list[object], combo_box: QComboBox):
    """
        Stores a list of stringed objects into a combo_box
        ie list[appointment_types], appointment_types_combo_box

        :param objects: put the list of Object (Models) you want to enter in here
        :param combo_box: put the QComboBox you want to modify here

        combo_boxes have a special feature that allows us to add data corresponding
        to the object_str
    """
    combo_box.clear()

    for obj in objects:
        combo_box.addItem(str(obj), obj)


def load_pending_appts_to_list(appointments: list[Appointment], list_widget: QListWidget):
    """
        Places a list of stringed objects into the list_widget
        ie list[Appointments], appointments_list_widget
            Will color red or green depending on if the appointment is available or not.
    
        :param objects: put the list of Object (Models) you want to enter in here
        :param list_widget: put the QListWidget you want to modify here
    """
    appt_dm = AppointmentDM()
    list_widget.clear()

    for appointment in appointments:
        try:
            appt_dm.check_appointment_available(appt=appointment)
            extra_info = " (available)"

        except AssertionError:  # Not available
            extra_info = " (not available)"
        
        item = __QListWidgetObject(obj=appointment, long_str=True, extra_info=extra_info)
        list_widget.addItem(item)

    appt_dm.close()


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
