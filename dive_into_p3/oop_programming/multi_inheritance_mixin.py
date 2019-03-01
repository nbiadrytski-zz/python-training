class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class LearnerMixin:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class TeacherMixin:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Tutor(Person, LearnerMixin, TeacherMixin):
    classes = []
    courses_taught = []

    def __init__(self, *args, **kwargs):
        super(Tutor, self).__init__(*args, **kwargs)


jane = Tutor("Jane", "Smith", "SMTJNX045")
jane.enrol('Math Course')
jane.assign_teaching('Lang Course')

print(jane.classes)
print(jane.courses_taught)