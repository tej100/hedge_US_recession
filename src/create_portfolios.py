# The purpose of this file is to create portfolios based on the cleaned data and output the portfolios (for auto running purposes)

import pandas as pd

from classes.asset_portfolio import AssetPortfolio
from classes.objects import import_data

# Import all data
data_dict = import_data("CLEAN_DATA", ignore_files=["README.md"])

# Replace all values in data_dict with AssetPortfolio objects
for k, v in data_dict.items():
    data_dict[k] = AssetPortfolio(k)

print(data_dict)