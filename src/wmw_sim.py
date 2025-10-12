import numpy as np
from scipy import stats
from tqdm import tqdm


def main():
    n_sim = 100
    n1 = 980000
    n2 = 980000

    # 検出力チェック
    cnt = 0
    for _ in tqdm(range(n_sim)):
        rng = np.random.default_rng()
        n_cv_1 = int(n1 * 0.0025)
        n_cv_2 = int(n_cv_1 * 1.08)
        x_cv_indices = rng.choice(n1, n_cv_1, replace=True)
        y_cv_indices = rng.choice(n2, n_cv_2, replace=True)
        xs = np.zeros(n1)
        ys = np.zeros(n2)
        for i in x_cv_indices:
            xs[i] += 1
        for i in y_cv_indices:
            ys[i] += 1
        res = stats.mannwhitneyu(xs, ys)
        if res.pvalue <= 0.05:
            cnt += 1
    print(cnt / n_sim)

    # 第一種の誤りチェック
    cnt = 0
    for _ in tqdm(range(n_sim)):
        rng = np.random.default_rng()
        n_cv_1 = int(n1 * 0.0025)
        n_cv_2 = n_cv_1
        x_cv_indices = rng.choice(n1, n_cv_1, replace=True)
        y_cv_indices = rng.choice(n2, n_cv_2, replace=True)
        xs = np.zeros(n1)
        ys = np.zeros(n2)
        for i in x_cv_indices:
            xs[i] += 1
        for i in y_cv_indices:
            ys[i] += 1
        res = stats.mannwhitneyu(xs, ys)
        if res.pvalue <= 0.05:
            cnt += 1
    print(cnt / n_sim)


if __name__ == "__main__":
    main()
