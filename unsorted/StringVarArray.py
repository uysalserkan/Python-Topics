""" X """
from tkinter import Tk
from tkinter import ttk
from tkinter import StringVar


df = ["Test1", "Test2", "Test3", "Test4", "Test5", "Test6", "Test7", "Test8", "Test9"]
i = 0
root = Tk()
root.title("String var")
root.geometry("500x500")

# TODO: Array ile işlenecek
testStringVar = StringVar(root)
testLabelStringVar = ttk.Label(root, textvariable=testStringVar)
testStringVar.set("Blank")
testLabelStringVar.grid(row=0, column=1)

listOfStrVar = []
listOfLabel = []
for i in range(len(df)):
    tempStr = StringVar(root)
    tempStr.set("Blank" + str(i))
    listOfStrVar.append(tempStr)
    tempLabel = ttk.Label(root, textvariable=listOfStrVar[i])
    listOfLabel.append(tempLabel)

print(len(listOfStrVar))
print(len(listOfLabel))
for j in range(len(df)):
    listOfLabel[j].grid(row=j, column=1)


def changeLabel():
    global i
    testStringVar.set(df[i])
    print(testStringVar.get())
    i += 1


ttk.Button(root, text="Change Variable", command=lambda: changeLabel()).grid(
    row=0, column=0
)
root.mainloop()
