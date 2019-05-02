class Event(list):
    """
    Event is smth (e.g. person gets ill or employee gets fired) that happens
    and doctor, mother, HR (subscribers) want to get notification when this happens.
    __call__ calls list of funcs the event happens.
    For every item (subscriber) inside this event we call that subscriber.
    """
    def __call__(self, *args, **kwargs):
        for item in self:
            print(f'Subscriber func {item.__name__}() is about to be called...')
            item(*args, **kwargs)  # (self.name, self.address) from self.falls_ill get passed here


class Person:
    """Observable"""
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # e.g. Doctor class can subscribe to this event and get notified when person falls ill
        self.falls_ill = Event()

    def catch_a_cold(self):
        print(f'{self.name} got sick..')
        self.falls_ill(self.name, self.address)


class Employee:
    """Observable"""
    def __init__(self, name, position):
        self.name = name
        self.position = position
        # e.g. HR class can subscribe to this event and get notified when person is fired
        self.get_fired = Event()

    def is_fired(self):
        print(f'{self.name} employed as {self.position} got fired...')
        self.get_fired(self.name, self.position)


# observer or subscriber: watching person
def call_doctor(name, address):  # doctor wants to be notified.
    print(f'A doctor has been called to cure {name} at {address}')


# observer or subscriber: watching person
def call_mother(name, address):  # mother wants to be notified.
    print(f'A mother has been called to come to {name} at {address}')


# observer or subscriber: watching employee
def call_hr(name, position):  # hr wants to be notified.
    print(f'HR has been called to hire {name} as {position}')


if __name__ == '__main__':
    person = Person('Sherlock', '221B Baker St')
    employee = Employee('John', 'developer')

    person.falls_ill.append(call_doctor)  # adding subscriber to listen to catch_a_cold event
    person.falls_ill.append(call_mother)  # adding subscriber to listen to catch_a_cold event
    person.catch_a_cold()  # fire event catch_a_cold
    # Sherlock got sick..
    # Subscriber func call_doctor() is about to be called...
    # A doctor has been called to cure Sherlock at 221B Baker St
    # Subscriber func call_mother() is about to be called...
    # A mother has been called to come to Sherlock at 221B Baker St

    employee.get_fired.append(call_hr)  # adding subscriber to listen to is_fired event
    employee.is_fired()  # fire is_fired event
    print('--------')
    # John employed as developer got fired...
    # Subscriber func call_hr() is about to be called...
    # HR has been called to hire John as developer

    employee.get_fired.remove(call_hr)  # hr unsubscribes from getting notifications
    employee.is_fired()
    # John employed as developer got fired...





