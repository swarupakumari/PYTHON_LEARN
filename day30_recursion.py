# Recursion in Python
# 🔹 What is Recursion?

# A function calling itself directly or indirectly.

# Used to solve problems that can be broken into smaller sub-problems of the same type.

# 🔹 Structure of a Recursive Function

# Every recursive function must have:

# Base Case → condition to stop recursion (avoids infinite loop).

# Recursive Case → function calling itself with a smaller/simpler input.

# 🔹 Example 1: Factorial
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # 120

# 🔹 Example 2: Fibonacci
def fibonacci(n):
    if n <= 1:   # Base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))  # 8

# 🔹 Example 3: Sum of List
# def list_sum(lst):
#     if len(lst) == 0:   # Base case
#         return 0
#     return lst[0] + list_sum(lst[1:])

# print(list_sum([1, 2, 3, 4]))  # 10

# 🔹 Advantages

# ✅ Elegant & shorter code.
# ✅ Matches mathematical definitions (factorial, Fibonacci, etc.).

# 🔹 Disadvantages

# ❌ Higher memory usage (function call stack).
# ❌ Slower than iteration for large inputs.

# 🔹 Common Interview Questions

# Q1. What is recursion?
# 👉 A function that calls itself until a base case is met.

# Q2. Why is a base case needed?
# 👉 To stop infinite recursion & prevent stack overflow.

# Q3. Recursion vs Iteration?
# 👉 Iteration uses loops, recursion uses function calls. Recursion is cleaner for problems like tree traversal, but iteration is more efficient.

# Q4. Write a recursive function for factorial/Fibonacci/reverse a string.

# ⚡Quick Trick:
# Recursion = Function repeats itself until it hits a base case.