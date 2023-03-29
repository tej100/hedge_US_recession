import pandas as pd
import numpy as np
import yfinance as yf

alts = yf.download(["SHY", "IEF", "TLT", "BTC-USD", "ETH-USD", "BZ=F", "GC=F", "VNQ"], start="2000-01-01",  end="2023-01-01", group_by="tickers")  # iShares 1-3 | iShares 7-10 | iShares 20+ yrs
alts = alts.rename(columns={"SHY":"T3","IEF":"T10","TLT":"T20", "BTC-USD":"BTC", "ETH-USD":"ETH", "BZ=F":"OIL", "GC=F":"GOLD", "VNQ":"REST"})