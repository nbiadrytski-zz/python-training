class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number
        self.learner = learner
        self.teacher = teacher


jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())

jane.learner.enrol('Math Course')
print(jane.learner.classes)  # ['Math Course']

jane.teacher.assign_teaching('Lang Course')
print(jane.teacher.courses_taught)  # ['Lang Course']


