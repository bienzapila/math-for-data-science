from scipy.stats import *

n, p = 10, .9

for k in range(0, 11):
    print(binom.pmf(k, n, p))