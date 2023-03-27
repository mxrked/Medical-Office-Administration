
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, VARCHAR, Date, Time, ForeignKey, Numeric, NVARCHAR, Float, NCHAR

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

    AppointmentType= relationship("AppointmentType", backref="AppointmentType")
    Patient = relationship("Patient", backref="Patient")
    Employee = relationship("Employee", backref="Employee")
    HospitalLocation = relationship("HospitalLocation", backref="HospitalLocation")

    def __str__(self) -> str:
        return f"Appointment on {self.ApptDate} at {self.ApptTime} for {self.Patient.FirstName} {self.Patient.LastName}"

class AppointmentType(Base):
    __tablename__ = "AppointmentType"

    ApptTypeID = Column(Integer, primary_key=True, nullable=False)

    ApptName = Column(VARCHAR(50))
    ApptLength = Column(Numeric(18, 0))

    def __str__(self) -> str:
        return f"{self.ApptName}"

class EmpUserRoleCross(Base):
    __tablename__ = "EmpUserRoleCross"

    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    RoleID = Column(Integer, ForeignKey("Role.RoleID"))   # Check later for table name change
    DepartmentID = Column(Integer, ForeignKey("Departments.DepartmentID"))
    OfficeID = Column(Integer, ForeignKey("Offices.OfficeID"))

    Employee = relationship("Employee", backref="Employee")
    Role = relationship("Role", backref="Role")
    Department = relationship("Department", backref="Department")
    Office = relationship("Offices", backref="Offices")

class EmpGroupCross(Base):
    __tablename__ = "EmpGroupCross"

    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID"))
    GroupID = Column(Integer, ForeignKey("Group.GroupID"))

    Employee = relationship("Employee", backref="Employee")
    Group = relationship("Group", backref="Group")

class EmpLocReferralCross(Base):
    __tablename__ = "EmpLocReferralCross"

    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID "))
    LocationID = Column(Integer, ForeignKey("Location.LocationID"))
    ReferralID = Column(Integer, ForeignKey("Referral.ReferralID"))

    Employee = relationship("Employee", backref="Employee")
    Location = relationship("Location", backref="Location")
    Referral = relationship("Referral", backref="Referral")

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

    EmployeeType = relationship("EmployeeType", backref="EmployeeType")

class EmployeeCredintials(Base):
    __tablename__ = "EmployeeCredintials"

    EmployeeID = Column(Integer, ForeignKey("Employee.EmployeeID")) # Child
    Title = Column(NCHAR(10), nullable=True)
    Status = Column(NCHAR(10))
    StartDate = Column(Date)
    EndDate = Column(Date, nullable=True)
    Length = Column(NCHAR(10), nullable=True)
    State = Column(NCHAR(10), nullable=True)
    Renewel = Column(NCHAR(10))

    Employee = relationship("Employee", backref="EmployeeCredintials")

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

