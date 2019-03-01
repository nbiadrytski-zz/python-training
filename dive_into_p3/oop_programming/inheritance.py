class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, student_type, *args, **kwargs):
        """
        A common convention is to add the specific parameters for each subclass to the beginning of the parameter list,
        and define all the other parameters using *args and **kwargs –
        then the subclass doesn’t need to know the details about the parent class’s parameters.
        """
        self.student_type = student_type
        self.classes = []
        super(Student, self).__init__(*args, **kwargs)

    def enroll(self, course):
        self.classes.append(course)


class StaffMember(Person):
    PERMANENT, TEMPORARY = range(2)

    def __init__(self, employment_type, *args, **kwargs):
        self.employment_type = employment_type
        super(StaffMember, self).__init__(*args, **kwargs)


class Lecturer(StaffMember):
    def __init__(self, *args, **kwargs):
        self.courses_taught = []
        super(Lecturer, self).__init__(*args, **kwargs)

    def assign_teaching(self, course):
        self.courses_taught.append(course)


jane = Student(Student.POSTGRADUATE, 'Jane', 'Smith', 'Number1')
jane.enroll('Math Course')
print(jane.classes)  # ['Math Course']

bob = Lecturer(StaffMember.PERMANENT, 'Bob', 'Jones', 'Number2')
bob.assign_teaching('Language Course')
print(bob.courses_taught)  # ['Language Course']
print(bob.name)  # Bob
