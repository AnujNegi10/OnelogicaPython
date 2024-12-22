# data types
# int
a = 2343

# string
b = "hello"

# subscripting
print("anuj"[0])

# primitive datatypes : int float boolean strings

# typecasting
print(int("123")+3)
print("anuj"+" "+"negi")
print(str(123)+str(456))
print(12.3+23)
print(int(34.5)+4)
print(123_2323_23)

# boolean
print(True)
print(False)

# type casting , errors , type errxor
 
print(type("hello"))
print(type(34))
print(type(3.5))
print(type(True))

# typecasting
print(int("123")+7) 

# print("number of letter in your name " + str(len(input("enter your name "))))

# space is also taken as a character

# Mathematical operations in python

print("My age: " + str(123))
print(123+456)
print(7-6)
print(4+3)
print(6/3)
print(6//3)
print(2**3)

# PEMDAS
# Parentheses , Exponents , Multiplication/Division , Add/Sub
# () , ** , * , / , + , -

print(int(3*3+3/3-3))
print(int(3*(3+3)/3-3))

# Number Manipulation and f strings in python

bmi = 84/1.34 ** 2
print(bmi)
print(int(bmi))

# round functin
print(round(bmi,2))

# f strings

print(f"your bmi is {bmi}")

# tip calculator

print("welcome to tip calcu")
bill = float(input("what is total bill "))
tip = float(input("what percentage of tip what would you like to give "))

people = int(input("how many people to split bill "))

bill_with_tip = tip/100*bill+bill
final = round(bill_with_tip,2)
print(f"your bill is now {final}")