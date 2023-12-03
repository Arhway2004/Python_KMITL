# 1
class Time:
    def __init__(self, H, M, S):
        self.H = H
        self.M = M
        self.S = S
        self.P = ""

    def period(self):
        if self.H >= 12:
            self.P = "PM"
        else:
            self.P = "AM"

    def tick(self):
        self.S += 1
        if self.S >= 60:
            self.S = 0
            self.M += 1
            if self.M >= 60:
                self.M = 0
                self.H += 1
                if self.H >= 24:
                    self.H = 0
        self.period() 

    def __str__(self):
        return f"{self.H}:{self.M}:{self.S} {self.P}"

    def print(self):
        print(self)

time = Time(10, 43, 32)
time.tick()
print(time)


# 2
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def add(self, other):
        result = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result.append(coeff1 + coeff2)
        return Polynomial(result)

    def scalar_multiply(self, n):
        result = [coeff * n for coeff in self.coefficients]
        return Polynomial(result)

    def multiply(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result)

    def power(self, n):
        if n == 0:
            return Polynomial([1])
        result = self
        for _ in range(n - 1):
            result = result.multiply(self)
        return result

    def diff(self):
        result = [0] * (len(self.coefficients) - 1)
        for i in range(1, len(self.coefficients)):
            result[i - 1] = i * self.coefficients[i]
        return Polynomial(result)

    def integrate(self):
        result = [0] + [coeff / (i + 1) for i, coeff in enumerate(self.coefficients)]
        return Polynomial(result)

    def eval(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                term = str(coeff)
                if i == 1:
                    term += 'x'
                elif i > 1:
                    term += f'x^{i}'
                terms.append(term)
        if not terms:
            return '0'
        return " + ".join(terms)


p = Polynomial((1, 9, -2))
print(p)  # Print the polynomial
q = p.power(2)
print(q)
r = p.add(q)
print(r)
s = r.diff()
print(s)
t = s.integrate()
print(t)
u = t.eval(3)
print(u)

# 3
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
