# Single Responsibility:
# A class should have just one responsibility: either cooking, or washing, but not both.
# Do not overload your objects with too many responsibilities


class Journal:
    """Keeps entries"""
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP --> Journal now not only stores, but also saves to file / loads entries
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class SaveManager:
    """Saves entries to file"""

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}\n')

p = SaveManager()
p.save_to_file(j, 'journal.txt')

# verify!
with open('journal.txt') as f:
    print(f.read())
