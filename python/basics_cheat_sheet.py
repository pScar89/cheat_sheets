# Python Cheat Sheet

# COMMENTS
# Single line comment
""" Multiline
    Comment """

# VARIABLES
x = 5  # Integer
y = 3.14  # Float
name = "John"  # String
is_coding = True  # Boolean

# DATA STRUCTURES
# List - Ordered, Mutable
my_list = [1, 2, 3]
# Tuple - Ordered, Immutable
my_tuple = (1, 2, 3)
# Set 
my_set = {1, 2, 3}
# Dictionary
my_dict = {"a": 1, "b": 2}

# CONTROL FLOW
# If-Else
if x > 5:
    print("Greater")
elif x == 5:
    print("Equal")
else:
    print("Lesser")

# Loops
# For loop
for i in range(5):
    print(i)
# While loop
while x < 10:
    x += 1


# FUNCTIONS
def my_function(param1, param2):
    return param1 + param2


# LAMBDA FUNCTIONS
square = lambda x: x * x

# EXCEPTION HANDLING
try:
    # code that might raise an exception
    pass
except Exception as e:
    print(e)
finally:
    # code that runs no matter what
    pass

# IMPORTING MODULES
import math
from datetime import datetime

# FILE HANDLING
# Read a file
with open("file.txt", "r") as file:
    content = file.read()
# Write to a file
with open("file.txt", "w") as file:
    file.write("Hello, world!")

# LIST COMPREHENSIONS
squares = [i * i for i in range(10)]

# DICTIONARY COMPREHENSIONS
squared_dict = {x: x * x for x in range(5)}

# SET COMPREHENSIONS
unique_squares = {x * x for x in [1, 2, 2, 3]}

# STRING FORMATTING
name = "Alice"
welcome = f"Hello, {name}"


# CLASSES
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")


# OBJECT CREATION
my_object = MyClass("Bob")

# WORKING WITH DATETIME
current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# MODULES OF INTEREST
# Math, datetime, sys, os, json, requests

# TIPS
# - Indentation is key in Python.
# - Use descriptive variable names.
# - Keep your code DRY (Don't Repeat Yourself).
# - Read and follow PEP 8 for style guide.
