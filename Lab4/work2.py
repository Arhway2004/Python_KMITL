
X = eval((input("Put the number")))
if type (X) == float:
    X = float(X)
    Y = input("Pleae choose floating or scientific")
    if Y == "floating":
        print(f"{X:.2f}")
    elif Y == "scientific":
        print(f"{X:e}")
    else:
        print("Invalid choice!")
elif type (X) == int:   
    if X == int(X):
        y=input("Pleae choose binary or octal or hexadecimal or decimal")
    if y == "binary":
        print(f"{bin(X)}")
    elif y == "octal":
        print(f"{oct(X)}")
    elif y == "hexadecimal":
        print(f"{hex(X)}")    
    elif y == "decimal":
        print(f"{X}")
    else:
        print("Invalid choice!")
else:
    print("Invalid number")

















# X = input("Put the number: ")
# try:
#     float_X = float(X)
#     # Check if it's a real number (float)
#     Y = input("Choose floating or scientific: ")
#     if Y.lower() == "floating":
#         print("F")
#     elif Y.lower() == "scientific":
#         print("S")
#     else:
#         print("Invalid choice!")

# except ValueError:
#     try:
#         int_X = int(X)
#         # Check if it's an integer
#         Y = input("Choose binary, octal, hexadecimal, or decimal: ")
#         if Y.lower() == "binary":
#             print("B")
#         elif Y.lower() == "octal":
#             print("O")
#         elif Y.lower() == "hexadecimal":
#             print("H")
#         elif Y.lower() == "decimal":
#             print("D")
#         else:
#             print("Invalid choice!")

#     except ValueError:
#         print("Invalid input. Please enter a valid number.")






# def display_real_number(number):
#     format_choice = input("Choose the display format (floating or scientific): ")

#     if format_choice.lower() == "floating":
#         print(f"Floating-point format: {number:.2f}")
#     elif format_choice.lower() == "scientific":
#         print(f"Scientific format: {number:e}")
#     else:
#         print("Invalid format choice!")

# def display_integer(number):
#     format_choice = input("Choose the display format (binary, octal, hexadecimal, or decimal): ")

#     if format_choice.lower() == "binary":
#         print(f"Binary format: {bin(number)}")
#     elif format_choice.lower() == "octal":
#         print(f"Octal format: {oct(number)}")
#     elif format_choice.lower() == "hexadecimal":
#         print(f"Hexadecimal format: {hex(number)}")
#     elif format_choice.lower() == "decimal":
        # print(f"Decimal format: {number}")
#     else:
#         print("Invalid format choice!")

# def main():
#     number_str = input("Enter a number: ")

#     try:
#         number = float(number_str)
#         if number.is_integer():
#             display_integer(int(number))
#         else:
#             display_real_number(number)
#     except ValueError:
#         print("Invalid input. Please enter a real number.")

# if __name__ == "__main__":
#     main()