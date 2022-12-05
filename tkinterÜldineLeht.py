from tkinter import *
from fileRead import FileRead

from random import randint

class TkinterWork():

  def __init__(self,root,array):
    self.root = root
    self.d = {}
    self.sorted_arr = sorted(array)
    self.key = []
    self.value = []

    
    for key in self.sorted_arr:
      
      self.d[key] = randint(0,600)
      
      self.key.append(key)
      self.value.append(self.d[key])

    self.arr = sorted(self.d.items(), key=lambda x: x[1],reverse=TRUE)



  def countries_write(self):

    riigid = Label(text="Riigid", bg="Purple", fg="white").grid(row=0,  column=0,  padx=10,  pady=1)

    a = 0

    for key in range(0,len(self.arr)-17):
      k = Label(text=self.arr[key][0]).grid(row=a+1,  column=0,  padx=10,  pady=1)
      a += 1

    a = 0
    riigid = Label(text="Riigid", bg="Purple", fg="white").grid(row=0,  column=7,  padx=10,  pady=1)

    for key in range(24,len(self.arr)):
      k = Label(text=self.arr[key][0]).grid(row=a+1,  column=7,  padx=10,  pady=1)
      a += 1

  def points(self):
    a = 0

    punktid = Label(text="Punktid", bg="Blue", fg="white").grid(row=0,  column=1,  padx=10,  pady=5)

    for value in range(0,len(self.arr)-17):

      v = Label(text=self.arr[value][1]).grid(row=a+1,  column=1,  padx=10,  pady=5)
      a += 1

    punktid = Label(text="Punktid", bg="Blue", fg="white").grid(row=0,  column=8,  padx=10,  pady=5)
    a=0
    for value in range(24,len(self.arr)):

      v = Label(text=self.arr[value][1]).grid(row=a+1,  column=8,  padx=10,  pady=5)
      a += 1


  def place(self):

    koht = Label(text = "Koht",bg ="Black",fg = "white").grid(row = 0,column = 2,  padx=10,  pady=5)
    
    a = 1


    for koht in range(len(self.arr)-17):
      koht = Label(text = koht+1).grid(row = a,column = 2,  padx=10,  pady=5)
      a+=1
    
    koht = Label(text = "Koht",bg ="Black",fg = "white").grid(row = 0,column = 9,  padx=10,  pady=5)
    a = 1

    for koht in range(24,len(self.sorted_arr)):
      koht = Label(text = koht+1).grid(row = a,column = 9,  padx=10,  pady=5)
      a+=1


  def buttons(self):
    
    main_window = Button(text = "Avaleht").grid(row=5,column = 15,padx=300)
    third_window = Button(text = "Kolmanda lehe peale").grid(row = 7, column=15,padx=300)
    fourth_window = Button(text = "Neljanda lehe peale").grid(row = 9,column=15,padx=300)


  def starter(self):
    self.root.geometry('3000x3000')
    self.countries_write()
    self.points()
    self.place()
    self.buttons()



root = Tk()
a = TkinterWork(root,FileRead('eurovision.txt').file_reading_return_set())
a.starter()
root.mainloop()
