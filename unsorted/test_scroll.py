import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root)
scrolly = tk.Scrollbar(root, orient='vertical', command=canvas.yview)

pressedY = 0


def mouse_pressed(e, label):
    pressedY = e.y
    print('p', e, label)


def mouse_released(e, label):
    print('r', e, label)


def mouse_motion(e, label):
    m = pressedY - e.y
    # print('m',e, label)
    canvas.yview_scroll(int(-1*(m/50)), "units")


labelList = []
for i in range(60):
    labelList.append(tk.Label(canvas, text=i))
    canvas.create_window(0, 20 * i, window=labelList[i])

    labelList[i].bind("<Button-1>", lambda e,
                      i=i: mouse_pressed(e, labelList[i]))
    labelList[i].bind("<ButtonRelease-1>", lambda e,
                      i=i: mouse_released(e, labelList[i]))
    labelList[i].bind("<B1-Motion>", lambda e,
                      i=i: mouse_motion(e, labelList[i]))

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)

canvas.create_window(fill='both', expand=True, side='left')
scrolly.pack(fill='y', side='right')

root.mainloop()
