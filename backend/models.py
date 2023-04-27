"""
models.py - a set of sqlalchemy models for working with the clinics Database.
Author: Jessica Weeks, Christina Fortin
Author: Jessica Weeks, Christina Fortin
"""
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Table, Integer, VARCHAR, Date, Time, ForeignKey, Numeric, NVARCHAR, CHAR
from backend.connection_string import DB


Base = declarative_base()

class Appointment(Base):
    """
        A sqlalchemy ORM for Appointment Table

        NOTE FOP FRONTEND: ApptStatus is very important to type in correct, use "Scheduled"
        This should be the only case you use this

        :param ApptDate: Datetime Date object
        :param ApptTime: Datetime Time object
        :param PatientID: Corresponds to patient. Use Patient.PatientID
        :param ApptStatus: A string, frontend should not be using this.
            Must be a set of statues in appointment_status_dm
        :param ApptEndTime: The time the appointment ends
        :param PhysicianID: Correspond to a Physician, Use Employee.EmployeeID
        :param ApptTypeID: Corresponds to a Appointment Type, Use AppointmentType.AppointmentTypeID
        :param LocationID: Corresponds to a Location, use Location.LocationID
        :param ApptReason: Reason for a appointment, can be any string

        :param AppointmentType: The AppointmentType Object. Use AppointmentType
        :param Patient: The Patient Object. Use Patient
        :param Employee: The Employee Object. Use Employee (Refers to Physician)
        :param Location: The Location Object. Use Location

            Has a str method if needed
    """
    __tablename__ = "Appointment"
    patient_name = ""

    AppointmentID = Column(Integer, primary_key=True)

    # nullable is set to FALSE by default unless a primary_key
    ApptDate = Column(Date)
    ApptTime = Column(Time)
    PatientID = Column(Integer, ForeignKey("Patient.PatientID"))
    ApptStatus = Column(VARCHAR(50))
    ApptEndtime = Column(Time)
    PhysicianID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    ApptTypeID = Column(Integer, ForeignKey("AppointmentType.ApptTypeID"))
    LocationID = Column(Integer, ForeignKey("Location.LocationID"))
    ApptReason = Column(VARCHAR(500))

    AppointmentType = relationship("AppointmentType", backref="ApptAppointmentType")
    Patient = relationship("Patient", backref="ApptPatient")
    Employee = relationship("Employee", backref="ApptEmployee")
    Location = relationship("Location", backref="ApptLocation")

    def __str__(self) ->  str:

        formated_time = self.ApptTime.strftime("%I:%M:%S %p")
        try: # Sometimes the patient name is decoupled
            return f"{formated_time} for {self.Patient}"
        except Exception:
            return f"{formated_time} for {self.patient_name}"
        
    def long_str(self) -> str:
        formated_time = self.ApptTime.strftime("%I:%M:%S %p")
        formated_endtime = self.ApptEndtime.strftime("%I:%M:%S %p")
        formated_date = self.ApptDate.strftime("%d/%m/%Y")
        try: # Sometimes the patient name is decoupled
            return f"{self.Patient} : {formated_time} till {formated_endtime} for {self.ApptReason}"
        except Exception:
            return f"{self.patient_name} : {formated_time} till {formated_endtime} \n Reason: {self.ApptReason} Date: {self.ApptDate}"
        
             
            
       
        

class AppointmentType(Base):
    """
        A sqlalchemy ORM for the AppointmentType Table
        
        :column ApptName: Refers to the appointments Name

            Has a str method if needed
    """
    __tablename__ = "AppointmentType"

    ApptTypeID = Column(Integer, primary_key=True)

    ApptName = Column(VARCHAR(50))

    def __str__(self) -> str:
        return f"{self.ApptName}"


EmpUserRoleCross = Table(
    'EmpUserRoleCross',
    Base.metadata,
    Column('DummyID', Integer, primary_key=True),
    Column('EmployeeID', Integer, ForeignKey("Employee.EmployeeID")),
    Column('RoleID', Integer, ForeignKey("Role.RoleID")),
    # Column('DepartmentID', Integer, ForeignKey("Departments.DepartmentID")),
    Column('LocationID', Integer, ForeignKey("Location.LocationID"))
)

EmpGroupCross = Table(
    'EmpGroupCross',
    Base.metadata,
    Column('DummyID', Integer, primary_key=True),
    Column('EmployeeID', Integer, ForeignKey("Employee.EmployeeID")),
    Column('GroupID', Integer, ForeignKey("Group.GroupID"))
)

