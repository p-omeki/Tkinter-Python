#Our First Hello World in Tkinter
'''
Tkinter is library in python that allows us to create graphical user interfaces, (GUI). With Tkinter you can create
windows, dialogs, buttons, menus, and other GUI components for your Python applications.
In the example below, we're going to create a simple GUI for windows with a display label/text "Hello World"
'''
from tkinter import *   ##What the '*' will do is that it will impoert all the tkinter functions in our code.

Window = Tk()  #We declare our object Window and assign it to class 'Tk()'

Window.geometry("300x200")

#We now create our label widget with the wording 'Hello World'
Label1 = Label(Window, text="Hello World")  #Inside the label, we pass object argument and text we want to be
                                               ## displayed in our GUI.
Label1.pack()  #The .pack() will add the parameter to the Window's tab

Window.mainloop() #The .mainloop will keep our GUI interface open until we close it and allow us perform operations.

