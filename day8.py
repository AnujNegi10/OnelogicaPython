# Functions
def greet(name):
    print("hello "+name)

greet("anuj")

# func that allows for inputs

def greet_with_name(name):
    print(f"hello {name} how are you ")
greet_with_name("ronaldo")

# parameter = argument

# function with more than 1 input 

def greet_with(n,location):
    print(f"My name is {n} and i live in {location}")

greet_with("messi","argentina")

# keyword arguments 

greet_with(location="argentina",n="messi")

# sum 
def add(a,b):
    c=a+b
    print(f"the sum is {c}")

add(2,3)