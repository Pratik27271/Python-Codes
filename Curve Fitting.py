import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1.0,2.0,3.0,4.0])
y=[1.0,2.9,4.8,6.7,8.6]
n=len(x)
sx=sum(x)
sy=sum(y)
sx2=sum(x**2)
sxy=sum(x*y)
a0=(sy*sx2-sx*sxy)/(n*sx2-(sx**2))
print(a0)
a1=(sx*sy-n*sxy)/((sx)**2-n*sx2)
print(a1)
yfit=a0+a1*x
plt.plot(x,y,'*',label='Data')
plt.plot(x,yfit,label='Fitted Line')
plt.legend()
plt.show()