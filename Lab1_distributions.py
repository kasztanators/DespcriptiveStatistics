import matplotlib.pyplot as plt
from scipy.stats import binom
## Exercise 1.

#As a sport analyst, you would like to calculate some probabilities for basketball player who is shooting guard.

#n = 10 attempts and
#p = 0.7 the probability for scoring three-points 

#Calculate the following probabilities: P(X ≤ 3), P(X < 3), P(X > 4) and P(X = 7).

n = 10
p = 0.7

r_values = list(range(n + 1))
mean, var = binom.stats(n, p)
dist = [binom.pmf(r, n, p) for r in r_values ]

plt.bar(r_values, dist)
plt.xlabel("x")
plt.ylabel("probablity")
plt.show()