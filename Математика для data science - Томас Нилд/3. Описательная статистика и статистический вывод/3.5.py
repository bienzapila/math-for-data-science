from scipy.stats import norm

print(norm.cdf(64.43, 64.43, 2.99))

print(norm.cdf(70, 64.43, 2.99) - norm.cdf(60, 64.43, 2.99))

print(norm.ppf(.95, loc=64.43, scale=2.99))