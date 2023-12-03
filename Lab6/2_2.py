import turtle
a = turtle.Turtle()
screen = turtle.Screen()
a.speed(0)
X = int(input("Enter the value of X:"))
a.left(90)
def draw_rectangle(Go):
    for x in range(4):
        a.forward(Go)
        a.right(90)
def main_loop():
    Go=X
    for y in range(4):
        for x in range(4):
            draw_rectangle(Go)
            Go+=X
        Go-=(X*4)
        a.penup()
        a.goto(0,0)
        a.pendown()
        a.right(90)

main_loop()

turtle.exitonclick()