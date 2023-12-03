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
