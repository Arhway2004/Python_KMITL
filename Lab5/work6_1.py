# A = int(input("Enter an integer"))

# if A % 2 == 0:
#     for x in range(1, (A - (A // 2)) + 1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#         row_values.reverse()
#         for value in row_values:
#             print(value, end=" ")
#         print()

#     for x in range((A - (A // 2)), 0, -1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#         row_values.reverse()
#         for value in row_values:
#             print(value, end=" ")
#         print()

# if A % 2 != 0:
#     for x in range(1,(A - ((A+1) // 2)) + 1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#         row_values.reverse()
#         for value in row_values:
#             print(value, end=" ")
#         print()

#     for x in range((A - ((A-1) // 2)), 0, -1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#         row_values.reverse()
#         for value in row_values:
#             print(value, end=" ")
#         print()
for f in range(0,-5,-1):
    c=(5/9)*(f-32)
    print(c)