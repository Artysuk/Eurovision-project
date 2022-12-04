from tkinter import *

class TkinterWindow:
    def __init__(self,root):
        self.root = root


    def menu(self):

        menuu = Menu(self.root)
        self.root.config(menu = menuu)

        subMenu = Menu(menuu)

        menuu.add_cascade(label = "Programm", menu = subMenu)

        subMenu.add_command(label="Välja", command = quit)

    def toolbar(self):

        self.toolbarr = Frame(self.root,background = "blue")

        firstPage = Button(self.toolbarr, text = "Menüü")
        firstPage.pack(side=LEFT)

        secondPage = Button(self.toolbarr,text = "Riigid, Hinded ja Koht",)
        secondPage.pack(side=LEFT)

        thirdPage = Button(self.toolbarr,text = "Hindamisleht")
        thirdPage.pack(side=LEFT)

        fourthPage = Button(self.toolbarr,text = "Võitja Leht")
        fourthPage.pack(side=LEFT)

        fourthPage = Button(self.toolbarr,text = "Internet Parse(?)")
        fourthPage.pack(side=LEFT)

        self.toolbarr.pack(side=TOP)