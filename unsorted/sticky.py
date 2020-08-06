from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

window = Tk()
window.title("My Program")
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab1.grid(row=0, column=0, sticky=NSEW)  # add sticky option

tab2 = ttk.Frame(tab_control)
tab2.grid(row=0, column=0)

tab_control.grid(row=0, column=0, sticky=NSEW)
tab_control.add(tab1, text="First")
tab_control.add(tab2, text="Second")

labe1frame_1 = LabelFrame(tab1, text="Frame_1")
labe1frame_1.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)


txtbox = scrolledtext.ScrolledText(labe1frame_1, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=NSEW)  # add sticky option

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
labe1frame_1.rowconfigure(0, weight=1)
labe1frame_1.columnconfigure(0, weight=1)

# configure the row and column size of parent window
tab1.columnconfigure(0, weight=3)
tab1.rowconfigure(0, weight=3)

window.mainloop()
