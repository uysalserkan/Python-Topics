from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar

# from tkinter import

root = Tk()

print(Tk.__mro__)
stst = True
chngText = StringVar()
chngText.set("Disable")

root.wm_title("Button Deactivation")

button1 = ttk.Button(root, text="Standart Button", state="normal")
button1.grid(row=0)


def disable():
    print("Button1 state is:", button1["state"])
    if button1["state"] == "normal":
        button1["state"] = "disabled"
        stst = False
        chngText.set("Enable")

    elif button1["state"] == "disabled":
        button1["state"] = "normal"
        chngText.set("Disable")
        stst = True


button2 = ttk.Button(root, textvariable=chngText, command=disable)
button2.grid(row=2, pady=(10, 2))

print("State is: ", stst)
root.mainloop()
