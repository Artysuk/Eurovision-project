from tkinter import *
from fileRead import FileRead
import tkinterHindamisLeht

root = Tk()

img = PhotoImage(file = "Eurovision.png")
label1 = Label(root, image = img)

label1.place(x = 0,y = 0)

class TkinterWork():

  def __init__(self, dictionary):
    self.d = {}
    self.sorted_d = sorted(dictionary)
    self.key = []
    self.value = []
    
    for key in self.sorted_d:
      
      self.d[key] = dictionary[key]
      
      self.key.append(key)
      self.value.append(dictionary[key])



  def riigid(self):

    riigid = Label(text="Riigid", bg="Blue", fg="white").grid(row=0, column=0)

    a = 0

    for key in self.key:
      k = Label(text=key).grid(row=a + 1, column=0)
      a += 1



  def punktid(self):
    a = 0

    punktid = Label(text="Punktid", bg="Blue", fg="white").grid(row=0,column=1,padx=200)

    for value in self.value:

      v = Label(text=value).grid(row=a + 1, column=1, padx=200)
      a += 1
      
  def koht(self):
    
      koht = Label(text = "Koht",bg ="Blue",fg = "white").grid(row = 0,column = 2,padx = 200)
    
      a = 1

      for koht in range(len(self.sorted_d)):
        koht = Label(text = self.sorted_d.index(self.sorted_d[koht])+1).grid(row = a,column = 2,padx = 200)
        a+=1

    

  def nupud(self,tk):
    pass
    '''
    tkl = TkinterHindamisLeht()


    
    teineLehtNupp = Button(text="Teise lehe juurde",command = tkl.print_something).grid(row = 5,column = 0,padx = 0)
    
    kolmasLehtNupp = Button(text="Kolmanda lehe juurde").grid(row = 6,column = 0,padx = 0)

    exitNupp = Button(text="Välja", command = quit).grid(row = 7,column = 0,padx = 0)
    '''

def starter():
  fr = FileRead('eurovision.txt')
  tk = TkinterWork(fr.file_reading_return_set())

  root.title("Eurovisiooni punktidesüsteem")
  root.geometry("500x500")

  tk.riigid()
  tk.punktid()
  tk.koht()
  tk.nupud(tk)
  root.mainloop()

