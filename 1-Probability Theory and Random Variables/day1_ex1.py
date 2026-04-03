import numpy as np

# Simulating 10,000 dice rolls
rolls = np.random.randint(1, 7, size=10000)

# Calculate probabilities
P_even = np.sum(rolls % 2 == 0) / len(rolls)
P_greater_than_4 = np.sum(rolls > 4) / len(rolls)

print("P(Even): ", P_even)
print("P(Greater than 4): ", P_greater_than_4)