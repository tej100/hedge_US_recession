# This file stores the AssetPortfolio object which is used to create a portfolio between the market and a specific asset.

import pandas as pd


class AssetPortfolio:
    
    def __init__(self, asset) -> None:
        """
        params: asset (str) - The name of the asset to be used in the portfolio (as denoted in CLEAN_DATA folder)
        """
        self.market = pd.read_csv("CLEAN_DATA/SP500.csv", index_col="Date", parse_dates=True)
        try:
            self.asset = pd.read_csv("CLEAN_DATA/" + asset + ".csv", index_col="Date", parse_dates=True)
        except FileNotFoundError:
            raise Exception("Invalid asset name")

        self.asset_returns = None
        self.market_returns = None
        self.asset_volatility = None
        self.market_volatility = None
        self.asset_sharpe_ratio = None
        self.market_sharpe_ratio = None
        self.asset_beta = None
        self.market_beta = None
        self.asset_alpha = None
        self.market_alpha = None
        self.asset_r_squared = None
        self.market_r_squared = None
        self.asset_t_value = None
        self.market_t_value = None
        self.asset_p_value = None
        self.market_p_value = None
        self.asset_covariance = None
        self.market_covariance = None
        self.asset_correlation = None
        self.market_correlation = None
        self.asset_mean = None
        self.market_mean = None
        self.asset_median = None
        self.market_median = None
        self.asset_max = None
        self.market_max = None
        self.asset_min = None
        self.market_min = None
        self.asset_std = None
        self.market_std = None
        self.asset_skew = None
        self.market_skew = None
        self.asset_kurtosis = None
        self.market_kurtosis = None
        self.asset_mad = None
        self.market_mad = None
        self.asset_sem = None
        self.market_sem = None
        self.asset_var = None
        self.market_var = None
        self.asset_quantile = None
        self.market_quantile = None
        self.asset_cumulative_returns = None
        self.market_cumulative_returns = None
        self.asset_cumulative_volatility = None
        self.market_cumulative_volatility = None
        self.asset_cumulative_sharpe_ratio = None
        self.market_cumulative_sharpe_ratio = None
        self.asset_cumulative_beta = None
        self.market_cumulative_beta = None
        self.asset_cumulative_alpha = None
        self.market_cumulative_alpha = None
        self.asset_cumulative_r_squared = None
        self.market_cumulative_r_squared = None
        self.asset_cumulative_t_value = None
        self.market_cumulative_t_value = None
        self.asset_cumulative_p_value = None
        self.market_cumulative_p_value = None