#from tkinter import * #
import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 500

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
x2 = 300
canvas.create_line(x2, 50, x2, 450)
canvas.create_oval(x2 - 50, 0, x2 + 50, 100)
canvas.create_oval(x2 - 50, 200, x2 + 50, 300)
canvas.create_oval(x2 - 50, 400, x2 + 50, 500)
    
    # Fin de votre code

canvas.grid()
root.mainloop()


