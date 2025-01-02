lst1=[]
def lst_square(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1

a= [1,2,3,4,5]
print(lst_square(a))

# how List comprehension will work

# ["what we have to return(i*i)" "for clause(for i in lst)" ]

my_lst = [5,4,3,2,1]
got_this = [i*i for i in my_lst if i%2==0]
print(got_this)

