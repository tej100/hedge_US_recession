# The purpose of this file is to create portfolios based on the cleaned data and output the portfolios (for auto running purposes)

import pandas as pd

from classes.asset_portfolio import AssetPortfolio
from classes.objects import import_data, rf
from loguru import logger


if __name__ == "__main__":

    ###############
    # Import Data #
    ###############

    # From CLEAN_DATA folder, import all data
    logger.info("Importing Data")
    data_dict = import_data("CLEAN_DATA", ignore_files=["README.md"])
    logger.success("Data Imported")

    ##########################
    # Full Period Portfolios #
    ##########################

    # Replace all values in data_dict with AssetPortfolio objects
    for k in data_dict.keys():
        logger.info(f"Creating Portfolio for {k}")
        data_dict[k] = AssetPortfolio(k)
        logger.success(f"Portfolio for {k} Created")

    # Make nested dictionary of all asset metrics
    metrics_dict = {}
    for k, v in data_dict.items():
        logger.info(f"Generating Metrics for Full Time Period: {k}")
        metrics_dict[k] = {
            "Correlation": v.correlation,
            "Excess Return": v.port_mean - rf,
            "Market Volatility": v.market_vol,
            "Asset Volatility": v.asset_vol,
            "Portfolio Volatility": v.port_vol,
            "Sharpe Ratio": v.sharpe_ratio,
            "Alpha": v.alpha,
            "Beta": v.beta
        }
        logger.success(f"Metrics for Full Period: {k} Generated")
    # Send to dataframe
    df = pd.DataFrame(metrics_dict).T
    df.to_csv("OUTPUT_FILES/metrics.csv")
    logger.success("Recession Metrics Outputted to metrics.csv")


    ########################
    # Recession Portfolios #
    ########################

    # Replace all values in data_dict with AssetPortfolio objects
    for k, v in data_dict.items():
        logger.info(f"Creating Portfolio for {k}")
        data_dict[k] = AssetPortfolio(k, "recession")
        logger.success(f"Portfolio for {k} Created")

    # Make nested dictionary of all asset metrics
    metrics_recession = {}
    for k, v in data_dict.items():
        logger.info(f"Generating Metrics for Recession Periods: {k}")
        metrics_recession[k] = {
            "Correlation": v.correlation,
            "Excess Return": v.port_mean - rf,
            "Market Volatility": v.market_vol,
            "Asset Volatility": v.asset_vol,
            "Portfolio Volatility": v.port_vol,
            "Sharpe Ratio": v.sharpe_ratio,
            "Alpha": v.alpha,
            "Beta": v.beta
        }
        logger.success(f"Metrics for Recession Periods: {k} Generated")
    # Send to dataframe
    df = pd.DataFrame(metrics_recession).T
    df.to_csv("OUTPUT_FILES/metrics_recession.csv")
    logger.success("Recession Metrics Outputted to metrics_recession.csv")


    ######################
    # Bullish Portfolios #
    ######################

    # Replace all values in data_dict with AssetPortfolio objects
    logger.info("Creating Portfolios for Bullish Periods")
    for k, v in data_dict.items(): data_dict[k] = AssetPortfolio(k, "bullish")

    # Make nested dictionary of all asset metrics
    metrics_bullish = {}
    for k, v in data_dict.items():
        metrics_bullish[k] = {
            "Correlation": v.correlation,
            "Excess Return": v.port_mean - rf,
            "Market Volatility": v.market_vol,
            "Asset Volatility": v.asset_vol,
            "Portfolio Volatility": v.port_vol,
            "Sharpe Ratio": v.sharpe_ratio,
            "Alpha": v.alpha,
            "Beta": v.beta
        }
    # Send to dataframe
    df = pd.DataFrame(metrics_bullish).T
    df.to_csv("OUTPUT_FILES/metrics_bullish.csv")
    logger.success("Bullish Metrics Outputted to metrics_bullish.csv")
