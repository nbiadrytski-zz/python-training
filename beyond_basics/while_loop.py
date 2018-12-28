correct_password = "test"

name = input("Enter name: ")
surname = input("Enter surname: ")
password = input("Enter password: ")

while password != correct_password:
    password = input("Wrong password! Enter again: ")

message = "Hi {} {}, you are logged in".format(name, surname)
print(message)