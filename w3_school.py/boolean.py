""" BOOLEAN VARİABLES """
# You can evaluate any expression in Python and get True or False.

# When you compare two values, Python evaluates the expression and returns a Boolean answer.

print(7 > 5)
print(7 == 5)
print(7 < 5)


# When you run a condition in an if statement, Python returns True or False.

a = 150
b = 39

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# The bool() function evaluates any value and returns True or False.

print(bool("Hello"))
print(bool()) #there is no value inside of the parentheses.

# Another value that evaluates to False is an object made from a class with a __len__ function that returns 0 or False.

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# You can create functions that returns a Boolean Value.

def myFunction() :
  return True

print(myFunction())


# You can execute code based on the Boolean answer of a function.

def myFunction() :
  return True

if myFunction():
  print("YES!") # Print "YES!" if the function returns True
else:
  print("NO!") # Print "NO!" if the function returns False
  

# Python has many built-in functions that return True or False, like the `isinstance()` function, which checks if an object is a certain type.

x = 200
print(isinstance(x, int))
