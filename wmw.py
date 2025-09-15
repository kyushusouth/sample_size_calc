from scipy import stats

# params
alpha = 0.05
power = 0.8
beta = 1 - power
r = 1
p = 0.501

z_alpha_half = stats.norm.ppf(q=1 - alpha / 2, loc=0, scale=1)
z_beta = stats.norm.ppf(q=1 - beta, loc=0, scale=1)

numerator = (z_alpha_half + z_beta) ** 2 * (1 + r)
denominator = 12 * r * (p - 0.5) ** 2
n1 = numerator / denominator
n2 = r * n1
n = n1 + n2
print(n)
