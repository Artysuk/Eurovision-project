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
from tkinter import messagebox

from random import randint
from fileRead import FileRead

import requests
from bs4 import BeautifulSoup



global array
array = FileRead('eurovision.txt').file_reading_return_array()

key = []
value = []
d = dict()
sorted_arr = sorted(array)

    
for keys in sorted_arr:
      
    d[keys[0]] = randint(0,600)
      
    key.append(keys[0])
    value.append(d[keys[0]])



#https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

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

        self.master.configure(bg = 'Purple')

        self.toolbar()
        self.text()

        

        

    def text(self):

        text1 = tk.Label(self,text="Eurovisiooni projekt (versioon 0.02)",font=('MS Sans Serif',20,'bold'),foreground='black').pack()
        text2 = tk.Label(self,text="Sisaldab:",font=('MS Sans Serif',15,'bold'),foreground='black',justify="left").pack()
        text3 = tk.Label(self,text="Peamenüü(Avaleht)",font=('MS Sans Serif',12,'bold'),foreground='black',justify="right").pack()
        text4 = tk.Label(self,text="Riikide koht ja punktid",font=('MS Sans Serif',12,'bold'),foreground='black').pack()
        text5 = tk.Label(self,text="Võimalus panna punkte ise",font=('MS Sans Serif',12,'bold'),foreground='black').pack()
        text6 = tk.Label(self,text="Näha võitjate lehte ja Eurovisiooni võitjaid viimase 50 aasta jooksul",font=('MS Sans Serif',12,'bold'),foreground='black').pack()
        text7 = tk.Label(self,text="2022",font=('MS Sans Serif',5,'bold'),foreground='black').pack()

    def menu(self):

        menuu = tk.Menu(self.root)

        self.root.config(menu = menuu)

        subMenu = tk.Menu(menuu)

        menuu.add_cascade(label = "Programm", menu = subMenu)

        subMenu.add_command(label="Välja", command = quit)




    def toolbar(self):

        self.toolbarr = tk.Frame(self,background = "blue")

        firstPage = tk.Button(self.toolbarr,text = "Riigid, punktid ja kohad", font=('MS Sans Serif', 10),command=lambda: self.master.switch_frame(PagePrintingMarks), bg="#CBC3E3").pack(side=tk.LEFT)

        secondPage = tk.Button(self.toolbarr,text = "Hindamisleht",font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageGivingMarks), bg="#CBC3E3").pack(side=tk.LEFT)

        thirdPage = tk.Button(self.toolbarr,text = "Võitja leht",font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageWinner), bg="#CBC3E3").pack(side=tk.LEFT)
        
        fourthPage = tk.Button(self.toolbarr,text = "Eurovisiooni võitjad",font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageInternetParse), bg="#CBC3E3").pack(side=tk.LEFT)

        self.toolbarr.pack(side=tk.TOP)


    

class PageWinner(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.master.title("Võitja")

        value = list({i for i in d if d[i]==max(d.values())})[0]
        self.toolbar()

        winner_text = tk.Label(self,text = f"Meie võitja on... {value} {max(d.values())} punktiga!",font=('MS Sans Serif',15,'bold'),foreground='black').pack()

    def toolbar(self):

      self.toolbarr = tk.Frame(self,background = "blue")

      mainpage = tk.Button(self.toolbarr,text = "Avaleht",font=('MS Sans Serif', 10),command=lambda: self.master.switch_frame(StarterPage), bg="#FFFFE0").pack(side=tk.LEFT)

      secondPage = tk.Button(self.toolbarr,text = "Riigid, punktid ja kohad", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PagePrintingMarks), bg="#FFFFE0").pack(side=tk.LEFT)

      thirdPage = tk.Button(self.toolbarr,text = "Hindamisleht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageGivingMarks), bg="#FFFFE0").pack(side=tk.LEFT)

      fourthPage = tk.Button(self.toolbarr,text = "Eurovisiooni võitjad", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageInternetParse), bg="#FFFFE0").pack(side=tk.LEFT)

      self.toolbarr.pack(side=tk.TOP)


