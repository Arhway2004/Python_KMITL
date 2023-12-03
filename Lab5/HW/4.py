A = int(input("num"))
a=1
for x in range(A):
    for y in range(0+a,x+1):
        print("*",end="")
    print("")    
for X in range(A - 1, 0, -1):
    for Y in range(X):
        print("*", end="")
    print("")
# for y in range(1,3):
#     print("*",end="")
# print("")  