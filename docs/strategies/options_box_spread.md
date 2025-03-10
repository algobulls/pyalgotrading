
## Options Box Spread

This is a template for implementing the Options Box Spread strategy in Python.

!!! Links
    - **[Strategy Code (.py)](https://github.com/your-username/pyalgostrategypool/blob/master/pyalgostrategypool/options_box_spread/_strategy.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

[//]: # (Optional placeholder for any Jupyter notebook references)

### Introduction

The Box Spread strategy is a market-neutral arbitrage approach combining a bull call spread and a bear put spread on the same underlying asset, with matching expiration dates but differing strike prices. The strategy locks in a fixed payoff, \( B - A \), by selecting a lower strike (A) and a higher strike (B), ensuring a consistent return regardless of the underlying asset's price movement. 

To construct a box spread:
1. **Bull Call Spread**
    - Buy a call option at strike A (lower strike).
    - Sell a call option at strike B (higher strike).
2. **Bear Put Spread**
    - Buy a put option at strike B (higher strike).
    - Sell a put option at strike A (lower strike).

### Strategy Parameters

| Name                                | Default Value | Expected Value | Description                                                                                                       |
|:------------------------------------|:------------:|:--------------:|:------------------------------------------------------------------------------------------------------------------|
| **LEG_ONE_TRANSACTION_TYPE**        |      1       | 1 or 2         | Transaction type for leg one (call buy or sell). [**BUY**: 1, **SELL**: 2]                                        |
| **LEG_ONE_TRADING_SYMBOL_SUFFIX**   |      1       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg one.                                                               |
| **LEG_ONE_STRIKE_DIRECTION**        |      0       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg one.                                                          |
| **LEG_ONE_NUMBER_OF_STRIKES**       |      0       | >= 0            | Number of strikes offset for leg one.                                                                             |
| **LEG_TWO_TRANSACTION_TYPE**        |      2       | 1 or 2         | Transaction type for leg two (call buy or sell). [**BUY**: 1, **SELL**: 2]                                        |
| **LEG_TWO_TRADING_SYMBOL_SUFFIX**   |      1       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg two.                                                               |
| **LEG_TWO_STRIKE_DIRECTION**        |      2       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg two.                                                          |
| **LEG_TWO_NUMBER_OF_STRIKES**       |      2       | >= 0            | Number of strikes offset for leg two.                                                                             |
| **LEG_THREE_TRANSACTION_TYPE**      |      1       | 1 or 2         | Transaction type for leg three (put buy or sell). [**BUY**: 1, **SELL**: 2]                                       |
| **LEG_THREE_TRADING_SYMBOL_SUFFIX** |      2       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg three.                                                             |
| **LEG_THREE_STRIKE_DIRECTION**      |      0       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg three.                                                        |
| **LEG_THREE_NUMBER_OF_STRIKES**     |      2       | >= 0            | Number of strikes offset for leg three.                                                                           |
| **LEG_FOUR_TRANSACTION_TYPE**       |      2       | 1 or 2         | Transaction type for leg four (put buy or sell). [**BUY**: 1, **SELL**: 2]                                        |
| **LEG_FOUR_TRADING_SYMBOL_SUFFIX**  |      2       | 1 or 2         | Trading symbol suffix ([CE: 1, PE: 2]) for leg four.                                                              |
| **LEG_FOUR_STRIKE_DIRECTION**       |      2       | 0, 1, or 2     | Strike direction ([ITM: 0, ATM: 1, OTM: 2]) for leg four.                                                         |
| **LEG_FOUR_NUMBER_OF_STRIKES**      |      0       | >= 0            | Number of strikes offset for leg four.                                                                            |