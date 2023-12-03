for x in range(50,-1,-1):
    if x%3 == 0:
        continue
    elif x%5 == 0:
        continue
    elif x ==1 :
        print(x,end='.')
    else:
        print(x,end=',')
    