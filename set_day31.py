# Python Set
# 🔹 What is a Set?

# Unordered collection of unique items.

# Defined using {} or set().

# No duplicates allowed.

# Mutable (you can add/remove items).

# my_set = {1, 2, 3, 4}
# print(my_set)   # {1, 2, 3, 4}

# 🔹 Creating a Set
# s1 = {1, 2, 3}
# s2 = set([4, 5, 6])
# empty_set = set()   # NOT {}

# 🔹 Important Properties

# Unordered → no indexing/slicing.

# Only immutable elements allowed (int, str, tuple). Lists/dicts ❌.

# s = {1, 2, "hello", (3, 4)}  # valid

# 🔹 Common Methods of Sets
# 🔸 Adding & Removing
# s = {1, 2, 3}
# s.add(4)          # {1, 2, 3, 4}
# s.update([5, 6])  # {1, 2, 3, 4, 5, 6}
# s.remove(2)       # removes 2, error if not found
# s.discard(10)     # removes safely (no error)
# s.pop()           # removes random element
# s.clear()         # empty set

# 🔸 Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # {3, 4}
print(a.difference(b))   # {1, 2}
print(b.difference(a))   # {5, 6}
print(a.symmetric_difference(b))  # {1, 2, 5, 6}

# 🔸 Membership Test
# s = {1, 2, 3}
# print(2 in s)   # True
# print(5 not in s)  # True

# 🔹 Frozen Set

# Immutable version of set.

# fs = frozenset([1, 2, 3])
# # fs.add(4) ❌ error

# 🔹 Interview Questions

# Q1. What is a set in Python?
# 👉 Unordered collection of unique, hashable items.

# Q2. Difference between remove() and discard()?
# 👉 remove() throws error if element not found, discard() does not.

# Q3. Can a list be added to a set?
# 👉 No, because list is mutable (unhashable).

# Q4. Use case of sets?
# 👉 Removing duplicates, membership testing, set operations (union, intersection).

# ⚡Quick Trick:
# 👉 Set = Unique bag of items 👜 (no duplicates, unordered).