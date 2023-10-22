# Inverse EMA Scalping 
This is a trading strategy called "Inverse EMA Scalping Regular Order Strategy" implemented in Python using the PyAlgoTrading library. The strategy is based on the exponential moving average crossover.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/inverse_ema_scalping.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**


!!! Tips "Jupyter Notebooks for Indian Exchange (NSE)"
    - **[Click here to view a working notebook for NSE exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/2f3fb6fb83fd09981e286fe2f0930249a848cc8e/jupyter/nse_jupyter_notebooks/Inverse%20EMA%20Scalping%20Crossover.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NSE exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/16b3e3f168057e89ab959770c4a9dec7507b6a04?urlpath=lab%2Ftree%2Fjupyter%2Fnse_equity%2Finverse_ema_scalping_crossover.ipynb){target=_blank}**

!!! Tips "Jupyter Notebooks for US Exchange (NASDAQ)"
    - **[Click here to view a working notebook for NASDAQ exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/526dabc0a92775f4184aaab543c0a9f424613a55/jupyter/nasdaq_jupyter_notebooks/Inverse%20EMA%20Scalping%20Crossover%20US.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NASDAQ exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/16b3e3f168057e89ab959770c4a9dec7507b6a04?urlpath=lab%2Ftree%2Fjupyter%2Fnasdaq_equity%2Finverse_ema_scalping_crossover_us.ipynb){target=_blank}**


## What is Inverse EMA 
Inverse EMA, also known as Reverse Exponential Moving Average (REMA), is a variation of the Exponential Moving Average (EMA) in the stock market. While the EMA gives more weight to recent price data, the Inverse EMA assigns more weight to older data points.

Here is a summary of Inverse EMA:

- Inverse EMA is calculated by applying the EMA formula in reverse, giving greater weight to older data points and less weight to recent prices.
- Instead of smoothing out price fluctuations like the EMA, the Inverse EMA amplifies them, making it more responsive to historical data.
- The formula for calculating Inverse EMA is similar to the EMA, but it uses a different smoothing factor or multiplier that assigns higher weight to older data points.
- The Inverse EMA is primarily used to identify historical patterns and potential turning points in the market.
- When the price crosses above the Inverse EMA, it may suggest a potential reversal from a downtrend to an uptrend, and vice versa when the price crosses below the Inverse EMA.
- Inverse EMA is not as widely used as the EMA or other moving averages, and its applications may vary among traders and analysts.
- Inverse EMA is a less commonly used variation of the Exponential Moving Average. While the EMA is designed to provide a smoothed average of recent prices, the Inverse EMA emphasizes historical data, potentially highlighting significant turning points in the market. Traders and analysts who utilize the Inverse EMA may incorporate it into their technical analysis toolkit to complement other indicators and gain insights into price reversals and historical patterns.


## Strategy Overview
This strategy implements a scalping strategy using Exponential Moving Averages (EMA). It generates entry and exit signals based on the inverse crossover of two EMAs.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                    |  Default Value  | Expected Value                                                    | Description                                                        |
|:------------------------|:---------------:|:------------------------------------------------------------------|:-------------------------------------------------------------------|
| **LARGER_TIME_PERIOD**  |      None       | greater than 0                                                    | Period (number of candles) by which large period EMA is calculated |
| **SMALLER_TIME_PERIOD** |      None       | greater than 0                                                    | Period (number of candles) by which short period EMA is calculated |


## Crossover Calculation

The `get_crossover_value` method calculates the crossover value based on the inverse crossover of the two EMAs of the closing prices. It uses the `talib.EMA` function from the Talib library to calculate the EMAs. The method then determines the inverse crossover between the two EMAs and returns the corresponding value (-1, 0, or 1).
