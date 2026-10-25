# ==================================================Classmethods and Staticmethods in Python============================================================

class Employee:
    raise_percentage = 4  # class variable to define the pay raise percentage for all the employees
    num_employees = 0  # class variable to keep track of the number of employees
    company_name = "Infosys"  # class variable to define the company name for all the employees

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@infosys.com"
        Employee.num_employees += 1  # incrementing the count of employees whenever a new employee object is created

    def get_full_name(self):
        return f"{self.first} {self.last}"

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_percentage / 100)

    @classmethod
    def set_raise_percentage(cls, percentage):
        cls.raise_percentage = percentage  # setting the raise percentage for the class variable

    # def set_raise_percentage(self, percentage):
    #     self.raise_percentage = percentage  # setting the raise percentage for the specific employee object

    @classmethod
    def get_count(cls):
        return cls.num_employees  # returning the total number of employees created so far

    @staticmethod
    def is_working(day):
        return day.weekday() < 5  # checking if the current day is a working day (Monday to Friday)


# print(Employee.get_count()) # it will give an error because we are trying to access the class method using the class name. 
# We need to create an object of the class to access the class method.

print(Employee.get_count()) # it will give the total number of employees created so far. It wont throw an error because 
# we are accessing the class method using the class name.

emp1 = Employee("Abhavya", "Singh", 50000)
print(emp1.get_count()) # it will give the total number of employees created so far. It wont throw an error because 
# we are accessing the class method using the object of the class.

print(Employee.raise_percentage)
Employee.set_raise_percentage(10)  # setting the raise percentage for the class variable using the class method
print(Employee.raise_percentage)  # accessing the class variable using the class name
print(emp1.raise_percentage)  # accessing the class variable using the object of the class

emp2 = Employee("Aradhya", "Singh", 60000)
print(Employee.get_count()) # it will give the total number of employees created so far.

import datetime
my_date = datetime.date(2024, 4, 15) # A monday
weekend = datetime.date(2024, 4, 14) # A sunday

print(Employee.is_working(my_date)) # it will return True because 15th April 2024 is a Monday which is a working day.
print(Employee.is_working(weekend)) # it will return False because 14th April 2024 is a Sunday which is not a working day.


# Another exampple 

class StringHelper:
    @staticmethod
    def to_snake_case(text):
        return text.replace(" ","_").lower()

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email and "com" in email


print(StringHelper.to_snake_case("Hello World")) # it will return "hello_world"
print(StringHelper.validate_email("abhavya.singh@python.com")) # it will return True because it is a valid email address
