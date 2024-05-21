########################## FUNCTION ###############################
 
def get_started():
    print("hello world")

get_started() # Calling the function


def  add(x,y):
    return   x + y      
print(add(45,6))     # Calling the function with arguments


def divide(a,b=6): # Default argument value is set to 6.  If no argument provided then it will take default valuedef multiply(a , b) : 
   sum = a/b 
   return sum

print(divide(16))
print(divide(18,5))  # now we are giving argument so default value will not be taken


def arbitary_eg(*args):    # *args is a special syntax in python which allows to pass any number of arguments
    print(args)

arbitary_eg("kathamndu","nyc","chicago") # We can pass as many arguments as we want without specifying in parameter

first = int(input("enter a number "))
second = int(input("enter second number "))
def multiple(x,*arg,**kwarg):
    print(x,arg,kwarg)


a,b,c,d= multiple(first,second) # yesma a, b, c, d ma value initialized garna milxa respectively
print(f"sum is {a}")
print(f"diffrence is {b}")
print(f"multiple is {c}")
print(f"quotient is {d}")


a= multiple(first, second) #a le multiple value lixa in the form of tuple
print(type(a))
print(f"addition = {a[0]} \nsubtraction = {a[1]} \nmultiple = {a[2]} \ndivison = {a[3]}" )



import conditional
from conditional import sum  #yesle arko ine ko funtion import gaerera call garxa
print(sum(40, 70))

from conditional import sum as multiply  #yesma as use gaerera long name lai yo file ma matrai short name use garna painxa 
print(multiply(90, 60))






































































































