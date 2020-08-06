from tkinter import (Tk, ttk, W, E, S, N, Button)

root = Tk()
root.geometry("650x650")
rootFrame = ttk.LabelFrame(root, text=u"\u23f5", padding="3 3 10 10")
belowFrame = ttk.LabelFrame(root, text="Second")
buttonStyle = ttk.Style()
buttonStyle.configure('run.TButton', foreground='green',
                      font=('Helvetica'), height=10, width=20)
textButton = ttk.Button(rootFrame, text="Exit", style='run.TButton',
                        command=root.destroy)

normalButton = ttk.Button(rootFrame, text="Test", style='run.TButton')
normalButton.grid(row=1, column=3)
text = ttk.Label(rootFrame, text="Test Broadcast")
text.grid(row=2, column=2)
rootFrame.grid(columnspan=20, rowspan=20)
textButton.grid(row=0, column=1, sticky=W+E+N+S)

belowFrame.grid(columnspan=2, rowspan=2)
second = ttk.Label(
    belowFrame, text="SecondSecondSecondSecondSecondSecondSecondSecondSecondSecondSecondSecondSecondSecond Change").pack()
second2 = ttk.Label(belowFrame, text="Second Change").pack()
second3 = ttk.Label(belowFrame, text="Second Change").pack()
second21 = ttk.Label(belowFrame, text="Second Change").pack()
second31 = ttk.Label(belowFrame, text="Second Change").pack()
second22 = ttk.Label(belowFrame, text="Second Change").pack()
second32 = ttk.Label(belowFrame, text="Second Change").pack()
second23 = ttk.Label(belowFrame, text="Second Change").pack()
second33 = ttk.Label(belowFrame, text="Second Change").pack()


root.mainloop()
