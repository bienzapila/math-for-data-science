from sympy import *
import webbrowser

x, y = symbols('x y')
z = x ** 2 / sqrt(2*y**3 - 1)
webbrowser.open('https://latex.codecogs.com/png.image?\dpi{200}' + latex(z))