def f(x,y):return x
x=0
y=2.0
h=0.1
while x<2.0:
    y=y+h*f(x,y)
    print(y)
    x+=h