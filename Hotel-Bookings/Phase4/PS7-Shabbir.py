"""
By Shabbir Ahmed Hasan
-- Analyze room type rates per night per person by hotel, and perform comparative analysis of average prices per night per country.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


DATAPATH = "Hotel-Bookings/Data/"

# 1. Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# 1.1 Clean the data
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# 2. Explore and clean the data
print(data.info())
print(data.describe())
data.dropna(inplace=True)

# 3. Calculate the rate per person per night
data["rate_per_person_per_night"] = data["room_rate_per_night"] / data["total_visitors"]

# 4. Group the data by hotel, room type, and country
grouped = data.groupby(["hotel", "assigned_room_type", "country"])

# 5. Calculate the average rate per person per night for each group
avg_rate = grouped["rate_per_person_per_night"].mean().reset_index()

print(avg_rate)

# 6. Create seaborn bar plots
plt.figure(figsize=(12, 8))
sns.barplot(x="hotel", y="rate_per_person_per_night", hue="assigned_room_type", data=avg_rate)
plt.title("Average Rate per Person per Night by Hotel and Room Type")
plt.xlabel("Hotel")
plt.ylabel("Rate per Person per Night")
plt.show()

# Create separate plots for each country
countries = data["country"].unique()

def chunk(l, n):
    for i in range(0, len(l), n):
        yield l[i: i+n]

for country_chunk in chunk(countries, 4):
    plt.figure(figsize=(12, 8))
    for i, country in enumerate(country_chunk):
        plt.subplot(2, 2, i+1)
        country_data = avg_rate[avg_rate["country"] == country]
        sns.barplot(x="hotel", y="rate_per_person_per_night", hue="assigned_room_type", data=country_data)
        plt.title(f"Average Rate per Person per Night by Hotel and Room Type - {country}")
        plt.xlabel("Hotel")
        plt.ylabel("Rate per Person per Night")
    plt.tight_layout()
    plt.show()
