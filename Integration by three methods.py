import numpy as np
def rect(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=x[1]-x[0]
    I=h*(sum(f(x))-f(b))
    return I

def trap(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=x[1]-x[0]
    I=(h/2.0)*(2.0*sum(f(x))-f(b)-f(a))
    return I

def simp(f,a,b,n):
    x=np.linspace(2,6,101)
    y=x**2
    h=x[1]-x[0]
    s1=y[0]+y[-1]
    s2=0
    for i in range(2,len(x)-2,2):
        s2+=2.0*y[i]
    s3=0
    for i in range(1,len(x)-1,2):
        s3+=4*y[i]
    I=(h/3.0)*(s1+s2+s3)
    return I

def simps(f,a,b,n):
    x=np.linspace(a,b,n+1)
    h=x[1]-x[0]
    I=(h/3.0)(f(a)+f(b)+2.0*sum(f(x)[2:len(x)-2:2])+4.0(sum(f(x)[1:len(x)-1:2])))
    return I

def f(x):return x**2
print("Result from rectangular rule=",rect(f,2,6,100))
print("Result from trapizoidal rule=",trap(f,2,6,100))
print("Result from simpson's rule=",simp(f,2,6,100))
print("Result from simpson's rule=",simps(f,2,6,100))