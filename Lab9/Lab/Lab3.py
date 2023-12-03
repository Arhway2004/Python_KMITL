# import tkinter as  T

# drawing = False
# last_x, last_y = None, None

# screen = T.Tk(screenName=None, baseName=None, className="JJ", useTk=1)
# screen.title("Spiner")
# screen.geometry('450x300')
# text=T.Label(screen,text="Drag the mouse to draw")
# canvas = T.Canvas(screen,bg="white",width = "400", height = "400")

# def start_drawing(event):
#     global drawing, last_x, last_y
#     drawing = True
#     last_x, last_y = event.x, event.y
# def stop_drawing(event):
#     global drawing
#     drawing = False

# def draw(event):
#     global canvas, last_x, last_y
#     if drawing:
#         x, y = event.x, event.y
#         canvas.create_line(last_x, last_y, x, y, fill="black", width=2)
#         last_x, last_y = x, y


# canvas.bind("<Button-1>", start_drawing)
# canvas.bind("<ButtonRelease-1>", stop_drawing)
# canvas.bind("<B1-Motion>", draw)

# button_1 = T.Button(screen,text='clear',width=5, height=2,command=lambda: canvas.delete("all")).pack()


# screen.mainloop()

import tkinter as T


drawing = False
last_x, last_y = None, None


root = T.Tk()
root.title("Draw with Mouse")


canvas = T.Canvas(root, bg="white", width=400, height=400)
canvas.pack()

def start_drawing(event):
    global drawing, last_x, last_y
    drawing = True
    last_x, last_y = event.x, event.y

def stop_drawing(event):
    global drawing
    drawing = False

def draw(event):
    global canvas, last_x, last_y
    if drawing:
        x, y = event.x, event.y
        canvas.create_line(last_x, last_y, x, y, fill="black", width=2)
        last_x, last_y = x, y




canvas.bind("<Button-1>", start_drawing)
canvas.bind("<ButtonRelease-1>", stop_drawing)
canvas.bind("<B1-Motion>", draw)

text=T.Label(root,text="Drag the mouse to draw").pack()
clear_button = T.Button(root, text="Clear", command=lambda: canvas.delete("all")).pack()


root.mainloop()
