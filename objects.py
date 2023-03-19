"""
objects.py - objects used to help model relationships within the Medical Office Admin database
Author: Jessica Weeks
"""

from datetime import date, time, datetime

class Appointment:
    """
    Represents a appointment made by a patient

    :param appointment_id: int, the unique identifier of the appointment.
    :param appt_date: date, the date of the appointment.
    :param appt_time: time, the time of the appointment.
    :param appt_type_id: int, the unique identifier of the appointment type.
    :param patient_id: int, the unique identifier of the patient who scheduled the appointment.
    :param appt_status: str, the status of the appointment, e.g. 'scheduled', 'cancelled', etc.
    :param visit_reason: str, the reason for the visit as provided by the patient.
    """
    def __init__(self,
                 appointment_id: int,
                 appt_date: date,
                 appt_time: time,
                 appt_type_id: int,
                 patient_id: int,
                 appt_status: str,
                 visit_reason: str):
        self.appointment_id = appointment_id
        self.appt_date = appt_date
        self.appt_time = appt_time
        self.appt_type_id = appt_type_id
        self.patient_id = patient_id
        self.appt_status = appt_status
        self.visit_reason = visit_reason

    @property
    def appointment_id(self):
        """ Refers to a appointment_id """
        return self._appointment_id

    @appointment_id.setter
    def appointment_id(self, appointment_id):
        self._appointment_id = appointment_id

    @property
    def appt_date(self):
        """ Refers to a appointment's date"""
        return self._appt_date

    @appt_date.setter
    def appt_date(self, appt_date):
        self._appt_date = appt_date

    @property
    def appt_time(self):
        """ Refers to a appointment's time"""
        return self._appt_time

    @appt_time.setter
    def appt_time(self, appt_time):
        self._appt_time = appt_time

    @property
    def appt_type_id(self):
        """ Refers to the appointment type's ID"""
        return self._appt_type_id

    @appt_type_id.setter
    def appt_type_id(self, appt_type_id):
        self._appt_type_id = appt_type_id

    @property
    def patient_id(self):
        """ Refers to a patient """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id

    @property
    def appt_status(self):
        """ 
        Should only be 
            checked in
            scheduled
            rescheduled
            in progress
            completed
            no show
            pending
        """
        return self._appt_status

    @appt_status.setter
    def appt_status(self, appt_status):
        if appt_status not in ["checked in", "scheduled", "rescheduled",
                               "in progress", "completed", "no show", "pending"]:
            raise ValueError("Invalid appointment status")
        self._appt_status = appt_status

    @property
    def visit_reason(self):
        """ A reason this visit is happening """
        return self._visit_reason

    @visit_reason.setter
    def visit_reason(self, visit_reason):
        self._visit_reason = visit_reason

class Patient:
    """ Represents a patient

        :param patient_id: int, the unique identifier of the patient.
        :param last_name: str, the last name of the patient.
        :param first_name: str, the first name of the patient.
        :param date_of_birth: str, the date of birth of the patient in the format 'YYYY-MM-DD'.
        """
    def __init__(self,
                 patient_id: int,
                 last_name: str,
                 first_name: str,
                 date_of_birth: date):
        self.patient_id = patient_id
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth

    @property
    def patient_id(self):
        """ Refers to a patient """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        self._patient_id = value

    @property
    def last_name(self):
        """ Refers to a patients last name, must be <= 50 char """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) > 50:
            raise ValueError("Last name cannot be longer than 50 characters")
        self._last_name = value

    @property
    def first_name(self):
        """ Refers to a patients first name, must be <= 50 char """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if len(value) > 50:
            raise ValueError("First name cannot be longer than 50 characters")
        self._first_name = value

    @property
    def date_of_birth(self):
        """ Date of birth with the DATE datatype """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError as exc:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD") from exc
        self._date_of_birth = value


class Referral:
    """
    Represents a referral made by an employee for a patient.

    :param referral_id: int, the unique identifier of the referral.
    :param referral_reason: str, the reason for the referral as provided by the employee.
    :param creation_date: date, the date the referral was created.
    :param employee_id: int, the unique identifier of the employee who created the referral.
    :param patient_id: int, the unique identifier of the patient who the referral is for.
    """
    def __init__(self,
                 referral_id: int,
                 referral_reason: str,
                 creation_date: date,
                 employee_id: int,
                 patient_id: int):
        self.referral_id = referral_id
        self.referral_reason = referral_reason
        self.creation_date = creation_date
        self.employee_id = employee_id
        self.patient_id = patient_id

    @property
    def referral_id(self):
        """ Refers to a referral's ID """
        return self._referral_id

    @referral_id.setter
    def referral_id(self, referral_id):
        self._referral_id = referral_id

    @property
    def referral_reason(self):
        """ Refers to a referral's reason """
        return self._referral_reason

    @referral_reason.setter
    def referral_reason(self, referral_reason):
        self._referral_reason = referral_reason

    @property
    def creation_date(self):
        """ Refers to a referral's creation date """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @property
    def employee_id(self):
        """ Refers to the employee's ID who created the referral """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def patient_id(self):
        """ Refers to the patient's ID who the referral is for """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id
