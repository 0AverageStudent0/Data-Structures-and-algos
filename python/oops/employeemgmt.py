#Create a base Employee class and derived classes like Manager and Developer with different salary calculation logic.
class Employee:
    def __init__(self,emp_name,emp_id,emp_mail,base_salary,):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_mail = emp_mail
        self.base_salary = base_salary

    def emp_details(self):
        print(f"employee name = {self.emp_name}")
        print(f"employee id = {self.emp_id}")
        print(f"employee mail = {self.emp_mail}")

class Manager(Employee):
    def salary(self,bonus):
        self.base_salary += bonus
        print(f"manager {self.emp_name} salary is ₹{self.base_salary}")

class Developer(Employee):
    def salary(self,pay_perhour,worked_hours):
        self.base_salary += (pay_perhour*worked_hours)
        print(f"Developers {self.emp_name} salary is {self.base_salary}")


m1 = Manager("pandu",12324,"pandu@gmail.com",120000)
m1.emp_details()
m1.salary(20000)