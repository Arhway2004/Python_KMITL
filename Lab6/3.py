# import turtle
# a = turtle.Turtle()
# screen = turtle.Screen()
# a.speed(0)
# def polygon(x=0, y=0,z=4,size=100):
#     x= int(input("Enter the value of X:"))
#     y= int(input("Enter the value of Y:"))
#     z= int(input("Enter the value of Z:"))
#     size= int(input("Enter the value of Size:"))
#     S=360/z
#     a.penup()
#     a.goto(x,y)
#     a.pendown()
#     for x in range(z):
#         a.forward(size)
#         a.right(S)
# polygon()


# turtle.exitonclick()
# import turtle

# a = turtle.Turtle()
# screen = turtle.Screen()
# a.speed(0)

# def polygon():
#     x = int(input("Enter the value of X: "))
#     y = int(input("Enter the value of Y: "))
#     z = int(input("Enter the number of sides: "))
#     size = int(input("Enter the size of sides: "))
    
#     S = 360 / z
#     a.penup()
#     a.goto(x, y)
#     a.pendown()
#     for x in range()
#     for _ in range(z):
#         a.forward(size)
#         a.right(S)

# polygon()

# turtle.exitonclick()
import turtle
turtle.speed(0)

#x, y, shape, side
def draw_polygon(x, y, shape=4, size=100):
    
    turtle.goto(x, y)
    for i in range(shape):
        turtle.pendown()
        turtle.forward(size)
        turtle.left(360/shape)
        turtle.penup()
    
turtle.penup()
draw_polygon(10, 10, 4, 200) 

turtle.exitonclick()
