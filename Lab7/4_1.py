class QuadraticEquation:
    def __init__(self, a, b, c, r1, r2):
        self.a = a
        self.b = b
        self.c = c
        self.r1 = r1
        self.r2 = r2
    
    def gerDiscriminant(self):
        return self.b**2 - 4 * self.a * self.c
    
    def getRoot1(self):
        discriminant = self.gerDiscriminant()
        if discriminant >= 0:
            return (-self.b + discriminant**0.5) / (2 * self.a)
        else:
            return None  # No real roots for negative discriminant
    
    def getRoot2(self):
        discriminant = self.gerDiscriminant()
        if discriminant >= 0:
            return (-self.b - discriminant**0.5) / (2 * self.a)
        else:
            return None  # No real roots for negative discriminant

# Create an instance of QuadraticEquation
equation = QuadraticEquation(1, -3, 2, None, None)

# Calculate and print the roots using the methods
root1 = equation.getRoot1()
root2 = equation.getRoot2()

if root1 is not None:
    print("Root 1:", root1)
else:
    print("No real roots for root 1")

if root2 is not None:
    print("Root 2:", root2)
else:
    print("No real roots for root 2")
