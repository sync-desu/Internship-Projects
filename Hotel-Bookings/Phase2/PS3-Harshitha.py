"""
By Harshitha P
-- Performing EDA on key attributes and identifying outliers."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


DATAPATH = "Hotel-Bookings/Data/"

# Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the dataset
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Histogram for lead time
plt.subplot(2, 2, 1)
sns.histplot(data["lead_time"], bins=30, kde=True)
plt.title("Distribution of Lead Time")
plt.xlabel("Lead Time")
plt.ylabel("Frequency")

# Histogram for total visitors
plt.subplot(2, 2, 2)
sns.histplot(data["total_visitors"], bins=30, kde=True)
plt.title("Distribution of Total Visitors")
plt.xlabel("Total Visitors")
plt.ylabel("Frequency")

# Histogram for room rate per night
plt.subplot(2, 2, 3)
sns.histplot(data["room_rate_per_night"], bins=30, kde=True)
plt.title("Distribution of Room Rate per Night")
plt.xlabel("Room Rate per Night")
plt.ylabel("Frequency")

# Histogram for rate per person per night
plt.subplot(2, 2, 4)
sns.histplot(data["rate_per_person_per_night"], bins=30, kde=True)
plt.title("Distribution of Rate per Person per Night")
plt.xlabel("Rate per Person per Night")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Scatter plot between lead time and total visitors
plt.subplot(2, 2, 1)
sns.scatterplot(x="lead_time", y="total_visitors", data=data)
plt.title("Lead Time vs Total Visitors")
plt.xlabel("Lead Time")
plt.ylabel("Total Visitors")

# Scatter plot between lead time and room rate per night
plt.subplot(2, 2, 2)
sns.scatterplot(x="lead_time", y="room_rate_per_night", data=data)
plt.title("Lead Time vs Room Rate per Night")
plt.xlabel("Lead Time")
plt.ylabel("Room Rate per Night")

# Box plot for lead time by visitor type
plt.subplot(2, 2, 3)
sns.boxplot(x="guest_age_group", y="lead_time", data=data)
plt.title("Lead Time by Guest Age Group")
plt.xlabel("Guest Age Group")
plt.ylabel("Lead Time")

# Box plot for room rate per night by visitor type
plt.subplot(2, 2, 4)
sns.boxplot(x="guest_age_group", y="room_rate_per_night", data=data)
plt.title("Room Rate per Night by Guest Age Group")
plt.xlabel("Guest Age Group")
plt.ylabel("Room Rate per Night")

plt.tight_layout()
plt.show()

# Box plot for lead time to detect outliers
plt.subplot(1, 2, 1)
sns.boxplot(y="lead_time", data=data)
plt.title("Box Plot for Lead Time")
plt.ylabel("Lead Time")

# Box plot for room rate per night to detect outliers
plt.subplot(1, 2, 2)
sns.boxplot(y="room_rate_per_night", data=data)
plt.title("Box Plot for Room Rate per Night")
plt.ylabel("Room Rate per Night")

plt.tight_layout()
plt.show()

# Detecting outliers using IQR
Q1 = data[["lead_time", "room_rate_per_night"]].quantile(0.25)
Q3 = data[["lead_time", "room_rate_per_night"]].quantile(0.75)
IQR = Q3 - Q1

outliers_lead_time = data[(data["lead_time"] < (Q1["lead_time"] - 1.5 * IQR["lead_time"])) | (data["lead_time"] > (Q3["lead_time"] + 1.5 * IQR["lead_time"]))]
outliers_room_rate_per_night = data[(data["room_rate_per_night"] < (Q1["room_rate_per_night"] - 1.5 * IQR["room_rate_per_night"])) | (data["room_rate_per_night"] > (Q3["room_rate_per_night"] + 1.5 * IQR["room_rate_per_night"]))]

print(f"Outliers lead_time shape: {outliers_lead_time.shape}")
print(f"Outliers room_rate_per_night shape: {outliers_room_rate_per_night.shape}")
