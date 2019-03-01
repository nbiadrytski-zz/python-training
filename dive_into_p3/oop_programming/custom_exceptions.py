class DuplicateUsernameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class UnderageError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f'{self.username} {self.email}'


example_list = [
    ("jane", "jane@example.com", 21),
    ("bob", "bob@example", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@somewhere", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]

directory = {}

for username, email, age in example_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()
        email_parts = email.split('@')
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise InvalidEmailError()

    except DuplicateUsernameError:
            print(f'Username {username} is in use.')
    except InvalidAgeError:
        print(f'Invalid age: {age}')
    except UnderageError:
        print(f'User {username} is underage.')
    except InvalidEmailError:
        print(f'{email} is not a valid email address.')

    else:
        directory[username] = User(username, email)
