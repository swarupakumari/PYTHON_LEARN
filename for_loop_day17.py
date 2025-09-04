# Theory

# Iterates over iterables (list, tuple, string, dict, range).

# Syntax:

# for var in iterable:
## body


# Supports break, continue, else.

# Diff from C/Java → Python loop works directly on data, not init/cond/inc.

# 🖥 Examples
# # 1. List
for fruit in ["apple", "banana"]:
   print(fruit)

# # 2. Range
# range(start, stop, step)
# start → beginning (default = 0)

# stop → end (exclusive)

# step → increment/decrement (default = 1)

# It’s a generator-like object (not a list). Use list(range(...)) to see numbers.


for i in range(3):
   print(i)

# # 3. Else
for i in range(2):
   print(i)
else:
   print("Done")

# # 4. Index + Value
for i, v in enumerate(["a","b"]):
   print(i, v)

# # 5. Dictionary
for k, v in {"a":1,"b":2}.items():
 print(k, v)

# 🎯 Interview Qs with Answers

# Q: Difference between Python for vs C/Java for?
# A:

# Python → loops over iterable items directly.

# C/Java → uses init; condition; increment.

# Python is simpler, no index handling unless needed.

# Q: How does for...else work in Python?
# A:

# The else block executes if the loop finishes normally (no break).

# for i in range(3):
#     if i == 1:
#         break
# else:
#     print("Else runs only if no break")


# Q: How to iterate with both index and value?
# A: Use enumerate().

# for i, val in enumerate(["x","y"]):
#     print(i, val)


# Q: How to loop through dictionary keys and values?
# A: Use .items().

# my_dict = {"a":1,"b":2}
# for k, v in my_dict.items():
#     print(k, v)


# Q: How to reverse a for loop?
# A: Use reversed() or step in range().

# for i in reversed(range(5)):
#     print(i)   # 4 3 2 1 0


# ⚡ Super Short Keys:

# enumerate() → index + value

# items() → dict key + value

# for...else → else runs if no break

# # reversed(range()) → reverse loop