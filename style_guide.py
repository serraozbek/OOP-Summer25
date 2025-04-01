"""Naming Convention"""

# Correct:
def calculate_sum(a, b):
    return a + b

class DataProcessor:  
    pass

# Wrong
def CalculateSum(a, b): 
    return a + b

class data_processor:  
    pass

"""Indentation"""

# Correct
if True:
    print("Hello")


# Wrong
# if True:
# print("Hello")       


"""Line Length"""
#Correct
def greet():
    print("Hello, My name is Serra Ozbek.")

# Wrong
def greet():
    print("Hello, My name is Serra Ozbek. I'm nineteen years old and I am learning phython.")


"""Whitespace Usage"""

# Correct
x = 3
y = x + 12

# Wrong
x=5
y=x+12

