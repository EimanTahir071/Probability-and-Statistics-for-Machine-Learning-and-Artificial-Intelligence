import numpy as np

rng = np.random.default_rng(42)

# Simulating 10,000 dice rolls
rolls = rng.integers(1, 7, size=10000)

# Calculate probabilities
p_even = np.sum(rolls % 2 == 0) / len(rolls)
p_greater_than_4 = np.sum(rolls > 4) / len(rolls)

print("P(Even): ", p_even)
print("P(Greater than 4): ", p_greater_than_4)