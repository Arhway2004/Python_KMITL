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
