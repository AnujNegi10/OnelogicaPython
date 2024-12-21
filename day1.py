# everything is an object in python

# these are single line comment
'''multi line comment'''

print("my name is anuj",4,2,sep="~")

print("anuj",end="\n")
print("branch - AIML")

# variables

a=12345
b = "anuj negi"
c = True
d = None
e = 45.4

print(a)
print(b)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# print(type(f))


int =323
float = 23.3
print(int+float)

bool  = True
print(int+bool)

com = complex(2,3)
print(com)

# List : list of items of different datatypes , mutable

# tuple : Immutable , same as list 

list = [2,3,[4,5],"anuj",[2,3,2,["negi"]],("tuple")]

print(list)

tuple = (2,3,[4,5],"anuj",[2,3,2,["negi"]],("tuple"))

print(tuple)

dict = {"name":"anuj","age":23,"friends":["ankur,vivek"],"istrue":True}

print(dict)
# .keys , .values , .ites are treated as methods

print(dict.keys())
print(dict.values())
print(dict.items())


# name = input("enter your name")

# print("hello" + name )

# print("hello " + input("enter your name")+"!")

#! print(input("what is your name")) Whatever the user types is returned as a string by the input() function.

# Variables

a = "Anuj Negi"
print(len(a))

userin = input("enter to find len ")

print(len(userin))

# brand name generator
print("\n")
br = input("enter city name ")
nm = input("enter pet name ")
print("your brand name is " + br+" "+ nm)