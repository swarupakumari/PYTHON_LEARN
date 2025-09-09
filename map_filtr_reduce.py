# Map, Filter, Reduce – Cheat Sheet
# ✅ 1. map(function, iterable)

# Applies a function to each item of an iterable.

# Returns a map object (convert using list()).

from functools import reduce


nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]

# ✅ 2. filter(function, iterable)

# Filters elements based on a condition (True/False).

# Returns a filter object (convert using list()).

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# ✅ 3. reduce(function, iterable)

# Reduces iterable to a single value by applying function cumulatively.

# Must be imported from functools.

# from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

# 📝 Quick Table
# Function	Purpose	Example	Output
# map()	Apply function to each item	map(lambda x: x*2, [1,2,3])	[2,4,6]
# filter()	Keep items matching condition	filter(lambda x: x>2, [1,2,3,4])	[3,4]
# reduce()	Reduce to single value	reduce(lambda x,y: x+y, [1,2,3,4])	10

# ⚡ Key Idea:

# map → transform

# filter → select

# reduce → combine