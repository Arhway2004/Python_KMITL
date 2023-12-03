A = int(input("num"))
a=A
x1=1
Y1=0
for w in range(A):
    for x in range(A):
        for y in range(x+x1):
            print("*",end="")
        print("")
    for X in range(A - 1, 1, -1):
        for Y in range(X):
            print("*", end="")
        print("")
    if A == 1:
        print("*", end="")
    a-=1
    A-=1
    Y1==1
 