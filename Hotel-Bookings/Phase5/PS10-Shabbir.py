"""
By Shabbir Ahmed Hasan
-- Perform a HeatMap Correlation Analysis.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


DATAPATH = "Hotel-Bookings/Data/"

# Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the data
numerical_cols = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numerical_cols:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Calculate the correlation matrix
corr_matrix = data[numerical_cols].corr().round(2)

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()
