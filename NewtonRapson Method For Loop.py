import numpy as n
def f(x):return n.sin(x)
def g(x):return n.cos(x)
x=float(input("Enter your guess root="))
while abs(f(x))>0.00001:
    x-=f(x)/g(x)
print(x)