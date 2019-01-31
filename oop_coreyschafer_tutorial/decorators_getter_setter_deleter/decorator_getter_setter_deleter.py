class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # email() is defined as method, but with @property decorator
    # we can access it as attribute, so
    # emp_1.email is a valid call
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Terry"
emp_1.fullname = "Jim T"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)
