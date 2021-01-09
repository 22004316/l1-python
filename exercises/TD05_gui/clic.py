import tkinter as tk

nb_clic=0
point=(0,0)

def clic(event):
    global nb_clic, point
    x = event.x
    y = event.y
    if nb_clic == 0:
        nb_clic = 1
        point=(x, y)
    else:
        nb_clic = 0
        if (WIDTH/2 - x) * (WIDTH/2 - point[0]) > 0  :
            color="blue"
        
        else:
            color="red"
        
        canvas.create_line(point, (x, y), fill=color)   



root = tk.Tk()
root.title("Clic")


#création des widgets
HEIGHT=500
WIDTH=500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
canvas.create_line((WIDTH/2, 0),(WIDTH/2,HEIGHT), fill="white")

canvas.bind("<Button-1>", clic)



#placement des widgets
canvas.grid()

root.mainloop()








import tkinter as tk

#définition de la fonction:
nb_clic=0
def clic(event):
    global nb_clic
    if nb_clic % 2 == 0:
        color="white"
    else:
        color="black"
    nb_clic+=1
    canvas.itemconfigure(carre, fill=color)
    if nb_clic > 9 :
        root.destroy()

        


root = tk.Tk()
root.title("Clic")


#création des widgets
HEIGHT=500
WIDTH=500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
carre = canvas.create_rectangle((WIDTH/2 - 50, HEIGHT/2 - 50),(WIDTH/2 + 50, HEIGHT/2 + 50), fill="black", outline="red")

canvas.bind("<Button-1>", clic)


#placement des widgets
canvas.grid()

root.mainloop()






import tkinter as tk

cpt = 0
objets = []

def clic(event):
    global cpt, objets
    x = event.x
    y = event.y

    if cpt < 8:
        objets.append(canvas.create_oval((x-25, y-25), (x+25,y+25), fill="red"))
    
    elif cpt == 8:
        for i in range(len(objets)):
            canvas.itemconfigure(objets[i], fill="yellow")

    elif cpt == 9:
        for i in objets:
            canvas.delete(i)   
        cpt = 0
        objets = []

    cpt += 1



root = tk.Tk()
root.title("Clic")


#création des widgets
HEIGHT=500
WIDTH=500

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")

canvas.bind("<Button-1>", clic)



#placement des widgets
canvas.grid()

root.mainloop()