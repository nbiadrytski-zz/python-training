class Account:

    def __init__(self, filepath):
        # self.filepath is a new instance variable
        self.filepath = filepath
        with open(filepath, 'r') as file:
            # self - Account object, balance - instance variable
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""

    # class variable which is shared by all object instances: jacks_checking and johns_checking
    type = "checking"

    # constructor
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        # self.fee --> Checking instance variable
        self.fee = fee

    # class method
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jacks_checking = Checking("jack.txt", 1)
jacks_checking.transfer(100)
jacks_checking.commit()
print(jacks_checking.balance)
print(jacks_checking.type)

johns_checking = Checking("john.txt", 1)
johns_checking.transfer(100)
johns_checking.commit()
print(johns_checking.balance)
print(johns_checking.type)

print(johns_checking.__doc__)
