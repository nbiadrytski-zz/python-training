class Employee:
    """Base class for all employees"""
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print(f'Total employees number: {self.emp_count}')

    def display_employee(self):
        print(f'Name: {self.name}, salary: {self.salary}')


emp1 = Employee('Master', 200)
emp2 = Employee('Slave', 100)

print(f'Total Employees: {Employee.emp_count}')

emp1.age = 7  # add age attribute
emp1.age = 10  # modify age attribute
del emp1.age  # delete age attribute

# check if object has attribute
print(hasattr(emp1, 'name'))  # True
print(hasattr(emp1, 'age'))  # False

# return value of attribute
print(getattr(emp1, 'name'))  # Master

# set attribute age at 11
setattr(emp2, 'age', 11)
print(getattr(emp2, 'age'))  # 11
# delete attribute
delattr(emp2, 'age')
print(hasattr(emp2, 'age'))  # False

