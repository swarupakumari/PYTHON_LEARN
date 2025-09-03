#conversion of one data type to other
# explict int(a)
a="1"
b="2" 
print(int(a)+int(b))
#implict python khus se 
#Implicit type casting:

# Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python
a=10
b=9.8
print(a+b) # chnges to float