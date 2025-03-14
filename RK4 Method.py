x,y,h=0,1.0,0.1
X,Y=[x],[y]
def RK2(f,x,y):
    k1=h*f(x,y)
    k2=h*f(x+h/2.0,y+k1/2.0)
    k3=h*f(x+h/2.0,y+k2/2.0)
    k4=h*f(x+h,y+k3)
    y+=1.0/6*(k1+2.0*k2+2.0*k3+k4)
    x+=h
    return x,y
def f(x,y):return x**2-y
while x<0.3:
    x,y=RK2(f,x,y)
    X.append(x)
    Y.append(y)
print(X,Y)