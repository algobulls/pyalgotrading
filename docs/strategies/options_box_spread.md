
## Options Box Spread

This is a template for implementing the Options Box Spread strategy in Python.

!!! Links
    - **[Strategy Code (.py)](https://github.com/your-username/pyalgostrategypool/blob/master/pyalgostrategypool/options_box_spread/_strategy.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

[//]: # (Optional placeholder for any Jupyter notebook references)

### Box Spread
- In the stock market, an options box spread is a market-neutral arbitrage strategy that combines a bull call spread and a bear put spread on the same underlying asset with the same expiration date. The aim is to lock in a nearly risk-free payoff equivalent to the difference between the two strike prices (discounted by the risk-free rate), irrespective of the underlying asset’s movement.

- To create a box spread, an investor typically does the following:
    1. Buy a call option at strike A (near-the-money or ITM).
    2. Sell a call option at strike B, where B > A (slightly OTM).
    3. Buy a put option at strike B (matching the call’s OTM strike).
    4. Sell a put option at strike A (the same lower strike as the first call).

- This four-leg structure forms a long box if the net cost is below the theoretical value. Conversely, if the net cost is above that theoretical value, one can initiate a short box by reversing the position. Real-world factors like transaction costs, bid-ask spreads, and liquidity must be considered for true arbitrage opportunities.

### Strategy Parameters

| Name                                | Default Value | Expected Value | Description                                                                                                       |
|:------------------------------------|:------------:|:--------------:|:------------------------------------------------------------------------------------------------------------------|
| **LEG_ONE_TRANSACTION_TYPE**        |      1       | 1 or 2         | Transaction type for leg one (call buy or sell). [**BUY**: 1, **SELL**: 2]                                        |
| **LEG_ONE_TRADING_SYMBOL_SUFFIX**   |      1       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg one.                                                               |
| **LEG_ONE_STRIKE_DIRECTION**        |      0       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg one.                                                          |
| **LEG_ONE_NUMBER_OF_STRIKES**       |      0       | > 0            | Number of strikes offset for leg one.                                                                             |
| **LEG_TWO_TRANSACTION_TYPE**        |      2       | 1 or 2         | Transaction type for leg two (call buy or sell). [**BUY**: 1, **SELL**: 2]                                        |
| **LEG_TWO_TRADING_SYMBOL_SUFFIX**   |      1       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg two.                                                               |
| **LEG_TWO_STRIKE_DIRECTION**        |      2       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg two.                                                          |
| **LEG_TWO_NUMBER_OF_STRIKES**       |      2       | > 0            | Number of strikes offset for leg two.                                                                             |
| **LEG_THREE_TRANSACTION_TYPE**      |      1       | 1 or 2         | Transaction type for leg three (put buy or sell). [**BUY**: 1, **SELL**: 2]                                       |
| **LEG_THREE_TRADING_SYMBOL_SUFFIX** |      2       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg three.                                                             |
| **LEG_THREE_STRIKE_DIRECTION**      |      2       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg three.                                                        |
| **LEG_THREE_NUMBER_OF_STRIKES**     |      2       | > 0            | Number of strikes offset for leg three.                                                                           |
| **LEG_FOUR_TRANSACTION_TYPE**       |      2       | 1 or 2         | Transaction type for leg four (put buy or sell). [**BUY**: 1, **SELL**: 2]                                        |
| **LEG_FOUR_TRADING_SYMBOL_SUFFIX**  |      2       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg four.                                                              |
| **LEG_FOUR_STRIKE_DIRECTION**       |      0       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg four.                                                         |
| **LEG_FOUR_NUMBER_OF_STRIKES**      |      0       | > 0            | Number of strikes offset for leg four.                                                                            |
| **RISK_FREE_RATE**                  |   0.01       | > 0            | Annualized risk-free rate used to discount \((B-A)\).                                                             |
| **EXIT_THRESHOLD**                  |   0.01       | >= 0           | Tolerance for exiting early if the box cost converges to the theoretical value.                                   |
| **TRANSACTION_COST_PERCENT**        |   0.0        | >= 0           | Percentage transaction cost accounting for slippage, commissions, or fees.                                       |
