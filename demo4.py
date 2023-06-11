#Self adjusting widgets in Tkinter
'''
The Self Adjusting Widgets will enable our widgets to adjust with themselves with the size of the windows. We use the 
'fill' function which we pass it in the '.pack()' to make this possible. X denotes width and Y denotes height/length.
Check  the example below...g
'''
from tkinter import *

Window = Tk()

Label1 = Label(Window, text="Fast X", bg="Blue")
Label1.pack(fill=X)
Label2 = Label(Window, text="Furious X", bg="Red")
Label2.pack(side=LEFT, fill=Y)  #The 'side=' aligns it to the left side of the window...

Window.mainloop()