# In Python, a static method is a method inside a class that does not depend on the instance (self) or the class (cls).

# It behaves just like a normal function but belongs to the class’s namespace. You define it using the @staticmethod decorator.

# ✅ Key Points:

# Does not take self (instance) or cls (class) as the first parameter.

# Can be called on the class itself or on its instances.

# Used when the method’s logic is related to the class but does not need to access class or instance attributes.

# 📌 Example:
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(num):
        return num % 2 == 0


# Call via class name
print(MathUtils.add(10, 20))     # Output: 30
print(MathUtils.is_even(4))      # Output: True

# # Call via instance
# obj = MathUtils()
# print(obj.add(5, 7))             # Output: 12

# 🔍 When to use @staticmethod?

# If you want to group utility functions inside a class for better organization.

# When the function logically belongs to the class but doesn’t require access to self (instance attributes) or cls (class attributes).

# 👉 Example: Math functions, validators, converters, etc