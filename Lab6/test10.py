import turtle

t = turtle.Turtle()

def draw_sq(n):
    t.penup()
    t.left(90)
    t.forward(((3 ** (1 / 2)) * n) / 2)
    t.left(90)
    t.forward(n / 2)
    t.left(180)
    
    for _ in range(6):
        t.pendown()
        t.forward(n)
        t.right(60)
    
    t.penup()
    t.forward(n / 2)
    t.right(90)
    t.forward(((3 ** (1 / 2)) * n) / 2)
    t.left(90)

def draw_spiral(s):
    while s >= 5:
        draw_sq(s)
        t.left(10)
        s *=0.75

t.speed(0)  # Set the turtle drawing speed to maximum

draw_spiral(142)

turtle.done()
