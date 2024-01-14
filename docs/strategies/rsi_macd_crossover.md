# RSI MACD Crossover
This is a trading strategy called "RSI MACD Crossovers" implemented in Python using the PyAlgoTrading library. The strategy is based on the RSI and MACD indicator crossover.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/rsi_macd_crossover/_strategy.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

!!! Tips "Jupyter Notebook for Indian Exchange (NSE)"
    - **[Click here to view a working notebook for NSE exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/master/jupyter/nse_equity/rsi_macd_crossover.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NSE exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/fe289cc5d5df69e7b87b930cce110326645cd99d?urlpath=lab%2Ftree%2Fjupyter%2Fnse_equity%2Frsi_macd_crossover.ipynb){target=_blank}**

# RSI and MACD Crossover
In the dynamic world of stock trading, effective strategies are the key to success. The combination of two powerful technical indicators, the Moving Average Convergence Divergence (MACD) and the Relative Strength Index (RSI), can be a game-changer for traders. This strategy leverages MACD and RSI crossovers to identify potential entry and exit points in the stock market.

Here is a summary of RSI and MACD in the stock market:
- The MACD is a trend-following momentum indicator. It consists of two lines: the MACD line and the Signal line. When the MACD line crosses above the Signal line, it generates a bullish signal, suggesting a potential uptrend. Conversely, a cross below the Signal line indicates a bearish signal, signaling a potential downtrend.

- The RSI is an oscillator that measures the speed and change of price movements. RSI values above 70 typically indicate an overbought condition, signaling a potential price reversal to the downside. RSI values below 30 suggest an oversold condition, indicating a potential price reversal to the upside.

- The essence of this strategy lies in the crossover of the MACD and RSI indicators. When the MACD generates a bullish crossover and the RSI confirms by being below 70 (not in an overbought condition), it could be an opportune time to consider a long (BUY) position. 

- Conversely, when the MACD produces a bearish crossover and the RSI is above 30 (not in an oversold condition), it may be a suitable moment to contemplate a short (SELL) position.

## Strategy Overview
The MACD and RSI crossover strategy is a robust approach that combines the strength of two widely used technical indicators. By identifying potential entry and exit points based on these crossovers, traders can make more informed decisions in the stock market.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                   |  Default Value  | Expected Value   | Description                                                                    |
|:-----------------------|:---------------:|:-----------------|:-------------------------------------------------------------------------------|
| **TIMEPERIOD_FAST**        |      None       | greater than 0   | Period (number of candles) by which EMA 2 is calculated             |
| **TIMEPERIOD_SLOW** |      None       | greater than 0  | Period (number of candles) by which EMA 2 is calculated  |
| **TIMEPERIOD_SIGNAL** |      None       | greater than 0  | Period (number of candles) by which  moving average is calculated  |
| **TIMEPERIOD_RSI** |      None       | greater than 0  | Period (number of candles) by which RSI is calculated   |
| **OVERSOLD_VALUE** |      None       | greater than 0  | Threshould value indicating potential buying opportunites  |
| **OVERBOUGHT_VALUE** |      None       | greater than 0  | Threshould value indicating potential selling opportunites  |

## Crossover Calculation

The `get_crossover_value` method calculates the crossover value based on the inverse crossover of the two EMAs of the closing prices. It uses the `talib.MACD` and `talib.RSI` function from the Talib library to calculate the MACD and RSI. The method then determines the crossover between the MACD and RSI and returns the corresponding value (-1, 0, or 1).