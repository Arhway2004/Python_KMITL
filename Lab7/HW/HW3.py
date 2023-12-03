# class LinearEquation:
#     def __init__(self,a,b,c,d,e,f):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#         self.__d = d
#         self.__e = e
#         self.__f = f
#     def isSovable(self):
#         if __a*__d - __b*__c >0:
#             True
#     def getX(self,x):
#         x=((__e*__d)-(__b*__f))/((__a*__d)-(__b*__c))

#     def getY(self,y):
#         y=((__a*__f)-(__e*__c))/((__a*d)-(__b*__c))
#     def __str__(self):
#         return f"Equation: {self.__a}x + {self.__b}y = {self.__e}\n         {self.__c}x + {self.__d}y = {self.__f}"

#     def print(self):
#         print(self)

# equation = LinearEquation(2, 3, 1, 4, 5, 6)

# if equation.isSolvable():
#     x = equation.getX()
#     y = equation.getY()
#     print(f"Solution: x = {x}, y = {y}")
# else:
#     print("The equation is not solvable.")
class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def isSolvable(self):
        return self.__a * self.__d - self.__b * self.__c != 0

    def getX(self):
        if self.isSolvable():
            return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    def getY(self):
        if self.isSolvable():
            return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)

    def __str__(self):
        return f"Equation: {self.__a}x + {self.__b}y = {self.__e}\n         {self.__c}x + {self.__d}y = {self.__f}"

    def print(self):
        print(self)

equation = LinearEquation(2, 3, 1, 4, 5, 6)

if equation.isSolvable():
    x = equation.getX()
    y = equation.getY()
    print(f"Solution: x = {x}, y = {y}")
else:
    print("The equation is not solvable.")
