from sympy import *

x = symbols('x')
f = x ** 2
result = diff(f, x)
print(result)

def func(x):
    return x ** 2

def dx_f(x):
    return 2 * x

slope_at_2 = dx_f(2)
print(slope_at_2)

dx_f = diff(f, x)
print(dx_f.subs(x, 2))