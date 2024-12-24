nums= [1,2,3]
for i in nums:
    print(i)

# highest score

sum1=0
marks = [23,45,56,78,99]
for m in marks:
    sum1 += m

print(sum1)

# using built-in func
builtin = sum(marks)
print(f"this is built in func {builtin}")

# to find the max score
max_sc = 0
std_marks = [98,43,23,32,45,55,100]
for s in std_marks:
    if s>max_sc:
        max_sc = s

print(max_sc)

# for loop with the in range function

# sum of n natural numbers

# !syntax => for num in range(a,b):
# ! it works from 1 to 9 (n-1)
sum2=0
n = int(input("enter the number "))
for i in range(1,n+1):
    sum2 += i
print(sum2)

# steps in range

for i in range(1,10,2):
    print(i)