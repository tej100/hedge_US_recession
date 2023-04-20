from asset_portfolio import AssetPortfolio

oil = AssetPortfolio("OIL")
# print(oil.market_vol, oil.asset_vol, oil.port_vol)
# print(oil.market_mean, oil.asset_mean, oil.portfolio_mean)
# print(oil.correlation)
# print(oil)
print("here",oil.CAPM())