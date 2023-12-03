# 1
import math

def print_btree(inputList, depth):
    for element in inputList:
        answer = '. ' * math.ceil(depth / 2) + str(element)
        print_btree(element, depth + 1) if type(element) == list else print(answer)

print_btree( [1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]], 0 )

# 2
def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return 2 * f(n // 2) + 1
    else:
        return 0

def display_f(n):
    for i in range(n + 1):
        result = f(i)
        print(f"f({i}) = {result}")

display_f(3)

# 3_1
def perm2(t):
    def generate_pairs(t, prefix):
        if len(prefix) == 2:
            print(prefix)
            return
        for i in range(len(t)):
            generate_pairs(t[:i] + t[i + 1:], prefix + (t[i],))

    generate_pairs(t, (), )


perm2((1, 2, 3))
# 3_2
def perm3(t):
    def generate_triples(t, prefix):
        if len(prefix) == 3:
            print(prefix)
            return
        for i in range(len(t)):
            generate_triples(t[:i] + t[i + 1:], prefix + (t[i],))

    generate_triples(t, ())

perm3((1, 2, 3, 4))

# 3_3
def perm(t, n):
    def generate_ntuples(t, prefix):
        if len(prefix) == n:
            print(prefix)
            return
        for i in range(len(t)):
            generate_ntuples(t[:i] + t[i + 1:], prefix + (t[i],))

    generate_ntuples(t, ())

perm((1, 2, 3), 3)

# 4
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

# 5
import tkinter as tk
import math

class Tree:
    def __init__(self):
        window = tk.Tk()
        window.title("Recursive Tree")
        window.resizable(width="false", height="false")
        # window.geometry('300x300+400+100')
        self.width, self.height = 300, 300
        self.canvas = tk.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        frame = tk.Frame(window)
        frame.pack()

        tk.Label(frame, text="Enter the depth ").grid(row=1, column=1, padx=2)
        self.depth = tk.Entry(frame, width=20, justify = "right")
        self.depth.grid(row=1, column=2)
        tk.Button(frame, text="Display", command=self.display).grid(row=1, column=3)

        window.mainloop()

    def display(self):
        self.canvas.delete(tk.ALL)
        check = min(self.width, self.height) // 3
        self.draw(self.width / 2, self.height - 15, self.width / 2, self.height - 15 - check, 0)

    def draw(self, x0, y0, x1, y1, current):
        self.canvas.create_line(x0, y0, x1, y1)
        if current < int(self.depth.get()):
            x2 = x1 + ((x1 - x0) * math.cos(0.1) - (y1 - y0) * math.sin(1)) / 2
            y2 = y1 + ((y1 - y0) * math.cos(0.1) + (x1 - x0) * math.sin(1)) / 2
            x3 = x1 + ((x1 - x0) * math.cos(0.1) + (y1 - y0) * math.sin(1)) / 2
            y3 = y1 + ((y1 - y0) * math.cos(0.1) - (x1 - x0) * math.sin(1)) / 2

            self.draw(x1, y1, x2, y2, current + 1)
            self.draw(x1, y1, x3, y3, current + 1)


Tree()