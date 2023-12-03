# 1
X = int(input("Enter a number:"))
guess = X/2
num=5
for y in range(8):
    temp = X/guess
    guess = (guess+temp)/2
    if y >= 5:
        print(f"The approximate square root value of {X} when iterated {num} times is {guess:.3f}")
        num+=1
        if y == 7:
            print(f"The actual square root of {X} is {guess:.3f}")
#2
import turtle
a = turtle.Turtle()
turtle = turtle.Screen()
turtle.screensize(2000,10000)
a.speed(0)
month = ["Month#1","Month#2","Month#3","Month#4","Month#5","Month#6","Month#7","Month#8","Month#9","Month#10","Month#11","Month#12"]
week = ["Su","Mo","Tu","We","Th","Fr","Sa"]
date = [31,28,31,30,31,30,31,31,30,31,30,31]
a.penup()
x=-157.5
x1=157.5
x2=-157.5
x3=-147.5
x_=-147.5
y=400
y1=400
y2=400
y3=373
y4=343
y5=370
y_=310

def draw_rectangle():
    a.forward(315)
    a.right(90)
    a.forward(210)
    a.right(90)
def draw_linex():
    a.pendown()
    a.forward(315)
    a.penup()
def draw_liney():
    a.pendown()
    a.forward(180)
    a.penup()  

full_version_canlendar = 0
while full_version_canlendar <= 12:
        a.goto(x,y)
        a.pendown()
        x4 = -147.5
        rectangle_1=0
        inside_line=0
        inside_up=0
        inside_1=0
        line_d = 1
        if full_version_canlendar == 3 or full_version_canlendar ==  6 or full_version_canlendar == 11:
            while rectangle_1<2:
                a.pendown()
                a.forward(315)
                a.right(90)
                a.forward(240)
                a.right(90)
                rectangle_1+=1
                a.penup()
                x1=x
            while inside_line < 7:
                a.goto(x1,y5)
                a.pendown()
                a.forward(315)
                a.penup()
                y5-=30
                inside_line+=1
            y1=y
            y1-=30
            x1=x
            a.right(90)
            while inside_up<6:
                x1+=45
                a.goto(x1,y1)
                a.pendown()
                a.forward(210)
                a.penup()  
                inside_up+=1
            a.goto(x3,y3)
            a.pendown()
            a.write(month[full_version_canlendar],font=("Arial", 20, "normal"))
            a.penup()
            line = 0
            while line<7:
                 a.goto(x4,y4)
                 x4 += 45
                 a.write(week[line],font=("Arial", 20, "normal"))
                 line+=1
            while line_d <= date[full_version_canlendar]:
                a.goto(x_,y_)
                x_ += 45
                a.write(line_d,font=("Arial", 20, "normal"))
                line_d+=1
                if x_ == 167.5:
                    x_=x3
                    y_-=30
            if full_version_canlendar == 11:
                break
            y_+=30
            y5+=30
        elif full_version_canlendar == 9:
            y_+=30
            while rectangle_1<2:
                a.pendown()
                draw_rectangle()
                rectangle_1+=1
                a.penup()
                x1=x
            while inside_line < 6:
                a.goto(x1,y5)
                draw_linex()
                y5-=30
                inside_line+=1
            y1=y
            y1-=30
            x1=x
            a.right(90)
            while inside_up<6:
                x1+=45
                a.goto(x1,y1)
                draw_liney()
                inside_up+=1
            a.goto(x3,y3)
            a.pendown()
            a.write(month[full_version_canlendar],font=("Arial", 20, "normal"))
            a.penup()
            line = 0
            while line<7:
                 a.goto(x4,y4)
                 x4 += 45
                 a.write(week[line],font=("Arial", 20, "normal"))
                 line+=1
            while line_d <= date[full_version_canlendar]:
                a.goto(x_,y_)
                x_ += 45
                a.write(line_d,font=("Arial", 20, "normal"))
                line_d+=1
                if x_ == 167.5:
                    x_=x3
                    y_-=30
        else:
            while rectangle_1<2:
                a.pendown()
                draw_rectangle()
                rectangle_1+=1
                a.penup()
                x1=x
            while inside_line < 6:
                a.goto(x1,y5)
                draw_linex()
                y5-=30
                inside_line+=1
            y1=y
            y1-=30
            x1=x
            a.right(90)
            while inside_up<6:
                x1+=45
                a.goto(x1,y1)
                draw_liney()
                inside_up+=1
            a.goto(x3,y3)
            a.pendown()
            a.write(month[full_version_canlendar],font=("Arial", 20, "normal"))
            a.penup()
            line = 0
            while line<7:
                 a.goto(x4,y4)
                 x4 += 45
                 a.write(week[line],font=("Arial", 20, "normal"))
                 line+=1
            while line_d <= date[full_version_canlendar]:
                a.goto(x_,y_)
                x_ += 45
                a.write(line_d,font=("Arial", 20, "normal"))
                line_d+=1
                if x_ == 167.5:
                    x_=x3
                    y_-=30
 

        a.penup()
        a.left(90)
        y_-=180
        y-=300
        y1-=300
        y2-=300
        y3-=300
        y4-=300
        y5-=120
        full_version_canlendar += 1
turtle.exitonclick()
# 3
A = int(input("num"))
a=A
x1=1
Y1=0
for w in range(A):
    for x in range(A):
        for y in range(x+x1):
            print("*",end="")
        print("")
    for X in range(A - 1, 1, -1):
        for Y in range(X):
            print("*", end="")
        print("")
    if A == 1:
        print("*", end="")
    a-=1
    A-=1
    Y1==1
 