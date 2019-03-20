letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def filter_vowels(letter):
    vowels = ['a', 'e', 'i']
    if letter in vowels:
        return True


filtered_vowels = filter(filter_vowels, letters)
for item in filtered_vowels:
    print(item)