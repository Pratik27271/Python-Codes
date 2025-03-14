def f(t,u):return (1-(4*t/3))*u
t=0
u=1.0
h=0.1
while t<3.0:
    u=u+h*f(t,u)
    print(t,u)
    t+=h