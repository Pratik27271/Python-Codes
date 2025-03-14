from scipy.integrate import quad
import numpy as np
mu,sig=0.5,1.0
def f(x):return 1.0/(sig*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sig**2))
r,e=quad(f,-np.inf,np.inf)
print(r)
print(e)