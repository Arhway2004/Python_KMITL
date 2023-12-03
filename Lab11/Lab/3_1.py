class Name:
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def setName(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return f"full name = {self.title} {self.firstName} {self.lastName}"

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def getDate(self):
        return f"{self.day}/{self.month}/{self.year}"  # e.g., 31/12/2010

    def getDateBC(self):
        return f"{self.day}/{self.month}/{self.year - 543}"

class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def setAddress(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def getAddress(self):
        return f"{self.houseNo}, {self.street}, "

class Department:
    def __init__(self, description, manager, employeelist):
        self.description = description
        self.manager = manager
        self.employeelist = employeelist

    def addEmployee(self, employee):
        self.employeelist.append(employee)
        employee.set_department(self)

    def deleteEmployee(self, employee):
        if employee in self.employeelist:
            self.employeelist.remove(employee)
            employee.set_department(None)

    def set_manager(self, employee):
        if employee.is_permanent_employee():
            self.manager = employee

    def printinfo(self):
        employee_names = [emp.name.getFullName() for emp in self.employeelist]
        manager_name = self.manager.name.getFullName() if self.manager else "None"
        print(f"employeelist:{self.employeelist}")
        print(f"Department Description: {self.description}")
        print(f"Manager: {manager_name}")
        print(f"Employees: {', '.join(employee_names)}")

class Person:
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address

    def printinfo(self):
        return f"Name: {self.name.getFullName()}, Birthdate: {self.birthdate.getDate()}, Address: {self.address.getAddress()}"

class Employee(Person):
    def __init__(self, startDate, department, name, birthdate, address):
        super().__init__(name, birthdate, address)
        self.startDate = startDate
        self.department = department

    def is_permanent_employee(self):
        return True 

    def printinfo(self):
        return super().printinfo() + f", Start Date: {self.startDate}, Department: {self.department.description}"

class TempEmployee(Employee):
    def __init__(self, wage, startDate, department, name, birthdate, address):
        super().__init__(startDate, department, name, birthdate, address)
        self.wage = wage

    def printinfo(self):
        return super().printinfo() + f", Wage: {self.wage}"

class PermEmployee(Employee):
    def __init__(self, salary, startDate, department, name, birthdate, address):
        super().__init__(startDate, department, name, birthdate, address)
        self.salary = salary

    def printinfo(self):
        return super().printinfo() + f", Salary: {self.salary}"


name = Name("Mr.", "John", "Doe")
birthdate = Date(1, 1, 1990)
address = Address("123 Main St", "Some Street", "Some District", "Some City", "Some Country", "12345")
employee = Employee("2023-10-03", Department("HR", None, []), name, birthdate, address)

print(employee.printinfo())

temp_employee = TempEmployee(20.0, "2023-10-04", Department("Finance", None, []), name, birthdate, address)
perm_employee = PermEmployee(50000, "2023-10-05", Department("Engineering", None, []), name, birthdate, address)

print(temp_employee.printinfo())
print(perm_employee.printinfo())

hr_department = Department("HR", None, [employee])
finance_department = Department("Finance", None, [temp_employee])
engineering_department = Department("Engineering", None, [perm_employee])
hr_department.set_manager(employee)
finance_department.set_manager(temp_employee)
engineering_department.set_manager(perm_employee)
