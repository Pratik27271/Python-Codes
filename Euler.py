import matplotlib.pyplot as plt
import numpy as np
def f(x,y):return y-x
x=0
y=0.5
h=0.01
xlist,ylist=[x],[y]
while x<=2.0:
    y=y+h*f(x,y)
    print (x,y)
    x+=h
    plt.plot(x,y,c='red',linestyle='-',lw=3,marker='o',ms=15)
plt.title('Factors of a function',size=30)
plt.xlabel('X-axis',size=20)
plt.ylabel('Y-axis',size=20)
plt.axhline()
plt.grid()
plt.show()