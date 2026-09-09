import sympy as PD

x = PD.symbols("x")
f= x**4  # E**x*2 = 2*e^x ,g=2
d = PD.diff(f, x)
d1 = PD.diff(f, x ,2)
print(d)
print(d1)