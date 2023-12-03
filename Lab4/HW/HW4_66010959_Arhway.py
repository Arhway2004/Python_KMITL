#Homework1
import turtle

a = turtle.Turtle()
turtle = turtle.Screen()
a.speed(10)
x0,y0 = eval(input("input point0 coordination:"))
x1,y1 = eval(input("input point1 coordination:"))
x2,y2 = eval(input("input point2 coordination:"))
a.penup()
a.goto(x0,y0)
a.pendown()
a.write("point0")
a.goto(x1,y1)
a.write("point1")
a.penup()
a.goto(x2, y2)
a.pendown()
# formular

m = (y1 - y0) / (x1 - x0)
c = y0 - (m * x0)
formular = x2 * m + c
if abs(formular - y2) == 0 :
    if x2 > x0 and x2 < x1:
        a.write("P2 is on the line")
    elif x2 > x0 and x2 > x1:
        a.write("P2 is on the right side") 
    elif x2 < x0 and x2 < x1:
        a.write("P2 is on the left side")
    elif x2 < x0 and x2 > x1:
        a.write("P2 is on the line")     
elif x2 > x0 and x2 < x1:
    a.write("P2 is on the midle P0 is on the left and P1 is on the right")
elif x2 > x0 and x2 > x1:
    a.write("P2 is on the right side")
elif x2 < x0 and x2 < x1:
    a.write("P2 is on the left side")
elif y0 == y1: 
    if x2 > x0:
        a.write("p2 is on the lower side of the line.")
    elif x2 > x1:
        a.write("p2 is on the upper side of the line.")
    elif x2 == x1 == x0:
        a.write("p2 is on the same line as p0 and p1.")
a.end_fill()
a.hideturtle()
turtle.exitonclick()

#Homework2
x1, y1 = eval(input("Input the center coordinates of Rectangle 1 x and y: "))
w1, h1 = eval(input("Input the width and height of Rectangle 1: "))
x2, y2 = eval(input("Input the center coordinates of Rectangle 2 x and y: "))
w2, h2 = eval(input("Input the width and height of Rectangle 2: "))
# R1
LR1 = x1 - w1 / 2
RR1 = x1 + w1 / 2
TR1 = y1 + h1 / 2
BR1 = y1 - h1 / 2
# R2
LR2 = x2 - w2 / 2
RR2 = x2 + w2 / 2
TR2 = y2 + h2 / 2
BR2 = y2 - h2 / 2
# formular & result
if (LR1 >= LR2 and RR1 <= RR2 and TR1 <= TR2 and BR1 >= BR2) or \
        (LR1 <= LR2 and RR1 >= RR2 and TR1 >= TR2 and BR1 <= BR2):
    print("Rectangle 1 is inside Rectangle 2")
elif(LR2 >= LR1 and RR2 <= RR1 and TR2 <= TR1 and BR2 >= BR1) or \
        (LR2 <= LR1 and RR2 >= RR1 and TR2 >= TR1 and BR2 <= BR1):
    print("Rectangle 2 is inside Rectangle 1")
elif RR1 < LR2 or LR1 > RR2 or TR1 < BR2 or BR1 > TR2:
    print("Rectangles do not overlap")
else:   
    print("Rectangles overlap")
