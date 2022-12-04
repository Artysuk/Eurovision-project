from tkinter import *
from fileRead import FileRead
import tkinterHindamisLeht

class TkinterWork():

  def __init__(self,master,file):
    self.file = file

    self.frame = Frame(master)
    self.frame.pack()



  def countries_write(self):
    pass

  def buttons(self):
    pass

  def points(self):
    pass

  def starter(self):
    pass

  def mainloop(self):
    self.frame.mainloop()



root = Tk()
a = TkinterWork(root,FileRead('eurovision.txt').file_reading_return_array())
root.mainloop()