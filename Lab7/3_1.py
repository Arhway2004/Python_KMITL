import turtle
a = turtle.Turtle()
screen = turtle.Screen()
a.speed(0)
class Rectangle:
    def __init__(A,x,y,width,height):
        A.x =x
        A.y =y
        A.width =width
        A.height =height
    def rec1(self):
        LR1 = self.x[1] - self.width[1] / 2
        RR1 = self.x[1] + self.width[1] / 2
        TR1 = self.y[1] + self.height[1] / 2
        BR1 = self.y[1] - self.height[1]/ 2
    def overlap(self):
        LR2 = self.x[2] - self.width[2] / 2
        RR2 = self.x[2] + self.width[2] / 2
        TR2 = self.y[2] + self.height[2] / 2
        BR2 = self.y[2] - self.height[2]/ 2  
    def result(self):
        if (LR1 >= LR2 and RR1 <= RR2 and TR1 <= TR2 and BR1 >= BR2) or (LR1 <= LR2 and RR1 >= RR2 and TR1 >= TR2 and BR1 <= BR2):
            return("Rectangle 1 is inside Rectangle 2")
        elif(LR2 >= LR1 and RR2 <= RR1 and TR2 <= TR1 and BR2 >= BR1) or (LR2 <= LR1 and RR2 >= RR1 and TR2 >= TR1 and BR2 <= BR1):
            return("Rectangle 2 is inside Rectangle 1")
        elif RR1 < LR2 or LR1 > RR2 or TR1 < BR2 or BR1 > TR2:
            return("Rectangles do not overlap")
        else:
            return("Rectangles overlap")
    def draw(self):
        a.penup()
        a.goto(self.x, self.y)
        a.pendown()
        for _ in range(2):
            a.forward(self.width)
            a.left(90)
            a.forward(self.height)
            a.left(90)
    def print(self):
        print(self)

A=Rectangle(0,0,100,200)
B=Rectangle(-200,0,100,100)
A.draw()
B.draw()
print(QuadraticEquation1.getRoot1())

turtle.exitonclick()