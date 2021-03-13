import tkinter as tk

HEIGHT = 500
WIDTH = 500
square_count = 0
circle_count = 0
cross_count = 0


def draw_cross(x, y):
    canvas.create_line((x-25, y-25), (x+25, y+25), fill="blue", width=3)
    canvas.create_line((x-25, y+25), (x+25, y-25), fill="blue", width=3)


def draw_square(x, y):
    canvas.create_rectangle((x-25, y-25), (x+25, y+25), fill="green")


def draw_circle(x, y):
    canvas.create_oval((x-25, y-25), (x+25, y+25), fill="red")


def clic(event):
    x = event.x
    y = event.y
    global cross_count, square_count, circle_count
    if x <= WIDTH//3 and cross_count < 2:
        draw_cross(x, y)
        cross_count += 1
    elif WIDTH//3 <= x <= (WIDTH//3)*2 and square_count < 3:
        draw_square(x, y)
        square_count += 1
    elif (WIDTH//3)*2 <= x <= WIDTH and circle_count < 3:
        draw_circle(x, y)
        circle_count += 1


def restart():
    global cross_count, square_count, circle_count
    cross_count = 0
    square_count = 0
    circle_count = 0
    canvas.delete("all")
    canvas.create_line((WIDTH//3, 0), (WIDTH//3, HEIGHT), fill="white")
    canvas.create_line((WIDTH-WIDTH//3, 0), (WIDTH-WIDTH//3, HEIGHT),
                       fill="white")


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
button = tk.Button(root, text="Restart", command=restart)

canvas.create_line((WIDTH//3, 0), (WIDTH//3, HEIGHT), fill="white")
canvas.create_line((WIDTH-WIDTH//3, 0), (WIDTH-WIDTH//3, HEIGHT), fill="white")
canvas.grid(row=0)
button.grid(row=1)
canvas.bind("<Button-1>", clic)


root.mainloop()
