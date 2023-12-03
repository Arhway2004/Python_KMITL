import tkinter as T
from tkinter import messagebox
import random

def draw_random_oval(event):
    x, y = event.x, event.y
    if 50 <= x <= 400 and 50 <= y <= 250:
        canvas.create_oval(x, y, x+10, y+10, fill=random.choice(colors))
    else:
        messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")

screen = T.Tk()
screen.title("tk")

canvas = T.Canvas(screen, width=400, height=400)
canvas.pack()

canvas.create_rectangle(50, 50, 400, 250, outline="black")
colors = ["yellow", "black", "red", "green", "brown", "blue", "white", "brown", "pink", "purple"]
canvas.bind("<Button-1>", draw_random_oval)

screen.mainloop()
