library("tidyverse")
library("WMWssp")
set.seed(42)

n_obs <- 800000
x_n_cv_obs <- 2000
y_n_cv_obs <- x_n_cv_obs * 1.08
indices <- 1:n_obs
x_cv_indices <- sample(indices, x_n_cv_obs, replace=TRUE)
y_cv_indices <- sample(indices, y_n_cv_obs, replace=TRUE)
xs <- rep(0, n_obs)
ys <- rep(0, n_obs)

for (i in x_cv_indices) {
  xs[i] <- xs[i] + 1
}
for (i in y_cv_indices) {
  ys[i] <- ys[i] + 1
}

sum(xs)
sum(xs ** 2)
sum(ys)

ssp <- WMWssp(xs, ys, alpha=0.05, power=0.8, t=0.5)
summary(ssp)
