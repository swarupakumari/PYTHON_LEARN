# 📌 Docstring in Python
# 🔹 Theory (Easy to Remember)

# Docstring (Documentation String) = special string used to document code.

# Written inside triple quotes (""" or ''') just below:

# function definition

# class definition

# module (file)

# Accessible using .__doc__.

# Helps others (and you) understand code easily.

# 🔹 Example: Function Docstring
def add(a, b):
    """This function takes two numbers and returns their sum."""
    return a + b
print(add.__doc__)
# # Output: This function takes two numbers and returns their sum.

# 🔹 Example: Class Docstring
# class Student:
#     """This class represents a student with name and age."""
    
#     def __init__(self, name, age):
#         """Initialize student with name and age."""
#         self.name = name
#         self.age = age

# 🔹 Example: Module Docstring (at top of file)
# """
# This module contains basic math operations:
# 1. add
# 2. subtract
# """
# def add(a, b):
#     return a + b

# 🔹 Interview Questions

# Q1. Difference between comment and docstring?
# 👉 Comment (#) is ignored by interpreter, docstring is stored in code object and can be accessed using .__doc__.

# Q2. Can every function/class have a docstring?
# 👉 Yes, recommended by PEP 257 (docstring convention).

# Q3. How to view a docstring?
# 👉 Use help(function_name) or function_name.__doc__.

# ✨ Quick Trick:
# 👉 Comment = for humans only
# 👉 Docstring = for humans + Python (accessible at runtime



#-------------------------------------------------------------------------------


# 🔹 Interview Questions

# Q1. What is PEP?
# 👉 Python Enhancement Proposal, design document to suggest or describe new features.

# Q2. Which PEP is most famous?

# Q1. What is PEP 8?
# 👉 Official Python style guide for writing clean, readable code.

# Q2. Most important PEP 8 rule?
# 👉 Indentation (4 spaces).

# Q3. Variable naming conventions?
# 👉 snake_case for variables/functions, PascalCase for classes, UPPER_CASE for constants.

# ✨ Quick Trick:
# 👉 PEP 8 = Clean Code Bible for Python.




# ===================================================================================================================================================================================================================================================
# The Zen of Python (PEP 20)
# 🔹 What is it?

# A collection of 19 guiding principles for writing Pythonic code.

# Written by Tim Peters.

# Acts like a philosophy for Python programming.

# 🔹 How to See It in Python
# import this


# 👉 Output = The Zen of Python.

# 🔹 Key Lines (Easy to Remember)

# Beautiful is better than ugly.

# Explicit is better than implicit.

# Simple is better than complex.

# Complex is better than complicated.

# Readability counts.

# Special cases aren’t special enough to break the rules.

# Errors should never pass silently.

# There should be one—and preferably only one—obvious way to do it.

# Now is better than never.

# If the implementation is hard to explain, it’s a bad idea.

# (There are 19 total, but these 10 are the most quoted 💡).

# 🔹 Interview Questions

# Q1. What is the Zen of Python?
# 👉 A set of guiding principles for Python (PEP 20), written by Tim Peters.

# Q2. How do you access it?
# 👉 import this

# Q3. Most important line?
# 👉 “Readability counts.”

# ✨ Quick Trick:
# 👉 Think of it as Python’s philosophy of simplicity & readability.