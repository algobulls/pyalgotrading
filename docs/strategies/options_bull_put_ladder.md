## Options Bull Put Ladder  

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_bull_put_ladder.py){target=_blank}**
    - **[Strategy Structure (common methods used in an options strategy)](common_options_strategy.md){target=_blank}**
    - **[Strategy Design (workflow of a strategy)](../pyalgotrad/structure.md){target=_blank}**

### Bull Put ladder
- In the stock market, an options bull put ladder is a strategy that involves buying and selling put options with different strike prices to profit from a moderate bullish outlook on the underlying asset. It is a complex strategy that combines both long and short put positions.

- To create a bull put ladder, an investor typically does the following:

    1. Sells a higher strike put option.
    2. Buys two lower strike put options.
    3. Sells a final even lower strike put option.

- The key feature of the bull put ladder is that it provides limited risk and potential for limited profit. The strategy is constructed in such a way that it can benefit from both a moderate rise in the price of the underlying asset and from time decay.

- The profit potential of the bull put ladder is highest if the price of the underlying asset rises to the level of the middle strike price at expiration. In this case, the investor can achieve the maximum profit. If the price of the underlying asset rises above the middle strike price, the profit potential is limited.

- On the other hand, if the price of the underlying asset remains above the higher strike price or increases, the strategy can result in losses. The maximum loss occurs if the price rises above the higher strike price.

- The bull put ladder is a moderately bullish strategy that aims to benefit from both time decay and the potential for a moderate increase in the price of the underlying asset. Traders implementing this strategy should carefully consider factors such as the strike prices, premium costs, and expiration date to assess their risk-reward profile.

- It is important to note that options trading involves risks, and traders should have a thorough understanding of the strategy and associated risks before employing it in the stock market.


### Initialization

The `__init__` method initializes the strategy and accepts parameters for configuring the strategy. The parameters are:


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
| **LEG_THREE_STRIKE_DIRECTION**      |       2       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **LEG_THREE_NUMBER_OF_STRIKES**     |       4       | greater than 0     | Number of strikes for leg one.                                     |


### Additional Notes

- The `transaction_type_map`, `tradingsymbol_suffix_map`, and `strike_direction_map` dictionaries are used for mapping transaction types, trading symbol suffixes, and strike directions, respectively.

- The strategy supports a single allowed expiry date, which can be modified for multiple expiry dates.

- The strategy uses the `get_options_instrument_with_strike_direction` method from the base class to fetch child instruments.

- The `initialize` method sets up the list of instruments processed for the day.

- The `options_instruments_set_up_local` method sets up the Call and Put Options instruments for a given base instrument.

- The `strategy_select_instruments_for_entry` method selects instruments for entry by setting up child instruments and appending them to the selected instruments list.

- The `strategy_enter_position` method
