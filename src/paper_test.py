# Default Imports
import os
import sys
import time
import warnings

# Data Manipulation
import pandas as pd
import numpy as np
import datetime as dt

# Data Visualization
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import seaborn as sns

# Module Imports
from classes.asset_portfolio import AssetPortfolio
from classes.objects import import_data
from classes.objects import color_palette

# Presets
warnings.filterwarnings("ignore")

# From CLEAN_DATA folder, import all data
data_dict = import_data("CLEAN_DATA", ignore_files=["README.md"])

# Replace all values in data_dict with AssetPortfolio objects
for k, v in data_dict.items(): data_dict[k] = AssetPortfolio(k)

print(data_dict)

# Analysis

# Make nested dictionary of all asset metrics
metrics_dict = {}
for k, v in data_dict.items():
    metrics_dict[k] = {
        "Correlation": v.correlation,
        "Excess Return": v.port_mean - v.market_mean,
        "Market Volatility": v.market_vol,
        "Asset Volatility": v.asset_vol,
        "Portfolio Volatility": v.port_vol,
        "Sharpe Ratio": v.sharpe_ratio,
        "Alpha": v.alpha,
        "Beta": v.beta
    }
# Send to dataframe
df = pd.DataFrame(metrics_dict).T
# df.to_csv("metrics.csv")
print(df)

# Plotting Excess Return bar graph matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
ax.bar(df.index, df["Excess Return"], color=color_palette["stevens red"])
ax.set_title("Excess Return of Assets vs. Market")
ax.set_xlabel("Asset")
ax.set_ylabel("Excess Return")
plt.xticks(rotation=90)
plt.show()

