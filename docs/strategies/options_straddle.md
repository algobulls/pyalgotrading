## Options Straddle 

This class represents the implementation of a options straddle trading strategy.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_straddle.py){target=_blank}**
    - **[Strategy Structure (common methods used in an options strategy)](common_options_strategy.md){target=_blank}**
    - **[Strategy Design (workflow of a strategy)](../pyalgotrad/structure.md){target=_blank}**

### Straddle Options
- In the stock market, an options straddle is a strategy where an investor simultaneously purchases a call option and a put option with the same strike price and expiration date on a particular underlying asset, such as a stock. The purpose of this strategy is to profit from significant price movements in the underlying asset, regardless of whether the price goes up or down.

- By using an options straddle, the investor is essentially betting on volatility rather than the direction of the price movement. If the price of the underlying asset experiences a substantial increase or decrease, either the call or put option will generate profits, offsetting any losses from the other option. The potential for profit is highest when there is a significant price swing, while the risk is limited to the cost of purchasing the options.

- This strategy is often employed when traders anticipate an upcoming event or announcement that could cause significant market volatility, such as earnings reports or regulatory decisions. The goal is to take advantage of the resulting price movement, regardless of whether it is upward or downward.

- It's important to note that options straddles can be risky as they require significant price movements to be profitable. If the price remains relatively stable, the trader may experience losses due to the cost of purchasing the options. Therefore, careful consideration of market conditions and risk management is crucial when implementing an options straddle strategy.

#### Parameters


| Name                                | Default Value | Expected Value     | Description                                                        |
|:------------------------------------|:-------------:|:-------------------|:-------------------------------------------------------------------|
| **_leg_one_transaction_type**       |       2       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **_leg_one_tradingsymbol_suffix**   |       1       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **_leg_one_strike_direction**       |       1       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **_leg_one_number_of_strikes**      |       0       | greater than 0     | Number of strikes for leg one.                                     |
| **_leg_two_transaction_type**       |       2       | 1 or 2             | Transaction type for leg one. [BUY: 1, SELL: 2]                    |
| **_leg_two_tradingsymbol_suffix**   |       2       | 1 or 2             | Trading symbol suffix for leg one. [CE: 1,  PE: 2]                 |
| **_leg_two_strike_direction**       |       1       | 0, 1 or 2          | Strike direction for leg one. [ITM: 0, ATM: 1,  OTM: 2]            |
| **_leg_two_number_of_strikes**      |       0       | greater than 0     | Number of strikes for leg one.                                     |

