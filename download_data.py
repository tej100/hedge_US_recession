# This file is solely for downloading all data from Yahoo Finance and saving
# it to a csv file to automate the process of downloading data as time goes on

import pandas as pd
import yfinance as yf
from loguru import logger

#############
# Arguments #
#############

start = "2000-01-01"
end = "2023-01-01"

tickers = {
    # ticker : name
    "SHY" : "T3",
    "IEF" : "T10",
    "TLT" : "T20",
    "SPY" : "SP500",
    "QQQ" : "NASDAQ",
    "DIA" : "DOW",
    "BTC-USD" : "BTC",
    "ETH-USD" : "ETH",
    "BZ=F" : "OIL",
    "GC=F" : "GOLD",
    "VNQ" : "REST"
}

#################
# Download Data #
#################
for k, v in tickers.items():
    data = pd.DataFrame(yf.download(k, start=start, end=end, progress=False))
    logger.success(f"{v}: Data Downloaded Successfully")
    data.to_csv("RAW_DATA/" + v + ".csv", header=True, index_label="Date")
    logger.success(f"{v}: Data Saved Successfully")