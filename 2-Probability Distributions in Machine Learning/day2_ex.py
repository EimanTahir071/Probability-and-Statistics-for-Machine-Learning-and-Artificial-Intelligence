#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Analyse sepal_length
feature = df["sepal_length"]
print("Skewness: ", skew(feature))
print("Kurtosis: ", kurtosis(feature))

# Visualize distribution
sns.histplot(feature, kde=True)
plt.title("Distribution of Sepal Lenth")
plt.show()