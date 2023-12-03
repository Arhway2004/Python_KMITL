import turtle as t
t.speed(-1)

class Disc(t.Turtle):
    def __init__(self, height):
        t.Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.ht()
        self.shapesize(1.5, height * 1.5, 4)
        self.st()

class Tower(list):
    def __init__(self, posX):
        self.posX = posX

    def push(self, disk):
        disk.setpos(self.posX, -150 + (34 * len(self)))
        self.append(disk)

    def pop(self):
        disk = list.pop(self)
        disk.sety(150)
        return disk

def hanoi(height, source, auxiliary, target):
    if height > 0:
        hanoi(height - 1, source, target, auxiliary)
        target.push(source.pop())
        hanoi(height - 1, auxiliary, source, target)

def main():
    tower1 = Tower(-250)
    tower2 = Tower(0)
    tower3 = Tower(250)
    for i in range(7, 0, -1):
        tower1.push(Disc(i))
    hanoi(7, tower1, tower2, tower3)
    t.mainloop()

if __name__ == "__main__":
    main()
