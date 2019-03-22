class Class:
    def __del__(self):  # runs right before object deletion
        print('deleted!!!')


c1 = Class()
c2 = Class()


c1.this_is_ref = c2
c2.this_is_ref = c1

del c1, c2

import gc
print(f'THRESHOLD -->: {gc.get_threshold()}')  # (700, 10, 10)
gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)
gc.collect()
print(f'IN GARBAGE NOW: {gc.garbage}')  # список объектов которые попали в мусор

# gc: collecting generation 2...
# IN GARBAGE NOW: [<__main__.Class object at 0x10b8ab7f0>, <__main__.Class object at 0x10b8bd358>,
# {'this_is_ref': <__main__.Class object at 0x10b8bd358>}, {'this_is_ref': <__main__.Class object at 0x10b8ab7f0>}]
# gc: objects in each generation: 370 1516 4873
# gc: done, 4 unreachable, 0 uncollectable, 0.0017s elapsed
#
# gc: collecting generation 2...
# gc: objects in each generation: 1 0 6634
# gc: done, 0.0011s elapsed
#
# gc: collecting generation 2...
# gc: objects in each generation: 122 0 6416
# gc: done, 2731 unreachable, 0 uncollectable, 0.0151s elapsed
#
# gc: collecting generation 2...
# gc: objects in each generation: 0 0 6219
# gc: done, 119 unreachable, 0 uncollectable, 0.0025s elapsed