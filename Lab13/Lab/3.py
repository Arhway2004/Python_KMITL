# def gcd(x,y):
#     if x or y == int:  
#        return x  
#     else:
#         return 
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# Example usage:
num1 = 46
num2 = 0
result = gcd(num1, num2)
print(result)
# print(f"The GCD of {num1} and {num2} is {result}")
# 