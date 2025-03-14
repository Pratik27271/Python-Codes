from scipy import integrate

# Define the function to integrate
def f(x):
    return x**2

# Define the limits of integration
lower_limit = 0
upper_limit = 2

# Integrate the function using quad method from scipy.integrate
result, error = integrate.quad(f, lower_limit, upper_limit)

print("The result of the integration is:", result)
print("Estimated error:", error)


