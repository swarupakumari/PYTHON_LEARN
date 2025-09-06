# Tuple in Python
# 🔹 Theory (Easy to Remember)

# A tuple is an ordered, immutable collection in Python.

# Defined using () parentheses (unlike lists that use []).

# Immutable → once created, you cannot change, add, or remove elements.

# Faster than lists (since immutability helps performance).

# Can store heterogeneous data (different types).

# 🔹 Example
# # Creating a tuple
my_tuple = (10, "Hello", 3.14, True)

print(my_tuple)           # (10, 'Hello', 3.14, True)
print(my_tuple[1])        # Access element → Hello
print(my_tuple[-1])       # Access last element → True

# # Tuple unpacking
# a, b, c, d = my_tuple
# print(a, c)               # 10 3.14

# # Nested tuple
# nested = (1, (2, 3), 4)
# print(nested[1][1])       # 3

# 🔹 Common Tuple Methods

# (since tuples are immutable, very few methods)

# count() → counts occurrences of a value.

# index() → returns index of first occurrence.

# Example:

# t = (1, 2, 2, 3, 4)
# print(t.count(2))   # 2
# print(t.index(3))   # 3

# 🔹 Interview Questions

# Q1. Difference between list and tuple in Python?
# 👉 List is mutable ([]), Tuple is immutable (()). Lists are slower, tuples are faster.

# Q2. Why use a tuple if list exists?
# 👉 Tuples are more memory-efficient, faster, and can be used as dictionary keys (since they’re immutable).

# Q3. Can a tuple contain a list?
# 👉 Yes. But if that list is changed, the tuple still technically remains the same (immutability is only for the tuple structure).

# ✨ Quick Trick to Remember:
# 👉 List = Flexible (mutable), Tuple = Fixed (immutable).



# t= (5, 2, 8, 5, 1)

# print(len(t))        # 5
# print(max(t))        # 8
# print(min(t))        # 1
# print(sum(t))        # 21
# print(sorted(t))     # [1, 2, 5, 5, 8]
# print(t.count(5))    # 2
# print(t.index(8))    # 2
# 🔹 Interview Quick Notes
# Only 2 tuple methods: count() and index().

# Everything else (len, max, min, sum, sorted) are built-in functions.

# Tuples are immutable → so no append(), remove(), or pop() like lists.

