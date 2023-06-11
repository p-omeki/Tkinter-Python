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

Entry1 = Entry(Window)
Entry2 = Entry(Window)
Window.mainloop()