import tkinter as tk

def create_circle(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10)

def remove_circle(event):
    x, y = event.x, event.y
    closest_circle = canvas.find_closest(x, y)
    if closest_circle:
        canvas.delete(closest_circle)

root = tk.Tk()
root.title("Circle Drawer")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

circles = []

canvas.bind("<Button-1>", create_circle)
canvas.bind("<Button-3>", remove_circle)

root.mainloop()
