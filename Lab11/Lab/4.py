from abc import abstractmethod
import turtle

class TwoDShape: 
    
    @abstractmethod
    def draw():
        pass
    

class Line(TwoDShape):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def draw(self): 
        turtle.penup()
        turtle.goto(self.x1, self.y1)
        turtle.pendown()
        turtle.goto(self.x2, self.y2)
        turtle.penup()
        
class Rectangle(TwoDShape):
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self): 
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.goto(self.x + self.width, self.y)
        turtle.goto(self.x + self.width, self.y + self.height)
        turtle.goto(self.x, self.y + self.height)
        turtle.goto(self.x, self.y)
        turtle.penup()
        
        
class Circle(TwoDShape):
    def __init__(self, x, y, radius):
        self.x = x 
        self.y = y
        self.radius = radius
        
    def draw(self): 
        turtle.penup()
        turtle.goto(self.x, self.y - self.radius)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        
class Square(TwoDShape): 
    def __init__(self, x, y, width):
        self.x = x 
        self.y = y
        self.width = width
        
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.goto(self.x + self.width, self.y)
        turtle.goto(self.x + self.width, self.y + self.width)
        turtle.goto(self.x, self.y + self.width)
        turtle.goto(self.x, self.y)
        turtle.penup()
        
sq1 = Square(0,0, 50)
sq1.draw()
rec1 = Rectangle(0,0, 50, 80)
rec1.draw()
turtle.penup()

turtle.pendown()
sq2 = Square(50,0, 50)
sq2.draw()
line = Line(50, 0, 100, 80)
line.draw()
turtle.penup()

turtle.pendown()
sq3 = Square(100,0, 50)
sq3.draw()
circle = Circle(125, 25, 10)
circle.draw()
turtle.penup()

turtle.pendown()
sq4 = Square(150,0, 50)
sq4.draw()
line2 = Line(160, 0, 190, 80)
line2.draw()
turtle.penup()

turtle.pendown()
sq5 = Square(200,0, 50)
sq5.draw()
circle2 = Circle(225, 25, 10)
circle2.draw()
turtle.penup()


turtle.exitonclick()

