import tkinter as tk
import random as rd

WIDTH = 800
HEIGHT = 600
RAYON = 20
balles = []
id_after = None
dx = []
dy = []


def get_color(r=0, g=0, b=0):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def touche_horizontal(balle):
    """ retourne True si touche en haut ou en bas, False sinon """
    cadre = canvas.coords(balle)
    if cadre[1] <= 0 or cadre[3] >= HEIGHT:
        return True
    else:
        return False


def touche_vertical(balle):
    """ retourne True si touche en haut ou en bas, False sinon """
    cadre = canvas.coords(balle)
    if cadre[0] <= 0 or cadre[2] >= WIDTH:
        return True
    else:
        return False


def touche_balle(i):
    """ retourne True si balle i touche une autre balle, et False sinon """
    liste = list(range(i)) + list(range(i+1, len(balles)))
    ci = canvas.coords(balles[i])
    for j in liste:
        cj = canvas.coords(balles[j])
        if (ci[0] < cj[0] < ci[2] and ci[1] < cj[1] < ci[3]) \
            or (cj[0] < ci[0] < cj[2] and cj[1] < ci[1] < cj[3]) \
            or (ci[0] < cj[2] < ci[2] and ci[1] < cj[1] < ci[3]) \
            or (cj[0] < ci[2] < cj[2] and cj[1] < ci[1] < cj[3]):
            return True
    return False


def deplace_balle():
    """ met en mouvement les balles """
    global id_after
    global dx, dy
    if balles == []:
        return
    for i in range(len(balles)):
        b = balles[i]
        if touche_horizontal(b):
            dy[i] = -dy[i]
        elif touche_vertical(b):
            dx[i] = -dx[i] 
        elif touche_balle(i):
            dy[i] = -dy[i]
            dx[i] = -dx[i] 
        canvas.move(b, dx[i], dy[i])
    id_after = canvas.after(10, deplace_balle)


def arrete_balle():
    """ stoppe le mouvement des balles"""
    if id_after is None:
        return
    canvas.after_cancel(id_after)


def creer_balle(event):
    """ ajoute une balle à l'endroit où l'on a cliqué
     d'une couleur aléatoire """
    global balles, dx, dy
    col = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
    balle_new = canvas.create_oval((event.x-RAYON, event.y-RAYON),
                                    (event.x+RAYON, event.y+RAYON), fill=col)
    balles.append(balle_new)
    dx.append(rd.randint(-5, 5))
    dy.append(rd.randint(-5, 5))


racine = tk.Tk()
racine.title("Balles qui rebondissent")
canvas = tk.Canvas(racine, bg="black", width=WIDTH, height=HEIGHT)
bouton_deplace = tk.Button(racine, text="start", command=deplace_balle)
bouton_arrete = tk.Button(racine, text="stop", command=arrete_balle)

canvas.grid(row=0, column=0, columnspan=2)
bouton_deplace.grid(row=1, column=0)
bouton_arrete.grid(row=1, column=1)

canvas.bind("<Button-1>", creer_balle)

racine.mainloop()
