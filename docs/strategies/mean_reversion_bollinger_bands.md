# Mean Reversion Bollinger Bands
This is a trading strategy called "Mean Reversion Bollinger Bands" implemented in Python using the PyAlgoTrading library. The strategy is based on the bollingerbands indicator.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/mean_reversion_bollinger_bands/_strategy.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**
    
!!! Tips "Jupyter Notebook for Indian Exchange (NSE)"
    - **[Click here to view a working notebook for NSE exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/master/jupyter/nse_equity/mean_reversion_bollinger_bands.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NSE exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/fe289cc5d5df69e7b87b930cce110326645cd99d?urlpath=lab%2Ftree%2Fjupyter%2Fnse_equity%2Fmean_reversion_bollinger_bands.ipynb){target=_blank}**
    
## Mean Reversion Bollinger Bands
In the dynamic world of stock trading, effective strategies can make all the difference. The Mean Reversion Bollinger Bands strategy is a powerful tool that traders can use to identify potential entry and exit points in the stock market.

Here is a summary of RSI and MACD in the stock market:
- Bollinger Bands are a volatility indicator that consists of a middle band (usually a simple moving average), an upper band, and a lower band. These bands expand and contract based on price volatility. The strategy leverages these bands to identify potential mean reversion opportunities.
- Mean reversion is the idea that prices tend to revert to their historical average over time. In this strategy, traders look for situations where the price deviates significantly from the middle Bollinger Band and expect it to revert to the mean.
- The Mean Reversion Bollinger Bands strategy involves identifying price movements that touch or cross the upper or lower bands and anticipating a reversal. 
- When the price touches the upper band, traders may consider a short (SELL) position, expecting a downward move.
- Conversely, when the price touches the lower band, it may signal a potential long (BUY) opportunity, anticipating an upward move.

## Strategy Overview
The Mean Reversion Bollinger Bands strategy is a robust approach that leverages the power of Bollinger Bands to identify potential mean reversion opportunities in the stock market.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                   |  Default Value  | Expected Value   | Description                                                                    |
|:-----------------------|:---------------:|:-----------------|:-------------------------------------------------------------------------------|
| **TIME_PERIOD**        |      None       | greater than 0   | Period (number of candles) by which Bollinger Bands are calculated             |
| **STANDARD_DEVIATION** |      None       | between 0 to 10  | Standard deviation (in percent) for upper and lower band from the signal bands |

## Decision Calculation

The `get_decision` method calculates the Bollinger Bands values for a given instrument based on the OHLC (Open, High, Low, Close) historical data. It uses the `talib.BBANDS` function from the Talib library to calculate the upper and lower bands. The method compares the previous candle's open, low, and close values with the upper and lower bands to determine the entry or exit action. If the conditions for a buy or sell signal are met, the corresponding action is returned.