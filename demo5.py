#Handling button click
"""
In handling button click, we basically define what we want our button to do once we click it. This is made possible by
having a function defined and calling that function onto 'command=' when we define our label.
Check the example below...
"""
from tkinter import *
Window = Tk()

def on_button_click():
    print("Hey, you've just clicked a button") #The output will be printed out as many times as possible, so long as we
                                                 ##keep on clicking the 'Click Here' button
#We define the button
Button1 = Button(Window, text="Click Here", command=on_button_click)
Button1.pack()

Window.mainloop()