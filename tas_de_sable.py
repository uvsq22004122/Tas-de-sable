import tkinter as tk

racine = tk.Tk() # Création de la fenêtre racine
canvas = tk.Canvas(racine, bg="red", height=500, width=500)
canvas.grid()
racine.mainloop()