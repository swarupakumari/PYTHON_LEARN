# Executes a block as long as condition is True.

# Syntax:

# while condition:
#     # body


# Must update condition inside loop → otherwise infinite loop.

# Supports break, continue, else.

# 🖥 Examples
# # 1. Basic counting
i = 1
while i <= 5:
    print(i)
    i += 1   # update condition

# # 2. With break
i = 1
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

# # 3. With continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# # 4. With else
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")

# 🎯 Interview Qs with Answers

# Q: Difference between for loop and while loop in Python?
# A:

# for → iterate over iterable or fixed range.

# while → run until condition becomes False (good for unknown iterations).

# Q: What happens if condition in while loop never becomes False?
# A: Infinite loop (keeps running until force-stopped).

# Q: Does while loop support else?
# A: Yes. Runs if loop ends normally (no break).

# Q: Write a while loop to print numbers 1 to 10.
# A:

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# Q: How would you create an infinite loop with while?
# A:

# while True:
#     # code


# ⚡ Super Short Keys:

# while → runs until condition False.

# Needs update to avoid infinite loop.

# Supports break, continue, else.

# Use while True for infinite loop.