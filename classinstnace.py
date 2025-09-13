# Defined inside a constructor (__init__) or directly inside methods using self.

# Unique for each object of the class.

# Changing it in one object does not affect other objects.

# Stored in the object’s namespace (dictionary).

# 👉 Example:

class Student:
    def __init__(self, name, age):
        self.name = name        # instance variable
        self.age = age          # instance variable

s1 = Student("Swarupa", 21)
s2 = Student("Riya", 22)

print(s1.name)  # Swarupa
print(s2.name)  # Riya

# 🔹 Class Variable

# Declared inside the class but outside methods.

# Shared by all objects of the class.

# Changing it through the class affects all objects, but changing via an object creates a new instance variable.

# Stored in the class’s namespace.

# 👉 Example:

class Student:
    college = "AEC"   # class variable (shared)

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Swarupa")
s2 = Student("Riya")

print(s1.college)  # AEC
print(s2.college)  # AEC

Student.college = "MAKAUT"  # change class variable
print(s1.college)  # MAKAUT
print(s2.college)  # MAKAUT

# 🔎 Quick Comparison Table
# Feature	Instance Variable (self.var)	Class Variable (Class.var)
# Where defined	Inside methods (__init__)	Directly inside the class
# Belongs to	Each object (separate copy)	Class (shared by all objects)
# Memory allocation	Created when an object is created	Created when class is defined
# Change effect	Affects only that object	Affects all objects