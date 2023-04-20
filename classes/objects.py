import yfinance as yf

rf = yf.download("^FVX", period="1w")["Adj Close"][-1]  # 5-yr T-bill rate