"""
By Shabbir Ahmed Hasan
-- Handle missing data.
"""

import pandas as pd
import numpy as np


DATAPATH = "Hotel-Bookings/Data/"

# Step 1: Load the dataset
data = pd.read_csv(f"{DATAPATH}HotelBooking Datasets.csv")

# Step 2: Fill numeric null values with 0, dropping non-numeric due to inconsistency
numeric = data.select_dtypes(include=np.number).columns.to_list()
for x in data.columns:
    if x in numeric:
        data[x].fillna(0, inplace=True)
data.dropna(inplace=True)
