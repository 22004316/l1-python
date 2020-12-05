import tkinter as tk
import random

def cicrle() :
    x1 = random.randint(500)
    y1 = random.randint(500)
    x2 = x1+100
    y2 = y1 + 100
    canvas.create_oval((x1, y1), (x2 , y2), fill = "blue")
    

root = tk.Tk()
root.title = "THIS is art"
canvas = tk.Canvas(root, width = 600, height = 700, bg = "black",
 bd = 5, relief = "raised")
button_couleur = tk.Button(root, text="Choisir une couleur", font = 
("arial", "10"))
button_cercle = tk.Button(root, text="Cercle", font = ("arial", "10"), command = circle)
button_carré = tk.Button(root, text="Carré", font = ("arial", "10"))
button_croix = tk.Button(root, text="Croix", font = ("arial", "10"))

button_couleur.grid(column = 1, row = 0)
button_cercle.grid(row = 1, column = 0)
button_carré.grid(row = 2, column = 0)
button_croix.grid(column = 0,row = 3)
canvas.grid(column = 1, row = 1, rowspan = 3)

root.mainloop()
