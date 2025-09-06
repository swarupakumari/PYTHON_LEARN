# 📌 Python Dictionary
# 🔹 What is a Dictionary?

# Key–Value pair collection.

# Unordered, mutable, indexed by keys.

# Keys must be unique & immutable (str, int, tuple).

# Values can be of any type.

student = {"name": "Swarupa", "age": 21, "course": "Python"}
print(student["name"])  # Swarupa

# 🔹 Creating a Dictionary
d1 = {"a": 1, "b": 2}
d2 = dict(x=10, y=20)
empty = {}

# 🔹 Accessing Values
print(d1["a"])        # 1
print(d1.get("c", 0)) # returns 0 if key not found (safe access)

# 🔹 Adding & Updating
d = {"a": 1, "b": 2}
d["c"] = 3          # add new key
d["a"] = 100        # update

# 🔹 Removing
d.pop("b")          # removes key b
d.popitem()         # removes last inserted item
del d["a"]          # delete specific key
d.clear()           # empty dictionary

# 🔹 Useful Methods
d = {"x": 10, "y": 20, "z": 30}

print(d.keys())      # dict_keys(['x','y','z'])
print(d.values())    # dict_values([10,20,30])
print(d.items())     # dict_items([('x',10),('y',20),('z',30)])

d.update({"y": 200, "w": 50})  # update / add multiple keys

# 🔹 Looping
# for key, value in d.items():
#     print(key, value)

# 🔹 Dictionary Comprehension
# squares = {x: x**2 for x in range(5)}
# print(squares)  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 🔹 Nested Dictionary
# students = {
#     "101": {"name": "Swarupa", "age": 21},
#     "102": {"name": "Riya", "age": 22}
# }
# print(students["101"]["name"])  # Swarupa

# 🔹 Interview Questions

# Q1. What is a dictionary in Python?
# 👉 A mutable collection of key-value pairs, where keys are unique.

# Q2. Difference between dict.get() and dict[]?
# 👉 dict[] raises KeyError if missing, .get() returns None or default.

# Q3. Can a list be used as a key?
# 👉 ❌ No, because lists are mutable. Tuples/strings/ints can be used.

# Q4. Difference between pop() and popitem()?
# 👉 pop(key) removes specific key; popitem() removes the last inserted item.

# ⚡ Quick Trick:
# 👉 Dictionary = real-life dictionary (word = key, meaning = value).


# Python Dictionary Methods Cheat Sheet
# Method	What it does	Example
# clear()	Remove all items	d = {'a':1}; d.clear(); print(d) → {}
# copy()	Returns a shallow copy	d2 = d.copy()
# get(key, default)	Get value of key; if not exist, return default	d.get('a',0)
# items()	Returns key-value pairs	d.items() → dict_items([('a',1)])
# keys()	Returns all keys	d.keys() → dict_keys(['a'])
# values()	Returns all values	d.values() → dict_values([1])
# pop(key, default)	Remove key & return value	d.pop('a',0)
# popitem()	Remove last inserted pair	d.popitem()
# setdefault(key, default)	Return value; if not exist, insert default	d.setdefault('b',2)
# update(other_dict)	Add/update items from another dict	d.update({'c':3})

# 💡 Tips for quick revision:

# Access: get, keys, values, items

# Modify: update, setdefault, pop, popitem, clear

# Copy: copy()