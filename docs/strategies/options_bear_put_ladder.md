## Options Bear Put Ladder 

This is a template for the Options Bear Put Ladder strategy. The strategy involves the combination of buying and selling put options to profit from a downward price movement in the underlying asset. It utilizes multiple legs with different strike prices and transaction types to create a ladder-like structure.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_bear_put_ladder.py){target=_blank}**
    - **[Strategy Structure (common methods used in an options strategy)](common_options_strategy.md){target=_blank}**
    - **[Strategy Design (workflow of a strategy)](../pyalgotrad/structure.md){target=_blank}**

### Bear Put Ladder
- In the stock market, an options bear put ladder is a strategy that combines buying and selling put options with different strike prices to profit from a moderate bearish view on the underlying asset. It involves a mix of long and short put positions.

- To implement a bear put ladder strategy, an investor generally follows these steps:
    1. Buys a put option with a lower strike price.
    2. Sells two put options with higher strike prices.
    3. Buys a final put option with an even higher strike price.

- The goal of the bear put ladder is to generate a limited profit if the price of the underlying asset remains below the middle strike price at expiration. The strategy benefits from time decay and a moderate decline in the price of the underlying asset.

- The maximum profit potential is reached when the price of the underlying asset is below the middle strike price at expiration. If the price continues to decrease, the profit potential remains limited. However, if the price rises above the higher strike price, the strategy can result in losses.

- The bear put ladder strategy combines short put options to generate premium income and long put options to provide protection against significant losses in case the price of the underlying asset declines substantially.

- Traders implementing the bear put ladder strategy should consider factors such as the strike prices, premium costs, and expiration date to assess the risk-reward profile. It's crucial to have a comprehensive understanding of options trading and associated risks before employing this strategy in the stock market.

- Keep in mind that options trading can be complex and involves substantial risks. It is advisable to consult with a qualified financial advisor or broker before engaging in options trading activities.

### Parameters


| Name                                | Default Value | Expected Value     | Description                                                        |
|:------------------------------------|:-------------:|:-------------------|:-------------------------------------------------------------------|
| **LEG_ONE_TRANSACTION_TYPE**        |       1       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **LEG_ONE_TRADING_SYMBOL_SUFFIX**   |       2       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **LEG_ONE_STRIKE_DIRECTION**        |       1       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_ONE_NUMBER_OF_STRIKES**       |       0       | greater than 0     | Number of strikes for leg one.                                     |
| **LEG_TWO_TRANSACTION_TYPE**        |       1       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **LEG_TWO_TRADING_SYMBOL_SUFFIX**   |       2       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **LEG_TWO_STRIKE_DIRECTION**        |       2       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_TWO_NUMBER_OF_STRIKES**       |       2       | greater than 0     | Number of strikes for leg one.                                     |
| **LEG_THREE_TRANSACTION_TYPE**      |       2       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **LEG_THREE_TRADING_SYMBOL_SUFFIX** |       2       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **LEG_THREE_STRIKE_DIRECTION**      |       0       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_THREE_NUMBER_OF_STRIKES**     |       2       | greater than 0     | Number of strikes for leg one.                                     |




