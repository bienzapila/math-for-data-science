from scipy.stats import *

s = 0
for k in range(50, 138):
    s += binom.pmf(k, 137, .4)

print(s)