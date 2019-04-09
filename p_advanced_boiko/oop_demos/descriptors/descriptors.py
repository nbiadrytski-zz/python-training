class Celsius:  # descriptor: handles getting, setting attrs

    def __get__(self, instance, owner):  # instance Celsius, owner Temperature
        print('Celsius __get__')
        return 5 * (instance.fahrenheit + 32) / 9

    def __set__(self, instance, value):
        print('Celsius __set__')
        instance.fahrenheit = 32 + 9 * value / 5


class Temperature:  # class Temperature handles these attrs by calling getattribute, setattribute methods

    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f


t = Temperature(212)  # fahrenheit is now 212
print(t.fahrenheit)  # 212
print(t.celsius)  # __get__ is called; 5 * (celsius.212 + 32) / 9 = 135.55555555555554

t.celsius = 0  # Celsius __set__; fahrenheit = 32 + 9 * 0 / 5 = 32
print(t.celsius)  # __get__ is called; 5 * (celsius.32 + 32) / 9 = 35.55555555555556
print(t.fahrenheit)  # 32.0
