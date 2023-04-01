"""
models.py - a set of sqlalchemy models for working with the clinics Database.
Author: Jessica Weeks, Christian Fortin
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import BLOB, Column, Table, Integer, String, VARCHAR, Date, Time, ForeignKey, Numeric, NVARCHAR, Float, NCHAR

Base = declarative_base()


class Appointment(Base):
    __tablename__ = "Appointment"

    AppointmentID = Column(Integer, primary_key=True, nullable=False)

    # nullable is set to FALSE by default unless a primary_key
    ApptDate = Column(Date)
    ApptTime = Column(Time)
    ApptTypeID = Column(Integer, ForeignKey("AppointmentType.ApptTypeID")) 
    PatientID = Column(Integer, ForeignKey("Patient.PatientID"))
    ApptStatus = Column(VARCHAR(50))
    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    VisitReason = Column(String)
    LocationID = Column(Integer, ForeignKey("HospitalLocation.LocationID"))

    AppointmentType= relationship("AppointmentType", backref="ApptAppointmentType")
    Patient = relationship("Patient", backref="ApptPatient")
    Employee = relationship("Employee", backref="ApptEmployee")
    HospitalLocation = relationship("HospitalLocation", backref="ApptHospitalLocation")

    def __str__(self) -> str:
        return f"Appointment on {self.ApptDate} at {self.ApptTime} for {self.Patient.FirstName} {self.Patient.LastName}"

class AppointmentType(Base):
    __tablename__ = "AppointmentType"

    ApptTypeID = Column(Integer, primary_key=True, nullable=False)

    ApptName = Column(VARCHAR(50))
    ApptLength = Column(Numeric(18, 0))

    def __str__(self) -> str:
        return f"{self.ApptName}"

EmpUserRoleCross = Table('EmpUserRoleCross', Base.metadata,
    Column('DummyID', Integer, primary_key=True),
    Column('EmployeeID', Integer, ForeignKey("Employee.EmployeeID")),
    Column('RoleID', Integer, ForeignKey("Role.RoleID")),
    Column('DepartmentID', Integer, ForeignKey("Departments.DepartmentID")),
    Column('OfficeID', Integer, ForeignKey("Offices.OfficeID"))
)

EmpGroupCross = Table('EmpGroupCross', Base.metadata,
    Column('DummyID', Integer, primary_key=True),
    Column('EmployeeID', Integer, ForeignKey("Employee.EmployeeID")),
    Column('GroupID', Integer, ForeignKey("Group.GroupID"))
)

EmpLocReferralCross = Table('EmpLocReferralCross', Base.metadata,
    Column('DummyID', Integer, primary_key=True),
    Column('EmployeeID', Integer, ForeignKey("Employee.EmployeeID ")),
    Column('LocationID', Integer, ForeignKey("Location.LocationID")),
    Column('ReferralID', Integer, ForeignKey("Referral.ReferralID"))
)

class Employee(Base):
    __tablename__ = "Employee"

    EmployeeID = Column(Integer, primary_key=True, nullable=False)

    LastName = Column(VARCHAR(50))
    MiddleName = Column(VARCHAR(50), nullable=True)
    FirstName = Column(VARCHAR(50))
    ssn = Column(NVARCHAR(9), nullable=True)
    DateOfBirth = Column(Date)
    Gender = Column(VARCHAR(10), nullable=True)
    Phone = Column(NVARCHAR(12), nullable=True)
    Email = Column(VARCHAR(50), nullable=True)
    StartDate = Column(Date)
    EndDate = Column(Date, nullable=True)
    Salary = Column(Numeric)
    apto = Column(Float, nullable=True)
    EmployeeTypeID = Column(Integer, ForeignKey("EmployeeType.EmployeeTypeID"), nullable=True)

    EmployeeType = relationship("EmployeeType", backref="EmpEmployeeType")

class EmployeeCredintials(Base):
    __tablename__ = "EmployeeCredintials"

    DummyID = Column(Integer, primary_key=True)

    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    Title = Column(NCHAR(10), nullable=True)
    Status = Column(NCHAR(10))
    StartDate = Column(Date)
    EndDate = Column(Date, nullable=True)
    Length = Column(NCHAR(10), nullable=True)
    State = Column(NCHAR(10), nullable=True)
    Renewel = Column(NCHAR(10))

    Employee = relationship("Employee", backref="ECEmployeeCredintials")

class EmployeeRoles(Base):
    __tablename__ = "EmployeeRoles"

    RoleID = Column(Integer, primary_key=True, nullable=True)

    RoleName = Column(NVARCHAR(50), nullable=True)
    RoleDescription = Column(NVARCHAR(50))
    RoleTitle = Column(NVARCHAR(10), nullable=True)


class EmployeeType(Base):
    __tablename__ = "EmployeeType"

    EmployeeTypeID = Column(Integer, primary_key=True, nullable=False)

    TypeDescription = Column(VARCHAR(50))

EmployeeRoleCross = Table(
    "EmployeeRoleCross",
    Base.metadata,
    Column("EmployeeID", ForeignKey("Employee.EmployeeID")),
    Column("RoleID", ForeignKey("Role.RoleID"))
)

class Event(Base):
    __tablename__ = "Event"

    EventID = Column(Integer, primary_key=True, nullable=False)

    EventName = Column(VARCHAR(50), nullable=False)
    StartDate = Column(Date, nullable=False)
    EndDate = Column(Date, nullable=False)
    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    WorkingDays = Column(VARCHAR(10))

    Employee = relationship("Employee", backref="EvEmployee")

class Lab(Base):
    __tablename__ = "Lab"

    LabID = Column(Integer, primary_key=True, nullable=False)

    LabTest = Column(String, nullable=False)

class LabOrder(Base):
    __tablename__ = "LabOrder"

    LabOrderID = Column(Integer, primary_key=True, nullable=False)

    OrderName = Column(VARCHAR(50), nullable=True)
    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    PatientID = Column(Integer, ForeignKey("Patient.PatientID"))
    LabDate = Column(Date, nullable=False)
    Results = Column(String, nullable=True)
    LabID = Column(Integer, ForeignKey("Lab.LabID"))
    LocationID = Column(Integer, ForeignKey("HospitalLocation.LocationID"))

    Employee = relationship("Employee", backref="LOEmployee")
    Patient = relationship("Patient", backref="LOPatient")
    Location = relationship("Location", backref="LOHospitalLocation")

class Patient(Base):
    __tablename__ = "Patient"

    PatientID = Column(Integer, primary_key=True, nullable=False)

    LastName = Column(VARCHAR(50), nullable=False)
    FirstName = Column(VARCHAR(50), nullable=False)
    MiddleName = Column(VARCHAR(50), nullable=True)
    Suffix = Column(VARCHAR(10), nullable=True)
    Gender = Column(VARCHAR(10), nullable=True)
    DateOfBirth = Column(Date, nullable=False)
    Phone = Column(NVARCHAR(12), nullable=True)
    Email = Column(VARCHAR(50), nullable=True)
    MaritalStatus = Column(VARCHAR(10), nullable=True)
    # ProviderID = Column(Integer, ForeignKey("") nullable=)
    PatientPhoto = Column(BLOB, nullable=True)
    RecordStatus = Column(Integer, nullable=True)

class Group(Base):
    __tablename__ = "Group"

    GroupID = Column(Integer, primary_key=True, nullable=False)

    GroupName = Column(VARCHAR(50), nullable=False)
    Description = Column(String, nullable=False)

GroupRoleCross = Table(
    "GroupRoleCross",
    Base.metadata,
    Column("GroupID", ForeignKey("Group.GroupID")),
    Column("RoleID", ForeignKey("Role.RoleID"))
)

class HospitalHours(Base):
    __tablename__ = "HospitalHours"

    HospitalHoursID = Column(Integer, primary_key=True, nullable=False)

    LocationID = Column(Integer, ForeignKey("HospitalLocation.LocationID"))
    DayOfWeek = Column(VARCHAR(50), nullable=False)
    OpenTime = Column(Time, nullable=False)
    CloseTime = Column(Time, nullable=False)

    Location = relationship("Location", backref="HHHospitalLocation")

class HospitalLocation(Base):
    __tablename__ = "HospitalLocation"

    HospitalLocationID = Column(Integer, primary_key=True, nullable=False)

    LocationName = Column(VARCHAR(50), nullable=False)
    Phone = Column(NVARCHAR(12), nullable=False)
    Email = Column(VARCHAR(50), nullable=False)
    Address = Column(VARCHAR(50), nullable=False)
    ZipCode = Column(VARCHAR(5), nullable=False)

class MessagingThread(Base):
    __tablename__ = "MessagingThread"

    MessageID = Column(Integer, primary_key=True, nullable=False)

    MessageSubject = Column(VARCHAR(50), nullable=False)
    MessageBody = Column(VARCHAR(), nullable=False)
    SenderName = Column(VARCHAR(50), nullable=False)
    SenderEmail = Column(VARCHAR(50), nullable=False)
    RecipientName = Column(VARCHAR(50), nullable=False)
    RecipientEmail = Column(VARCHAR(50), nullable=False)
    Date = Column(Date, nullable=False)
    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    PatientID = Column(Integer, ForeignKey("Patient.PatientID"))

    Employee = relationship("Employee", backref="MTEmployee")
    Patient = relationship("Patient", backref="MTPatient")

class Role(Base):
    __tablename__ = "Role"

    RoleID = Column(Integer, primary_key=True, nullable=False)

    RoleName = Column(VARCHAR(50), nullable=False)
    RoleDescription = Column(VARCHAR, nullable=True)

class User(Base):
    __tablename__ = "User"

    UserID = Column(Integer, primary_key=True, nullable=False)

    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    Username = Column(NCHAR(10), nullable=False)
    EmailAddress = Column(VARCHAR(), nullable=False)
    Password = Column(VARCHAR(), nullable=False)
