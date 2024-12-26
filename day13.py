# debugging
def my():
    for i in range(1,20+1):
        
        if i==20:
            print("you got it")
my()

# try and catch 

try:
    marks = int(input("enter a number"))
except Exception:
    print("invalid input")
    marks = int(input("enter the marks"))
if marks>18:
    print(f"you pass at {marks}")