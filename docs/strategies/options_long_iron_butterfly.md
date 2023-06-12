## Options Long Iron Butterfly Template

This is a template for implementing the Options Long Iron Butterfly strategy in Python.

Click [here](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_long_iron_butterfly.py) to check the strategy code.

### Long Iron Butterfly
- In the stock market, an options long iron butterfly is a complex strategy that involves buying two options with the same expiration date but different strike prices. It combines elements of both a bullish and bearish strategy and is designed to profit from low volatility in the underlying asset.

- To create a long iron butterfly, an investor typically does the following:

    1. Buys an at-the-money (ATM) put option.
    2. Buys an ATM call option.
    3. Sells an out-of-the-money (OTM) put option with a lower strike price.
    4. Sells an OTM call option with a higher strike price.

- The key feature of the long iron butterfly is that the sold options (OTM put and OTM call) help offset the cost of the purchased options (ATM put and ATM call). This results in a limited-risk, limited-reward strategy.

- The strategy profits when the price of the underlying asset remains within a specific range, known as the "profit zone." The profit zone is determined by the strike prices of the options involved in the strategy. If the price of the underlying asset is within this range at expiration, the investor can achieve the maximum profit.

- However, if the price of the underlying asset moves significantly beyond the profit zone, the strategy can result in losses. The maximum loss occurs if the price falls below the lower strike price or rises above the higher strike price.

- The long iron butterfly is commonly used when traders anticipate low volatility in the underlying asset. It is a neutral strategy that seeks to benefit from the passage of time and a decrease in implied volatility. Traders implementing this strategy should carefully analyze factors such as the strike prices, premium costs, and expiration date to determine their risk-reward profile.

- It's important to note that options trading involves risks, and traders should have a thorough understanding of the strategy and associated risks before employing it in the stock market.


### Strategy Parameters

The strategy accepts the following parameters:

- `LEG_ONE_TRANSACTION_TYPE`: Transaction type for leg one (BUY: 1 | SELL: 2)
- `LEG_ONE_TRADING_SYMBOL_SUFFIX`: Trading symbol suffix for leg one (CE: 1 | PE: 2)
- `LEG_ONE_STRIKE_DIRECTION`: Strike direction for leg one (ITM: 0 | ATM: 1 | OTM: 2)
- `LEG_ONE_NUMBER_OF_STRIKES`: Number of strikes for leg one

- `LEG_TWO_TRANSACTION_TYPE`: Transaction type for leg two (BUY: 1 | SELL: 2)
- `LEG_TWO_TRADING_SYMBOL_SUFFIX`: Trading symbol suffix for leg two (CE: 1 | PE: 2)
- `LEG_TWO_STRIKE_DIRECTION`: Strike direction for leg two (ITM: 0 | ATM: 1 | OTM: 2)
- `LEG_TWO_NUMBER_OF_STRIKES`: Number of strikes for leg two

- `LEG_THREE_TRANSACTION_TYPE`: Transaction type for leg three (BUY: 1 | SELL: 2)
- `LEG_THREE_TRADING_SYMBOL_SUFFIX`: Trading symbol suffix for leg three (CE: 1 | PE: 2)
- `LEG_THREE_STRIKE_DIRECTION`: Strike direction for leg three (ITM: 0 | ATM: 1 | OTM: 2)
- `LEG_THREE_NUMBER_OF_STRIKES`: Number of strikes for leg three

- `LEG_FOUR_TRANSACTION_TYPE`: Transaction type for leg four (BUY: 1 | SELL: 2)
- `LEG_FOUR_TRADING_SYMBOL_SUFFIX`: Trading symbol suffix for leg four (CE: 1 | PE: 2)
- `LEG_FOUR_STRIKE_DIRECTION`: Strike direction for leg four (ITM: 0 | ATM: 1 | OTM: 2)
- `LEG_FOUR_NUMBER_OF_STRIKES`: Number of strikes for leg four


