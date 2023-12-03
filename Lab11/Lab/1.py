class Point:
    def __init__(self, x=0.00, y=0.00):
        self.x = x
        self.y = y

    def pointinfo(self):
        print(f"Position: {self.x}, {self.y};")

class Circle(Point):
    def __init__(self, x=0.00, y=0.00, radius=0.00):
        super().__init__(x, y)  # Call the constructor of the parent class (Point)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def printinfo(self):
        super().pointinfo()  # Call the pointinfo method of the parent class (Point)
        print(f"Radius: {self.radius}; Area: {self.area()};")

# Create a Circle object
circle = Circle(2.0, 3.0, 5.0)

# Print information about the Circle
circle.printinfo()
