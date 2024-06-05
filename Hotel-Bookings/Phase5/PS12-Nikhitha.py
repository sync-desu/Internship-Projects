"""
By Chilaka Nikhitha
-- Visualize booking cancellations across years and countries, and identify cancellation patterns by hotel type and market segment.
"""

import pandas as pd
import numpy as np
import seaborn as sns
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
# Summarize cancellations by year and country
cancellations_by_year_country = data.groupby(["arrival_date_year", "country"])["is_canceled"].sum().reset_index()

# Summarize cancellations by hotel type and market segment
cancellations_by_hotel_market = data.groupby(["hotel", "market_segment"])["is_canceled"].sum().reset_index()

# Step 3: Visualize the data

# Visualization 1: Cancellations over Years by Country
sns.lineplot(data=cancellations_by_year_country, x="arrival_date_year", y="is_canceled", hue="country", marker="o")
plt.title("Booking Cancellations over Years by Country")
plt.xlabel("Year")
plt.ylabel("Number of Cancellations")
plt.legend(title="Country")
plt.grid(True)
plt.show()

# Visualization 2: Cancellations by Hotel Type and Market Segment
sns.barplot(data=cancellations_by_hotel_market, x="hotel", y="is_canceled", hue="market_segment", errorbar=None)
plt.title("Booking Cancellations by Hotel Type and Market Segment")
plt.xlabel("Hotel Type")
plt.ylabel("Number of Cancellations")
plt.legend(title="Market Segment")
plt.grid(True)
plt.show()

# Visualization 3: Heatmap of Cancellations by Year and Country
pivot_table = cancellations_by_year_country.pivot_table(values="is_canceled", index="country", columns="arrival_date_year", aggfunc="sum")
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap of Booking Cancellations by Year and Country")
plt.xlabel("year")
plt.ylabel("Country")
plt.show()
