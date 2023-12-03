# 1
user_input = int(input("Enter an integer: "))
if user_input < 0:
    print("Negative are not supported.")
elif user_input == 0:
    print("Binary representation: 0")
else:
    binary_string = ""
    while user_input > 0:
        remainder = user_input % 2
        binary_string = str(remainder) + binary_string
        user_input = user_input // 2
    print(f"Binary representation: {binary_string}")
    binary_str = binary_string[::-1]
    decimal_value = 0
    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal_value += 2 ** i
    print(f"Converted back to integer: {decimal_value}")

# 2
user_input = input("Enter some text: ")
char_count = {}
total_chars = len(user_input)

print("Character Frequency Table")

for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    percentage = (count / total_chars) * 100
    print(f"{char}: {percentage:.2f}%")
    
# 3
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

# 4
first_9_digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")

if len(first_9_digits) != 9 or not first_9_digits.isdigit():
    print("Invalid input.")
else:

    total = 0
    for i in range(9):
        digit = int(first_9_digits[i])
        total += digit * (i + 1)

    checksum = total % 11
    isbn_10 = first_9_digits + str(checksum if checksum < 10 else 'X')

    print("Your ISBN-10 number is", isbn_10)
