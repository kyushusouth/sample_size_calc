import math

import numpy as np
from scipy import stats
from tqdm import tqdm


def main():
    rng = np.random.default_rng(42)

    alpha = 0.05
    power = 0.8
    beta = 1 - power
    r = 1
    p1 = 0.02
    p2 = p1 * 1.06
    num_simulation = 1000

    p = (p1 + r * p2) / (1 + r)
    z_alpha_half = stats.norm.ppf(q=1 - alpha / 2, loc=0, scale=1)
    z_beta = stats.norm.ppf(q=1 - beta, loc=0, scale=1)

    numerator1 = z_alpha_half * math.sqrt((r + 1) * p * (1 - p))
    numerator2 = z_beta * math.sqrt(r * p1 * (1 - p1) + p2 * (1 - p2))
    numerator = (numerator1 + numerator2) ** 2
    denominator = r * (p1 - p2) ** 2
    n1 = numerator / denominator
    n2 = r * n1
    n = math.ceil(n1 + n2)

    sig_cnt = 0
    for _ in tqdm(range(num_simulation)):
        xs = rng.binomial(1, p1, n)
        ys = rng.binomial(1, p2, n)

        p1_obs = np.mean(xs)
        p2_obs = np.mean(ys)
        p_obs = (p1_obs + r * p2_obs) / (1 + r)

        z = abs(p1_obs - p2_obs) / math.sqrt((1 + r) * p_obs * (1 - p_obs) / (r * n1))
        if z_alpha_half < abs(z):
            sig_cnt += 1

    print(f"power = {sig_cnt / num_simulation}")


if __name__ == "__main__":
    main()
