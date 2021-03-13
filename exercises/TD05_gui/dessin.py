import tkinter as tk
import random


def cicrle():
    global objects
    x1 = random.randint(0, 500)
    y1 = random.randint(0, 600)
    objects.append(canvas.create_oval(x1, y1, x1+100, y1+100,
     fill=color, outline=color))


def carre():
    global objects
    x = random.randint(0, 500)
    y = random.randint(0, 600)
    objects.append(canvas.create_rectangle(x, y, x+100, y+100,
     fill=color, outline=color))


def draw_cross():
    global objects
    x = random.randint(0, 500)
    y = random.randint(0, 600)
    objects.append(canvas.create_line(x, y, x+100, y+100,
    width=4, fill=color))
    objects.append(canvas.create_line(x, y+100, x+100,
     y, width=4, fill=color))


def choose_color():
    global color
    color = input("Choose a valid color")


def undo():
    global objects
    if len(objects) != 0:
        if canvas.type(objects[-1]) == 'line':
            canvas.delete(objects[-1])
            del(objects[-1])
            canvas.delete(objects[-1])
            del(objects[-1])
        else:
            canvas.delete(objects[-1])
            del(objects[-1])


root = tk.Tk()
root.title = "THIS is art"
color = "blue"
objects = []
canvas = tk.Canvas(root, width=600, height=700, bg="black",
 bd=5, relief="raised")
button_couleur = tk.Button(root, text="Choisir une couleur", font=("arial", "10"), command=choose_color)
button_cercle = tk.Button(root, text="Cercle", font=("arial", "10"),
 command=cicrle)
button_carré = tk.Button(root, text="Carré", font=("arial", "10"),
 command=carre)
button_croix = tk.Button(root, text="Croix", font=("arial", "10"),
 command=draw_cross)
button_undo = tk.Button(root, text='Undo', font=("arial", "10"),
 command=undo)
button_couleur.grid(column=1, row=0)
button_cercle.grid(row=1, column=0)
button_carré.grid(row=2, column=0)
button_croix.grid(column=0, row=3)
button_undo.grid(column=0, row=4)
canvas.grid(column=1, row=1, rowspan=3)

root.mainloop()
