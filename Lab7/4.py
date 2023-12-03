class QuadraticEquation:
    def __init__(self,a,b,c):
        self.a =a
        self.b =b
        self.c =c

    def gerDiscriminant(self):
        return self.b**2 - 4 * self.a * self.c
    
    def getRoot1(self):
        discriminant = self.gerDiscriminant()
        if discriminant < 0:
            return 0
        elif discriminant >= 0:
            return (-self.b+discriminant**0.5)/(2*self.a)
    def getRoot2(self):
        discriminant = self.gerDiscriminant()
        if discriminant < 0:
            return 0
        if discriminant >= 0:
            return (-self.b-discriminant**0.5)/(2*self.a)
    def __str__(self):
        root1 = self.getRoot1()
        root2 = self.getRoot2()
        return f"Root 1: {root1:.2f}\nRoot 2: {root2:.2f}"
    def print(self):
        print(self)
QuadraticEquation1 = QuadraticEquation(10,100,10)
QuadraticEquation1.print()
print(QuadraticEquation1.getRoot1())
