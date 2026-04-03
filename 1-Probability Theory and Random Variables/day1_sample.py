import numpy as np


def validate_distribution(outcomes, probabilities):
    if len(outcomes) != len(probabilities):
        raise ValueError("outcomes and probabilities must have the same length")
    if np.any(probabilities < 0):
        raise ValueError("probabilities must be non-negative")
    if not np.isclose(np.sum(probabilities), 1.0):
        raise ValueError("probabilities must sum to 1")


def die_stats():
    # Random variable: dice roll
    outcomes = np.array([1, 2, 3, 4, 5, 6])
    probabilities = np.array([1/6] * 6)
    validate_distribution(outcomes, probabilities)

    # Expectation
    expectation = np.sum(outcomes * probabilities)
    print(f"Expectation (Mean): {expectation}")

    # Variance and Standard Deviation
    variance = np.sum((outcomes - expectation)**2 * probabilities)
    std_dev = np.sqrt(variance)
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")


if __name__ == "__main__":
    die_stats()
