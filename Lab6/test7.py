import turtle as a

while True:
    user_input = input("turtle|>")
    
    if user_input == "quit":
        break
    elif user_input == "fd":
        argument = int(input("argument: "))
        a.forward(argument)
    elif user_input == "back":
        argument = int(input("argument: "))
        a.backward(argument)
    elif user_input == "left":
        argument = int(input("argument: "))
        a.left(argument)
    elif user_input == "right":
        argument = int(input("argument: "))
        a.right(argument)
    elif user_input == "pu":
        a.penup()
    elif user_input == "pd":
        a.pendown()
    elif user_input == "reset":
        a.reset()

a.done()
