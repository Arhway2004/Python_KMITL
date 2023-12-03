z = 0
Z = 0
for x in  range(5):
    y = eval(input("Enter an integer:"))
    if y >= 0:
        z += y
        print("Current sum:",z)
    elif y < 0:
        Z += y
        print("Current sum:",Z)
    else:
        print("Error")
