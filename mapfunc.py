def multiple(n):
    if n%5==0:
        return f"{n} is multiple"
    else:
        return f"{n} is not a multiple"
    
lst = [12,10,5,60,75,3,4,6]
print(list(map(multiple,lst)))
# map(function_name,iterable)

#! filter functions

def even(num):
    if num%2==0:
        return True
lst1=[1,2,3,4,5,6,7]

# print(list(filter(even,lst1)))

# lambda with filter function
print(list(filter(lambda num:num%2==0,lst)))
    