import turtle

a = turtle.Turtle()
screen = turtle.Screen()
a.speed(0)

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def draw(self):
        a.penup()
        a.goto(self.x, self.y - self.radius)
        a.pendown()
        a.circle(self.radius)
    
    def getArea(self):
        area = 3.14 * (self.radius)**2
        return area
    
    def getPerimeter(self):
        perimeter = 2 * 3.14 * self.radius
        return perimeter
    
    def move(self):
        a.penup()
        a.goto(self.x, self.y + self.radius)
        a.pendown()

A = Circle(0, 0, 100)

A.draw()
A.move()

area = A.getArea()
perimeter = A.getPerimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)

turtle.exitonclick()
