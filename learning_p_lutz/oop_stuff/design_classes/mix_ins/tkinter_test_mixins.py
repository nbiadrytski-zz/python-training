from learning_p_lutz.oop_stuff.design_classes.mix_ins.listinherited import ListInherited
from tkinter import Button


class MyButton(ListInherited, Button):  # Both classes have a __str__; ListTree first: use its __str__
    pass


B = MyButton(text='spam')
open('savetree.txt', 'w').write(str(B))  # save to file

print(B)