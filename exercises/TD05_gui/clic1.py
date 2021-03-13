import tkinter as tk


def color_pixel(event):
    x = event.x
    y = event.y
    canvas.create_line((x, y), (x+1,y), fill="red")


root = tk.Tk()
root.title("Clic")

#création des widgets
canvas = tk.Canvas(root, height=500, width=500, bg="black")

canvas.bind("<Button-1>", color_pixel)


#placement des widgets
canvas.grid()

root.mainloop()
