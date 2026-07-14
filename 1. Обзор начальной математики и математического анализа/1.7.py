from sympy import *

def derivative(f, x, step_size):
    m = ((f(x + step_size) - f(x))/((x+step_size) - x))
    return m

def my_func(x):
    return x ** 2

result = derivative(my_func, 2, 0.1)
print(result)

n = symbols('n')
lim_result = limit(derivative(my_func, 2, n), n, 0)
print(lim_result)