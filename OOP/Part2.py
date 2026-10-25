# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first 
#         self.last = last
#         self.pay = pay
#         self.email = f"{first.lower()}.{last.lower()}@infosys.com"

#     def get_full_name(self):
#         return f"{self.first} {self.last}"

#     def pay_raise(self, percentage):
#         self.pay = int(self.pay * (1 + percentage / 100))

# emp1 = Employee("Abhavya", "Singh", 50000)
# print(emp1.__dict__)  # prints the attributes of emp1 object

# emp1.pya = 90000 # suppose a typo mistake is made while assigning the salary to emp1 object. So, it will create a new attribute pya 
# # in emp1 object instead of updating the pay attribute. And also It wont show any error. So, we need to be careful while assigning 
# # the values to the attributes of an object.

# print(emp1.__dict__)  # prints the attributes of emp1 object after the typo mistake

# employees = [Employee("Abhavya", "Singh", 50000), Employee("Aradhya", "Singh", 60000)]

# employees[0].department = "IT"  # adding a new attribute department to the first employee object in the list 

# for emp in employees:
#     print(emp.department)  # prints the department of each employee object in the list. It will print "IT" for the first employee and 
#     # will give an error for the second employee as it does not have the department attribute.

#  To avoid such errors, we can use __slots__ attribute in the class. It will restrict the attributes that can be added to the objects 
# of the class.

# we will write the same Employee class with __slots__ attribute to restrict the attributes that can be added to the objects of the class.


#  =============================================__slots__ attribute in the class========================================================

# class Employee:
#     __slots__ = ["first", "last", "pay", "email"]  # restricting the attributes that can be added to the objects of the class

#     def __init__(self, first, last, pay):
#         self.first = first 
#         self.last = last
#         self.pay = pay
#         self.email = f"{first.lower()}.{last.lower()}@infosys.com"

#     def get_full_name(self):
#         return f"{self.first} {self.last}"

#     def pay_raise(self, percentage):
#         self.pay = int(self.pay * (1 + percentage / 100)) # this has one issue because this pay raise percentage is same for all the employees. 
#         # So, we can use class variables to define the pay raise percentage for all the employees.

# emp1 = Employee("Abhavya", "Singh", 50000)
# emp1.department = "IT"  # trying to add a new attribute department to the emp1 object. It will give an error as department is not in 
# # the __slots__ attribute of the class.


# ==============================================class variables==========================================================


# class Employee:
#     raise_percentage = 4  # class variable to define the pay raise percentage for all the employees

#     def __init__(self, first, last, pay):
#         self.first = first 
#         self.last = last
#         self.pay = pay
#         self.email = f"{first.lower()}.{last.lower()}@infosys.com"

#     def get_full_name(self):
#         return f"{self.first} {self.last}"

#     def pay_raise(self, percentage):
#         self.pay = int(self.pay * (1 + self.raise_percentage / 100)) # this has one issue because this pay raise percentage is same for all the employees. 
#         # So, we can use class variables to define the pay raise percentage for all the employees.

# emp1 = Employee("Abhavya", "Singh", 50000)
# emp2 = Employee("Aradhya", "Singh", 60000)

# print(Employee.raise_percentage)  # accessing the class variable using the class name

# # Access through the object
# print(emp1.raise_percentage)  # accessing the class variable using the object of the class
# print(emp2.raise_percentage)  # accessing the class variable using the object of the class

# emp1.pay_raise(emp1.raise_percentage)  # calling the pay_raise method using the object of the class
# print(emp1.pay)  # prints the updated pay of emp1 object after the pay raise

# print(emp1.__dict__) # it wont show the class variable raise_percentage in the emp1 object as it is a class variable and not an 
# # instance variable.

# print(Employee.__dict__) # it will show the class variable raise_percentage in the Employee class as it is a class variable and not an
# # instance variable.


# # when we call the raise_percentage using the object of the class, it will first look for the instance variable in the object. 
# # If it does not find it, it will look for the class variable in the class. So, if we change the value of the class variable 
# # using the class name, it will change for all the objects of the class. But if we change the value of the class variable using 
# #  the object of the class, it will create a new instance variable in that object and will not affect the other objects of the class.

# emp1.raise_percentage = 10  # changing the value of the class variable using the object of the class. It will create a new instance 
# # variable in emp1 object.
# print(emp1.raise_percentage)  # accessing the class variable using the object of the class.
# emp1.pay_raise(emp1.raise_percentage)  # calling the pay_raise method using the object of the class. It will use the instance variable
# print(emp1.pay)  # prints the updated pay of emp1 object after the pay raise using the instance variable


# ==============================================Overriding class variables==========================================================

class Employee:
    raise_percentage = 4  # class variable to define the pay raise percentage for all the employees
    count = 0  # class variable to keep track of the number of employees

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@infosys.com"
        Employee.count += 1  # incrementing the count of employees whenever a new employee object is created

    def get_full_name(self):
        return f"{self.first} {self.last}"

    def pay_raise(self, percentage):
        self.pay = int(self.pay * (1 + self.raise_percentage / 100)) # this has one issue because this pay raise percentage is same for all the employees. 
        # So, we can use class variables to define the pay raise percentage for all the employees.

emp1 = Employee("Abhavya", "Singh", 50000)
emp2 = Employee("Aradhya", "Singh", 60000)

# what if i want to change the value of raise_percentage, maybe 1.07. SO I can directly change from the class value itself. 

Employee.raise_percentage = 1.07
print(Employee.raise_percentage)  # accessing the class variable using the class name
print(emp1.raise_percentage)  # accessing the class variable using the object of the class
print(emp2.raise_percentage)  # accessing the class variable using the object of the class

# we are changing the value of raise_percentage at the root/class level. So, it will change for all the objects of the class. 

#  But what if I want to change the value of raise_percentage for only emp1 object. So, I can override the class variable for that object only.

emp1.raise_percentage = 1.08
print(emp1.raise_percentage)  # accessing the instance variable using the object of the class

