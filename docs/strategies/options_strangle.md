## Options Strangle Template

The `StrategyOptionsStrangle` class is a strategy template for trading options strangles. It is derived from the `StrategyOptionsBaseV2` class.

Click [here](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_strangle.py) to check the strategy code.

### Strangle Options
In the stock market, an options strangle is a strategy where an investor simultaneously buys or sells a call option and a put option on the same underlying asset but with different strike prices and the same expiration date. The purpose of this strategy is to profit from significant price volatility in the underlying asset.

Unlike an options straddle, which involves purchasing options at the same strike price, an options strangle involves selecting different strike prices. Typically, the investor buys an out-of-the-money call option (with a strike price above the current market price) and an out-of-the-money put option (with a strike price below the current market price).

The strategy aims to benefit from a significant price movement in either direction. If the price of the underlying asset moves significantly upwards, the call option can generate profits. Conversely, if the price moves significantly downwards, the put option can generate profits. The investor is essentially betting on increased price volatility rather than predicting the direction of the price movement.

Options strangles are commonly used when traders anticipate a substantial price movement but are unsure about the direction. This strategy allows for potential profits in either an upward or downward market scenario. However, it's important to note that options strangles can involve higher risks, as the underlying asset's price must move significantly to offset the cost of purchasing both options.

Traders employing options strangles should carefully consider factors such as the expected price volatility, the expiration date, and the costs associated with purchasing the options. Implementing risk management techniques and monitoring market conditions are essential when utilizing an options strangle strategy.

### Parameters

The following parameters can be set in the Parameters Configuration Pane:

- `LEG_ONE_TRANSACTION_TYPE`: The transaction type for the first leg (BUY: 1 | SELL: 2).
- `LEG_ONE_TRADING_SYMBOL_SUFFIX`: The trading symbol suffix for the first leg (CE: 1 | PE: 2).
- `LEG_ONE_STRIKE_DIRECTION`: The strike direction for the first leg (ITM: 0 | ATM: 1 | OTM: 2).
- `LEG_ONE_NUMBER_OF_STRIKES`: The number of strikes for the first leg.

- `LEG_TWO_TRANSACTION_TYPE`: The transaction type for the second leg (BUY: 1 | SELL: 2).
- `LEG_TWO_TRADING_SYMBOL_SUFFIX`: The trading symbol suffix for the second leg (CE: 1 | PE: 2).
- `LEG_TWO_STRIKE_DIRECTION`: The strike direction for the second leg (ITM: 0 | ATM: 1 | OTM: 2).
- `LEG_TWO_NUMBER_OF_STRIKES`: The number of strikes for the second leg.


