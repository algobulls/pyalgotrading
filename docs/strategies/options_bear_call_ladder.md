## Options Bear Call Ladder

This class implements the Options Bear Call Ladder strategy.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_bear_call_ladder.py){target=_blank}**
    - **[Strategy Structure (common methods used in an options strategy)](common_options_strategy.md){target=_blank}**
    - **[Strategy Design (workflow of a strategy)](../pyalgotrad/structure.md){target=_blank}**

### Bear Call Ladder
- In the stock market, an options bear call ladder is a strategy that involves buying and selling call options with different strike prices to profit from a moderate bearish outlook on the underlying asset. It is a complex strategy that combines both long and short call positions.

- To create a bear call ladder, an investor typically does the following:
    1. Sells a lower strike call option.
    2. Buys two higher strike call options.
    3. Sells a final even higher strike call option.

- The bear call ladder aims to generate a limited profit if the price of the underlying asset remains below the middle strike price at expiration. The strategy benefits from time decay and a moderate decrease in the price of the underlying asset.

- The maximum profit potential of the bear call ladder is achieved when the price of the underlying asset is below the middle strike price at expiration. If the price declines further, the profit potential remains limited. However, if the price rises above the higher strike price, the strategy can result in losses.

- The key feature of the bear call ladder is the combination of short call options, which generate premium income, and long call options, which provide protection against unlimited losses in case the price of the underlying asset rises sharply.

- Traders implementing the bear call ladder strategy should carefully consider factors such as the strike prices, premium costs, and expiration date to assess their risk-reward profile. It's important to note that options trading involves risks, and traders should have a thorough understanding of the strategy and associated risks before employing it in the stock market.

- Please be aware that options trading can be complex and involves significant risks. It is always recommended to consult with a qualified financial advisor or broker before engaging in options trading activities.



### Parameters

| Name                                | Default Value  | Expected Value     | Description                                                        |
|:------------------------------------|:--------------:|:-------------------|:-------------------------------------------------------------------|
| **LEG_ONE_TRANSACTION_TYPE**        |       1        | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **LEG_ONE_TRADING_SYMBOL_SUFFIX**   |       1        | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **LEG_ONE_STRIKE_DIRECTION**        |       1        | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_ONE_NUMBER_OF_STRIKES**       |       0        | greater than 0     | Number of strikes for leg one.                                     |
| **LEG_TWO_TRANSACTION_TYPE**        |       1        | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **LEG_TWO_TRADING_SYMBOL_SUFFIX**   |       1        | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **LEG_TWO_STRIKE_DIRECTION**        |       2        | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_TWO_NUMBER_OF_STRIKES**       |       2        | greater than 0     | Number of strikes for leg one.                                     |
| **LEG_THREE_TRANSACTION_TYPE**      |       2        | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **LEG_THREE_TRADING_SYMBOL_SUFFIX** |       1        | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **LEG_THREE_STRIKE_DIRECTION**      |       0        | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_THREE_NUMBER_OF_STRIKES**     |       2        | greater than 0     | Number of strikes for leg one.                                     |



