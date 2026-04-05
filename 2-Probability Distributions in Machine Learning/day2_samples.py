import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson
import seaborn as sns

# Gaussian Distribution
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, loc=0, scale=1), label="Gaussian (u=0, s=1)")

# Binomial Distribution
n, p = 10, 0.5
bar_width = 0.4
x_binom = np.arange(0, n+1)
plt.bar(x_binom - bar_width/2, binom.pmf(x_binom, n, p), width=bar_width, alpha=0.7, label="Binomial (n=10, p=0.5)")

#Poisson Distribution
lam = 3
x_poisson = np.arange(0, 10)
plt.bar(x_poisson + bar_width/2, poisson.pmf(x_poisson, lam), width=bar_width, alpha=0.7, label="Poisson (l = 3)")

# Uniform Distribution
x = np.random.uniform(low=0, high=10, size=1000)
sns.histplot(x, kde=True, stat="density", label="Uniform", color="red")

plt.title("Probability Distributions")
plt.legend()
plt.show()