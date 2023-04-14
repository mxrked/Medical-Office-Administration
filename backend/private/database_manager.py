import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from backend.models import Base
from backend.connection_string import DB
from backend.models import *
from datetime import time, date

engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}")
Session = sessionmaker(bind=engine)
session = Session()


def create_database():
    engine = sa.create_engine(f"mssql+pyodbc:///?odbc_connect={DB}")
    Base.metadata.create_all(engine)


def populate_location(session):
    

    loc1 = Location(
        Location_Name="Kernersville Practice Center",
        Address_1="2728 Aaron Place Lane",
        Address_2="Space H4",
        City="Kernersville",
        State="NC",
        ZipCode="27285",
        Phone="985-275-99",
        Email="Kernersvillepractice@hospital.com"
    )

    loc2 = Location(
        Location_Name="WinstonSalem Practice Center",
        Address_1="2334 Northwest Blvd",
        Address_2="Suite A 123",
        City="Winston-Salem",
        State="NC",
        ZipCode="27040",
        Phone="336-618-57",
        Email="WinstonSalempractice@hospital.com"
    )

    loc3 = Location(
        Location_Name="MountAiry Practice Center",
        Address_1="8312 Rockford Street",
        Address_2="Suite 145",
        City="Mount Airy",
        State="NC",
        ZipCode="27030",
        Phone="919-684-45",
        Email="MountAirypractice@hospital.com"
    )
    
    
    session.add(loc1)
    session.add(loc2)
    session.add(loc3)

    session.commit()

def populate_lab(session):

    labs_list = labs_list = ["Hematology Tests", 
                             "Electrolytes Tests",
                             "Blood Chemistry Tests",
                             "Microbiology Tests",
                             "Urinalysis",
                             "Toxicology Tests",
                             "Endocrinology Tests",
                             "Pathology Tests",
                             "Infectious Disease Tests",
                             "Respiratory Tests",
                             "Oncology Tests",
                             "Allergy Testing Tests",
                             "Cardiac Markers",
                             "Gynecology Tests",
                             "Rheumatology Tests"]

    for lab_test in labs_list:
        
        lab_to_add = Lab(LabTest=lab_test)

        session.add(lab_to_add)


    session.commit()    

def populate_user_type(session):

    session.add(
        UserType(UserType="Employee")
    )
    session.add(
        UserType(UserType="Patient")
    )
    session.commit()

def populate_employee_type(session):

    job_titles = ['Doctors',
                  'Physician Assistant',
                  'Nurse Practitioner',
                  'Nurse',
                  'CNA I',
                  'CNA II',
                  'Practice Manager',
                  'Office Manager',
                  'Billing Manager',
                  'Purchasing Manager',
                  'Patient Care Manager',
                  'Reception/Registration',
                  'Billing/Insurance',
                  'Human Resources',
                  'Office Administration',
                  'Purchasing Specialists',
                  'Medical Coder',
                  'Medical Records Clerk',
                  'Medical Transcriptionist']
    
    for t in job_titles:
        session.add(
            EmployeeType(Type=t)
        )
    
    session.commit()

