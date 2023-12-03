# class Caculator:
#     def __init__(self,acc=0.00):
#         self.acc = acc
#     def set_accumualtor(self,a):
#         return self.acc == a
#     def get_accumulator(self):
#         print(f"{self.acc}")
#     def add(self,x):
#         self.acc += x
#     def subtract(self,x):
#         self.acc -= x
#     def multiply(self,x):
#         self.acc *= x
#     def divide(self,x):
#         self.acc /= x
#     def print_result():
#         print(f"Result:{self.acc}")

# class Sci_calc_(Caculator):
#     def __init__(self,acc=0.00):
#         super().__init__(acc)
#     def square(self):
#         self.acc = self.acc**2
#     def exp(x):
#         self.acc = self.acc**x
#     def factorial():
#         result = 1
#         for i in range(1, int(self.acc) + 1):
#             result *= i
#         self.acc = result
#     def print_result():
#         super().print_result()
#         print(f"Result{self.acc}")

# sci_calc_ = Sci_calc_(100)
# sci_calc_.print_result()

class Calculator:
    def __init__(self, acc=0.00):
        self.acc = acc

    def set_accumulator(self, a):
        self.acc = a

    def get_accumulator(self):
        print(f"{self.acc}")

    def add(self, x):
        self.acc += x

    def subtract(self, x):
        self.acc -= x

    def multiply(self, x):
        self.acc *= x

    def divide(self, x):
        if x != 0:
            self.acc /= x
        else:
            print("Error: Division by zero")

    def print_result(self):
        print(f"Result: {self.acc}")

class Sci_calc_(Calculator):
    def __init__(self, acc=0.00):
        super().__init__(acc)

    def square(self):
        self.acc = self.acc**2

    def exp(self, x):
        self.acc = self.acc**x

    def factorial(self):
        result = 1
        for i in range(1, int(self.acc) + 1):
            result *= i
        self.acc = result

    def print_result(self):
        super().print_result()
        print(f"Result: {self.acc:.1e}")

sci_calc_ = Sci_calc_(100)
sci_calc_.print_result()

