# Default Imports
import os
import sys
import time
import warnings
from loguru import logger

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
from classes.objects import color_palette, rf

# Presets
warnings.filterwarnings("ignore")

# From CLEAN_DATA folder, import all data
data_dict = import_data("CLEAN_DATA", ignore_files=["README.md"])

recession_portfolios = {}
bullish_portfolios = {}
full_portfolios = {}

# Replace all values in data_dict with AssetPortfolio objects
for k in data_dict.keys():
    logger.info(f"Creating Portfolios for {k}")
    full_portfolios[k] = AssetPortfolio(k)
    recession_portfolios[k] = AssetPortfolio(k, "recession")
    bullish_portfolios[k] = AssetPortfolio(k, "bullish")
    logger.success(f"Portfolios for {k} Created")


############
# Analysis #
############

# Import csvs from OUTPUT_FILES folder
full_metrics = pd.read_csv("OUTPUT_FILES/metrics.csv", index_col="Unnamed: 0")
recession_metrics = pd.read_csv("OUTPUT_FILES/metrics_recession.csv", index_col="Unnamed: 0")
bullish_metrics = pd.read_csv("OUTPUT_FILES/metrics_bullish.csv", index_col="Unnamed: 0")

print(full_metrics)


# WORK HERE