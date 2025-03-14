from scipy.integrate import simps
import numpy as np
mu,sig=0.5,1.0
def f(x):return 1.0/(sig*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sig**2))
x_values=np.linspace(-np.inf,np.inf,1000)
result=simps(f(x_values),x_values)
print(result)