# Infosys wnat to build a HR system. They need to save employee details like name, age, salary, email and department. They also want to calculate the annual salary of each employee.


# 1st approach 
emp1_first = "Abhavya"
emp1_last = "Singh"
emp1_email = "abhavya.singh@infosys.com"
emp1_pay = 50000

emp2_first = "Aradhya"
emp2_last = "Singh"
emp2_email = "aradhya.singh@infosys.com"
emp2_pay = 60000


# what is there are 20000+ employees? It will be very difficult to manage all the employee details. So we can use functions to manage the employee details.


def employee_details(first, last, pay):
    email =  f"{first.lower()}.{last.lower()}@infosys.com"
    return {"First Name": first, "Last Name": last, "Email": email, "Salary": pay}


emp1 = employee_details("Abhavya", "Singh", 50000)
emp2 = employee_details("Aradhya", "Singh", 60000)
print(emp1 ,"\n", emp2)

def pay_raise(emp, percentage):
    emp["Salary"] = int(emp["Salary"] * (1+percentage/100))
    return emp


pay_raise(emp2, 4)
print(employee_details("Aradhya", "Singh", emp2["Salary"]))


#  these functions and  data are disconnected. So we can use classes to manage the employee details and functions together.

class Employee:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = f"{first.lower()}.{last.lower()}@infosys.com"

    def get_full_name(self):
        return f"{self.first} {self.last}"

    def pay_raise(self, percentage):
        self.pay = int(self.pay * (1 + percentage / 100))
        return self

    

    
emp1 = Employee("Abhavya", "Singh", 50000)
emp2 = Employee("Aradhya", "Singh", 60000)

print(emp1.first, emp1.last)
print(emp2.email)
print(emp1.pay)

#  Instance :- Whenver we create an object of a class, it is called an instance of that class. In the above example, emp1 and emp2 are instances of the Employee class.
#  Each instance has its own copy of the attributes defined in the class. In the above example, emp1 and emp2 have their own copies of first, last, pay and email attributes.
#  changine one does not affect the other. For example, if we change the pay of emp1, it will not affect the pay of emp2. 

emp1.pay = 70000
print(emp1.pay)
print(emp2.pay)


#  To look all the details and attributes of an instance, we can use the __dict__ attribute. It will return a dictionary containing all the attributes and their values of the instance.
print(emp1.__dict__)


print(emp1.get_full_name())
print(emp1.pay)
print(emp1.pay_raise(10).pay)  # we can also chain the methods. It will return the instance itself after applying the pay raise. So we can call the pay attribute of the instance after applying the pay raise.

