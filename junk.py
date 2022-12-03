from tkinter import *
 
pack = False
 
def insert():
    global pack
    if pack:
        frame2.pack_forget()
        b.pack_forget()
        frame.pack()
        b.pack()
        pack = False
    else:
        l['text'] = e1.get()
        frame.pack_forget()
        b.pack_forget()
        frame2.pack()
        b['text'] = 'Назад'
        b.pack()
        pack = True
 
root = Tk()
 
frame = Frame(root)
e1 = Entry(frame, width=50)
e1.pack()
frame.pack()
 
frame2 = Frame(root)
l = Label(frame2, text="", font="Arial 32")
l.pack()
 
b = Button(text="Вставить", command=insert)
b.pack()
root.mainloop()