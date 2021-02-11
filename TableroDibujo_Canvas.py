import tkinter as tk

#Funcion
#function
def dibujar(event):
    colorTool = 'grey'
    x1, y1 = (event.x - 1) , (event.y - 1)
    x2, y2 = (event.x + 1) , (event.y + 1)
    canvas.create_oval(x1,y1,x2,y2, fill = colorTool)


# Tamaño del tablero
canvas_ancho = 500
canvas_alto = 500

#Iniciamos
#start
master = tk.Tk()
master.title("Dibujar con el mouse.")

#Llamamos libreria
#I call bookstore
canvas=tk.Canvas(master, width=canvas_ancho, height=canvas_alto)
canvas.pack(fill=tk.BOTH)
canvas.bind("<B1-Motion>", dibujar)

#Etiqueta instruccion
#Instruction label
mensaje=tk.Label(master, text = "Mantenga presionado click izquierdo para dibujar.")
mensaje.pack(side=tk.BOTTOM)

#Bucle
#loop
master.mainloop()
