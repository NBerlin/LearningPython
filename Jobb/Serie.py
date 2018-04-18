import xlwt
from tkinter import *
from tkinter import ttk
book = xlwt.Workbook(encoding="utf-8")

def setTeams():
    antallag=int(lag.get())
    knapp.co




#windowsetup
root = Tk()
root.title("Seriespel")
mainframe = ttk.Frame(root, padding="5 5 30 30")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
lag = StringVar()


#inputfields
text_entry = ttk.Entry(mainframe, width=7, textvariable=lag)
text_entry.grid(column=2, row=1, sticky=(W, E))
knapp = ttk.Button(mainframe,text="Lag", command=setTeams)
knapp.grid(column=2,row=5,sticky=S)

#labels
ttk.Label(mainframe, text="Hur många ligor?").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
