# MACD Crossover 
This is a trading strategy called "MACD Crossovers" implemented in Python using the PyAlgoTrading library. The strategy is based on the MACD indicator crossover.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/macd_crossover.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

!!! Tips "Jupyter Notebook for Indian Exchange (NSE)"
    - **[Click here to view a working notebook for NSE exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/master/jupyter/nse_equity/macd_crossover.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NSE exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/fe289cc5d5df69e7b87b930cce110326645cd99d?urlpath=lab%2Ftree%2Fjupyter%2Fnse_equity%2Fmacd_crossover.ipynb){target=_blank}**

# MACD Crossover 

In the dynamic world of stock trading, mastering effective strategies is the key to success. The Moving Average Convergence Divergence (MACD) Crossover strategy is a powerful tool that can help traders identify potential entry and exit points in the stock market.

Here is a summary of RSI and MACD in the stock market:
- The MACD is a trend-following momentum indicator that consists of two lines: the MACD line and the Signal line. 
- A bullish signal is generated when the MACD line crosses above the Signal line, indicating a potential uptrend. 
- Conversely, a bearish signal occurs when the MACD line crosses below the Signal line, suggesting a potential downtrend.
- When the MACD crosses above the Signal line, it's a signal to consider a long (BUY) position. 
- Conversely, when the MACD crosses below the Signal line, it may be time to think about a short (SELL) position.

## Strategy Overview
The MACD Crossover strategy is a robust approach that leverages the power of the MACD indicator to identify potential entry and exit points in the stock market.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                   |  Default Value  | Expected Value   | Description                                                                    |
|:-----------------------|:---------------:|:-----------------|:-------------------------------------------------------------------------------|
| **TIMEPERIOD_FAST**        |      None       | greater than 0   | Period (number of candles) by which EMA 2 is calculated             |
| **TIMEPERIOD_SLOW** |      None       | greater than 0  | Period (number of candles) by which EMA 2 is calculated  |
| **TIMEPERIOD_SIGNAL** |      None       | greater than 0  | Period (number of candles) by which  moving average is calculated  |

## Crossover Calculation

The `get_crossover_value` method calculates the crossover value based on the inverse crossover of the two EMAs of the closing prices. It uses the `talib.MACD` function from the Talib library to calculate the MACDs. The method then determines the crossover between the two MACDs and returns the corresponding value (-1, 0, or 1).