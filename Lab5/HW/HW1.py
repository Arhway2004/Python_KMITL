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
