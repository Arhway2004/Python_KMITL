import turtle

a = turtle.Turtle()
screen = turtle.Screen()
a.speed(0)

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def intersect(self, other):
        LR1 = self.x - self.width / 2
        RR1 = self.x + self.width / 2
        TR1 = self.y + self.height / 2
        BR1 = self.y - self.height / 2
        
        LR2 = other.x - other.width / 2
        RR2 = other.x + other.width / 2
        TR2 = other.y + other.height / 2
        BR2 = other.y - other.height / 2
        
        if (LR1 >= LR2 and RR1 <= RR2 and TR1 <= TR2 and BR1 >= BR2) or \
           (LR1 <= LR2 and RR1 >= RR2 and TR1 >= TR2 and BR1 <= BR2):
            return "Rectangle 1 is inside Rectangle 2"
        elif (LR2 >= LR1 and RR2 <= RR1 and TR2 <= TR1 and BR2 >= BR1) or \
             (LR2 <= LR1 and RR2 >= RR1 and TR2 >= TR1 and BR2 <= BR1):
            return "Rectangle 2 is inside Rectangle 1"
        elif RR1 < LR2 or LR1 > RR2 or TR1 < BR2 or BR1 > TR2:
            return "C = A is not intersect B"
        else:
            return "C = A.intersect(B)"
    
    def draw(self):
        a.penup()
        a.goto(self.x - self.width / 2, self.y - self.height / 2)
        a.pendown()
        for _ in range(2):
            a.forward(self.width)
            a.left(90)
            a.forward(self.height)
            a.left(90)

A = Rectangle(0, 0, 100, 200)
B = Rectangle(-200, 0, 100, 100)

A.draw()
B.draw()

print(A.intersect(B))


turtle.exitonclick()
