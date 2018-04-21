from tkinter import *
root = Tk()

def add(event=None):
    file = open("arbetat.txt","a")
    namn=txtboxNamn.get()
    tiddatum = txtboxTid.get()
    file.write(namn + " " + tiddatum+ "\n" )
    txtboxTid.delete(0,END)
    txtboxNamn.delete(0,END)
    txtboxNamn.focus()
    file.close()

labelNamn = Label(root,text="Namn")
labelNamn.pack()
txtboxNamn = Entry(root)
txtboxNamn.pack(side=TOP)
labelTid = Label(root,text="Datum/Tid")
labelTid.pack()
txtboxTid = Entry(root)
txtboxTid.pack()
btnKlar = Button(root,text="Lägg till",command=add)
btnKlar.pack()
txtboxNamn.focus()
root.bind('<Return>', add)

root.mainloop()


