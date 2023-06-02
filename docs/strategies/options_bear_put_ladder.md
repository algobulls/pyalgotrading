## Options Bear Put Ladder Template 

This is a template for the Options Bear Put Ladder strategy. The strategy involves the combination of buying and selling put options to profit from a downward price movement in the underlying asset. It utilizes multiple legs with different strike prices and transaction types to create a ladder-like structure.

Click [here](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/options_bear_put_ladder.py) to check the strategy code.


### Bear Put Ladder
In the stock market, an options bull put ladder is a strategy that involves buying and selling put options with different strike prices to profit from a moderate bullish outlook on the underlying asset. It is a complex strategy that combines both long and short put positions.

To create a bull put ladder, an investor typically does the following:

1. Sells a higher strike put option.
2. Buys two lower strike put options.
3. Sells a final even lower strike put option.

The key feature of the bull put ladder is that it provides limited risk and potential for limited profit. The strategy is constructed in such a way that it can benefit from both a moderate rise in the price of the underlying asset and from time decay.

The profit potential of the bull put ladder is highest if the price of the underlying asset rises to the level of the middle strike price at expiration. In this case, the investor can achieve the maximum profit. If the price of the underlying asset rises above the middle strike price, the profit potential is limited.

On the other hand, if the price of the underlying asset remains above the higher strike price or increases, the strategy can result in losses. The maximum loss occurs if the price rises above the higher strike price.

The bull put ladder is a moderately bullish strategy that aims to benefit from both time decay and the potential for a moderate increase in the price of the underlying asset. Traders implementing this strategy should carefully consider factors such as the strike prices, premium costs, and expiration date to assess their risk-reward profile.

It's important to note that options trading involves risks, and traders should have a thorough understanding of the strategy and associated risks before employing it in the stock market.


### Parameters

- `LEG_ONE_TRANSACTION_TYPE` (int, default: 1): Transaction type for leg one. BUY: 1 | SELL: 2.
- `LEG_ONE_TRADING_SYMBOL_SUFFIX` (int, default: 1): Trading symbol suffix for leg one. CE: 1 | PE: 2.
- `LEG_ONE_STRIKE_DIRECTION` (int, default: 1): Strike direction for leg one. ITM: 0 | ATM: 1 | OTM: 2.
- `LEG_ONE_NUMBER_OF_STRIKES` (int, default: 0): Number of strikes for leg one.

- `LEG_TWO_TRANSACTION_TYPE` (int, default: 1): Transaction type for leg two. BUY: 1 | SELL: 2.
- `LEG_TWO_TRADING_SYMBOL_SUFFIX` (int, default: 1): Trading symbol suffix for leg two. CE: 1 | PE: 2.
- `LEG_TWO_STRIKE_DIRECTION` (int, default: 2): Strike direction for leg two. ITM: 0 | ATM: 1 | OTM: 2.
- `LEG_TWO_NUMBER_OF_STRIKES` (int, default: 2): Number of strikes for leg two.

- `LEG_THREE_TRANSACTION_TYPE` (int, default: 2): Transaction type for leg three. BUY: 1 | SELL: 2.
- `LEG_THREE_TRADING_SYMBOL_SUFFIX` (int, default: 1): Trading symbol suffix for leg three. CE: 1 | PE: 2.
- `LEG_THREE_STRIKE_DIRECTION` (int, default: 0): Strike direction for leg three. ITM: 0 | ATM: 1 | OTM: 2.
- `LEG_THREE_NUMBER_OF_STRIKES` (int, default: 2): Number of strikes for leg three.



