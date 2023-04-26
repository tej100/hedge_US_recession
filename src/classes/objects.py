import yfinance as yf
import os
import pandas as pd

# Risk-free rate
rf = yf.download("^FVX", period="1w", progress=False)["Adj Close"][-1]  # 5-yr T-bill rate

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