import turtle

a = turtle.Turtle()
turtle = turtle.Screen()
a.speed(10)
A = eval(input("enter N"))
S = 100
# a.right(90)
Y = 100/A
Y_Y = 100/A
for w in range(A):
    for x in range(A):#x
        for y in range(4):
            a.forward(Y)
            a.right(90)
        a.forward(Y)
    a.penup()
    a.goto(0,-(Y_Y))
    a.pendown()
    Y_Y += Y
# for x in range(5):#x
#     for y in range(4):
#         a.forward(20)
#         a.right(90)
#     a.forward(20)
    
    
    # if x == 4:
        # continue
    # a.right(90)




a.end_fill()
a.hideturtle()
turtle.exitonclick()