def populate_hours(session):

    list_of_hours = []

    days_mon_fri = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    location_1 = session.query(Location).filter_by(Location_Name="Kernersville Practice Center").first()
    location_2 = session.query(Location).filter_by(Location_Name="WinstonSalem Practice Center").first()
    location_3 = session.query(Location).filter_by(Location_Name="MountAiry Practice Center").first()

        # Location 1
    session.add( HospitalHours(
            LocationID=location_1.LocationID,
            WeekNumber=None,
            DayOfWeek="Sunday",
            OpenTime=None,
            CloseTime=None,
            Location = location_1
        )
    )

    
    
    for day in days_mon_fri:
        session.add( HospitalHours(
            LocationID=location_1.LocationID,
            WeekNumber=None,
            DayOfWeek= day,
            OpenTime= time(8,0),
            CloseTime= time(17,0),
            Location = location_1
        )
    )
    
    session.add(
        HospitalHours(
            LocationID=location_1.LocationID,
            WeekNumber="1",
            DayOfWeek= "Saturday",
            OpenTime= None,
            CloseTime= None,
            Location = location_1
        )
    )

    session.add(
        HospitalHours(
            LocationID=location_1.LocationID,
            WeekNumber="2",
            DayOfWeek= "Saturday",
            OpenTime= time(8,0),
            CloseTime= time(12,0),
            Location = location_1
        )
    )

       # Location 2
    session.add( HospitalHours(
            LocationID=location_2.LocationID,
            WeekNumber=None,
            DayOfWeek="Sunday",
            OpenTime=None,
            CloseTime=None,
            Location = location_2
        )
    )

    for day in days_mon_fri:
        session.add( HospitalHours(
            LocationID=location_2.LocationID,
            WeekNumber=None,
            DayOfWeek= day,
            OpenTime= time(8,0),
            CloseTime= time(17,0),
            Location = location_2
        )
    )
        
    session.add(HospitalHours(
            LocationID=location_2.LocationID,
            WeekNumber="1",
            DayOfWeek= "Saturday",
            OpenTime= time(8,0),
            CloseTime= time(12,0),
            Location = location_2
        )
    )

    session.add(HospitalHours(
            LocationID=location_2.LocationID,
            WeekNumber="2",
            DayOfWeek= "Saturday",
            OpenTime= None,
            CloseTime= None,
            Location = location_2
        )
    )

        # Location 3
    session.add( HospitalHours(
            LocationID=location_3.LocationID,
            WeekNumber=None,
            DayOfWeek="Sunday",
            OpenTime=None,
            CloseTime=None,
            Location = location_3
        )
    )

    for day in days_mon_fri:
        session.add( HospitalHours(
            LocationID=location_3.LocationID,
            WeekNumber=None,
            DayOfWeek= day,
            OpenTime= time(8,0),
            CloseTime= time(17,0),
            Location = location_3
        )
    )
        
    session.add(HospitalHours(
            LocationID=location_3.LocationID,
            WeekNumber=None,
            DayOfWeek= "Saturday",
            OpenTime= None,
            CloseTime= None,
            Location = location_3
        ))
        
    session.commit()

def populate_users(session):

    employee_user = session.query(UserType).filter_by(UserType="Employee").first()
    patient_user = session.query(UserType).filter_by(UserType="Patient").first()

    
    session.add( # Our Physician
        User(UserTypeID=employee_user.UserTypeID,
            UserName="nellie2005",
            Password="LipstickLeaveUniversity",
            Email="nellie2005@gmail.com",

            UserType = employee_user

        )
    )

    session.add( # Our Receptionist
        User(
            UserTypeID=employee_user.UserTypeID,
            UserName="saul1989",
            Password="eSeoc9Iequi",
            Email="saul1989@yahoo.com",

            UserType = employee_user
        )
    )

    session.add( # Our Patient
        User(
            UserTypeID=patient_user.UserTypeID,
            UserName="rashad1978",
            Password="Thabiex9eeSh",
            Email="rashad1978@gmail.com",

            UserType = patient_user
        )
    )

    session.add( # Our Admin
        User(
            UserTypeID=employee_user.UserTypeID,
            UserName="jazmyn_schmi",
            Password="zoo4wioxohX",
            Email="jazmyn_schmi@hotmail.com",

            UserType = employee_user
        )
    )
    
    session.commit()

