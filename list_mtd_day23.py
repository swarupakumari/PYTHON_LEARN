nums = [3, 1, 2, 2]

nums.append(5)        # [3,1,2,2,5]
nums.insert(1, 99)    # [3,99,1,2,2,5]
nums.extend([6,7])    # [3,99,1,2,2,5,6,7]
nums.remove(2)        # removes first 2 → [3,99,1,2,5,6,7]
print(nums.pop())     # 7, list=[3,99,1,2,5,6]
print(nums.index(99)) # 1
print(nums.count(2))  # 1
nums.sort()           # [1,2,3,5,6,99]
nums.reverse()        # [99,6,5,3,2,1]
new = nums.copy()     # shallow copy
# 🎯 Interview Qs with Answers
# Q: Difference between append() and extend()?
# A:

# append(x) → adds element as a single item.

# extend(iterable) → adds all elements of iterable.

# python
# Copy code
# l=[1]; l.append([2,3]) # [1,[2,3]]
# l=[1]; l.extend([2,3]) # [1,2,3]
# Q: Difference between remove() and pop()?
# A:

# remove(x) → removes first occurrence of value.

# pop([i]) → removes element at index (default last) and returns it.

# Q: Difference between sort() and sorted()?
# A:

# list.sort() → sorts in-place, returns None.

# sorted(list) → returns a new sorted list, original unchanged.

# Q: What does copy() do?
# A: Creates a shallow copy (copies references, not deep objects).

# Q: How to reverse a list without using reverse()?
# A:

# python
# Copy code
# nums[::-1]   # slicing method
# ⚡ Super Short Keys:

# Add → append(), insert(), extend()

# Remove → remove(), pop(), clear()

# Info → index(), count()

# Order → sort(), reverse()

# Copy → copy()