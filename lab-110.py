# Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Working with input strings
name = input("What is your name? ")
print(name)

# Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
# In the format() function, the opening and closing braces ({}) act as placeholders for
# the variables that will be passed to (that is, put between) the function's parentheses.
print("{}, you like a {} {}!".format(name, color, animal))
