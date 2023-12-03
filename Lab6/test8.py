import turtle as t

def tri(n):
    t.penup()
    t.left(90)
    t.forward((n * (3 ** (1 / 2))) / 4)
    t.right(90)
    t.pendown()
    
    t.right(60)
    t.forward(n)
    t.right(120)
    t.forward(n)
    t.right(120)
    t.forward(n)
    
    t.penup()
    t.right(150)
    t.forward((n * (3 ** (1 / 2))) / 4)
    t.left(90)

def spiral(n):
    while n >= 5:
        tri(n)
        t.right(10)
        n *= 0.65

t.speed(1)  # Set the turtle drawing speed to maximum

spiral(150)

t.done()
