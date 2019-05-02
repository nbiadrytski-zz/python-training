from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()

    def on(self):  # when called we end up in on(self, switch) from OffState
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print('Light is already on')

    def off(self, switch):
        print('Light is already off')


class OnState(State):
    def __init__(self):
        print('Light turned on')

    def off(self, switch):
        print('Turning light off...')
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print('Light turned off')

    def on(self, switch):
        print('Turning light on...')
        switch.state = OnState()


if __name__ == '__main__':
    # 1. Switch()'s __init__is called which makes self.state an object of type OffState()
    # 2. Then OffState's __init__ is called which prints prints:
    # Light turned off
    sw = Switch()
    # 3. Switch's on() is called which makes self.state to call on() from OffState which prints
    # Turning light on...
    # 4. and makes switch.state object of type OnState()
    # 5. Therefore OnState()'s __init__ is called which prints:
    # Light turned on
    sw.on()
    # 6. self.state is now of OnState(), that's why when sw.off() it calls OnState()'s off() which prints:
    # Turning light off...
    # 7. and makes switch.state object of type OffState()
    # 8. Since switch.state is now OffState()'s object, then OffState()'s __init__ is called which prints:
    # Light turned off
    sw.off()
