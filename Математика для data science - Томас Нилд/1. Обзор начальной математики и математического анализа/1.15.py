from sympy import *

x = symbols('x')
func = 3 * x ** 2 + 1

ans = integrate(func, (x, 0, 2))
print(ans)