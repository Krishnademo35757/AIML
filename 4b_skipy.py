from scipy.optimize import root

# Define a function whose root we want to find
def func(x):
    return x**3 - 6*x**2 + 11*x - 6

# Use scipy.optimize.root to find the root
result = root(func, x0=0.0)
print("Root found at x =", result.x)
