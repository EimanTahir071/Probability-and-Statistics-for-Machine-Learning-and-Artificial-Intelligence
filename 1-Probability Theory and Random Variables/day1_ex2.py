import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

EXAMPLE = "uniform"


def plot_dice_pmf():
    outcomes = [1, 2, 3, 4, 5, 6]
    probabilities = [1 / 6] * 6
    plt.bar(outcomes, probabilities, color="blue", alpha=0.7)
    plt.title("PMF of a Dice Roll")
    plt.xlabel("Outcomes")
    plt.ylabel("Probability")
    plt.show()


def plot_uniform_pdf():
    x = np.linspace(0, 1, 100)
    pdf = uniform.pdf(x, loc=0, scale=1)
    plt.plot(x, pdf, color="red")
    plt.title("PDF of Uniform(0,1)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.show()


if EXAMPLE == "dice":
    plot_dice_pmf()
elif EXAMPLE == "uniform":
    plot_uniform_pdf()
else:
    raise ValueError("EXAMPLE must be either 'dice' or 'uniform'")