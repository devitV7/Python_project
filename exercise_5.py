import sympy as pd

x = pd.symbols("x")
f = x
derivative = pd.diff(f,x)
print(derivative)