# import tkinter as tk
# window = tk.Tk()
# window.title("C语言中文网")
# window.geometry('400x200')
# # 创库不允许改变
# window.resizable(0,0)
# window.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# # 创建画布
# canvas = tk.Canvas(window,
#                    bg='#CDC9A5',
#                    height=200,
#                    width=300)
# canvas.pack()
# window.mainloop()

from tkinter import *
from tkinter import messagebox
import random

class Helpme:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, bg="white", width=600, height=400)
        self.canvas.pack(fill=BOTH, expand=True)
        self.displayrec()
        self.canvas.bind("<Button-1>", self.displaycircle)
        window.mainloop()
    def displayrec(self):
        self.canvas.create_rectangle(50, 50, 400, 250, outline="black", tags = "rec")
    def displaycircle(self, event):
        color = ["yellow", "black", "red", "green", "brown", "blue", "white", "brown", "pink", "purple"]
        x, y = event.x, event.y
        if 50 <= x <= 400 and 50 <= y <= 250:
            self.canvas.create_oval(x, y, x+10, y+10, fill = random.choice(color))
        else:
            messagebox.showwarning("Warning", "Mouse pointer is not in the rectangle")

Helpme()