import yfinance as yf
import os
import pandas as pd

# Risk-free rate
rf = yf.download("^FVX", period="1w", progress=False)["Adj Close"][-1] / 100  # 5-yr T-bill rate

recession_periods = [
    pd.date_range(start='1953-07-01', end='1954-05-01'),
    pd.date_range(start='1957-08-01', end='1958-04-01'),
    pd.date_range(start='1960-04-01', end='1961-02-01'),
    pd.date_range(start='1969-12-01', end='1970-11-01'),
    pd.date_range(start='1973-11-01', end='1975-03-01'),
    pd.date_range(start='1980-01-01', end='1980-07-01'),
    pd.date_range(start='1981-07-01', end='1982-11-01'),
    pd.date_range(start='1990-07-01', end='1991-03-01'),
    pd.date_range(start='2001-03-01', end='2001-11-01'),
    pd.date_range(start='2007-12-01', end='2009-06-01'),
    pd.date_range(start='2020-02-01', end='2020-08-07')
]

bullish_periods = [
    pd.date_range(start = '1949-06-01', end = '1953-07-01'),
    pd.date_range(start = '1954-05-01', end = '1956-08-01'),
    pd.date_range(start = '1958-04-01', end = '1960-04-01'),
    pd.date_range(start = '1962-06-01', end = '1966-02-01'),
    pd.date_range(start = '1966-10-01', end = '1968-11-01'),
    pd.date_range(start = '1970-05-01', end = '1973-01-01'),
    pd.date_range(start = '1975-03-01', end = '1980-01-01'),
    pd.date_range(start = '1982-11-01', end = '1987-08-01'),
    pd.date_range(start = '1987-12-01', end = '1990-07-01'),
    pd.date_range(start = '1991-03-01', end = '2000-03-01'),
    pd.date_range(start = '2002-10-01', end = '2007-10-01'),
    pd.date_range(start = '2009-06-01', end = '2020-02-01'),
    pd.date_range(start = '2020-08-07', end = '2021-12-31')
]

# Function to import all files in a directory
def import_data(directory : str, ignore_files : list = []) -> dict:
    """
    Imports all data files from a directory.
    Returns a dictionary with the file name as the key and the dataframe as the value.
    """
    data_dict = {}
    # Get all files in directory (make sure your relative root is the project repository)
    for filename in os.scandir(directory):
        if filename.is_file() and filename.name not in ignore_files:
            df = pd.read_csv(directory + "/" + filename.name, index_col="Date", parse_dates=True)
            name = filename.name.split(".")[0]
            data_dict[name] = df
    return data_dict

# Stevens Colors
color_palette = {
    "stevens red" : "#A32638",
    "stevens grey" : "#7F7F7F",
    "dark grey" : "#363D45",
    "dark blue" : "#004380",
    "medium blue" : "#4896CF",
    "light blue" : "#E7F2FB",
    "light grey" : "#E4E5E6",
    "medium orange" : "#E7842E",
    "light orange" : "#FFF2E8",
    "medium gold" : "#EBC73B",
    "light gold" : "#FFFAE6",
    "black" : "#000000"
}