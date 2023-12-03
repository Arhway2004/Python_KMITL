#1
def time(h=0, m=0):
    if h >= 12:
        period = "PM"
        if h > 12:
            h -= 12
    else:
        period = "AM"
        if h == 0:
            h = 12

    return f"{h}:{m:02d} {period}"
print(time(h=23, m=24))
#2
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
#3
def number_to_words(number):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number == 0:
        return ones[number]

    if 1 <= number <= 9:
        return ones[number]
    
    if 11 <= number <= 19:
        return teens[number - 10]
    
    if 20 <= number <= 99:
        return tens[number // 10] + ("-" + ones[number % 10] if number % 10 != 0 else "")
    
    if 100 <= number <= 999:
        return ones[number // 100] + " hundred" + (" and " + number_to_words(number % 100) if number % 100 != 0 else "")

    return "I don't know."

user_input = int(input("Enter a number: "))
print(number_to_words(user_input))
#4
def calculate_combination(amount=4203):
    result = {}

    if amount >= 1000:
        result[1000] = amount // 1000
        amount %= 1000
    
    if amount >= 500:
        result[500] = amount // 500
        amount %= 500
    
    if amount >= 100:
        result[100] = amount // 100
        amount %= 100
    
    if amount >= 50:
        result[50] = amount // 50
        amount %= 50
    
    if amount >= 20:
        result[20] = amount // 20
        amount %= 20
    
    if amount >= 10:
        result[10] = amount // 10
        amount %= 10
    
    if amount >= 5:
        result[5] = amount // 5
        amount %= 5
    
    if amount >= 2:
        result[2] = amount // 2
        amount %= 2
    
    if amount >= 1:
        result[1] = amount

    return result

def main():
    amount = int(input("Input your amount of money: "))
    combination = calculate_combination(amount)
    
    print("Combination:")
    if 1000 in combination:
        print(f"1000-Baht notes: {combination[1000]}")
    if 500 in combination:
        print(f"500-Baht notes: {combination[500]}")
    if 100 in combination:
        print(f"100-Baht notes: {combination[100]}")
    if 50 in combination:
        print(f"50-Baht notes: {combination[50]}")
    if 20 in combination:
        print(f"20-Baht notes: {combination[20]}")
    if 10 in combination:
        print(f"10-Baht coins: {combination[10]}")
    if 5 in combination:
        print(f"5-Baht coins: {combination[5]}")
    if 2 in combination:
        print(f"2-Baht coins: {combination[2]}")
    if 1 in combination:
        print(f"1-Baht coins: {combination[1]}")

main()
#5
def reverse(number):
    return int(str(number)[::-1])

input_number = int(input("Enter an integer: "))
reversed_result = reverse(input_number)
print("Reversed:", reversed_result)
