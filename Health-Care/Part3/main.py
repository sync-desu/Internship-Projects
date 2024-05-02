"""
Team Members:
- Shabbir Ahmed Hasan (22BTRCL139)
- Chilaka Nikhitha (22BTRCL042)
- Harshitha P (22BTRCL064)
- Amrit Sutradhar (22BTRCL014) : Leader

Typehinting, formatting, merging and finalization of this code
have been performed by Amrit Sutradhar.
"""

import pandas as pd
import numpy as np


DATA_PATH = "Health-Care/Data/"
SAVE_PATH = "Health-Care/Clean-Data/"


### Problem Statement 13: Simplifying dataset with multiple headers (by Amrit Sutradhar)
govthosp_data = pd.read_csv(f"{DATA_PATH}government_hospitals.csv", header=[0, 1])
govthosp_rename_map = {
    "Unnamed: 0_level_1": "",
    "Unnamed: 2_level_0": "Rural hospitals",
    "Unnamed: 4_level_0": "Urban hospitals",
    "Unnamed: 5_level_1": ""
}
govthosp_data = govthosp_data.rename(columns=govthosp_rename_map)

govthosp_required_map = {
    "State/UT": govthosp_data["States/UTs"],
    "Rural_Government_Hospitals": govthosp_data["Rural hospitals"]["No."],
    "Rural_Government_Beds": govthosp_data["Rural hospitals"]["Beds"],
    "Urban_Government_Hospitals": govthosp_data["Urban hospitals"]["No."],
    "Urban_Government_Beds": govthosp_data["Urban hospitals"]["Beds"],
    "Last_Updated": govthosp_data["As on"]
}
required_govthosp_data = pd.DataFrame(govthosp_required_map)
print(f"13] Simplified multi-header dataset\n{required_govthosp_data.head()}\n")


### Problem Statement 14: Simplifying dataset with multiple headers (by Amrit Sutradhar)
def update_date(date: str) -> str:
    if date is not np.nan:
        valid = []
        for x in date.split("."):
            valid.append(x)
        return "-".join(valid[::-1])
    return np.nan
required_govthosp_data["Last_Updated"] = required_govthosp_data["Last_Updated"].apply(update_date)
print(f"14.1] Updating date\n{required_govthosp_data.head()}\n")

def normalize_names(name: str) -> str:
    chars = name.split()
    if name.isupper():
        nchars = []
        for word in chars:
            nchars.append(word.capitalize())
        chars = nchars
    name = " ".join(chars)
    return name.replace("*", "").replace("&", "and")
required_govthosp_data["State/UT"] = required_govthosp_data["State/UT"].apply(normalize_names)
print(f"14.2] Updating State/UT (normalizing)\n{required_govthosp_data.head()}\n")

required_govthosp_data.to_csv(f"{SAVE_PATH}government_hospital.csv", index=False)
