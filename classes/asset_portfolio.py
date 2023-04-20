# This file stores the AssetPortfolio object which is used to create a portfolio between the market and a specific asset.

import pandas as pd
import numpy as np
from scipy.stats import norm, t
from objects import rf

class AssetPortfolio:

    asset_weight = 0.5
    market_weight = 1-asset_weight
    
    def __init__(self, asset : str) -> None:
        """
        params: asset (str) - The name of the asset to be used in the portfolio (as denoted in CLEAN_DATA folder)
        """
        self.market_name = "SP500"
        self.asset_name = asset

        self.market = pd.read_csv("CLEAN_DATA/SP500.csv", index_col="Date", parse_dates=True)
        try:
            self.asset = pd.read_csv("CLEAN_DATA/" + asset + ".csv", index_col="Date", parse_dates=True)
        except FileNotFoundError:
            raise Exception("Invalid asset name")
        
        
        # Share time index for both assets
        self.__align_index()

        # Create portfolio object
        self.portfolio = self.create_portfolio()

        # Get log returns of asset and market
        self.__log_returns()

        # Get metrics of assets and portfolio
        self.correlation = self.__correlation()
        self.market_mean, self.asset_mean, self.portfolio_mean = self.__mean_returns()
        self.market_vol, self.asset_vol, self.port_vol = self.__volatility()
        self.sharpe_ratio = (self.portfolio_mean - rf) / self.port_vol

        # Get CAPM of asset vs market
        self.alpha, self.beta = self.CAPM()
        
        # Hypothesis Testing of mean returns of portfolio with respect to risk-free rate?

        # Get Sharpe Ratio of portfolio (rolling?)

        # Maybe even F-test of volatilities of different portfolios?

        # self.asset_returns = self.asset["Log Returns"]
        # self.market_returns = self.market["Log Returns"]



    ###########
    # METHODS #
    ###########

    def __repr__(self) -> str:
        return f"AssetPortfolio({self.asset_name})"
    
    def __correlation(self) -> float:
        return self.asset["Log Returns"].corr(self.market["Log Returns"])
    
    def __volatility(self) -> tuple:
        asset_vol = self.asset["Log Returns"].std() * np.sqrt(252)
        market_vol = self.market["Log Returns"].std() * np.sqrt(252)
        self.weights = np.array([self.asset_weight, self.market_weight])
        log_returns = pd.concat([self.market["Log Returns"], self.asset["Log Returns"]], axis = 1)
        portfolio_vol = np.sqrt(np.dot(self.weights.T, np.dot(log_returns.cov()*252, self.weights)))
        return (market_vol, asset_vol, portfolio_vol)
    
    def __mean_returns(self) -> tuple:
        asset_mean = self.asset["Log Returns"].mean()
        market_mean = self.market["Log Returns"].mean()
        port_mean = self.asset_weight*asset_mean + self.market_weight * market_mean
        return (market_mean, asset_mean, port_mean)
    
    def __log_returns(self):
        self.market['Log Returns'] = np.log1p(self.market['Returns'])
        self.asset['Log Returns'] = np.log1p(self.asset['Returns'])

    def __align_index(self):
        """
        Aligns the index of the asset and market dataframes to be the same.
        """
        idx = self.market.join(self.asset, how="inner", lsuffix=".M", rsuffix=".A", on="Date").index
        self.market = self.market.loc[idx]
        self.asset = self.asset.loc[idx]

    def create_portfolio(self):
        df = pd.concat([self.market["Adj Close"], self.asset["Adj Close"]], axis=1)
        df.columns = ["Market", "Asset"]
        df["Portfolio"] = df["Market"]*self.market_weight + df["Asset"]*self.asset_weight
        return df
    
    def CAPM(self) -> tuple:
        """
        Calculates the CAPM of the asset vs the market.
        """
        var = np.var(self.market["Log Returns"])
        cov = self.market["Log Returns"].cov(self.asset["Log Returns"])
        beta = cov / var
        alpha = self.asset_mean - rf - beta * (self.market_mean - rf)
        return (alpha, beta)
    
    def test_returns(self, alpha_level : float = 0.05) -> bool:
        """
        Hypothesis Test to see if the mean returns of the portfolio are significantly greater from the risk-free rate.
        """
        mean = self.portfolio_mean
        std = self.port_vol
        t_stat = (mean - rf) / (std / np.sqrt(len(self.portfolio)))
        p_value = 1 - t.cdf(t_stat, len(self.portfolio)-1)
        
        return True if p_value < alpha_level else False


    def test_volatility(self, other_vol : float):
        """
        Hypothesis Test to see if the volatility of the portfolio is significantly different from the market.
        """
        f_stat = (self.port_vol**2) / (other_vol**2)
        p_value = 1 - norm.cdf(f_stat)

        
    def optimize_weights(self):
        """
        Optimizes the weights of the portfolio to maximize the Sharpe Ratio.
        """
        pass
            


if __name__ == "__main__":
    # Testing purposes
    port = AssetPortfolio("OIL")