"""
By Amrit Sutradhar
-- Identifying the top-3 countries from which the highest number of guests have placed bookings.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


DATAPATH = "Hotel-Bookings/Data/"

# Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the dataset
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Calculate the count of guests per country
country_counts = data["country"].value_counts()
total_guests = country_counts.sum()

# Calculate the percentage of total guests per country and round to 2 decimal places
country_percentage = (country_counts / total_guests) * 100
country_percentage = country_percentage.round(2)

# Identify the top 3 countries by the percentage of total guests
top_3_countries = country_percentage.head(3)

# Plotting the percentage of guests per country
plt.subplot(1, 2, 1)
country_percentage.plot(kind="bar")
plt.title("Percentage of Total Guests per Country")
plt.xlabel("Country")
plt.ylabel("Percentage")

# Highlighting the top 3 countries
plt.subplot(1, 2, 2)
top_3_countries.plot(kind="bar", color=["blue", "orange", "green"])
plt.title("Top 3 Countries by Percentage of Guests")
plt.xlabel("Country")
plt.ylabel("Percentage")

plt.tight_layout()
plt.show()
