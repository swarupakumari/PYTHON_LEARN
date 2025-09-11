class Student:
    def __init__(self, name, roll):
        self.__name = name
        self.__roll = roll

    @property
    def name(self):   # getter
        return self.__name

    @name.setter
    def name(self, new_name):  # setter
        self.__name = new_name


s1 = Student("Swarupa", 101)

# Access like an attribute
print(s1.name)   # getter

# Modify like an attribute
s1.name = "Anita"   # setter
print(s1.name)
