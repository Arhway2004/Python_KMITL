# import turtle
# a = turtle.Turtle()
# turtle = turtle.Screen()
# a.speed(0)

# X=int(input("X"))
# def rectangle(x,y,num):
#     a.penup()
#     a.goto(x,y)
#     a.pendown()
#     for x in range(4):
#         a.forward(num)
#         a.right(90)

# def loop():
#         x=-100
#         y=100
#         num=200
#         while num >= X:
#              rectangle(x,y,num)
#              x-=X
#              y-=X
#              num-=X
# loop()

# turtle.exitonclick()

# import turtle
# a = turtle.Turtle()
# turtle = turtle.Screen()
# a.speed(0)

# X=int(input("X"))
# def rectangle(x,y,num):
#     a.penup()
#     a.goto(x,y)
#     a.pendown()
#     for x in range(2):
#         a.forward(num)
#         a.right(90)
#         a.forward(num)
#         a.right(90)

# def loop():
#     x = -100
#     y = 100
#     num = 200
#     for xxx in range(4):
#         for xx in range(num // X):  # Adjust the loop range
#             rectangle(x, y, num)
#             x += X
#             y -= X
#             num -= X
#         a.penup()
#         a.goto(0,0)
#         a.pendown()
#         a.left(90)
# loop()

# turtle.exitonclick()
import turtle
a = turtle.Turtle()
screen = turtle.Screen()
a.speed(0)
X = int(input("Enter the value of X:"))


# def draw_rectangle(x, y, num):
#     a.penup()
#     a.goto(x, y)
#     a.pendown()
#     for _ in range(2):
#         a.forward(num)
#         a.right(90)
#         a.forward(num)
#         a.right(90)
def main_loop():
    x = -100
    y = 100
    num = 200
    for _ in range(4): 
        for _ in range(num // X): 
            a.penup()
            a.goto(x, y)
            a.pendown()
            for _ in range(2):
                a.forward(num)
                a.right(90)
                a.forward(num)
                a.right(90)
            x += X
            y -= X
            num -= X
def _4loop():
    for x in range(4):
        main_loop()
        a.right(90)

_4loop()


turtle.exitonclick()

