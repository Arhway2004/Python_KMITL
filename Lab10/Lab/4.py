import turtle

def histogram():
    data_list = [1, 2, 2, 1, 3, 4, 6, 5, 3, 4, 5, 6, 4, 3, 5, 4, 5, 3, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4]
    char_count = {}
    
    for char in data_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_count = max(char_count.values())
    bar_height = max_count * 20

    window = turtle.Screen()
    t = turtle.Turtle()

    for char, count in char_count.items():
        t.penup()
        t.forward(20)
        t.pendown()
        t.right(90)
        t.penup()
        t.fd(20)
        t.pendown()
        t.write(f"{char}", font=("Arial", 15, "normal"))
        t.right(180)
        t.penup()
        t.fd(20)
        t.pendown()
        t.right(90)


        t.left(90)
        t.forward(count * 20)
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(count * 20)
        t.left(90)

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(max_count * 35)

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(90)
    t.forward(bar_height + 5)

    t.hideturtle()
    window.mainloop()

histogram()
