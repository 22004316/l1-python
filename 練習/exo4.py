import tkinter as tk

root = tk.Tk()

HEIGHT = 500
WIDTH = 500
cote = 50
pause = False


def inside_square(x, y):
    '''returns True if the point (x, y) is inside the square
    and False otherwise'''
    inf = HEIGHT//2-cote//2
    sup = HEIGHT//2+cote//2
    return inf <= x <= sup and inf <= y <= sup


def change_size(event):
    global cote
    global pause
    if not pause:
        if inside_square(event.x, event.y) and cote >= 20:
            cote -= 10
            canvas.coords(square, WIDTH//2-cote//2, HEIGHT//2-cote//2, WIDTH
                          // 2+cote//2, HEIGHT//2+cote//2)
        elif not inside_square(event.x, event.y) and cote <= 100:
            cote += 10
            canvas.coords(square, WIDTH//2-cote//2, HEIGHT//2-cote//2, WIDTH
                          // 2+cote//2, HEIGHT//2+cote//2)


def button_pause():
    global pause
    if not pause:
        button.config(text="Restart")
        pause = True
    else:
        button.config(text="Pause")
        pause = False


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
button = tk.Button(root, text="Pause", command=button_pause)

square = canvas.create_rectangle(WIDTH//2-cote//2, HEIGHT//2-cote//2,
                                 WIDTH//2+cote//2, HEIGHT//2+cote//2,
                                 fill="red")

canvas.bind("<Button-1>", change_size)
canvas.grid(row=0)
button.grid(row=1)

root.mainloop()
