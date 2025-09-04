# A list is an ordered, mutable, indexed collection.

# Allows duplicate elements.

# Defined with square brackets [].

# Supports slicing, nesting, and many built-in methods.

# 🖥 Examples
# # 1. Create list
nums = [1, 2, 3, 4]

# # 2. Access
print(nums[0])      # 1
print(nums[-1])     # 4

# # 3. Modify
nums[1] = 20
print(nums)         # [1, 20, 3, 4]

# # 4. Slicing
print(nums[1:3])    # [20, 3]

# 5. Add elements
nums.append(5) #end mai add
nums.insert(2, 99) # position
print(nums)         # [1, 20, 99, 3, 4, 5]

# # 6. Remove elements
nums.remove(20)
print(nums)         # [1, 99, 3, 4, 5]
nums.pop()          # removes last

# # 7. List comprehension
squares = [x**2 for x in range(5)]
print(squares)      # [0,1,4,9,16]

# 🎯 Interview Qs with Answers

# Q: Difference between list and tuple in Python?
# A:

# List → mutable, defined with [].

# Tuple → immutable, defined with ().

# Q: How are lists stored in memory in Python?
# A: Lists are dynamic arrays (resizable), store references to objects.

# Q: How do you remove duplicates from a list?
# A: Convert to set, then back to list.

# my_list = [1,2,2,3]
# print(list(set(my_list)))  # [1,2,3]


# Q: How do you sort a list in Python?
# A:

# nums = [4,1,3]
# nums.sort()        # modifies in place → [1,3,4]
# sorted_nums = sorted(nums)  # returns new sorted list


# Q: Explain list comprehension.
# A: One-line way to create lists.

# [x for x in range(5) if x%2==0]  # [0,2,4]


# ⚡ Super Short Keys:

# List = ordered + mutable.

# Allows duplicates.

# Methods → .append(), .insert(), .remove(), .pop(), .sort(), .reverse().

# List comprehension → quick list building.