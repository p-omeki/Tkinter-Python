#Grid Layout in Tkinter
'''
The Grid Layout allows you to create a grid-like arrangement of widgets within a frame or window.
Grid layout allows you to specify the row and column position of each widget to control their placement.
'''
from tkinter import *
Window = Tk()
Window.geometry("300x200")

Label1 = Label(Window, text="First Name:")
Label2 = Label(Window, text="Second Name:")

Entry1 = Entry(Window) #The 'Entry' will act as our 'input', it will accepts values. Only applicable in Tkinter
Entry2 = Entry(Window)

Label1.grid(row=0, column=0)
Label2.grid(row=1, column=0)

Entry1.grid(row=0, column=1)
Entry2.grid(row=1, column=1)

Window.mainloop()
#Notice we don't have the '.pack()' in grid layout?