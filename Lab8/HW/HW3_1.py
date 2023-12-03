import turtle


user_input = input("Enter some text: ")

char_count = {}
for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_count = max(char_count.values())
bar_height = max_count * 20
window = turtle.Screen()
t = turtle.Turtle()
a = turtle.Turtle()

for char, count in char_count.items():
    # for write chars
    t.penup()
    t.forward(20)
    t.pendown()
    t.right(90)
    t.penup()
    t.fd(20)
    t.pendown()
    t.write(f"{char}",font=("Arial", 15, "normal"))
    t.right(180)
    t.penup()
    t.fd(20)
    t.pendown()
    t.right(90)

    # graph
    t.left(90)
    t.forward(count * 20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(count * 20)
    t.left(90)
t.penup()
t.goto(0,0)
t.pendown()
t.forward(max_count*35)
a.left(90)
a.forward(max_count*25)
t.hideturtle()
window.mainloop()
