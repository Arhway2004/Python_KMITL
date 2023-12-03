import turtle as t

def cercle(radius):
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()
    
    t.circle(radius)
    
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)

def spiral(n):
    while n >= 5:
        cercle(n)
        n *= 0.75

t.speed(0)  # Set the turtle drawing speed to maximum

spiral(150)

t.done()
