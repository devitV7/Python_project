import sympy as sp

x = sp.symbols('x')
f = x**2

derivative = sp.diff(f, x,2 )

print(derivative)