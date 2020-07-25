from tkinter import (Tk, Button, StringVar)


def ResizeFunction(main):
    main.geometry("540x380")


main = Tk()
HE.set("240x")
WI.set("180")
main.geometry("{}{}".format(H, W))

resizeButton = Button(main, text="RESIZE", command=ResizeFunction(main))
resizeButton.pack()

main.mainloop()
