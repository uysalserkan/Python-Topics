from tkinter import (Tk, Canvas, RIGHT, BOTH, Frame, Button,X,Y)
root = Tk()


def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


root.overrideredirect(True)  # turns off title bar, geometry
root.geometry('400x100+200+200')  # set new geometry

# make a frame for the title bar
title_bar = Frame(root, bg='white', relief='raised', bd=2)

# put a close button on the title bar
close_button = Button(title_bar, text='X', command=root.destroy)

# a canvas for the main area of the window
window = Canvas(root, bg='black')

# pack the widgets
title_bar.pack(expand=1, fill=X)
close_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)

root.mainloop()
