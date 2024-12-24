import random
letters = ['a', 'b', 'c','d','e','f','x','y','z']
symbols = ['!', '@', '#', '$']
numbers = [1,2,3,4,5,6,7,8,9,10]

print("welcome to pypsswrd generator")
l = input("enter y if want letters")
s = input("enter y if want symbol")
n = input("enter y if want number")
psswrd = ""

# ! easy level

if l=="y":
    for i in range(1,5):
        psswrd += random.choice(letters)
if s=="y":
    for i in range(1,3):
        psswrd += random.choice(symbols)
if n=="y":
    for i in range(1,3):
        psswrd += str(random.choice(numbers))
print(f"your generated password is {psswrd}")

#  