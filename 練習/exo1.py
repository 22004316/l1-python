import tkinter as tk

root = tk.Tk()
HEIGHT = 500
WIDTH = 500
clic_inorout = True
clic_count = 0


def clic(event):
    global clic_inorout, clic_count
    x = event.x
    y = event.y
    if clic_inorout is True:
        if 200 <= x <= 350 and 200 <= y <= 350:
            if clic_count == 0:
                canvas.itemconfig(rectangle, fill="blue")
                clic_count = 1
            else:
                canvas.itemconfig(rectangle, fill="red")
                clic_count = 0
        else:
            clic_inorout = False


def restart():
    global clic_inorout
    clic_inorout = True


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
rectangle = canvas.create_rectangle((200, 200), (350, 330), fill="red")
button = tk.Button(root, text="Recommencer", command=restart)

canvas.bind("<Button-1>", clic)

canvas.grid(row=1)
button.grid(row=2)

root.mainloop()
