import random
letters = ['a', 'b', 'c','d','e','f','x','y','z']
symbols = ['!', '@', '#', '$']
numbers = [1,2,3,4,5,6,7,8,9,10]

print("welcome to pypsswrd generator")
# l = input("enter y if want letters")
# s = input("enter y if want symbol")
# n = input("enter y if want number")
# psswrd = ""

# # ! easy level

# if l=="y":
#     for i in range(1,5):
#         psswrd += random.choice(letters)
# if s=="y":
#     for i in range(1,3):
#         psswrd += random.choice(symbols)
# if n=="y":
#     for i in range(1,3):
#         psswrd += str(random.choice(numbers))
# print(f"your generated password is {psswrd}")

# ! easy level 2.0
# l = int(input("enter the num of L "))
# s = int(input("enter the num of L "))
# n = int(input("enter the num of L "))

# password = ""
# for char in range(0,l):
#     password += random.choice(letters)
# for char in range(0,s):
#     password += random.choice(symbols)
# for char in range(0,n):
#     password += str(random.choice(numbers))
# print(password)

#! hard langusge

l = int(input("enter the num of L "))
s = int(input("enter the num of L "))
n = int(input("enter the num of L "))

password = ""
password_list = []
for char in range(0,l):
    password_list.append(random.choice(letters))
for char in range(0,s):
    password_list.append(random.choice(symbols))
for char in range(0,n):
    password_list.append((random.choice(numbers)))
print(password_list)

# shuffle func: it used to shuffle a list  (In-Place Shuffling)

random.shuffle(password_list)
print(password_list)

for char in password_list:
    password += str(char)
print(password)