# formatted inputs 

def formated(fname,lname):
    # docstrings
    """take fname and lname"""

    if fname=="" or lname=="":
        return "no name given"
    newf = fname.title()
    newl = lname.title()

    return f"results: {newf} {newl}"

print(formated(input("enter fname: ") , input("enter lname: ")))

# storing function as a variable name

def add(n,m):
    return n+m 

my_var_func = add
print(my_var_func(10,20))
