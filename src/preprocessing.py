# Preprocessing
# The purpose of this file is to preprocess all the raw data and output clean data (for auto running purposes)

# __Imports__

import pandas as pd
import os
from classes.objects import import_data

# __Download Data__

data_dict = import_data("RAW_DATA", ignore_files=["README.md"])

# Categorize data based on where we pulled them from and put them in their own lists

# Yahoo Finance Data
yfinance_data = ["T3", "T10", "T20", "SP500", "NASDAQ", "DOW", "BTC", "ETH", "OIL", "GOLD", "REST"]

# Clean Yahoo Finance Data

for k in yfinance_data:
    # Interpolate missing values
    data_dict[k] = data_dict[k][["Adj Close", "Volume"]].interpolate(method="time")
    data_dict[k]["Returns"] = data_dict[k]["Adj Close"].pct_change().fillna(0)
    # Check if there are still any nan values in the data
    if not data_dict[k].notna().all().all():
        raise Exception("NaNs in data")

# ## Export all Cleaned Data

# Push all cleaned data files to csv in CLEAN_DATA folder
for k, v in data_dict.items():
    v.to_csv("CLEAN_DATA/" + k + ".csv", header=True, index_label="Date")