def populate_employee(session):

    doctors = session.query(EmployeeType).filter_by(Type="Doctors").first()
    receptionist = session.query(EmployeeType).filter_by(Type="Reception/Registration").first()
    admin = session.query(EmployeeType).filter_by(Type="Office Manager").first()

    jennifer_user = session.query(User).filter_by(UserName="nellie2005").first() # physician

    william_user = session.query(User).filter_by(UserName="saul1989").first() # Receptionist

    admin_user = session.query(User).filter_by(UserName="jazmyn_schmi").first() # Admin

    # Physician
    session.add( Employee(
        Title="Dr.",
        Last_Name="Hall",
        FirstName="Jennifer",
        Address="395 Haymond Rocks Road",
        City="Winston-Salem",
        State="NC",
        ZipCode="27101",
        Phone="541-545-7294",
        Gender = "Female",
        EmployeeTypeID= doctors.EmployeeTypeID,
        Position= "General Practitioner",
        UserID= jennifer_user.UserID,
        Email="jazmyn_schmi@hotmail.com",

        EmployeeType=doctors,
        User=jennifer_user
    ))

    # Receptionist
    session.add( Employee(
            Title="Mr.",
            Last_Name="Fitzgerald",
            FirstName="William",
            Address="4850 Half and Half Drive",
            City="Winston-Salem",
            State="NC",
            ZipCode="27101",
            Phone="561-214-4575",
            Gender = "Male",
            EmployeeTypeID= receptionist.EmployeeTypeID,
            Position= "Receptionist/Registration",
            UserID= william_user.UserID,
            Email="saul1989@yahoo.com",

            EmployeeType=receptionist,
            User=william_user
        )
    )

    # Admin
    session.add( Employee(
            Title="Ms.",
            Last_Name="Cassey",
            FirstName="Brown",
            Address="3532 Gregory Lane",
            City="Winston-Salem",
            State="NC",
            ZipCode="27101",
            Phone="502-544-2469",
            Gender = "Female",
            EmployeeTypeID = admin.EmployeeTypeID,
            Position= "Admin",
            UserID= admin_user.UserID,
            Email="saul1989@yahoo.com",

            EmployeeType=admin,
            User=admin_user
        )
    )

    # Un Usered employees
    session.add(Employee(
        Title="Ms.",
        Last_Name="Bradford",
        FirstName="Daniell",
        Address="4868 Conifer Drive",
        City="Bellevue",
        State="WA",
        ZipCode="98004",
        Phone="425-467-7553",
        Gender = "Female",
        EmployeeTypeID = doctors.EmployeeTypeID,
        Position= "Admin",
        UserID=None,
        Email="timmothy1989@hotmail.com",

        EmployeeType=doctors,
        User=None
        )
    )

    session.commit()

    




if __name__ == "__main__":
    # Make sure its not already done!

    pass

session.close()
engine.dispose()

var = """
Sample Data ideas:

Employees
    1. A Scheduler
    2. A Physician
    3. A Scheduler & Physician

Users:
    1. A Scheduler (Emp 1)
    2. A Physican (Emp 2)
    3. A Scheduler & Physician (Emp 3)
    4. A Patient 

Employee Type:
    EmployeeTypeID	Type - Refer to Temp_EmployeeType
    1	Doctors
    2	Physician Assistant
    3	Nurse Practitioner
    4	Nurse
    5	CNA I
    6	CNA II
    7	Practice Manager
    8	Office Manager
    9	Billing Manager
    10	Purchasing Manager
    11	Patient Care Manager
    12	Reception/Registration
    13	Billing/Insurance
    14	Human Resources
    15	Office Administration
    16	Purchasing Specialists
    17	Medical Coder
    18	Medical Records Clerk
    19	Medical Transcriptionist

Appointment Type:
    ApptTypeID	ApptName
    T01	Primary Care Visit
    T02	Physical Exam
    T03	Follow-up Visit
    T04	Ear, Nose and Throat
    T05	Emergency Visit
    T06	Initial Visit
    T07	Women's Health/ Family Planning
    T08	Injections/Labs

RoleID	Role
    R01	Log into Employee System
    R02	Edit Make Referrals Tab/Edit Order Labs Tab
    R03	Edit Appointments Tab/Edit CheckIn Tab/Edit CheckO
    R04	Log into Patient Portal

LocationID	LocationName	Address 1	Address 2	City	State	ZipCode	Phone	Email
    HL01	Kernersville Practice Center	2728 Aaron Place Lane	Space H4	Kernersville	NC	-27285    	985-275-99     	Kernersvillepractice@hospital.com
    HL02	WinstonSalem Practice Center	2334 Northwest Blvd	Suite A 123	Winston-Salem	NC	-27040    	336-618-57     	WinstonSalempractice@hospital.com
    HL03	MountAiry Practice Center	8312 Rockford Street	Suite 145	Mount Airy	NC	-27030    	919-684-45     	MountAirypractice@hospital.com

Lab
    LabID	LabTest
    4001	Hematology Tests
    4002	Electrolytes Tests
    4003	Blood Chemistry Tests
    4004	Microbiology Tests
    4005	Urinalysis 
    4006	Toxicology Tests
    4007	Endocrinology Tests
    4008	Pathology Tests
    4009	Infectious Disease Tests
    4010	Respiratory Tests
    4011	Oncology Tests
    4012	Allergy Testing Tests
    4013	Cardiac Markers
    4014	Gynecology Tests
    4015	Rheumatology Tests

Lab Orders:


"""
