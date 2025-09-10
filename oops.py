# 🔹 What is a Class?

# A class is a blueprint for creating objects.

# It defines attributes (variables) and methods (functions).

# 🔹 What is an Object?

# An object is an instance of a class.

# You can create many objects from one class.

# ✅ Example: Class and Object in Python
# Defining a class
class Student:
    # Constructor (called automatically when object is created)
    def __init__(self, name, roll):
        self.name = name   # attribute
        self.roll = roll   # attribute

    # Method
    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Creating objects
s1 = Student("Swarupa", 101)
s2 = Student("Anita", 102)

# Calling method using objects
s1.display()
s2.display()