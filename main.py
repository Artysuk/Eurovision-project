'''
projekt: Eurovisiooni punktitabel Tkinteriga
Karoliina Valge, Artur Kašnikov

loeb failist sisse puktide info
Tkinter aknas näidatakse kahes veerus kõik osalejad ja nende punktiseis (alguses kõigil 0)
žüriipunktide osa: 
punktitabeli all näidatakse riigi nime, mis hetkel žüriipunkte annab (ning  Label’ina punktid 1, 2, … 8, 10,  ja 12)
punktitabelis näidatakse, mis riik mitu punkti sai ja seejärel liidetakse see punktiseisule juurde, vajadusel muudetakse riikide järjekorda punktitabelis
protsess kestab, kuni kõik punktid on ära jagatud
Rahvapunktide osa: 
alustatakse riigist, mis sai kokku kõige vähem žüriipunkte.
punktitabelis näidatakse, mitu mitu punkti sai riik rahvalt kokku ja liidetakse juurde punktiseisule, vajadusel muudetakse riikide järjekorda punktitabelis
protsess kestab, kuni kõik punktid on ära jagatud
Lõpp:
Kui kõik punktid on jagatud, näidatakse aknas suurelt riik, mis sai kõige rohkem punkte

'''
import tkinter as tk
from tkinter import ttk

from random import randint
from threading import Thread
from fileRead import FileRead


LARGEFONT = ('Verdana',35)

global array
array = FileRead('eurovision.txt').file_reading_return_array()


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StarterPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StarterPage(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.master.title("Avaleht")

        self.master.configure(bg = '#856ff8')

        self.toolbar()
        self.text()

        

        

    def text(self):

        text1 = tk.Label(self,text="Eurovisiooni projekt(versioon 0.02)",font=('Times New Roman',17,'bold'),bg="red",foreground='black').pack()
        text2 = tk.Label(self,text="Sisaldab:",font=('Times New Roman',15,'bold'),bg="Orange",foreground='white').pack()
        text3 = tk.Label(self,text="Peamenüü(Avaleht)",font=('Times New Roman',12,'bold'),bg="yellow",foreground='black').pack()
        text4 = tk.Label(self,text="Riikide koht ja hind",font=('Times New Roman',12,'bold'),bg="green",foreground='white').pack()
        text5 = tk.Label(self,text="Võimalust panna punkte ise",font=('Times New Roman',12,'bold'),bg="blue",foreground='black').pack()
        text6 = tk.Label(self,text="Näha võitjate leht ja näha võitjaid viimase 50 aasta jooksul",font=('Times New Roman',12,'bold'),bg="indigo",foreground='white').pack()
        text7 = tk.Label(self,text="2022",font=('Times New Roman',8,'bold'),bg="violet",foreground='black').pack()

    def menu(self):

        menuu = tk.Menu(self.root)

        self.root.config(menu = menuu)

        subMenu = tk.Menu(menuu)

        menuu.add_cascade(label = "Programm", menu = subMenu)

        subMenu.add_command(label="Välja", command = quit)




    def toolbar(self):

        self.toolbarr = tk.Frame(self,background = "blue")

        firstPage = tk.Button(self.toolbarr,text = "Riigid, Hinded ja Koht",command=lambda: self.master.switch_frame(PageOne)).pack(side=tk.LEFT)

        thirdPage = tk.Button(self.toolbarr,text = "Hindamisleht",command=lambda: self.master.switch_frame(PageTwo)).pack(side=tk.LEFT)

        fourthPage = tk.Button(self.toolbarr,text = "Võitja Leht")
        fourthPage.pack(side=tk.LEFT)

        fourthPage = tk.Button(self.toolbarr,text = "Internet Parse(?)")
        fourthPage.pack(side=tk.LEFT)

        self.toolbarr.pack(side=tk.TOP)


    

class PageTwo(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("PageTwo")
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StarterPage)).pack()


class PageOne(tk.Tk):

  def __init__(self,master):

    tk.Frame.__init__(self, master)

    self.d = {}
    self.sorted_arr = sorted(array)
    self.key = []
    self.value = []

    
    for key in sorted(array):
      
      self.d[key] = randint(0,600)
      
      self.key.append(key)
      self.value.append(self.d[key])

    self.arr = sorted(self.d.items(), key=lambda x: x[1],reverse=tk.TRUE)



  def countries_write(self):

    riigid = self.master.Label(text="Riigid", bg="Purple", fg="white").grid(row=0,  column=0,  padx=10,  pady=1)

    a = 0

    for key in range(0,len(self.arr)-17):
      k = self.master.Label(text=self.arr[key][0]).grid(row=a+1,  column=0,  padx=10,  pady=1)
      a += 1

    a = 0
    riigid = self.master.Label(text="Riigid", bg="Purple", fg="white").grid(row=0,  column=7,  padx=10,  pady=1)

    for key in range(24,len(self.arr)):
      k = self.master.Label(text=self.arr[key][0]).grid(row=a+1,  column=7,  padx=10,  pady=1)
      a += 1

  def points(self):
    a = 0

    punktid = self.master.Label(text="Punktid", bg="Blue", fg="white").grid(row=0,  column=1,  padx=10,  pady=5)

    for value in range(0,len(self.arr)-17):

      v = self.master.Label(text=self.arr[value][1]).grid(row=a+1,  column=1,  padx=10,  pady=5)
      a += 1

    punktid = self.master.Label(text="Punktid", bg="Blue", fg="white").grid(row=0,  column=8,  padx=10,  pady=5)
    a=0
    for value in range(24,len(self.arr)):

      v = self.master.Label(text=self.arr[value][1]).grid(row=a+1,  column=8,  padx=10,  pady=5)
      a += 1


  def place(self):

    koht = self.master.Label(text = "Koht",bg ="Black",fg = "white").grid(row = 0,column = 2,  padx=10,  pady=5)
    
    a = 1


    for koht in range(len(self.arr)-17):
      koht = self.master.Label(text = koht+1).grid(row = a,column = 2,  padx=10,  pady=5)
      a+=1
    
    koht = self.master.Label(text = "Koht",bg ="Black",fg = "white").grid(row = 0,column = 9,  padx=10,  pady=5)
    a = 1

    for koht in range(24,len(self.sorted_arr)):
      koht = self.master.Label(text = koht+1).grid(row = a,column = 9,  padx=10,  pady=5)
      a+=1


  def buttons(self):
    
    main_window = tk.Button(text = "Avaleht").grid(row=5,column = 15,padx=300)
    third_window = tk.Button(text = "Kolmanda lehe peale").grid(row = 7, column=15,padx=300)
    fourth_window = tk.Button(text = "Neljanda lehe peale").grid(row = 9,column=15,padx=300)


  def starter(self):
    self.root.geometry('3000x3000')
    self.countries_write()
    self.points()
    self.place()
    self.buttons()







if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
