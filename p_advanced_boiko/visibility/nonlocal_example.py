def tester(start):
    state = start

    def nested(lable):
        nonlocal state
        print(lable, state)
        state += 1  # we can change var state from parent def due to nonlocal
    return nested


f = tester(0)
f('Dan0')  # Dan0 0
f('Dan1')  # Dan 1 1

g = tester(10)
g('Liza0')  # Liza0 10
g('Liza1')  # Liza1 11

f('Dan2')  # Dan2 2
