import numpy as n
def f(x):return n.sin(x)
a=float(input("Enter the value of a="))
b=float(input("Enter the value of b="))
while f(a)*f(b)>0:
    print("No root is available in this interval")
    break
while abs(a-b)>0.00001:
    c=(a+b)*0.5
    if f(c)==0:
        print("The root is",c)
    if f(a)*f(c)>0:
        a=c
    else:
        b=c
print("The root is",(a+b)*0.5)