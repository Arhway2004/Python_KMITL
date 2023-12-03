lst = [1,2,3,4,5,6]
for i in range(1,6):
    lst[i] = lst[i-4]
print(lst)