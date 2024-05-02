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


### Problem Statement 1: Filter required columns (by Shabbir Ahmed Hasan)
census_data = pd.read_csv("Health-Care/Data/census_2011.csv")
required_columns = [
    "State name", "District name", "Population", "Male", "Female",
    "Literate", "Male_Literate", "Female_Literate", "Rural_Households",
    "Urban_Households", "Households", "Age_Group_0_29", "Age_Group_30_49",
    "Age_Group_50", "Age not stated"
]

filtered_data = census_data[required_columns]


### Problem Statement 2: Rename columns (by Chilaka Nikhitha)
column_name_mapping = {
    "State name": "State/UT",
    "District name": "District",
    "Male_Literate": "Literate_Male",
    "Female_Literate": "Literate_Female",
    "Rural_Households": "Households_Rural",
    "Urban_Households": "Households_Urban",
    "Age_Group_0_29": "Young_and_Adult",
    "Age_Group_30_49": "Middle_Aged",
    "Age_Group_50": "Senior_Citizen",
    "Age not stated": "Age_Not_Stated"
}

filtered_data = filtered_data.rename(columns=column_name_mapping)


### Problem Statement 3: Rename State/UT names (by Harshitha P)
def rename_states(name: str) -> str:
    formatted_words = []
    for word in name.split():
        if word.lower() == "and":
            formatted_words.append(word.lower())
        else:
            formatted_words.append(word.capitalize())
    return " ".join(formatted_words)

filtered_data["State/UT"] = filtered_data["State/UT"].apply(rename_states)


### Problem Statement 4: Update new State/UT formations (by Amrit Sutradhar)
telangana_districts = ["Adilabad", "Nizamabad", "Karimnagar", "Medak",
"Hyderabad", "Rangareddy", "Mahbubnagar", "Nalgonda", "Warangal", "Khammam"]
laddakh_districts = ["Leh(Ladakh)", "Kargil"]

def update_state_formations(row: pd.Series) -> pd.Series:
    if row["District"] in telangana_districts:
        row["State/UT"] = "Telangana"
    elif row["District"] in laddakh_districts:
        row["State/UT"] = "Laddakh"
    return row

filtered_data = filtered_data.apply(update_state_formations, axis=1)

telangana_data = filtered_data.loc[filtered_data["State/UT"] == "Telangana"]
laddakh_data = filtered_data.loc[filtered_data["State/UT"] == "Laddakh"]


if __name__ == "__main__":
    print(f"1] Filtered data:\n{filtered_data.head()}\n")
    print(f"2] Data with renamed columns:\n{filtered_data.head()}\n")
    print(f"3] Data with renamed & uniform State/UT:\n{filtered_data.head()}\n")
    print(f"4.1] Updated Telangana district data:\n{telangana_data}\n")
    print(f"4.2] Updated Laddakh district data:\n{laddakh_data}\n")
