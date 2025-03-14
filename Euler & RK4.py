import numpy as np
import matplotlib.pyplot as plt
def f(x,y):return x**2-y
x,y,h=0,1.0,0.1
X,Y=[x],[y]
P,Q=[x],[y]
def Euler(f,x,y):
    y+=h*f(x,y)
    x+=h
    return x,y

while x<3.0:
    x,y=Euler(f,x,y)
    P.append(x)
    Q.append(y)
print(P,Q)

x,y=0,1.0
def RK2(f,x,y):
    k1=h*f(x,y)
    k2=h*f(x+h/2.0,y+k1/2.0)
    k3=h*f(x+h/2.0,y+k2/2.0)
    k4=h*f(x+h,y+k3)
    y+=1.0/6*(k1+2.0*k2+2.0*k3+k4)
    x+=h
    return x,y
while x<3.0:
    x,y=RK2(f,x,y)
    X.append(x)
    Y.append(y)
print(X,Y)

x_exact=np.linspace(0,3,100)
y_exact=x_exact**2.0-2.0*x_exact+2.0-np.exp(-x_exact)
plt.title("Euler and RK4 Method")
plt.plot(x_exact,y_exact,'*',label='Exact Solution')
plt.plot(P,Q,label='Euler')
plt.plot(X,Y,'+',label='RK4')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.grid()
plt.show()
