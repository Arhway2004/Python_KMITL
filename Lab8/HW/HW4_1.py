first_9_digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")

if len(first_9_digits) != 9 or not first_9_digits.isdigit():
    print("Invalid input. Please enter exactly 9 numeric digits.")
else:

    total = 0
    for i in range(9):
        digit = int(first_9_digits[i])
        total += digit * (i + 1)

    checksum = total % 11
    isbn_10 = first_9_digits + str(checksum if checksum < 10 else 'X')

    print("Your ISBN-10 number is", isbn_10)
