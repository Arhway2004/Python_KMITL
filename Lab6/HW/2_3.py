import turtle
a = turtle.Turtle()
screen = turtle.Screen()
a.speed(0)
months = ["January 2023", "February 2023", "March 2023", "April 2023", "May 2023", "June 2023", "July 2023", "August 2023", "September 2023", "October 2023", "November 2023", "December 2023"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mo","Tu","We","Th","Fr","Sa","Su"]
a.penup()
pen1 = int(input("Enter the number of days in the month: "))
pen1-=1
def draw_calendar(pen=pen1,y1=170,x1=-112.5):    
            if pen == 0 or pen == 3 or pen == 9:
                a.goto(-157.5, 200)
                a.pendown()    
                for x in range(2):
                    a.forward(315)
                    a.right(90)
                    a.forward(240)
                    a.right(90)
                    # a.penup()
                for x in range(7):
                    a.goto(-157.5,y1)
                    a.pendown()
                    a.forward(315)
                    a.penup()
                    y1-=30
                a.right(90)
                for x in range(6):
                    a.goto(x1,170)
                    a.pendown()
                    a.forward(210)
                    a.penup()
                    x1+=45  
            else:
                a.goto(-157.5, 200)
                a.pendown()    
                for x in range(2):
                    a.forward(315)
                    a.right(90)
                    a.forward(210)
                    a.right(90)

                for x in range(6):
                    a.goto(-157.5,y1)
                    a.pendown()
                    a.forward(315)
                    a.penup()
                    y1-=30
                a.right(90)
                for x in range(6):
                   a.goto(x1,170)
                   a.pendown()
                   a.forward(180)
                   a.penup()
                   x1+=45
            a.penup()  

def write_date(pen=pen1,x2=-147.5,M1=-147.5,y2=115):
        a.goto(-45,175)
        a.pendown()
        a.write(months[pen],font=("Arial", 20, "normal"))
        a.penup()
        for x in range(7):
            a.goto(x2,145)
            a.pendown()
            a.write(week[x],font=("Arial", 20, "normal"))
            a.penup()
            x2+=45
            # monday
        if pen1 == 4:
            M1=-147.5
            a.goto(M1,y2)
            a.pendown
            # tuesday
        elif pen1 == 7:
            M1=-102.5
            a.goto(M1,y2)
            a.pendown
            # wednesday
        elif pen1 == 1 or pen1 ==2 or pen1==10:
            M1=-57.5
            a.goto(M1,y2)
            a.pendown
            # thusday
        elif pen1 == 5:
            M1=-12.5
            a.goto(M1,y2)
            a.pendown
            # friday
        elif pen1 == 8 or pen1==11:
            M1=33.5
            a.goto(M1,y2)
            a.pendown 
            # saturday
        elif pen1 == 3 or pen1==6:
            M1=78.5
            a.goto(M1,y2)
            a.pendown 
        elif pen1 == 0 or pen1 == 9:
            M1=123.5
            a.goto(M1,y2)
            a.pendown 
            # sunday 
        for day in range(1, days_in_month[pen - 1] + 1):
            a.goto(M1, y2)
            a.pendown()
            a.write(day, font=("Arial", 20, "normal"))
            a.penup()
            M1 += 45
            if M1 > 158.5:
                a.penup()
                y2 -= 30
                M1 = -147.5
                a.goto(M1, y2)
                a.pendown()
                

draw_calendar(pen=pen1,y1=170,x1=-112.5)
write_date(pen=pen1,x2=-147.5,M1=-147.5,y2=115)
turtle.exitonclick()