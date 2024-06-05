"""
By Chilaka Nikhitha
-- Visualize the most booked room types across countries and perform an analysis for reserved_room_type, sorted by values, with hue set to hotel.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


DATAPATH = "Hotel-Bookings/Data/"

# Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the data
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Group the data by country and room type and count the occurrences
room_type_counts = data.groupby(["hotel", "country", "reserved_room_type"])["reserved_room_type"].count().reset_index(name="counts")

# Sort the data by counts in descending order
room_type_counts = room_type_counts.sort_values(by=["counts"], ascending=False)

# Create a countplot visualization
plt.figure(figsize=(15, 8))
sns.countplot(x="reserved_room_type", hue="hotel", data=room_type_counts, order=room_type_counts["reserved_room_type"].value_counts().index)
plt.title("Popularity of Room Types Across Countries")
plt.xlabel("Room Type")
plt.ylabel("Number of Bookings")
plt.legend(title="Country")
plt.show()
