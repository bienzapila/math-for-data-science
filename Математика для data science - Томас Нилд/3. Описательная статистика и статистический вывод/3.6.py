from scipy.stats import norm
import matplotlib.pyplot as plt
import random

data = []
for _ in range(100000):
    rand = random.uniform(0, 1)
    rand_v = norm.ppf(rand, 64.43, 2.99)
    data.append(rand_v)
print(data)
plt.hist(data, bins=100)
plt.show()

