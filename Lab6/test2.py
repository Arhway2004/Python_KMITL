import turtle

a = turtle.Turtle()
turtle_screen = turtle.Screen()
a.speed(0)

def turtles(word):
    while word != "quiet":
        argument = 0
        if word == "fd":
            argument = int(input("Argument: "))
            a.forward(argument)
        elif word == "back":
            argument = int(input("Argument: "))
            a.backward(argument)
        word = input("Enter command ('fd', 'back', or 'quiet'): ")

initial_word = input("Enter  ")
turtles(initial_word)

turtle_screen.exitonclick()
