# if __name__ == "__main__": in Python
# 1. What it is?

# Special construct that checks whether a Python file is run directly or imported.

# 2. How it works

# Every Python file has a built-in variable __name__.

# If the file is run directly → __name__ == "__main__".

# If the file is imported as a module → __name__ == module_name.

# 3. Example

# file: myscript.py

# def greet():
#     print("Hello!")

# if __name__ == "__main__":
#     greet()


# Run directly →

# python myscript.py


# Output:

# Hello!


# Import into another file:

# import myscript


# Output: (no output) → because the if block won’t run.

# 4. Why use it?

# To separate reusable code (functions, classes) from script execution.

# Prevents code from running automatically on import.

# 5. Interview Q&A
# Q	A
# What is __name__?	A built-in variable in every Python module.
# Value of __name__ when file is run directly?	"__main__".
# Value of __name__ when file is imported?	Module name (e.g., "myscript").
# Why use if __name__ == "__main__":?	To ensure code runs only when file is executed directly, not when imported.
# Best practice?	Put tests, demo code, or script-specific logic inside this block.

# ⚡ Shortcut memory hook:
# 👉 "__main__" = main program entry point.