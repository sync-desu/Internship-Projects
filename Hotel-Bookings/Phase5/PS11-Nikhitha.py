"""
By Chilaka Nikhitha
-- Visualize the percentage of adults accompanying children to hotels across countries using a pie chart.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATAPATH = "Hotel-Bookings/Data/"

# Step 1: Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the data
numerical_cols = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numerical_cols:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Step 2: Analyze the data
# Group by "country" and sum "total_visitors"
country_data = data.groupby("country")["total_visitors"].sum().reset_index()

# Calculate total and percentages
total_visitors = country_data["total_visitors"].sum()
country_data["Percentage"] = (country_data["total_visitors"] / total_visitors) * 100

# Step 3: Visualize the data using a pie chart
labels = country_data["country"]
sizes = country_data["Percentage"]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Percentage of Adults Accompanying Children to Hotels by Country")
plt.show()
