from tkinter import *
import file_read

root = Tk()
file = 'eurovision.txt'

#Creating a Label widget
myLabel = Label(root,text = ['Australia:1,2,3,4,12,321,312,3123,123,12312,312,312,3']).grid(row=0,column=0)
myLabel1 = Label(root,text = 'Hello world').grid(row=1,column=1)

#Showing it onto the screen

root.mainloop()