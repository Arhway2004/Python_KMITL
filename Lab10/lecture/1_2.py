isCovered = 99*[False]
endOfInput = False
while not endOfInput:
    s = input("enter")
    items = s.split()
    lst = [eval(x)for x in items]

    for number in lst:
        if number == 0:
            endOfInput = True
        else:2
            isCovered[number-1]= True
            
allCovered = True
for i in range(99):
    if not isCoveered[i]:
        allCovered = False
        break
if allCovered:
    print("cover all")
else:
    print("don't cover")