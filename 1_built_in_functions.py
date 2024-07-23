# Built In Functions

# print() : prints data to the screen so it is visible to the user
print('string1', 'string2', sep='==========')

# \n : new line character
print("string1\n\n\n")
print("We're here now")

# \t : tab special character
print("this is\t\t", 'separated')

# \\ : backslash characters adds a backslash
print("this string should now have a backslash\\")

# String concatenation (adding multiple strings together to make a single string)
words = " add"
print("We can" + words + " strings together")

# Formatted strings
name = 'Alice'
age = 30

# using .format()
print("Name: {},\nAge: {}".format(name, age))

# Modern formatted string
print(f"Name: {name},\nAge: {age}")

#---------#

# input() : used to take user input
# name = input("What is your name? ")
# print(f"Hello, {name}!!")

# type() : can be used to return the data type of data stored in a variable
num = 10
print(type(num))

# isinstance(var, type) : checks if a variable holds a specific data type, always returns a boolean value (True or Fale)
num = 10
print(isinstance(num, int))

# len() : returns the length of an iterable object
message = "Hello"
print(len(message))

# abs() : returns the absolute value
number = -5
print(abs(number))

# round() : rounds a number to the nearest integer or specified number of decimal places
# must be a decimal above .5, for ex 4.51, in order to round up

number = 4.567
print(round(number)) # output: 5
print(round(number, 2)) # output: 4.57

print(round(4.5)) # output: 4
print(round(4.51)) # output: 5

# sum() : returns the sum of all items inside of an iterable
numbers = [1, 2, 3, 4]
print(sum(numbers))

# min() : return the smallest value in an iterable
print(min(numbers))

# max() : returns the largest value in an iterable
print(max(numbers))

# pow(<num>, <to the power of>) : returns the power of a number
print(pow(2, 3)) # output: 8

# divmod() : returns a tuple containing the quotient and remainder of division
print(divmod(10, 3))

#--------------#

# int() : converts a value to an integer
print(int("10") + 5)
# print("10" + 5)

# str() : converts a value into a string
print(str(10), type(str(10)))

# float() : convert a alue to a floating point number
print(float("10.5"), type(float("10.5")))

# bool() : converts a value to a boolean value (True or False)
print(bool(0)) # output: False
print(bool(23)) # output: True
print(bool([])) # output: False
print(bool("")) # output: False
print(bool(-1)) # output: False
print(bool(-84)) # output: False

names = []
print(bool(names))
print(bool(len(names)))

# if True:
if names:
    print("Hey look, there are names in here!")
else:
    print("Uh oh, no names in here yet")