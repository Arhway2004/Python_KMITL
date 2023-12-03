# for x in range(5):
#     print("1")
#     for y in range(1,5):
#         print(y)
# print("\n")
# for x in range(5):
#     print("1")
#     for y in range(1, 5):
#         print(y)
#     print()

for i in range(0, 5):
    num = 1
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
    print()

for i in range(4, 0, -1):
    num = 1
    for j in range(0, i):
        print(num, end=" ")
        num = num + 1
    print()
