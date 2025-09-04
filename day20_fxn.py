# # Python Functions – Quick Revision
# # 📘 Theory

# # A function is a reusable block of code.

# # Defined with def keyword.

# # Helps avoid repetition, improves readability.

# # Can take parameters and return values.

# #def check():
#    #pass so pass will know that av ke pass bhai baad mai lkrna ya ake pura kr lenge

# # Types:

# # Built-in (print(), len(), etc.)

# # User-defined (def my_func():)

# # Anonymous (lambda).

# # Syntax:

# def function_name(parameters):
#     # body
#     return value

# # 🖥 Examples
# 1. Simple function
def greet():
    print("Hello!")

greet()

# # 2. With parameters
def add(a, b):
    return a + b

print(add(5, 3))  # 8

# # 3. Default parameter
def greet(name="Guest"):
    print("Hello", name)

greet()          # Hello Guest
greet("Swarupa") # Hello Swarupa

# # 4. Keyword arguments
def info(name, age):
    print(f"{name} is {age} years old")

# info(age=21, name="Swarupa")

# # 5. Lambda function
square = lambda x: x * x
print(square(4))  # 16

# # 🎯 Interview Qs with Answers

# # Q: Difference between built-in and user-defined functions?
# # A:

# # Built-in → provided by Python (len(), sum()).

# # User-defined → created with def.

# # Q: What are default arguments?
# # A: Parameters with preset values, used when no value is passed.

# # def greet(name="Guest"): print("Hello", name)


# # Q: What is *args and **kwargs?
# # A:

# # *args → variable-length positional arguments (tuple).

# # **kwargs → variable-length keyword arguments (dict).

# # def demo(*args, **kwargs):
# #     print(args, kwargs)
# # demo(1,2,3, a=4, b=5)


# # Q: What is a lambda function?
# # A: Small anonymous function, written with lambda.

# # cube = lambda x: x**3
# # print(cube(3))  # 27


# # Q: Difference between return and print?
# # A:

# # print() → displays value to console.

# # return → sends value back to caller, can be stored/used further.

# # ⚡ Super Short Keys:

# # def → define function

# # *args → many positional args

# # **kwargs → many keyword args

# # lambda → one-line function

# # return ≠ print





# Python *args & **kwargs – Quick Revision
# 📘 Theory

# Used for variable-length arguments in functions.

# *args → collects extra positional arguments as a tuple.

# **kwargs → collects extra keyword arguments as a dictionary.

# Can be mixed with normal parameters.

# 🖥 Examples
# 1. Using *args
def add_all(*args):
    return sum(args)

print(add_all(2, 3, 4))   # 9

# 2. Using **kwargs
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

show_details(name="Swarupa", age=21)

# 3. Mix of args + kwargs
def demo(a, *args, **kwargs):
    print("a =", a)
    print("args =", args)
    print("kwargs =", kwargs)

demo(1, 2, 3, x=4, y=5)
# a = 1
# args = (2, 3)
# kwargs = {'x': 4, 'y': 5}

# 🎯 Interview Qs with Answers

# Q: What is the difference between *args and **kwargs?
# A:

# *args → handles multiple positional arguments → tuple.

# **kwargs → handles multiple keyword arguments → dict.

# Q: Can you use *args and **kwargs together?
# A: Yes. The order is: **normal params → *args → default params → kwargs.

# Q: What is the output of this?

# def func(*args, **kwargs):
#     print(args, kwargs)
# func(1,2, name="Swarupa", age=21)


# A:

# (1, 2) {'name': 'Swarupa', 'age': 21}


# Q: When would you use *args vs **kwargs?
# A:

# *args → when you don’t know how many values will be passed.

# **kwargs → when you don’t know how many named arguments will be passed.

# Q: What happens if you pass both normal and keyword args without defining them?
# A: They will be collected inside *args (for values) and **kwargs (for names).

# ⚡ Super Short Keys:

# *args → many values → tuple

# **kwargs → many key=value → dict

# Order = normal → *args → default → **kwargs