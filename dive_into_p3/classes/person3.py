import datetime


class Person3:
    def __init__(self, name, surname, birthdate, address, phone, email):  # params passed to __init__ method
        self.name = name  # attribute
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.phone = phone
        self.email = email

    # whenever we call a method on an object,
    # the object itself is automatically passed in as the first parameter (self)
    def get_age(self):  # instance method
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age


person = Person3(  # # person is an instance of Person3 class
    'Jane',
    'Doe',
    datetime.date(1986, 3, 31),
    'Minsk, Nezavisimosti pr-t, 165-2',
    '333 45 87',
    'jane.doe@mail.com'
)

print(person.name)
print(person.email)
print(person.get_age())

for key in ["a", "b", "c"]:
    print(mydict[key])