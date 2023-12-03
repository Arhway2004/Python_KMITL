# 1
class Clock:
    def __init__(self):
        self.hh = 0
        self.mm = 0 
        self.ss = 0  

    def run(self):
        while True:
            self.display_time()
            self.increment_time()

    def increment_time(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
                if self.hh == 24:
                    self.hh = 0

    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m
        self.ss = s

    def display_time(self):
        print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")


class AlarmClock(Clock):
    def __init__(self):
        super().__init__()
        self.alarm_hh = 0
        self.alarm_mm = 0
        self.alarm_ss = 0
        self.alarm_on_off = False

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s

    def alarm_on(self):
        self.alarm_on_off = True

    def alarm_off(self):
        self.alarm_on_off = False

    def run(self):
        while True:
            self.display_time()
            self.display_alarm_time()
            self.increment_time()
            if self.alarm_on_off and self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                print("Alarm is going off!")
                break

    def display_alarm_time(self):
        print(f"Alarm Time: {self.alarm_hh:02d}:{self.alarm_mm:02d}:{self.alarm_ss:02d}")


# Example usage:
clock = AlarmClock()
clock.setTime(9, 30, 0)
clock.setAlarmTime(10, 31, 0) 
clock.alarm_on() 
clock.run()  

# 2
import turtle

class Robot(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100

    def move(self, newX, newY):
        if self.energy > 0:
            self.x = newX
            self.y = newY
            self.energy -= 10

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.circle(20)
        turtle.penup()

    def displayStatus(self):
        print(f"x={self.x}, y={self.y}, health={self.health}, energy={self.energy}")

    def command(self, robotList):
        print("Possible actions: move")
        action = input("Enter action ('move'): ")
        if action == 'move':
            new_x = int(input("Enter new x-coordinate: "))
            new_y = int(input("Enter new y-coordinate: "))
            self.move(new_x, new_y)

class MedicBot(Robot):
    def heal(self, r):
        if self.energy >= 20 and abs(self.x - r.x) <= 10 and abs(self.y - r.y) <= 10:
            self.energy -= 20
            r.health += 10

    def command(self, robotList):
        print("Possible actions: move, heal")
        action = input("Enter action ('move' or 'heal'): ")
        if action == 'move':
            super().command(robotList)
        elif action == 'heal':
            target = int(input("Enter the index of the robot to heal: "))
            if 0 <= target < len(robotList):
                self.heal(robotList[target])

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and abs(self.x - r.x) <= 10 and abs(self.y - r.y) <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50

    def displayStatus(self):
        super().displayStatus()
        print(f"missile={self.missile}")

    def command(self, robotList):
        print("Possible actions: move, strike")
        action = input("Enter action ('move' or 'strike'): ")
        if action == 'move':
            super().command(robotList)
        elif action == 'strike':
            target = int(input("Enter the index of the robot to strike: "))
            if 0 <= target < len(robotList):
                self.strike(robotList[target])

def RobotBattle():
    robotList = []
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    while True:
        turtle.clear()
        for robot in robotList:
            robot.draw()
        print("==== Robot ====")
        for i, robot in enumerate(robotList):
            print(i, ":")
            robot.displayStatus()
        print("=============")
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList.append(newRobot)
        elif choice.isdigit() and 0 <= int(choice) < len(robotList):
            n = int(choice)
            robotList[n].command(robotList)
        else:
            print("Invalid input. Please enter a valid choice.")

        robotList = [robot for robot in robotList if robot.health > 0]

    turtle.done()

RobotBattle()

# 3
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RectangleD:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def getWidth(self):
        return abs(self.x2 - self.x1)

    def getHeight(self):
        return abs(self.y2 - self.y1)

    def getCenter(self):
        center_x = (self.x1 + self.x2) / 2.0
        center_y = (self.y1 + self.y2) / 2.0
        return Point(center_x, center_y)

def getRectangle(points):
    if len(points) % 2 != 0:
        raise ValueError("Input should contain an even number of coordinates")

    min_x = float('inf')
    min_y = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')

    for i in range(0, len(points), 2):
        x = float(points[i])
        y = float(points[i + 1])

        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    bounding_rect = RectangleD(min_x, min_y, max_x, max_y)
    return bounding_rect

def drawRectangle(rectangle):
    turtle.penup()
    turtle.goto(rectangle.x1, rectangle.y1)
    turtle.pendown()
    
    for _ in range(2):
        turtle.forward(rectangle.getWidth() * 10)
        turtle.left(90)
        turtle.forward(rectangle.getHeight() * 10)
        turtle.left(90)

    turtle.penup()
    turtle.goto(rectangle.getCenter().x * 10, rectangle.getCenter().y * 10)
    turtle.pendown()

if __name__ == "__main__":
    input_points = input("Enter the points (as x1 y1 x2 y2 x3 y3 ...): ").split()
    
    try:
        bounding_rect = getRectangle(input_points)
        center = bounding_rect.getCenter()
        width = bounding_rect.getWidth()
        height = bounding_rect.getHeight()
        
        print(f"The bounding rectangle is centered at ({center.x}, {center.y}) "
              f"with width {width} and height {height}")
        
        turtle.speed(10) 
        drawRectangle(bounding_rect)
        turtle.done()
        
    except ValueError as e:
        print(f"Error: {e}")
# 3_1
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
# 3_2
class StationaryGood:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_cost(self):
        return self.price

class Magazine(StationaryGood):
    def __init__(self, name, price):
        super().__init__(name, price)

class Book(StationaryGood):
    def __init__(self, name, price):
        discounted_price = price * 0.9
        super().__init__(name, discounted_price)

class Ribbon(StationaryGood):
    def __init__(self, name, length_in_meters, price_per_meter):
        self.length_in_meters = length_in_meters
        cost = length_in_meters * price_per_meter
        super().__init__(name, cost)

def getTotalCost(basket):
    total_cost = 0
    for item in basket:
        total_cost += item.get_cost()
    return total_cost

basket = [
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Magazine("Computer World", 70),
    Book("Windows 7 for Beginners", 200),
    Book("Windows 7 for Beginners", 200),
    Ribbon("Blue Ribbon", 10, 5),
]

total_cost = getTotalCost(basket)

print(f"Total cost of goods in the basket: {total_cost} Bahts")

