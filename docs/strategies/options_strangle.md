## Options Strangle 

The `StrategyOptionsStrangle` class is a strategy template for trading options strangles. It is derived from the `StrategyOptionsBaseV2` class.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_strangle.py){target=_blank}**
    - **[Strategy Structure (common methods used in an options strategy)](strategy_guides/common_options_strategy.md){target=_blank}**
    - **[Strategy Design (workflow of a strategy)](strategy_guides/structure.md){target=_blank}**
    - **[Running this strategy for NSE exchange in Jupyter Notebook using pyalgotrading (.ipynb)](https://nbviewer.org/github/algobulls/pyalgotrading/blob/d77ba21f66764971362b51c1a39367a1f78c308d/jupyter/nse_options_jupyter_notebooks/options_strangle.ipynb){target=_blank}**
    - **[Executing the Jupyter Notebook for Options](https://mybinder.org/v2/gh/algobulls/pyalgotrading/0a1c06d6e159b3bebf2348efd198608b662c3ffc?urlpath=lab%2Ftree%2Fjupyter%2Fnse_options%2Foptions_strangle.ipynb){target=_blank}**

### Strangle Options
- In the stock market, an options strangle is a strategy where an investor simultaneously buys or sells a call option and a put option on the same underlying asset but with different strike prices and the same expiration date. The purpose of this strategy is to profit from significant price volatility in the underlying asset.

- Unlike an options straddle, which involves purchasing options at the same strike price, an options strangle involves selecting different strike prices. Typically, the investor buys an out-of-the-money call option (with a strike price above the current market price) and an out-of-the-money put option (with a strike price below the current market price).

- The strategy aims to benefit from a significant price movement in either direction. If the price of the underlying asset moves significantly upwards, the call option can generate profits. Conversely, if the price moves significantly downwards, the put option can generate profits. The investor is essentially betting on increased price volatility rather than predicting the direction of the price movement.

- Options strangles are commonly used when traders anticipate a substantial price movement but are unsure about the direction. This strategy allows for potential profits in either an upward or downward market scenario. However, it is important to note that options strangles can involve higher risks, as the underlying asset's price must move significantly to offset the cost of purchasing both options.

- Traders employing options strangles should carefully consider factors such as the expected price volatility, the expiration date, and the costs associated with purchasing the options. Implementing risk management techniques and monitoring market conditions are essential when utilizing an options strangle strategy.


### Parameters

The following parameters can be set in the Parameters Configuration Pane:

| Name                                | Default Value | Expected Value     | Description                                                        |
|:------------------------------------|:-------------:|:-------------------|:-------------------------------------------------------------------|
| **_leg_one_transaction_type**       |       2       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **_leg_one_tradingsymbol_suffix**   |       1       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **_leg_one_strike_direction**       |       2       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **_leg_one_number_of_strikes**      |       2       | greater than 0     | Number of strikes for leg one.                                     |
| **_leg_two_transaction_type**       |       2       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **_leg_two_tradingsymbol_suffix**   |       2       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **_leg_two_strike_direction**       |       2       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **_leg_two_number_of_strikes**      |       2       | greater than 0     | Number of strikes for leg one.                                     |



