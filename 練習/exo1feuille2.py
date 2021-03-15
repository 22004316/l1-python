import tkinter as tk
import random as rd

root = tk.Tk()
mvmt_state = False

def start():
    global mvmt_state
    if mvmt_state
    mouvement(balle)


def creer_balle():
    ball = canvas.create_oval((300-20, 200-20), (300+20, 200+20), fill='blue')
    return [ball, rd.randint(1, 7), rd.randint(1, 7)]


def mouvement(balle):
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(30, lambda: mouvement(balle))


canvas = tk.Canvas(root, height=400, width=600, bg='black')
button = tk.Button(root, text="Démarrer", font="20", command=start)
balle = creer_balle()

canvas.grid(row=0)
button.grid(row=1)


root.mainloop()
