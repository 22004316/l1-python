def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

import tkinter as tk
import random

def draw_pixel(i, j, color) :
    '''colorie le pixel (i, j) du canvas de la couleur color'''
    canvas.create_line(i, j, i+1, j, fill = color)

def ecran_aleatoire() :
    '''remplit le canevas de manière à ce que chaque pixel soit
     d'une couleur choisie au hasard'''
    for i in range(255) :
        for j in range(255) :
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color = get_color(r,g,b)
            draw_pixel(i ,j, color )

def degrade_gris():
    for i in range(256):
        color = get_color(i, i, i)
        for j in range(256):
            draw_pixel(i, j, color)         


#def degrade_gris() :
    #for i in range(256):
    #    for j in range(256):
    #        draw_pixel(i, j, )
    #    canvas.create_line(i, i, i,256-i, fill = "black")
     #   draw_pixel

root = tk.Tk()
button_alea = tk.Button(root, text = "Aléatoire", font = ("arial", "10"), command = ecran_aleatoire)
button_degrade = tk.Button(root, text = "Dégradé gris", font = ("arial", "10"), command = degrade_gris)
button_2d = tk.Button(root, text = "Dgradé 2D", font = ("arial", "10"))
canvas = tk.Canvas(root, width = 256, height = 256, bg = "black")

button_alea.grid(column = 0, row = 1, padx = 10)
button_degrade.grid(column = 0, row = 3, padx = 10)
button_2d.grid(column = 0, row = 5, padx = 10)
canvas.grid(column = 1, row = 0,rowspan = 7 )

root.mainloop()



#définition des fonctions:




def degrade_2D():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            color = get_color(i, 0, j)
            draw_pixel(i, j, color)

