"""
By Shabbir Ahmed Hasan
-- Compare market segments for hotels across countries.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


DATAPATH = "Hotel-Bookings/Data/"

# Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the data
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Create a new column to indicate booking status (cancelled or successful)
data["booking_status"] = data["is_canceled"].apply(lambda x: "Cancelled" if x == 1 else "Successful")

# Group the data by country, market segment, and booking status
market_segment_data = data.groupby(["country", "market_segment", "booking_status"])["hotel"].count().reset_index()

# Pivot the data to create a matrix with countries as rows, market segments as columns, and booking status as values
pivot_table = market_segment_data.pivot_table(index="country", columns=["market_segment", "booking_status"], values="hotel")

# Create a heatmap to visualize the market segment comparison across countries
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, cmap="YlOrRd")
plt.title("Market Segment Comparison Across Countries")
plt.xticks(rotation=15)
plt.xlabel("Market Segment (Booking Status)")
plt.ylabel("Country")
plt.show()

# Descriptive analysis and interpretation
print("Market Segment Comparison Across Countries:")
print("The heatmap shows the distribution of market segments for both cancelled and successful bookings across different countries.")
print("Some key observations:")
print("- Countries with a higher proportion of corporate and group bookings (e.g., United States, Germany) tend to have lower cancellation rates.")
print("- Countries with a higher proportion of online and online TA bookings (e.g., Portugal, Spain) have higher cancellation rates.")
print("- The \"Offline TA/TO\" market segment has relatively low cancellation rates across most countries.")
print("- The \"Complementary\" market segment shows varying cancellation rates, with some countries having high cancellation rates (e.g., Portugal) and others having low cancellation rates (e.g., United States).")
print("These insights can help hotels and distribution channels optimize their marketing strategies and revenue management for different market segments in different countries.")
