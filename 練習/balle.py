import tkinter as tk
import random as rd

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
x_mur = LARGEUR//2

rebond_count = 0


###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 4, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global mur, x1, a
    canvas.move(balle[0], balle[1], balle[2])
    a = rd.randint(1, 100)
    if a < 10:
        canvas.delete(mur)
        rebond2()
        if x1 != x_mur:
            mur = canvas.create_line(x_mur, 0, x_mur, HAUTEUR, fill='white')
            rebond()
    canvas.after(40, mouvement)
    print(a)


def rebond():
    """Fait rebondir la balle sur les bords du canevas avec mur"""
    global balle, rebond_count, x1, a
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= x_mur:
        balle[1] = -balle[1]
        rebond_count += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        rebond_count += 1
    if rebond_count >= 30:
        pass
    a = rd.randint(1, 100)


def rebond2():
    """Fait rebondir la balle sur les bords du canevas sans mur"""
    global balle, rebond_count, x1, a
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        rebond_count += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        rebond_count += 1
    if rebond_count >= 30:
        pass
    a = rd.randint(1, 100)

######################
# programme principal


racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
mur = canvas.create_line(x_mur, 0, x_mur, HAUTEUR, fill='white')
canvas.grid()
balle = creer_balle()
mouvement()
racine.mainloop()
