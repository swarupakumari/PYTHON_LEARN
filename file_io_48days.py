# 🔹 Python File I/O – Cheat Sheet

# Python lets you work with files (read, write, append, etc.) using the built-in open() function.

# ✅ Opening a File
# file = open("myfile.txt", "mode")


# Modes:

# "r" → Read (default, error if file not found)

# "w" → Write (create new / overwrite)

# "a" → Append (write at end, file created if not exists)

# "x" → Create (error if file exists)

# "b" → Binary mode (e.g., "rb", "wb")

# "t" → Text mode (default)

# ✅ Reading from File
# f = open("data.txt", "r")

# print(f.read())      # Read entire file
# print(f.read(10))    # Read first 10 chars
# print(f.readline())  # Read one line
# print(f.readlines()) # Read all lines as list

# f.close()

# ✅ Writing to File
# f = open("data.txt", "w")
# f.write("Hello World\n")   # Overwrites file
# f.writelines(["A\n", "B\n"])  # Write list of strings
# f.close()

# ✅ Appending to File
# f = open("data.txt", "a")
# f.write("New line\n")   # Adds at end
# f.close()

# ✅ Best Practice → Using with

# Automatically closes file:

# with open("data.txt", "r") as f:
#     data = f.read()
#     print(data)

# ✅ File Object Methods

# f.read(size) → Read size chars/bytes (or all)

# f.readline() → Read single line

# f.readlines() → Read all lines as list

# f.write(str) → Write string

# f.writelines(list) → Write multiple strings

# f.seek(offset) → Move file pointer

# f.tell() → Get current pointer position

# f.close() → Close file

# 📝 Quick Revision Keywords:

# Open: open(filename, mode)

# Read: read, readline, readlines

# Write: write, writelines

# Pointer: seek, tell

# Close: close() / with