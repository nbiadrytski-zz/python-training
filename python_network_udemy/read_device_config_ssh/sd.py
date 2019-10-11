def check_relay_state(val):
    try:
        print('In try')
        if val == 1:
            print('in first if')
        elif val == 2:
            print('in else')
        else:
            raise ValueError('in value error')
    finally:
        print('in finally')


if __name__ == '__main__':
    check_relay_state(3)
