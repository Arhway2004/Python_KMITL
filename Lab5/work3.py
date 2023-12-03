# import turtle
# a = turtle.Turtle()
# a.speed(10)
# a.pencolor("black")
# a.fillcolor("black") 


# A = eval(input("enter N"))
# Y = 100/A
# Y_Y = 100/A
# for w in range(A):
#     for x in range(A):#x
#         for y in range(4):
#             a.forward(Y)
#             a.right(90)
#         a.forward(Y)
#     a.penup()
#     a.goto(0,-(Y_Y))
#     a.pendown()
#     Y_Y += Y
# turtle.exitonclick()
import turtle

a = turtle.Turtle()
a.speed(10)
a.pencolor("black")
a.fillcolor("black")

A = eval(input("Enter N: "))
Y = 100 / A
Y_Y = 100 / A

for row in range(A):
    for column in range(A):
        if (row + column) % 2 == 0:  # Check if row + column is even
            a.begin_fill()
        for x in range(4):
            a.forward(Y)
            a.right(90)
        a.forward(Y)
        if (row + column) % 2 == 0:
            a.end_fill()

    a.penup()
    a.goto(0, -(Y_Y))
    a.pendown()
    Y_Y += Y

turtle.exitonclick()
