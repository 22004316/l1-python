import tkinter as tk

def color_pixel(event):
    x = event.x
    y = event.y
    canvas.create_line((x, y), (x+1,y), fill="red")

clic_count = 0
point = (0, 0)

def clic(event) : 
    global clic_count, point
    x = event.x
    y = event.y
    if clic_count == 0 :
        clic_count = 1
        point = (x, y)
    else :
        clic_count = 0
        if (250-x)*(250-point[0])> 0 :
            color = "blue"
        else : 
            color = "red"    
        canvas.create_line(point, (x,y), fill = color, width = 3)    


root = tk.Tk()
root.title("Clic")


#création des widgets
canvas = tk.Canvas(root, height=500, width=500, bg="black")
canvas.create_line(250, 0, 250, 500, fill = "white")
canvas.bind("<Button-1>", clic)


#placement des widgets
canvas.grid()

root.mainloop()
