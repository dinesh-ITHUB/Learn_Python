# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)

# Casting - If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type - You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))

# Case-Sensitive
a = 4
A = "Sally"
#A will not overwrite a
print(A)
print(a)

# Single or Double Quotes?
x = "John"
print(x)
# is the same as
x = 'John'
print(x)

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Local Variable
# Declaring a function  
def add():  
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  
  
# Calling a function  
add()  

# Global Variables
# Declare a variable and initialize it  
x = 101  
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x)  
  
mainFunction()  
print(x)  

# Delete a variable
# Assigning a value to x  
x = 6  
print(x)  
# deleting a variable.   
del x  
print(x)  