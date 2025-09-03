# Strings are immutable 
# when we apply any method  it make new string
s="Swarupa!!!!!!!!!!" 
print(len(s))
print(s.upper())
print(s.lower())
print(s.rstrip("!"))
print(s.replace("Swarupa","Rupa"))
print(s.capitalize())   # first charcter as capital and and other to lower
print(s.count('a'))
print(s.center(50))  # align to center
print(s.endswith('i')) # reply true or false
print(s.find('a'))# first occurernce index dega  if not find it will give -1 
#print(s.index('T')) # error de dega if occuerence ni h toh
print(s.isalnum()) # is al n numberic
# It checks whether all the characters in a string are alphanumeric (i.e., only letters A–Z, a–z or digits 0–9).

# Returns True if all characters are alphanumeric and the string is not empty.

# Returns False if the string contains spaces, special characters, or is empty.
print(s.islower()) # true false
print(s.istitle())  # show true if all letter first of word is captial or false

print(s.swapcase()) # convert upper to lower and lower to upper
