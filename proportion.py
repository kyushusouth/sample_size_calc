import math

from scipy import stats

# params
alpha = 0.05
power = 0.8
beta = 1 - power
r = 1
p1 = 0.02
p2 = p1 * 1.06

p = (p1 + r * p2) / (1 + r)
z_alpha_half = stats.norm.ppf(q=1 - alpha / 2, loc=0, scale=1)
z_beta = stats.norm.ppf(q=1 - beta, loc=0, scale=1)

numerator1 = z_alpha_half * math.sqrt((r + 1) * p * (1 - p))
numerator2 = z_beta * math.sqrt(r * p1 * (1 - p1) + p2 * (1 - p2))
numerator = (numerator1 + numerator2) ** 2
denominator = r * (p1 - p2) ** 2
n1 = numerator / denominator
n2 = r * n1
n = n1 + n2
print(n)

z = abs(p1 - p2) / math.sqrt((1 + r) * p * (1 - p) / (r * n1))
print(z)
print(z_alpha_half)