class Employee(Base):
    """
        A sqlalchemy ORM for the Employee Table

        We shouldn't be making these so im not putting more params

        :Column EmployeeID: Refers to Employee (Use for other model's)
        :Column EmployeeTypeID: Refers to EmployeeType
        :Column UserID: Refers to User

            Has a str method if needed

        You should souly pull these objects from the db and use these columns
    """
    __tablename__ = "Employee"

    EmployeeID = Column(Integer, primary_key=True)

    Title = Column(VARCHAR(10))
    Last_Name = Column(VARCHAR(50))
    FirstName = Column(VARCHAR(50))
    Address = Column(NVARCHAR(50))
    City = Column(NVARCHAR(50))
    State = Column(NVARCHAR(50))
    ZipCode = Column(CHAR(10))
    Phone = Column(NVARCHAR(12))
    Gender = Column(VARCHAR(50))
    EmployeeTypeID = Column(Integer, ForeignKey("EmployeeType.EmployeeTypeID"))
    Position = Column(VARCHAR(50))
    UserID = Column(Integer, ForeignKey("User.UserID"))
    Email = Column(VARCHAR(50))
    LocationID = Column(Integer, ForeignKey("Location.LocationID"))

    EmployeeType = relationship("EmployeeType", backref="EmpEmployeeType")
    User = relationship("User", backref="EmpUser")
    Location = relationship("Location", backref="EmpLocation")

    def __str__(self) -> str:
        return f"{self.Title} {self.FirstName}, {self.Last_Name} ({self.Position})"

class EmployeeType(Base):
    __tablename__ = "EmployeeType"

    EmployeeTypeID = Column(Integer, primary_key=True)

    Type = Column(VARCHAR(50))

EmployeeRoleCross = Table(
    "EmployeeRoleCross",
    Base.metadata,
    Column("EmployeeID", ForeignKey("Employee.EmployeeID")),
    Column("RoleID", ForeignKey("Role.RoleID"))
)


