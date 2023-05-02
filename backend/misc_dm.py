"""
misc_data_manger.py - Handles miscellaneous tasks for interacting with the DB
Author: Christina Fortin
"""
from backend.private.data_manager import DataManager
from backend.models import Referral, LabOrder, Lab, Patient, Location, Employee
from datetime import date


class MiscDM(DataManager):
    """
    Handles miscellaneous tasks for interacting with the DB
    Includes:
           • Adding Referrals
           • Adding Lab Orders
           • Add Patients
           • Get Locations
           • Getting Labs (Types of Lab Orders)

    Uses self.session (From DataManger Superclass) to handle SQL Queries
    """
    def __init__(self):
        super().__init__()

    def add_referral(self, referral: Referral):
        """ Adds a referral to the DB """
        with self.session_scope() as session:
            session.add(referral)
            session.commit()

    def add_lab_order(self, lab_order: LabOrder):
        """ Adds a lab order to the DB """
        with self.session_scope() as session:
            session.add(lab_order)
            session.commit()

    def add_patient(self, patient: Patient):
        """ Adds a patient to the DB """
        with self.session_scope() as session:
            session.add(patient)
            session.commit()

    def get_lab_tests(self) -> list[Lab]:
        """ Returns list of lab tests """
        
        with self.session_scope() as session:
            labs = session.query(Lab)\
                .order_by(Lab.LabTest)\
                .all()
            
            session.expunge_all()
            return labs

    def get_locations(self) -> list[Location]:
        """ Returns list of all locations """
        
        with self.session_scope() as session:
            locations = session.query(Location)\
                .order_by(Location.Location_Name)\
                .all()
            session.expunge_all()

            return locations
    
    def get_location_with_id(self, id: int) -> Location:
        """ Returns location with given id """
        with self.session_scope() as session:
            location = session.query(Location)\
               .filter(Location.LocationID == id)\
               .first()
            session.expunge_all()
            return location
    
    def get_location_id(self, location: Location) -> int:
        """ 
        Returns location id with a location
        
        For the soul purpose of settings_dalog.py
            Accessing Location.LocationID outside of a session can lead to errors
            So this is just a safety procaution
        """
        with self.session_scope() as session:
            session.add(location)
            location_id = session.query(location.LocationID)\
                .filter(location.LocationID == location.LocationID)\
                .first()
            session.expunge_all()
            return location_id

    def create_referral(self, creation_date: date, referral_reason: str, patient: Patient, employee: Employee) -> \
            Referral:
        
        with self.session_scope() as session:
            session.add(patient)
            session.add(employee)
            referral = Referral(
                PatientID=patient.PatientID,
                PhysicianID=employee.EmployeeID,
                ReferralReason=referral_reason,
                ReferralDate=creation_date,

                Patient=patient,
                Employee=employee
            )

            session.expunge_all()

            return referral
    
    def create_lab_order(self, order_name: str,
                         patient: Patient,
                         employee: Employee,
                         lab_date: date,
                         lab: Lab,
                         location: Location) -> LabOrder:

        with self.session_scope() as session:
            session.add(patient)
            session.add(employee)
            session.add(lab)
            session.add(location)
            lab_order = LabOrder(
                OrderName=order_name,
                PatientID=patient.PatientID,
                PhysicianID=employee.EmployeeID,
                LabDate=lab_date,
                Lab=lab,
                Location=location
            )
        
            session.expunge_all()

            return lab_order
        