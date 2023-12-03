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
