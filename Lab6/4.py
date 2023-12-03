# def sum_of_digits(x=2,y=3,z=4,A=0):
#     A+=x
#     A+=y
#     A+=z
#     return A

# aa=sum_of_digits()
# print(aa)
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input("input"))
result = sum_of_digits(n)
print(result)  # This will print: 18

