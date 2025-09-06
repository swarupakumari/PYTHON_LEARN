# f-strings in Python
# 🔹 Theory (Easy to Remember)

# f-strings = formatted string literals (introduced in Python 3.6).

# Start a string with f or F → lets you directly embed Python expressions inside {}.

# Faster & cleaner than format() or % formatting.

# 🔹 Example
name = "Swarupa"
age = 22

# Using f-string
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Swarupa and I am 22 years old


# but for shwing the name and age as it is means to just copy the print as it is we will use double curly braces
print(f"My name is {{name}} and I am {{age}} years old.")


# # Expressions inside f-string
# print(f"Next year I will be {age + 1}.")
# # Output: Next year I will be 23

# 🔹 Formatting Numbers
# pi = 3.14159265
# print(f"Pi rounded to 2 decimals: {pi:.2f}")   # 3.14
# print(f"Binary of 5: {5:b}")                    # 101
# print(f"Percentage: {0.856:.2%}")               # 85.60%

# 🔹 Multi-line f-string
# name = "Python"
# version = 3.12
# msg = f"""
# Hello, {name}!
# You are using version {version}.
# """
# print(msg)

# 🔹 Interview Questions

# Q1. Why use f-strings instead of format()?
# 👉 Cleaner, more readable, faster.

# Q2. Can f-strings evaluate expressions?
# 👉 Yes → {2+3}, {len("hello")}, etc.

# Q3. Are f-strings available in Python 3.5?
# 👉 No, only from Python 3.6+.