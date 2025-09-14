# What is a Class Method?

# A method that is bound to the class, not the instance.

# It takes cls (class itself) as the first argument instead of self.

# Declared using the @classmethod decorator.

# Can access and modify class variables, but not instance variables directly.

# 📌 Example
# class Student:
#     college = "AEC"   # class variable

#     def __init__(self, name):
#         self.name = name   # instance variable

#     @classmethod
#     def change_college(cls, new_college):
#         cls.college = new_college   # modifying class variable


# # Before changing
# print(Student.college)   # AEC

# # Change using class method
# Student.change_college("MAKAUT")

# print(Student.college)   # MAKAUT

# 🔎 Key Points

# Use @classmethod when you need to work with class-level data.

# Can be called by both class and objects.

# Often used as factory methods → alternate ways to create objects.

# 📌 Factory Method Example
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, info_str):
#         name, age = info_str.split("-")
#         return cls(name, int(age))  # returning new object


# # Creating object using constructor
# s1 = Student("Swarupa", 21)

# # Creating object using class method
# s2 = Student.from_string("Riya-22")

# print(s1.name, s1.age)   # Swarupa 21
# print(s2.name, s2.age)   # Riya 22


# ✅ Quick Recap of Decorators in Classes

# @staticmethod → no self, no cls → utility function inside class.

# @classmethod → gets cls, can modify class state.

# Normal method → gets self, works on object instance.
the