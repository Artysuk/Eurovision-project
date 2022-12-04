from tkinter import *
from parent import TkinterWindow

class Avaleht(TkinterWindow):

    def text(self):

        text1 = Label(self.root,text="Eurovisiooni projekt(versioon 0.02)",font=('Times New Roman',17,'bold'),bg="red",foreground='black').pack()
        text2 = Label(self.root,text="Sisaldab:",font=('Times New Roman',15,'bold'),bg="Orange",foreground='white').pack()
        text3 = Label(self.root,text="Peamenüü(Avaleht)",font=('Times New Roman',12,'bold'),bg="yellow",foreground='black').pack()
        text4 = Label(self.root,text="Riikide koht ja hind",font=('Times New Roman',12,'bold'),bg="green",foreground='white').pack()
        text5 = Label(self.root,text="Võimalust panna punkte ise",font=('Times New Roman',12,'bold'),bg="blue",foreground='black').pack()
        text6 = Label(self.root,text="Näha võitja/te leht ja näha võitjaid viimase 50 aasta jooksul",font=('Times New Roman',12,'bold'),bg="indigo",foreground='white').pack()
        text7 = Label(self.root,text="2022",font=('Times New Roman',8,'bold'),bg="violet",foreground='black').pack()
    

    def starter(self):

        self.root.title("Avaleht")
        self.root.geometry('500x200')

        self.root.configure(bg = '#856ff8')

        self.menu()
        self.toolbar()
        self.text()

        self.root.mainloop()


root = Tk()
a = Avaleht(root)
a.starter()






