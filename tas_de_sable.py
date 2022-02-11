import tkinter as tk


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", width=600, height=600)
score= tk.Button(racine, text="Score", fg="black", bg="white")

canvas.create_rectangle(562.5, 150, 600,187.5, fill="white")
canvas.create_rectangle(187.5, 75, 225,112.5, fill="white")
canvas.create_rectangle(450, 525, 487.5,562.5, fill="white")
canvas.create_rectangle(0, 450, 37.5,487.5, fill="white")


a, u = 0, 0

while a != 16 :
    canvas.create_line(37.5+u,0, 37.5+u,600)
    canvas.create_line(0,37.5+u, 600,37.5+u)
    u += 37.5
    a+=1

canvas.grid(column=0, row=1)
score.grid(column=0, row=2)


racine.mainloop()