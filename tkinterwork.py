from tkinter import *
import file_read

root = Tk()
file = 'eurovision.txt'

#Creating a Label widget
myLabel = Label(root,text = file_read.file_reading_return_array(file)).grid(row=0,column=0)
myLabel1 = Label(root,text = 'Hello world').grid(row=1,column=1)

#Showing it onto the screen

root.mainloop()