class PageInternetParse(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("Eurovisiooni võitjad")
        self.võitjate_parsimine()
        self.toolbar()


    def võitjate_parsimine(self):

      url = requests.get("http://www.eurovisioon.ee/voitjad.php").text
      soup = BeautifulSoup(url,'lxml')
      tabel = soup.find('div',{'class':'col-md-8'})
      v = []
      #parsimise osa
      for row in tabel.find_all("div", class_="caption"):
          k = row.find_all('h3')[0]
          k = k.text.replace('.',' -').replace(' ',' - ',1)
          k = k.strip().split(" - ")
          k2 = row.find_all('p')[0]
          k.append(k2.text.strip())
          v.append(k)
      #tulemuse parandamise osa
      for i in range(len(v)):
          del v[i][1]
          for e in range(len(v[i])):
              if "\\" in r"%r" % v[i][e]:
                  v[i][e] = r"%r" % v[i][e]
                  v[i][e] = v[i][e].replace("\\x8a", "Š").replace("\\x9e", "ž")


      tk.Label(self,text = "Aasta ----- Bändi/Esineja nimi ----- Laulu nimi ----- Riik",bg="blue",fg="white").grid(row=0,  column=0,  padx=10,  pady=1)

      a = 3
      

      for s in range(len(v)-40):

        tk.Label(self,text = f'{v[s][0]} ----- {v[s][1]} ----- {v[s][2]} ----- {v[s][3]}').grid(row=a+1,  column=0,  padx=10,  pady=1)
        a+=1


      a = 3
      

      for s in range(69-40,len(v)-11):

        tk.Label(self,text = f'{v[s][0]} ----- {v[s][1]} ----- {v[s][2]} ----- {v[s][3]}').grid(row=a+1,  column=4,  padx=10,  pady=1)
        a+=1

      a = 3
      

      for s in range(69-11,len(v)):

        tk.Label(self,text = f'{v[s][0]} ----- {v[s][1]} ----- {v[s][2]} ----- {v[s][3]}').grid(row=a+1,  column=7,  padx=10,  pady=1)
        a+=1




    def toolbar(self):

        self.toolbarr = tk.Frame(self,background = "blue")

        mainPage = tk.Button(self.toolbarr,text = "Avaleht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(StarterPage), bg="#ADD8E6").grid(row = 0, column = 1)

        fifthPage = tk.Button(self.toolbarr,text = "Riigid, punktid ja kohad", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PagePrintingMarks), bg="#ADD8E6").grid(row = 0, column = 4)

        thirdPage = tk.Button(self.toolbarr,text = "Hindamisleht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageGivingMarks), bg="#ADD8E6").grid(row = 0, column = 2)

        fourthPage = tk.Button(self.toolbarr,text = "Võitja leht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageWinner), bg="#ADD8E6").grid(row = 0, column = 3)

        


        self.toolbarr.grid(row = 0, column = 4)


class PageGivingMarks(tk.Frame):

    def __init__(self, master):

        tk.Frame.__init__(self, master)
        self.master.title("Punktide andmine")

        self.toolbar()
        self.buttons()

    def point_putter(self,arg,widget,array_of_used_countries = []):
      
      if self.country.get() in array_of_used_countries:

        a = messagebox.showerror("Critical Error :o ","Viga, ei tohi lisada sama riigile punkte kaks korda. Proovi uuesti")
        array_of_used_countries.clear()
        self.master.switch_frame(PageGivingMarks)

      if self.country.get() not in d:

        a = messagebox.showerror("Critical Error :o ","Viga, seda riiki ei eksisteeri. Proovi uuesti")
        array_of_used_countries.clear()
        self.master.switch_frame(PageGivingMarks)

        
      else:
        array_of_used_countries.append(self.country.get())
      

      
      widget.pack_forget()

      match arg:
        case 12:
          d[self.country.get()] += 12
        case 10:
          d[self.country.get()] += 10
        case 9:
          d[self.country.get()] += 9
        case 8:
          d[self.country.get()] += 8
        case 7:
          d[self.country.get()] += 7
        case 6:
          d[self.country.get()] += 6
        case 5:
          d[self.country.get()] += 5
        case 4:
          d[self.country.get()] += 4
        case 3:
          d[self.country.get()] += 3
        case 2:
          d[self.country.get()] += 2
        case 1:
          d[self.country.get()] += 1



    def buttons(self):
      text = tk.Label(self,text = "Kirjuta riik siia (eesti keeles)\n• Jälgi, et sa kirjutaksid õigesti\n• Ära kirjuta sama riigi 2 korda", font=('MS Sans Serif',12,'bold')).pack(side=tk.TOP)

      self.country = tk.Entry(self)
      self.country.pack()

      btn12=tk.Button(self, text="12", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(12,btn12))
      btn12.pack(pady=10)

      btn10=tk.Button(self, text="10", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(10,btn10))
      btn10.pack(pady=10)
  
      btn9=tk.Button(self, text="9", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(9,btn9))
      btn9.pack(pady=10)

      btn8=tk.Button(self, text="8", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(8,btn8))
      btn8.pack(pady=10)

      btn7=tk.Button(self, text="7", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(7,btn7))
      btn7.pack(pady=10) 

      btn6=tk.Button(self, text="6", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(6,btn6))
      btn6.pack(pady=10)

      btn5=tk.Button(self, text="5", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(5,btn5))
      btn5.pack(pady=10)

      btn4=tk.Button(self, text="4", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(4,btn4))
      btn4.pack(pady=10)

      btn3=tk.Button(self, text="3", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(3,btn3))
      btn3.pack(pady=10)

      btn2=tk.Button(self, text="2", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(2,btn2))
      btn2.pack(pady=10)

      btn1=tk.Button(self, text="1", font= ('Helvetica bold', 10), command=lambda:
      self.point_putter(1,btn1))
      btn1.pack(pady=10)





    def toolbar(self):

      self.toolbarr = tk.Frame(self,background = "blue")

      firstPage = tk.Button(self.toolbarr,text = "Avaleht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(StarterPage), bg="#FFCCCB").pack(side=tk.LEFT)

      secondPage = tk.Button(self.toolbarr,text = "Riigid, punktid ja kohad", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PagePrintingMarks), bg="#FFCCCB").pack(side=tk.LEFT)

      thirdPage = tk.Button(self.toolbarr,text = "Võitja leht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageWinner), bg="#FFCCCB").pack(side=tk.LEFT)
        
      fourthPage = tk.Button(self.toolbarr,text = "Eurovisiooni võitjad", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageInternetParse), bg="#FFCCCB").pack(side=tk.LEFT)

      self.toolbarr.pack(side=tk.TOP)


    


class PagePrintingMarks(tk.Frame):

  def __init__(self,master):

    tk.Frame.__init__(self, master)
    self.master.title("Tulemused")

    
    self.arr = sorted(d.items(), key=lambda x: x[1],reverse=tk.TRUE)
    arr = self.arr
    

    self.toolbar()
    self.countries_write()
    self.points()
    self.place()



  def countries_write(self):

    riigid = tk.Label(self,text="Riigid", font=('MS Sans Serif',10,'bold','underline'), bg="#800000", fg="white").grid(row=1,  column=1,  padx=5,  pady=1)

    a = 1

    for key in range(0,len(self.arr)-17):

      if a == 1:
        k = tk.Label(self,text=self.arr[key][0], background="gold").grid(row=a+1,  column=1,  padx=5,  pady=1)
      elif a == 2:
        k = tk.Label(self,text=self.arr[key][0], background="silver").grid(row=a+1,  column=1,  padx=5,  pady=1)
      elif a == 3:
        k = tk.Label(self,text=self.arr[key][0], background="#CD7F32").grid(row=a+1,  column=1,  padx=5,  pady=1)
      else:
        k = tk.Label(self,text=self.arr[key][0]).grid(row=a+1,  column=1,  padx=5,  pady=1)
      a += 1

    a = 1
    riigid = tk.Label(self,text="Riigid",font=('MS Sans Serif',10,'bold','underline'), bg="#800000", fg="white").grid(row=1,  column=8,  padx=5,  pady=1)

    for key in range(24,len(self.arr)):
      k = tk.Label(self,text=self.arr[key][0]).grid(row=a+1,  column=8,  padx=5,  pady=1)
      a += 1


  def toolbar(self):

        self.toolbarr = tk.Frame(self,background = "blue")

        mainPage = tk.Button(self.toolbarr,text = "Avaleht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(StarterPage), bg="#90EE90").grid(row = 0, column = 1)

        thirdPage = tk.Button(self.toolbarr,text = "Hindamisleht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageGivingMarks), bg="#90EE90").grid(row = 0, column = 2)

        fourthPage = tk.Button(self.toolbarr,text = "Võitja Leht", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageWinner), bg="#90EE90").grid(row = 0, column = 3)

        fifthPage = tk.Button(self.toolbarr,text = "Eurovisiooni võitjad", font=('MS Sans Serif', 10), command=lambda: self.master.switch_frame(PageInternetParse), bg="#90EE90").grid(row = 0, column = 4)


        self.toolbarr.grid(row = 0, column = 4)



  def points(self):
    a = 1

    punktid = tk.Label(self,text="Punktid",font=('MS Sans Serif',10,'bold','underline'), bg="#800000", fg="white").grid(row=1,  column=2,  padx=10,  pady=5)

    for value in range(0,len(self.arr)-17):

      if a == 1:
        v = tk.Label(self,text=self.arr[value][1], background="gold").grid(row=a+1,  column=2,  padx=10,  pady=5)
      elif a == 2:
        v = tk.Label(self,text=self.arr[value][1], background="silver").grid(row=a+1,  column=2,  padx=10,  pady=5)
      elif a == 3:
        v = tk.Label(self,text=self.arr[value][1], background="#CD7F32").grid(row=a+1,  column=2,  padx=10,  pady=5)
      else:
        v = tk.Label(self,text=self.arr[value][1]).grid(row=a+1,  column=2,  padx=10,  pady=5)
      a += 1

    punktid = tk.Label(self,text="Punktid",font=('MS Sans Serif',10,'bold','underline'), bg="#800000", fg="white").grid(row=1,  column=9,  padx=10,  pady=5)

    a=1
    for value in range(24,len(self.arr)):

      v = tk.Label(self,text=self.arr[value][1]).grid(row=a+1,  column=9,  padx=10,  pady=5)
      a += 1





  def place(self):

    koht = tk.Label(self,text = "Koht",font=('MS Sans Serif',10,'bold','underline'),bg ="#800000",fg = "white").grid(row = 1,column = 3,  padx=10,  pady=5)
    
    a = 2

    for koht in range(len(self.arr)-17):

      if a == 2:
        koht = tk.Label(self,text = koht+1, background="gold").grid(row = a,column = 3,  padx=10,  pady=5)
      elif a == 3:
        koht = tk.Label(self,text = koht+1, background="silver").grid(row = a,column = 3,  padx=10,  pady=5)
      elif a == 4:
        koht = tk.Label(self,text = koht+1, background="#CD7F32").grid(row = a,column = 3,  padx=10,  pady=5)
      else:
        koht = tk.Label(self,text = koht+1).grid(row = a,column = 3,  padx=10,  pady=5)
      a+=1
    
    koht = tk.Label(self,text = "Koht",font=('MS Sans Serif',10,'bold','underline'),bg ="#800000",fg = "white").grid(row = 1,column = 10,  padx=10,  pady=5)
    a = 2

    for koht in range(24,len(sorted_arr)):
      koht = tk.Label(self,text = koht+1).grid(row = a,column = 10,  padx=10,  pady=5)
      a+=1









if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
