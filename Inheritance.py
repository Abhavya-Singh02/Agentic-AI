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

    def pay_raise(self):
        self.pay = int(self.pay * (1 + self.raise_percentage / 100)) # this has one issue because this pay raise percentage is same for all 
        # the employees.



# Developers - everything an employee has, plus a programming language they know. So, we can create a new class Developer which will inherit 
# the Employee class and will have an additional attribute programming language.

# Managers - everything an employee has, plus a list of employees they manage. So, we can create a new class Manager which will inherit the
# Employee class and will have an additional attribute list of employees they manage.


class Developer(Employee): # Inheritance - Now every developer is an employee, so we can use inheritance to create a new class Developer 
    # which will inherit the Employee class and will have an additional attribute programming language.
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # calling the constructor of the parent class Employee to initialize the attributes of the 
        # parent class.
        self.prog_lang = prog_lang # initializing the additional attribute programming language for the Developer class.

dev1 = Developer("Abhavya", "Singh", 50000, "Python")
print(dev1.first, dev1.last, dev1.pay, dev1.email, dev1.prog_lang) # accessing the attributes of the Developer class and the parent class Employee.



class Manager(Employee): # Inheritance - Now every manager is an employee, so we can use inheritance to create a new class Manager
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay) # calling the constructor of the parent class Employee to initialize the attributes of the 
        # parent class.
        if employees is None:
            self.employees = [] # initializing the additional attribute list of employees for the Manager class.
        else:
            self.employees = employees


    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp) # adding an employee to the list of employees managed by the manager.

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp) # removing an employee from the list of employees managed by the manager.

    def print_employees(self):
        for emp in self.employees:
            print("-->", emp.get_full_name()) # printing the full name of the employees managed by the manager.

# one more scenario :- Suppose infosys decides: when a manager gets a raise, all the employees under that manager will also get a small bonus
# too. The plan apply_raise() from employeee doesn't know anything about reports - it just bumps self.pay. so we can override the apply_raise()
#  method in the Manager class to add the bonus for the employees under that manager.
    def apply_raise(self):
        super().pay_raise() # calling the apply_raise() method of the parent class Employee to apply the raise for the manager.
        for emp in self.employees:
            emp.pay += 1000 # adding a bonus of 1000 to the pay of each employee under that manager.


dev2 = Developer("Aradhya", "Singh", 60000, "Java")
mgr1 = Manager("Amit", "Kumar", 80000, [dev1]) # creating a manager object and passing a list of employees managed by the manager.

print(f"Manager Name: - {mgr1.get_full_name()}") # accessing the attributes of the Manager class and the parent class Employee.
mgr1.add_employee(dev2) # adding an employee to the list of employees managed by the manager.
mgr1.print_employees() # printing the full name of the employees managed by the manager.


mgr1.remove_employee(dev1) # removing an employee from the list of employees managed by the manager.
mgr1.print_employees() # printing the full name of the employees managed by the manager.



print('Before Raise')
print(f"Manager Name: - {mgr1.get_full_name()} and Salary: - {mgr1.pay}")
print(f"Employee Name: - {dev2.get_full_name()} and Salary: - {dev2.pay}")  

print('After Raise')
mgr1.apply_raise() # applying the raise for the manager and the employees under that manager.
print(f"Manager Name: - {mgr1.get_full_name()} and Salary: - {mgr1.pay}")
print(f"Employee Name: - {dev2.get_full_name()} and Salary  : - {dev2.pay}")        




    