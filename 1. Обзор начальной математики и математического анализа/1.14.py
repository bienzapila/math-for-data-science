from sympy import *

x = symbols('x')
func = 3 * x ** 2 + 1
ans = diff(func)
print(ans.subs(x, 3))