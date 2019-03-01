class InspectObject:  # object is a parent class for each class

    def __init__(self, name, surname, salary=1000, bonus=200):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.bonus = bonus

    def fullname(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.name} {self.surname} is an object of {__class__}'

    def __add__(self, other):
        return self.salary + other.salary


obj = InspectObject("Jane", "Smith")
obj1 = InspectObject("Dan", "Brown")

print(dir(obj))  # attributes amd method available for obj

# object info is printed due to __str__ method
print(obj)  # Jane Smith is an object of <class '__main__.InspectObject'>

print(obj.__add__(obj1))  # 2000

# instance attributes of an object, with their names as keys
print(obj.__dict__)  # {'name': 'Jane', 'surname': 'Smith', 'salary': 1000, 'bonus': 200}
