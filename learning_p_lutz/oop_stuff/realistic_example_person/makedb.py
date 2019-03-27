from learning_p_lutz.oop_stuff.realistic_example_person.person import Person, Manager
import shelve


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):  # Use object's name attr as key
    db[obj.name] = obj  # Store object on shelve by key
db.close()