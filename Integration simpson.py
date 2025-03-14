from scipy.integrate import simps
import numpy as np
def f(x):return x**2
x_values = np.linspace(0, 2, 1000)
result = simps(f(x_values), x_values)
print("The result of the integration using Simpson's rule is:", result)