"""
In composition one of the classes is composed of one or more instance of other classes.
In other words one class is container and other class is content
and if you delete the container object then all of its contents objects are also deleted.
"""


class Salary:  # content
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:  # container
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annual_salary(self):
        return f'Total annual salary + bonus: {str(self.salary.get_total() + self.bonus)}'


emp = Employee(100, 10)
print(emp.annual_salary())
