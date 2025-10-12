import math

from scipy import stats


def proportion_test_sample_size(
    alpha: float, beta: float, r: float, p1: float, p2: float
):
    """比率の差の検定において必要なサンプルサイズを計算する

    Args:
        alpha (float): 有意水準
        beta (float): 第二種の誤りを起こす確率（1 - 検出力）
        r: 第一群のサンプルサイズ`n1`と第二群のサンプルサイズ`n2`の比率(`r=n1/n2`)
        p1: 第一群の母比率
        p2: 第二群の母比率

    Returns:
        n (int): 必要なサンプルサイズ

    """
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
    return n


def main():
    alpha = 0.05
    power = 0.8
    beta = 1 - power
    r = 1
    p1 = 0.02
    p2 = p1 * 1.06

    n = proportion_test_sample_size(alpha, beta, r, p1, p2)
    print(n)


if __name__ == "__main__":
    main()
