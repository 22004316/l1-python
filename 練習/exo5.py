import tkinter as tk

HEIGHT = 600
WIDTH = 600
line1 = 200
line2 = 400
clic_count = 0


def clic(event):
    global line1, line2, clic_count
    x = event.x
    if x <= line1:
        line1 -= 10
        line2 -= 10
        change_color()
        canvas.coords(left_line, line1, 0, line1, 600)
        canvas.coords(right_line, line2, 0, line2, 600)
    elif line1 < x <= line2:
        line1 += 10
        line2 -= 10
        change_color()
        canvas.coords(left_line, line1, 0, line1, 600)
        canvas.coords(right_line, line2, 0, line2, 600)
    else:
        line1 += 10
        line2 += 10
        change_color()
        canvas.coords(left_line, line1, 0, line1, 600)
        canvas.coords(right_line, line2, 0, line2, 600)


def change_color():
    global clic_count, left_line, right_line
    if clic_count == 0:
        canvas.itemconfig(left_line, fill="blue")
        canvas.itemconfig(right_line, fill="red")
        clic_count = 1
    else:
        canvas.itemconfig(left_line, fill="red")
        canvas.itemconfig(right_line, fill="blue")
        clic_count = 0


def restart():
    global line1, line2
    canvas.delete('all')
    line1 = 200
    line2 = 400
    canvas.create_line((line1, 0), (line1, 600), fill="red")
    canvas.create_line((line2, 0), (line2, 600), fill="blue")


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
button = tk.Button(root, text="Restart", command=restart)

left_line = canvas.create_line((WIDTH//3, 0), (WIDTH//3, HEIGHT), fill="red")
right_line = canvas.create_line((WIDTH-WIDTH//3, 0), (WIDTH-WIDTH//3, HEIGHT),
                                fill="blue")

canvas.grid(row=0)
button.grid(row=1)
canvas.bind("<Button-1>", clic)

root.mainloop()
