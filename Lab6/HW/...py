class Dog:
    def __init__(self):
        pass
    def __str__(self):
        return "This is a Dog object"

ozzy = Dog()
print(ozzy)

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"This is a Cat object named {self.name} and it is {self.age} years old."

# Creating instances of the Cat class with different attributes
ozzy = Cat("Ozzy", 3)
buddy = Cat("Buddy", 5)

# Printing the attributes of the Cat instances
print(ozzy)
print(buddy)
