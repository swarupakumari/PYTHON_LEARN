# 🔹 Inheritance in Python

# 👉 Definition:
# Inheritance allows a class (child/derived) to acquire properties & methods of another class (parent/base).
# It promotes code reusability.

# 🔹 Types of Inheritance in Python

# Single Inheritance → One parent, one child.

# Multilevel Inheritance → Child → Grandchild.

# Multiple Inheritance → One child inherits from multiple parents.

# Hierarchical Inheritance → One parent, many children.

# Hybrid Inheritance → Combination of above.

# 🔹 Example
# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

# Derived class (inherits Person)
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)   # call parent constructor
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Object
s = Student("Swarupa", 101)
s.show()