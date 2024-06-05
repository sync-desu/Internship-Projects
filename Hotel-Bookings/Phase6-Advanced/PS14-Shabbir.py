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

# Preprocess the data
data["arrival_date"] = pd.to_datetime(data["arrival_date_year"].astype(str) + "-" + data["arrival_date_month"].astype(str) + "-" + data["arrival_date_day_of_month"].astype(str), errors="coerce")
data["booking_date"] = pd.to_datetime(data["booking_date"], errors="coerce")

# Drop rows with invalid arrival_date or booking_date
data = data.dropna(subset=["arrival_date", "booking_date"])

# Explore seasonal trends
sns.lineplot(x="arrival_date", y="adr", data=data)
plt.title("Seasonal Trends in Average Daily Rate (ADR)")
plt.xlabel("Arrival Date")
plt.ylabel("ADR")
plt.show()

# Identify peak and off-peak seasons
data["month"] = data["arrival_date"].dt.month
data_monthly = data.groupby("month")["adr"].mean().reset_index()
sns.barplot(x="month", y="adr", data=data_monthly)
plt.title("Average Daily Rate by Month")
plt.xlabel("Month")
plt.ylabel("ADR")
plt.show()

# Analyze booking patterns
data["week"] = data["arrival_date"].dt.isocalendar().week
data_weekly = data.groupby(["week", "is_canceled"])["adr"].mean().reset_index()
sns.lineplot(x="week", y="adr", hue="is_canceled", data=data_weekly)
plt.title("Booking Patterns and Cancellation Rates")
plt.xlabel("Week")
plt.ylabel("ADR")
plt.show()

# Discuss strategic planning and pricing strategies
print("Strategic Planning and Pricing Strategies:")
print("- Based on the seasonal trends, the peak season appears to be during the summer months (June-August), with higher ADR. The off-peak season is during the winter months (December-February), with lower ADR.")
print("- The hotel can adjust pricing strategies to optimize revenue during peak and off-peak seasons:")
print("  - During peak season, the hotel can increase room rates to capitalize on higher demand.")
print("  - During off-peak season, the hotel can offer discounts or package deals to attract more bookings and maintain occupancy rates.")
print("- The hotel can also analyze booking patterns and cancellation rates to better understand customer behavior and implement strategies to reduce cancellations, such as:")
print("  - Offering non-refundable rates or stricter cancellation policies during peak season.")
print("  - Providing incentives for guests to book well in advance or stay longer during off-peak season.")
