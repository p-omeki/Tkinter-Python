#Frames in Tkinter
'''
Frames are containers used to group and organize other widgets, essentially 'rectangular' regions within a window
where you can place other GUI like buttons, entry fields and more.
Check the example below, we are going to create a simple "Click Here" frame button...
'''
from tkinter import *

Window = Tk()   #Marks the start of our Tkinter
Window.geometry("300x200") #Sets the size of our Window

NewFrame = Frame(Window)
NewFrame.pack()

Button1 = Button(NewFrame, text="Click Here", fg="Blue")
Button1.pack(side=BOTTOM)

Window.mainloop() #Marks the end of our Tkinter