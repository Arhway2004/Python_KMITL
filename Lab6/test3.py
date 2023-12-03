import turtle as a
def draw_sq(size):
    a.penup()
    a.backward(size/2)
    a.left(90)
    a.forward(size/2)
    a.right(90)
    a.pendown()
    for x in range(4):
        a.forward(size)
        a.right(90)
    a.penup()
    a.forward(size/2)
    a.right(90)
    a.forward(size/2)
    a.left(90)

def spiral_sq(size):

    while size>5: 
        draw_sq(size)
        a.left(10)
        size*=0.75
        


spiral_sq(150)
a.done()
        





