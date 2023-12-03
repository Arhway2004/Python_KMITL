import turtle

class Char:
    def draw(self, x, y):
        pass

    def getWidth(self):
        pass

class Char0(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(50)
        turtle.penup()

    def getWidth(self):
        return 100

class Char1(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x + 25, y + 100)
        turtle.pendown()
        turtle.setheading(270)
        turtle.forward(200)
        turtle.penup()

    def getWidth(self):
        return 50

class Char2(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.penup()

    def getWidth(self):
        return 100

class Char3(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fd(100)
        turtle.right(90)
        turtle.fd(50)
        turtle.right(90)
        turtle.fd(100)
        turtle.right(180)
        turtle.fd(100)
        turtle.right(90)
        turtle.fd(50)
        turtle.right(90)
        turtle.fd(100)
        turtle.penup()

    def getWidth(self):
        return 100

class Char4(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.right(135)
        turtle.forward(100)
        turtle.left(135)
        turtle.forward(100)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(100)
        turtle.penup()

    def getWidth(self):
        return 100

class Char5(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(0)
        turtle.backward(100)
        turtle.left(90)
        turtle.backward(100)
        turtle.left(90)
        turtle.backward(100)
        turtle.right(90)
        turtle.backward(100)
        turtle.right(90)
        turtle.backward(100)
        turtle.penup()

    def getWidth(self):
        return 100

class Char6(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(100)
            turtle.right(90)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.penup()

    def getWidth(self):
        return 100

class Char7(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(100)
        turtle.right(135)
        turtle.forward(140)
        turtle.penup()

    def getWidth(self):
        return 100

class Char8(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(100)
        turtle.right(180)
        turtle.circle(150)
        turtle.penup()

    def getWidth(self):
        return 100

class Char9(Char):
    def draw(self, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        for _ in range(6):
            turtle.forward(100)
            turtle.right(90)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.penup()

    def getWidth(self):
        return 100

char_objects = {
    '0': Char0(),
    '1': Char1(),
    '2': Char2(),
    '3': Char3(),
    '4': Char4(),
    '5': Char5(),
    '6': Char6(),
    '7': Char7(),
    '8': Char8(),
    '9': Char9(),
}

def drawNum(x):
    if isinstance(x, int):
        x = str(x)

    total_width = 0
    for digit in x:
        if digit in char_objects:
            char = char_objects[digit]
            char_width = char.getWidth()
            char.draw(total_width, 0)
            total_width += char_width + 10

if __name__ == "__main__":
    turtle.speed(1)
    input_digit = input("Enter a number or a string of digits (0-9): ")
    drawNum(input_digit)
    turtle.done()
