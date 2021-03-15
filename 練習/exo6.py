import tkinter as tk

root = tk.Tk()

cote = 50
color = ["black"]


def change_color(event):
    global circle, color
    x = event.x
    y = event.y
    if x <= cote and y <= cote:
        canvas.itemconfig(circle, fill="green")
        color.append("green")
    elif cote < x <= 2*cote and y <= cote:
        canvas.itemconfig(circle, fill="yellow")
        color.append("yellow")
    elif 2*cote < x <= 3*cote and y <= cote:
        canvas.itemconfig(circle, fill="blue")
        color.append("blue")
    else:
        canvas.itemconfig(circle, fill="black")
        color.append("black")


def undo():
    global color, circle
    if len(color) >= 2:
        if color[-1] == color[-2]:
            while color[-1] == color[-2]:
                del color[-1]
        del color[-1]
        canvas.itemconfig(circle, fill=color[-1])


canvas = tk.Canvas(root, height=500, width=500, bg='white')
button = tk.Button(root, text='Annuler', font="20", command=undo)

canvas.create_rectangle((0, 0), (cote, cote), fill="green")
canvas.create_rectangle((cote, 0), (2 * cote, cote), fill="yellow")
canvas.create_rectangle((2 * cote, 0), (3 * cote, cote), fill="blue")
circle = canvas.create_oval((250-25, 250-25), (250+25, 250+25), fill='black')

canvas.grid(column=1, row=0)
button.grid(column=0, row=0)
canvas.bind("<Button-1>", change_color)

root.mainloop()
