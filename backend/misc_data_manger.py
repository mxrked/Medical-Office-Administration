from backend.data_manager import DataManger
from backend.models import Referrals, LabOrder, Lab, Patient, HospitalLocation
import sqlalchemy as sa

class MiscDataManager(DataManger):

    def __init__(self):
        super().__init__()

    def add_referral(self, referral: Referrals):
        self.session.add(referral)
        self.session.commit()

    def add_lab_order(self, lab_order: LabOrder):
        self.session.add(lab_order)
        self.session.commit()

    def add_patient(self, patient: Patient):
        self.session.add(patient)
        self.session.commit()

    def get_lab_tests(self) -> list[Lab]:
        labs = self.session.query(Lab)\
            .order_by(Lab.LabTest)\
            .all()
        return labs

    def get_locations(self) -> list[HospitalLocation]:
        locations = self.session.query(HospitalLocation)\
            .order_by(HospitalLocation.LocationName)\
            .all()
        return locations
