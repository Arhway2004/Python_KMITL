import turtle as a

def draw(number):
    a.penup()
    a.left(90)
    a.forward(((3**1/2)*number)/2)
    a.right(90)
    a.backward((number / 2))
    a.pendown()
    for i in range(6):
        a.forward(number)
        a.right(60)
    a.penup()
    a.forward((number / 2))
    a.right(90)
    a.forward(((3**1/2)*number)/2)
    a.left(90)

def draw_r(number):
    while number>20:
        draw(number)
        # a.right(10)
        number-=30
a.speed()
draw_r(250)
a.done
