# Raising Custom Errors in Python
# 1. Why Custom Errors?

# Built-in exceptions (ValueError, ZeroDivisionError) may not always explain your case.

# Custom exceptions make error handling more meaningful & readable.

# 2. Syntax

# Define a class that inherits from Exception.

# Use raise to trigger it.

# Step 1: Define custom exception
class MyError(Exception):
    """Custom exception class"""
    pass

# Step 2: Raise it
raise MyError("Something went wrong!")

#3. Custom Error with Extra Info
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value not allowed: {value}")

# # Usage
# num = -5
# if num < 0:
#     raise NegativeNumberError(num)


# Output:

# Negative value not allowed: -5

# 4. Handling Custom Errors
# try:
#     raise NegativeNumberError(-10)
# except NegativeNumberError as e:
#     print("Caught custom error:", e)

# 5. Interview Quick Q&A
# Q	A
# How do you create a custom error?	By defining a class that inherits from Exception and raising it using raise.
# Why use custom exceptions?	To make error messages meaningful and handle specific cases in code.
# Can you catch a custom error like built-in ones?	Yes, using except CustomError as e:
# Best practice?	Inherit from Exception, not BaseException (to avoid interfering with system-level exceptions).