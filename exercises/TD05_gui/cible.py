import tkinter as tk
import random

root = tk.Tk()
root.title('cible')

colors = [ "blue", "green", "black", "yellow", "magenta", "red"]
length = random.randint(500,1000)
number_of_circles = random.randint(1,100)
circle_width = length // (number_of_circles*2)

canvas = tk.Canvas(root, width = length, height = length,bg = "black",
 relief = "raised")

for i in range(number_of_circles) :
    canvas.create_oval(circle_width*i, circle_width*i, length-(circle_width
    *i), length-(circle_width*i), fill = colors[i % len(colors)], 
    outline = colors[i % len(colors)] )



canvas.grid()




root.mainloop() 

