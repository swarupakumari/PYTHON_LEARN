# Python os Module – Cheat Sheet

# The os module in Python provides functions to interact with the Operating System (files, directories, environment variables, etc.).

# ✅ Commonly Used os Functions
# 1. Working with Current Directory
# import os

# print(os.getcwd())   # Get current working directory
# os.chdir("C:/Users") # Change current working directory

# 2. File & Directory Operations
# os.listdir()          # List files & folders in current directory
# os.mkdir("test")      # Create single directory
# os.makedirs("a/b/c")  # Create nested directories
# os.rmdir("test")      # Remove empty directory
# os.removedirs("a/b/c")# Remove nested empty directories

# 3. File Handling
# os.remove("file.txt")   # Delete file
# os.rename("old.txt", "new.txt")  # Rename file

# 4. Path Operations (os.path)
# os.path.join("folder", "file.txt")   # Join paths safely
# os.path.exists("file.txt")           # Check if path exists
# os.path.isfile("file.txt")           # Check if file
# os.path.isdir("folder")              # Check if directory
# os.path.abspath("file.txt")          # Get absolute path

# 5. Environment Variables
# print(os.environ)          # Get all environment variables
# print(os.environ['PATH'])  # Access a specific variable

# 6. Process Management
# os.system("echo Hello")    # Run system command
# print(os.getpid())         # Get current process ID
# print(os.name)             # OS type: 'posix', 'nt'

# 📝 Quick Revision Keywords:

# Directory: getcwd, chdir, listdir, mkdir, rmdir

# File: remove, rename

# Path: join, exists, isfile, isdir, abspath

# Env: environ

# Process: system, getpid, name

