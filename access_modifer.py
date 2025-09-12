# 🔹 Access Modifiers in Python

# In Python, access modifiers control the visibility of class members (variables & methods).
# Unlike Java/C++, Python doesn’t have strict enforcement but uses conventions.

# 1. Public

# Members accessible anywhere inside or outside the class.

# Default in Python.

class Student:
    def __init__(self, name):
        self.name = name   # public

obj = Student("Swarupa")
print(obj.name)   # ✅ Accessible

# 2. Protected (_var)

# Prefix with single underscore _.

# By convention → “intended” to be accessed only in the class & subclasses (not enforced).

class Student:
    def __init__(self, name):
        self._name = name   # protected

class Child(Student):
    def display(self):
        print(self._name)   # ✅ Accessible in subclass

obj = Child("Swarupa")
obj.display()
print(obj._name)   # ⚠️ Accessible, but not recommended

# 3. Private (__var)

# Prefix with double underscore __.

# Name mangling occurs → variable is internally stored as _ClassName__var.

# Can’t be accessed directly outside the class.

class Student:
    def __init__(self, name):
        self.__name = name   # private

    def display(self):
        print(self.__name)   # ✅ Accessible inside class

obj = Student("Swarupa")
obj.display()
# print(obj.__name)   ❌ Error
print(obj._Student__name)   # ✅ Access using name mangling

# 🔹 Summary Table
# Modifier	Syntax	Accessibility
# Public	var	Anywhere
# Protected	_var	Class + Subclass (convention)
# Private	__var	Only inside class (via name mangling outside)

#we use everything as public but for private we use name mangling