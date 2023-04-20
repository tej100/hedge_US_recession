from asset_portfolio import AssetPortfolio
from objects import rf

oil = AssetPortfolio("OIL")
gold = AssetPortfolio("GOLD")
print(oil.port_vol, gold.port_vol)
print(oil.port_mean, gold.port_mean)
print(oil.correlation, gold.correlation)
print(oil, "\n", gold)
oil.test_returns()
gold.test_returns()
oil.test_volatility(gold)
