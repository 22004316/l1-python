import tkinter as tk
import random as rd

etat_balle = 1

root = tk.Tk()


def creer_balle():
    '''creer une balle muni d'une direction de mouvement aléatoire'''
    circle = c.create_oval((300-20, 200-20), (300+20, 200+20), fill='blue')
    x = rd.randint(1, 7)
    y = rd.randint(1, 7)
    return [circle, x, y]


def mouvement(b):
    '''fait bouger la balle dans une direction aléatoire
     selon les valeurs de la liste balle'''
    global id_after
    c.move(b[0], b[1], b[2])
    rebond2(b)
    id_after = c.after(30, lambda: mouvement(b))


def start():
    '''démarre ou arrête le mouvement de la balle'''
    global etat_balle
    if etat_balle == 1:
        mouvement(balle)
        button.config(text='Arrêter')
    else:
        c.after_cancel(id_after)
        button.config(text='Démarrer')
    etat_balle = 1 - etat_balle


def rebond1(balle):
    '''change la direction de la balle si elle touche un bord'''
    x0, y0, x1, y1 = c.coords(balle[0])
    if y1 >= 400 or y0 <= 0:
        balle[2] = -balle[2]
    if x1 >= 600 or x0 <= 0:
        balle[1] = -balle[1]


def rebond2(b):
    '''la balle reapparait en haut ou à gauche'''
    x0, y0, x1, y1 = c.coords(b[0])
    if y1 >= 400:
        c.move(b[0], 0, -400)
    if x1 >= 600:
        c.move(b[0], -600, 0)


c = tk.Canvas(root, height=400, width=600, bg='black')
button = tk.Button(root, text='Démarrer', font='20', command=start)
balle = creer_balle()


c.grid(row=0)
button.grid(row=1)


root.mainloop()
