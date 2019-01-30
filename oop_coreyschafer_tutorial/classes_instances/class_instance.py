import datetime


# https://www.youtube.com/watch?v=3ohzBxoFHAY&index=5&list=PL8VJNbyU7HbdQNbzrodhFd6pKHZkUgJzL
class Employee:

    num_of_emps = 0  # class var, incremented in __init__ constructor
    raise_amount = 1.04  # class var; shared across instances

    def __init__(self, first, last, pay):  # instance vars
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    @classmethod  # alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @classmethod  # using class_name.method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def fullname(self):  # instance method using instance_name.method
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):  # instance method
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    # sum up employees' salaries
    def __add__(self, other):
        return self.pay + other.pay

    # return number of chars in fullname
    def __len__(self):
        return len(self.fullname())


class Developer(Employee):

    raise_amount = 1.10  # overriding from Employee

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("N", "B", 50000, "Python")  # create Employee using __init__ constructor
dev_2 = Developer("Test", "User", 60000, "Developer")
dev_str_3 = Employee.from_string("John-Doe-70000")  # create Employee using class method

mgr_1 = Manager("Sue", "Somelastname", 90000, [dev_1])

# print(help(Developer))

print("Dev 1 email: " + dev_1.email)
print("Dev 2 email: " + dev_2.email)
print("Dev 3 email: " + dev_str_3.email)

print("Dev 1 salary: ", dev_1.pay)
dev_1.apply_raise()
print("Dev 1 salary after raise: ", dev_1.pay)

my_date = datetime.date(2019, 1, 29)
print("Is this a workday? ", Employee.is_workday(my_date))
print("=" * 30)

print("mgr_1 email: ", mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()
print("=" * 30)

print("Is mgr_1 a Manager? ", isinstance(mgr_1, Manager))
print("Is mgr_1 an Employee? ", isinstance(mgr_1, Employee))
print("Is mgr_1 a Developer? ", isinstance(mgr_1, Developer))
print("=" * 30)

print("Is Developer a subclass of Employee? ", issubclass(Developer, Employee))
print("=" * 30)

emp_1 = Employee("Kaly", "Henson", 600)
emp_2 = Employee("Stacy", "Jameson", 700)
print("printing emp_1 object using __repr__ method: ", repr(emp_1))  # printing emp_1 object using __repr__ method
print("printing emp_1 object using __str__ method: ", str(emp_1))  # printing emp_1 object using __str__ method
# Same as
print(emp_1.__repr__())
print(emp_1.__str__())
print("=" * 30)

print("emp_1 + emp_2 salaries summed: ", emp_1 + emp_2)
print("=" * 30)

print("number of chars in emp_1 fullname: ", len(emp_1))


