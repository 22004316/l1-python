import tkinter as tk

root = tk.Tk()
HEIGHT = 500
WIDTH = 500
clic_count = 0
pause = False


def clic(event):
    global clic_count, x, y, x2, y2, pause
    if not pause:
        clic_count += 1
        if clic_count == 1:
            x = event.x
            y = event.y
        elif clic_count == 2:
            x2 = event.x
            y2 = event.y
            canvas.create_line(x, y, x2, y2, fill='blue')
        elif clic_count == 3:
            x = event.x
            y = event.y
        elif clic_count == 4:
            x2 = event.x
            y2 = event.y
            canvas.create_line(x, y, x2, y2, fill='red')
        elif clic_count == 5:
            canvas.delete('all')
            clic_count = 0


def button_pause():
    global pause
    if pause is False:
        pause = True
        button.config(text="Restart")
    else:
        pause = False
        button.config(text='Pause')


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
button = tk.Button(root, text="Pause", command=button_pause)


canvas.grid(row=1)
button.grid(row=2)
canvas.bind("<Button-1>", clic)

root.mainloop()
