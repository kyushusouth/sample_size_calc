from statsmodels.stats.power import tt_ind_solve_power

mean1 = 0.0027
mean2 = mean1 * 1.1
std = 0.1
effect_size = (mean1 - mean2) / std
n = tt_ind_solve_power(
    effect_size=effect_size,
    nobs1=None,
    alpha=0.05,
    power=0.8,
    ratio=1.0,
    alternative="two-sided",
)
print(n)
