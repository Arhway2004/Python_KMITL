import turtle as a
def draw_nested_squares(s,g):
    while s >=20:
        draw_square(s)
        s-=(g*2)


def draw_square(n):
    a.penup()
    a.back(n/2)
    a.left(90)
    a.forward(n/2)
    a.right(90)
    a.pendown()
    for x in range(4):
        a.fd(n)
        a.right(90)
    a.penup()
    a.forward(n/2)
    a.right(90)
    a.forward(n/2)
    a.left(90)

draw_nested_squares(200,20)