class Event(Base):
    __tablename__ = "Event"

    EventID = Column(Integer, primary_key=True)

    EventName = Column(VARCHAR(50), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"), nullable=True)
    WorkingDays = Column(VARCHAR(50))

    Employee = relationship("Employee", backref="EvEmployee")

    def __str__(self) -> str:
        return self.EventName

class Lab(Base):
    """
        A SQL ORM for the Lab Table

        You should only be pulling this information

        :column: LabID
        :column: LabTest (The Labs name)
    """
    __tablename__ = "Lab"

    LabID = Column(Integer, primary_key=True)

    LabTest = Column(VARCHAR(50), nullable=False)

    def __str__(self) -> str:
        return self.LabTest


class LabOrder(Base):
    """
        A SQL ORM for the LabOrder table

        :param OrderName: String, Name of the order
        :param PatientID: Int, use Patient.PatientID
        :param PhysicianID: Int, use Employee.EmployeeID
        :param LabDate: date, use a datetime date object
        :param LabID: Int, use Lab.LabID
        :param LocationID: Int, use Location.LocationID

        :param Employee: Object, use Employee/Physician
        :param Patient: Object, use Patient
        :param Location: Object, use Location
    """
    __tablename__ = "LabOrder"

    LabOrderID = Column(Integer, primary_key=True)

    OrderName = Column(VARCHAR(50))
    PatientID = Column(Integer, ForeignKey("Patient.PatientID"))
    PhysicianID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    LabDate = Column(Date, nullable=False)
    LabID = Column(Integer, ForeignKey("Lab.LabID"))
    LocationID = Column(Integer, ForeignKey("Location.LocationID"))

    Employee = relationship("Employee", backref="LOEmployee")
    Patient = relationship("Patient", backref="LOPatient")
    Location = relationship("Location", backref="LOLocation")
    Lab = relationship("Lab", backref="LOLab")

class Patient(Base):
    """
        A SQL ORM for the Patient Table

        :param Last_Name: String, Last name of the patient
        :param First_Name: String, First name of the patient
        :param Address: String, Address of the patient
        :param City: String, City of the patient
        :param State: String, State of the patient
        :param ZipCode: String, Zip code of the patient
        :param Gender: String, Gender of the patient
        :param DateOfBirth: date, Use Date from Datetime library
        :param Race: String, Race of the patient
        :param UserID: Int, use User.UserID
        :param Phone: String, Phone number of the patient
        :param Email: String, Email address of the patient

        :param User: Object, use User

    """
    __tablename__ = "Patient"

    PatientID = Column(Integer, primary_key=True)

    Last_Name = Column(VARCHAR(50))
    First_Name = Column(VARCHAR(50))
    Address = Column(NVARCHAR(50))
    City = Column(VARCHAR(50))
    State = Column(VARCHAR(50))
    ZipCode = Column(CHAR(10))
    Gender = Column(VARCHAR(50))
    DateOfBirth = Column(Date)
    Race = Column(VARCHAR(50))
    UserID = Column(Integer, ForeignKey("User.UserID"), nullable=True)
    Phone = Column(CHAR(15))
    Email = Column(VARCHAR(50))

    User = relationship("User", backref="PatientUser")

    def __str__(self) -> str:
        return f"{self.First_Name}, {self.Last_Name}"


class Group(Base):
    __tablename__ = "Group"

    GroupID = Column(Integer, primary_key=True)

    Group = Column(VARCHAR(50))


GroupRoleCross = Table(
    "GroupRoleCross",
    Base.metadata,
    Column("GroupID", ForeignKey("Group.GroupID")),
    Column("RoleID", ForeignKey("Role.RoleID"))
)


class HospitalHours(Base):
    __tablename__ = "HospitalHours"

    HospitalHoursID = Column(Integer, primary_key=True)

    LocationID = Column(Integer, ForeignKey("Location.LocationID"), nullable=False)
    WeekNumber = Column(NVARCHAR(50), nullable=True)
    DayOfWeek = Column(NVARCHAR(50), nullable=False)
    OpenTime = Column(Time, nullable=True)
    CloseTime = Column(Time, nullable=True)


    Location = relationship("Location", backref="HHLocation")


class Location(Base):
    """
        A sqlalchemy ORM to represent locations

        You should only be pulling these, not creating them

        :column LocationID:
        :column Location_Name:

        is stringable
    """
    __tablename__ = "Location"

    LocationID = Column(Integer, primary_key=True)

    Location_Name = Column(VARCHAR(50), nullable=False)
    Address_1 = Column(NVARCHAR(50), nullable=False)
    Address_2 = Column(NVARCHAR(50), nullable=False)
    City = Column(VARCHAR(50), nullable=False)
    State = Column(VARCHAR(50), nullable=False)
    ZipCode = Column(CHAR(10), nullable=False)
    Phone = Column(NVARCHAR(12), nullable=False)
    Email = Column(VARCHAR(50), nullable=False)

    def __str__(self) -> str:
        return f"{self.Location_Name}"

class Role(Base):
    __tablename__ = "Role"

    RoleID = Column(Integer, primary_key=True)

    Role = Column(VARCHAR(500), nullable=False)

class User(Base):
    """
    A sqlalchemy orm for User Table

    :column UserTypeID: Refers to User Type
    :column UserName:
    :column Password:
    """
    __tablename__ = "User"

    UserID = Column(Integer, primary_key=True)

    UserTypeID = Column(Integer, ForeignKey("UserType.UserTypeID"))
    UserName = Column(VARCHAR(50), nullable=False)
    Password = Column(NVARCHAR(50), nullable=False)
    Email = Column(VARCHAR(50), nullable=False)

    UserType = relationship("UserType", backref="UUserType")

    def __str__(self) -> str:
        return f"{self.Username}"

class Referral(Base):
    """
    A sqlalchemy orm for Referral Table
    
    :param ReferralReason:
    :param PatientID: int, Use Patient.PatientID
    :param PhysicianID: int, Use Employee.EmployeeID
    :param ReferralDate: date, Use date from Datetime library
    
    :param Patient: Patient Object, use Patient
    :param Employee: Employee Object, use Employee
    """
    __tablename__ = "Referral"

    ReferralID = Column(Integer, primary_key=True)

    ReferralReason = Column(VARCHAR(50))
    PatientID = Column(Integer, ForeignKey("Patient.PatientID"))
    PhysicianID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    ReferralDate = Column(Date)

    Patient = relationship("Patient", backref="RePatient")
    Employee = relationship("Employee", backref="ReEmployee")

    def __str__(self) -> str:
        return f"Referral for {self.Patient} by {self.Employee}"


class UserType(Base):
    __tablename__ = "UserType"

    UserTypeID = Column(Integer, primary_key=True, nullable=False)

    UserType = Column(VARCHAR(50), nullable=False)
