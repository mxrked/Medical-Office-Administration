from data_manager import *

class MiscDataManager(DataManger):

    def __init__(self):
        super().__init__()

    def add_refferal(self, referral: Referrals):
        pass

    def add_lab_order(self, lab_order: LabOrder):
        pass

    def add_patient(self, patient: Patient):
        pass

    def get_lab_tests(self) -> list[Lab]:
        labs = []
        return labs

    def get_locations(self) -> list[HospitalLocation]:
        locations = self.session.query(HospitalLocation)\
            .order_by(HospitalLocation.LocationName)\
            .all()
        return locations
