from datetime import date, time

class Appointment:
    def __init__(self, appointment_id: int, appt_date: date, appt_time: time, appt_type_id: int, patient_id: int, appt_status: str, visit_reason: str):
        self._appointment_id = appointment_id
        self._appt_date = appt_date
        self._appt_time = appt_time
        self._appt_type_id = appt_type_id
        self._patient_id = patient_id
        self._appt_status = appt_status
        self._visit_reason = visit_reason

    @property
    def appointment_id(self) -> int:
        return self._appointment_id

    @property
    def appt_date(self) -> date:
        return self._appt_date

    @property
    def appt_time(self) -> time:
        return self._appt_time

    @property
    def appt_type_id(self) -> int:
        return self._appt_type_id

    @property
    def patient_id(self) -> int:
        return self._patient_id

    @property
    def appt_status(self) -> str:
        return self._appt_status

    @property
    def visit_reason(self) -> str:
        return self._visit_reason