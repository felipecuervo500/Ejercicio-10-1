import tkinter as tk
def Mostrar():
    if seleccion.get()==1:
        mensaje="Tu sabor es Pollo y champiñones"
    if seleccion.get()==2:
        mensaje="Tu sabor es Hawaiana"
    if seleccion.get()==3:
        mensaje="Tu sabor es Carnes"
    if seleccion.get()==4:
        mensaje="Tu sabor es Super Especial"
    if seleccion.get()==5:
        mensaje="Tu sabor es Mexicana"
    if seleccion.get()==6:
        mensaje="Por favor escoge de nuevo"

    lblMensaje.config(text=mensaje)

window = tk.Tk()
seleccion = tk.IntVar()

rbnPolloChampi = tk.Radiobutton(window, text="Pollo y champiñones", variable=seleccion, value=1, 
    command=Mostrar).pack( anchor = tk.W )

rbnHawai = tk.Radiobutton(window, text="Hawaiana", variable=seleccion, value=2, 
    command=Mostrar).pack( anchor = tk.W )

rbnCarnes = tk.Radiobutton(window, text="Carnes", variable=seleccion, value=3, 
    command=Mostrar).pack( anchor = tk.W )

rbnSuperE = tk.Radiobutton(window, text="Super Especial", variable=seleccion, value=4, 
    command=Mostrar).pack( anchor = tk.W )

rbnMexi = tk.Radiobutton(window, text="Mexicana", variable=seleccion, value=5, 
    command=Mostrar).pack( anchor = tk.W )

rbnReini = tk.Radiobutton(window, text="Reiniciar", variable=seleccion, value=6, 
    command=Mostrar).pack( anchor = tk.W )

lblMensaje = tk.Label(window)
lblMensaje.pack()

window.mainloop()
