from tkinter import *
# now we don't need to prefix methods with tkinter.method_name() with * import

window = Tk()


def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


b1 = Button(window, text="Execute", command=km_to_miles)
# position your button
b1.grid(row=0, column=0)

e1_value = StringVar()
# text field widget
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# text widget
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()

