# A = int(input("Enter an integer"))

# for x in range(0, A):
#     num = 1

#     # print(num,end=" ")
#     for x in range(x + 1):
#         reversed_num_str = str(num)[::-1]
#         print(reversed_num_str, end=" ")
#         num *= 2
#     # num *= 2
#     print()
# A = int(input("Enter an integer"))

# if A %2 ==0:
#     for x in range(1, (A-(A//2)) + 1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#             row_values.reverse()  
#             for value in row_values:
#                 print(value, end=" ")
#     print() 
#     for x in range((A-(A//2)),0, -1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#             row_values.reverse()  
#         for value in row_values:
#             print(value, end=" ")
        
#     print() 


# if A %2 !=0:
#     for x in range(1, (A) + 1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#             row_values.reverse()  
#             for value in row_values:
#                 print(value, end=" ")
#     print() 
#     for x in range((A-1),0, -1):
#         num = 1
#         row_values = []
#         for y in range(x):
#             row_values.append(num)
#             num *= 2
#             row_values.reverse()  
#         for value in row_values:
#             print(value, end=" ")
        
#     print() 
A = int(input("Enter an integer"))

if A % 2 == 0:
    for x in range(1, (A - (A // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - (A // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

if A % 2 != 0:
    for x in range(1,(A - ((A+1) // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - ((A-1) // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()
