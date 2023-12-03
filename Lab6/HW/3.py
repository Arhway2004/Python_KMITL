# # # x,y,z= eval(input("point 1:"))
# # # z= eval(input())
# # # x1,y1,z1= eval(input("point 1:"))
# # # x2,y2= eval(input("point 2:"))
# # # x3,y3= eval(input("point 3:"))
# # # def convert(x, y, z):
# # #     for num in [x, y, z]:
# # #         if num == 1:
# # #             return "one"
# # #         elif num == 2:
# # #             return "two"
# # #         elif num == 3:
# # #             return "three"
# # #         elif num == 4:
# # #             return "four"
# # #         elif num == 5:
# # #             return "five"
# # #         elif num == 6:
# # #             return "six"
# # #         elif num == 7:
# # #             return "seven"
# # #         elif num == 8:
# # #             return "eight"
# # #         elif num == 9:
# # #             return "nine"
# # #         else:
# # #             return "unknown"

# # # # Get three integer values from the user
# # # x,y,z = map(int, input("Enter three numbers separated by spaces: ").split())

# # # X = convert(x)
# # # Y = convert(Y)
# # # Z = convert(Z)
# # # print(f"x: {x}, y: {y}, z: {z}")

# # def convert(x,y,z):
# #     if x == 1 or y == 1 or z == 1:
# #         return "one"
# #     elif x == 2 or y == 2 or z == 2:
# #         return "two"
# #     elif x == 3 or y == 3 or z == 3:
# #         return "three"
# #     elif x == 4 or y == 4 or z == 4:
# #         return "four"
# #     elif x == 5 or y == 5 or z == 5:
# #         return "five"
# #     elif x == 6 or y == 6 or z == 6:
# #         return "six"
# #     elif x == 7 or y == 7 or z == 7:
# #         return "seven"
# #     elif x == 8 or y == 8 or z == 8:
# #         return "eight"
# #     elif x == 9 or y == 9 or z == 9:
# #         return "nine"
# #     else:
# #         return "unknown"

# # x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())
# # # y = int(input("Enter three numbers separated by spaces: "))
# # # z = int(input("Enter three numbers separated by spaces: "))
# # # X = convert(x)
# # # Y = convert(y)
# # # Z = convert(z)
# # # if x
# # print(f"{x},{y},{z}")

# def convert(number):
#     if number == 1:
#         return "one"
#     elif number == 2:
#         return "two"
#     elif number == 3:
#         return "three"
#     elif number == 4:
#         return "four"
#     elif number == 5:
#         return "five"
#     elif number == 6:
#         return "six"
#     elif number == 7:
#         return "seven"
#     elif number == 8:
#         return "eight"
#     elif number == 9:
#         return "nine"
#     else:
#         return "unknown"

# x, y, z = map(int, input("Enter three numbers separated by spaces: ").split())

# x_word = convert(x)
# y_word = convert(y)
# z_word = convert(z)

# print(f"{x_word} {y_word}, {z_word}")

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
