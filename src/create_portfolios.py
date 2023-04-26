# The purpose of this file is to create portfolios based on the cleaned data and output the portfolios (for auto running purposes)

import pandas as pd

from classes.asset_portfolio import AssetPortfolio
from classes.objects import import_data

if __name__ == "__main__":
    # From CLEAN_DATA folder, import all data
    data_dict = import_data("CLEAN_DATA", ignore_files=["README.md"])

    # Replace all values in data_dict with AssetPortfolio objects
    for k, v in data_dict.items(): data_dict[k] = AssetPortfolio(k)

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
    df.to_csv("OUTPUT_FILES/metrics.csv")

