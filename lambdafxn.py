# Python Lambda Function – Cheat Sheet
# ✅ What is a Lambda?

# A lambda function is a small, anonymous function.

# Defined using the lambda keyword (instead of def).

# Can have any number of arguments but only one expression.

# ✅ Syntax
# lambda arguments: expression

# ✅ Example
square = lambda x: x**2
print(square(5))   # Output: 25

# ✅ Multiple Arguments
add = lambda a, b: a + b
print(add(3, 4))   # Output: 7

# ✅ Common Use Cases
# 1. With map()
# nums = [1, 2, 3, 4]
# squares = list(map(lambda x: x**2, nums))
# print(squares)  # [1, 4, 9, 16]

# 2. With filter()
# nums = [1, 2, 3, 4, 5]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4]

# 3. With sorted()
# data = [(1, 'b'), (2, 'a'), (3, 'c')]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)  # [(2, 'a'), (1, 'b'), (3, 'c')]

# 📝 Quick Points to Remember

# Anonymous: No name (can assign to a variable if needed).

# Single Expression Only.

# Used with map, filter, reduce, sorted for quick operations.