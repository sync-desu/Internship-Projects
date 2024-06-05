import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


DATAPATH = "Hotel-Bookings/Data/"

# Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Clean the data
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)

# Order of months
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Create a figure and axes
fig, axes = plt.subplots(2, 1)

# Create the line plot for total visitors with custom palette and month order
sns.lineplot(
    data=data, 
    x="arrival_date_month", 
    y="total_visitors", 
    hue="arrival_date_year", 
    linewidth=2, 
    ax=axes[0], 
    hue_order=sorted(data["arrival_date_year"].unique()), 
    palette="Set2"
)

# Set the title and labels for the total visitors plot
axes[0].set_title("Total Bookings by Month")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Number of Bookings")
axes[0].set_xticks(range(len(month_order)))
axes[0].set_xticklabels(month_order)
axes[0].legend(title="Year")

# Create the line plot for weekend visitors with custom palette and month order
sns.lineplot(
    data=data, 
    x="arrival_date_month", 
    y="weekend_visitors", 
    hue="arrival_date_year", 
    linewidth=2, 
    ax=axes[1], 
    hue_order=sorted(data["arrival_date_year"].unique()), 
    palette="Set1"
)

# Set the title and labels for the weekend visitors plot
axes[1].set_title("Weekend Bookings by Month")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Number of Weekend Bookings")
axes[1].set_xticks(range(len(month_order)))
axes[1].set_xticklabels(month_order)
axes[1].legend(title="Year")

# Show the plot
plt.tight_layout()
plt.show()

# Calculate the year with the most weekend bookings
weekend_bookings_per_year = data.groupby("arrival_date_year")["weekend_visitors"].sum()
year_with_most_weekend_bookings = weekend_bookings_per_year.idxmax()

print(f"The year with the most weekend bookings is {year_with_most_weekend_bookings} with {weekend_bookings_per_year.max()} weekend bookings.")
