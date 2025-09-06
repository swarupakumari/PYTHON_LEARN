# python Exception Handling – Quick Revision
# 1. Keywords

# try: code to test for exceptions

# except: handle exceptions

# else: runs if no exception occurs

# finally: runs always

# 2. Basic Example
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception")
finally:
    print("Always executed")


# Output:

# Cannot divide by zero
# Always executed

# 3. Multiple Exceptions
try:
    num = int(input())
    print(10 / num)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

# 4. Raising Exceptions
# x = -5
# if x < 0:
#     raise ValueError("x cannot be negative")

# 5. Custom Exception
# class MyError(Exception):
#     pass

# raise MyError("Custom exception")

# 6. Important Notes

# finally always executes, even if return is in try.

# else runs only if no exception occurs.

# Avoid bare except: → catches all exceptions (bad practice).

# Multiple exceptions can be caught in one except.

# 7. Common Interview Q&A
# Q	A
# Difference finally vs else?	else: runs if no exception, finally: runs always
# Can try exist without except?	Yes, only with finally
# Difference raise vs assert?	raise: explicitly raise exception; assert: check condition, raises AssertionError if false
# What happens if exception is not handled?	Program terminates with traceback
# How to catch multiple exceptions?	except (TypeError, ValueError) as e: