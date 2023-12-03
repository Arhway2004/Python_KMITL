# import turtle

# def main():
#     print("Hello, welcome to Turtle World!")
#     while True:
#         command = input("turtle|>")
#         if command == "quit":
#             break
#         elif command == "fd" or command == "back" or command == "lt" or command == "rt":
#             argument = input("Please input its argument:")
#             execute_turtle_command(command, argument)
#         elif command == "pu":
#             turtle.penup()
#         elif command == "pd":
#             turtle.pendown()
#         elif command == "reset":
#             turtle.reset()
#         else:
#             print("Wrong command, please try again.")

#     print("Exiting Turtle World!")

# def execute_turtle_command(command, argument):
#     try:
#         value = float(argument)
#         if command == "fd":
#             turtle.forward(value)
#         elif command == "back":
#             turtle.backward(value)
#         elif command == "lt":
#             turtle.left(value)
#         elif command == "rt":
#             turtle.right(value)
#     except ValueError:
#         print("Invalid argument. Please provide a valid number.")

# if __name__ == "__main__":
#     turtle.speed(1)  # Set the turtle speed (1 is slowest)
#     main()
