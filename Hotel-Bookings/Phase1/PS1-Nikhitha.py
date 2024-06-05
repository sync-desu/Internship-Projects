"""
By Chilaka Nikhitha
-- Calculating summary statistics, highlighting key attributes using various visualizations, and identifying normal/skewed distribution.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats


DATAPATH = "Hotel-Bookings/Data/"


# Step 1: Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Step 2: Create visualizations
def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i: i+n]

numeric = data.select_dtypes(include=np.number).columns
first_half, second_half = chunk(numeric, round(len(numeric)/2))

#Histograms
for x in chunk(first_half, 4):
    for i, column in enumerate(x, 1):
        plt.subplot(2, 2, i)
        sns.histplot(data[column].dropna().values, kde=True)
        plt.title(f"Histogram of {column}")
    plt.tight_layout()
    plt.show()

# Box plots
for x in chunk(second_half, 4):
    for i, column in enumerate(x, 1):
        plt.subplot(2, 2, i)
        sns.boxplot(x=data[column].values)
        plt.title(f"Box Plot of {column}")
    plt.tight_layout()
    plt.show()

# Step 4: Identify distributions as normal or skewed
normality_results = {}
for column in numeric:
    stat, p_value = stats.shapiro(data[column].dropna())
    if p_value > 0.05:
        normality_results[column] = "Normal"
    else:
        normality_results[column] = "Skewed"

# Step 5: Provide a detailed report of findings
report = f"Summary Statistics:\n{data.describe()}\n\nDistribution Analysis:"
for column, distribution in normality_results.items():
    report += f"{column}: {distribution}\n"

print(report)
