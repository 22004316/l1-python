import tkinter as tk


def color_pixel(event):
    x = event.x
    y = event.y
    canvas.create_line((x, y), (x+1, y), fill="red")


def clic_circle(event):
    x = event.x
    y = event.y
    if x <= 200:
        canvas.create_oval(x-50, y-50, x+50, y+50, fill="blue")
    elif x >= 300:
        canvas.create_oval(x-50, y-50, x+50, y+50, fill="red")     


root = tk.Tk()
root.title("Clic")


#création des widgets
canvas = tk.Canvas(root, height=500, width=500, bg="black")
canvas.create_line(250, 0, 250, 500, fill="white")
canvas.bind("<Button-1>", clic_circle)


#placement des widgets
canvas.grid()

root.mainloop()
