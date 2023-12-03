# import turtle
# a = turtle.Turtle()
# turtle = turtle.Screen()
# # turtle.screensize(2000,10000)
# a.speed(0)
# month = ["January 2023","February 2023","March 2023","April 2023","May 2023","June 2023","July 2023","August 2023","September 2023","Octorber 2023","November 2023","December 2023"]
# date = [31,28,31,30,31,30,31,31,30,31,30,31]
# pen = int(input())
# a.penup()

# def rectangle(pen):
#     full_version_canlendar=0
#     while full_version_canlendar <= 12:
#         inside_line=0
#         a.goto(157.5,400)
#         if pen ==3 or pen ==6 or pen==11:
#             for x in range(4):
#                 a.forward(315)
#                 a.right(90)
#                 a.forward(240)
#                 a.right(90)
#                 a.penup()
#             while inside_line < 7:
#                 a.goto(157.5,370)
#                 a.pendown()
#                 a.forward(315)
#                 a.penup()
#                 y5-=30
#                 inside_line+=1

# rectangle(pen)
# turtle.exitonclick()

import turtle

# Create a turtle named 'a'
a = turtle.Turtle()

# Create a turtle screen
screen = turtle.Screen()

# Set drawing speed to the fastest
a.speed(0)

# Define month names and their corresponding days
months = ["January 2023", "February 2023", "March 2023", "April 2023", "May 2023", "June 2023", "July 2023", "August 2023", "September 2023", "October 2023", "November 2023", "December 2023"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Get the input for the pen value (assuming pen represents the number of days in the month)
pen = int(input("Enter the number of days in the month: "))

# Move the turtle's pen up
a.penup()

# Function to draw a rectangle grid for the calendar
def draw_calendar(pen):
    # Loop through each month
    for month_name, days in zip(months, days_in_month):
        a.goto(157.5, 400)
        
        # Draw the rectangle for the calendar grid
        for _ in range(4):
            a.pendown()
            a.forward(315)
            a.right(90)
            a.forward(240)
            a.right(90)
            a.penup()
        
        # Draw the horizontal lines inside the grid
        for _ in range(7):
            a.goto(157.5, 370)
            a.pendown()
            a.forward(315)
            a.penup()
            # Adjust the vertical position for the next line
            a.goto(157.5, a.ycor() - 30)
        
        # Assuming you want to print the month name on the calendar
        a.goto(157.5, 440)
        a.write(month_name, align="center", font=("Arial", 14, "normal"))
        
        # Move the turtle to the next month's position
        a.goto(a.xcor() + 350, a.ycor())
    
# Call the function to draw the calendar
draw_calendar(pen)

# Close the turtle graphics window on click
turtle.exitonclick()
