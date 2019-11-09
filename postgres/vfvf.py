class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_salary(self):
        print("Salary is unknown")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def show_salary(self):
        print("Salary is", self.salary)