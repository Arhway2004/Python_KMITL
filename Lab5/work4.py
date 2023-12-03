for x in range(1,50):
    if x % 3 == 0:
        continue  
    if x == 49:
        print(x)
        break
    print(x,end=(","))
