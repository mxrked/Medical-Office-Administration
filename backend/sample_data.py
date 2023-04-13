"""
Used for loading up sample ORM for testing.
We shouldn't be using any db calls
"""
from backend.models import Appointment, User, EmployeeType, Patient, Employee, AppointmentType, Location
from datetime import date, time


emp_type = EmployeeType(
    Type = "Type"
)

emp_user = User(
    UserTypeID=1,
    UserName="UserName",
    Password="Password",
    Email="Email@bob.com"
)


appt_type = AppointmentType(
    ApptName="Appt Name"
)


starting_loc = Location(
    LocationID=1,
    Location_Name="Winston-Salem",
    Address_1="Address 1",
    Address_2="Address 2",
    City="City",
    State="North Carolina",
    ZipCode="12345",
    Phone="336-775-0047",
    Email="bob@bob.com"
)

starting_patient = Patient(
    Last_Name="Weeks",
    First_Name="Jessca",
    Address="Address",
    City="Winston-Salem",
    State="North Carolina",
    ZipCode="27101",
    Gender="Female",
    DateOfBirth=date(2000,2,17),
    Race="White",
    Phone="Phone",
    Email = "Email"
)

starting_employee = Employee(
            Title="Mr.",
            Last_Name="Doe",
            FirstName="John",
            Address="123 Main St.",
            City="Seattle",
            State="WA",
            ZipCode="98101",
            Phone="555-555-1212",
            Gender="Male",
            EmployeeTypeID=1,
            Position="Manager",
            UserID=1,
            Email="johndoe@example.com",

            User=emp_user,
            EmployeeType=emp_type

)

other_employee = Employee(
            Title="Misses.",
            Last_Name="Jane",
            FirstName="John",
            Address="123 Main St.",
            City="Seattle",
            State="WA",
            ZipCode="98101",
            Phone="555-555-1212",
            Gender="Male",
            EmployeeTypeID=1,
            Position="Owner",
            UserID=1,
            Email="johndoe@example.com",

            User=emp_user,
            EmployeeType=emp_type

)


appointments = []
employees = [other_employee,other_employee]
locations = []

test_appt = Appointment(
    ApptDate=date(2000,2,10),
    ApptTime=time(10,00),
    PatientID=1,
    ApptStatus="Scheduled",
    ApptLength=15,
    PhysicianID=1,
    ApptTypeID=1,
    LocationID=1,
    ApptReason="Test Appointment",

    Patient=starting_patient,
    Employee=starting_employee,
    AppointmentType=appt_type,
    Location=starting_loc,
    )

for i in range(10):
    appointments.append(
        test_appt
    )
    employees.append(
        starting_employee
    )
    locations.append(
        starting_loc
    )

