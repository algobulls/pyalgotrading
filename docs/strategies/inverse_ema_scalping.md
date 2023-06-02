# Inverse EMA Scalping Regular Order Strategy 
This is a trading strategy called "Inverse EMA Scalping Regular Order Strategy" implemented in Python using the PyAlgoTrading library. The strategy is based on the exponential moving average crossover.

Click [here](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/inverse_ema_scalping.py) to check the strategy code.

## What is Inverse EMA 
Inverse EMA, also known as Reverse Exponential Moving Average (REMA), is a variation of the Exponential Moving Average (EMA) in the stock market. While the EMA gives more weight to recent price data, the Inverse EMA assigns more weight to older data points.

Here's a summary of Inverse EMA:

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

 - `LARGER_TIME_PERIOD`: Period (number of candles) by which large period EMA is calculated
 - `SMALLER_TIME_PERIOD`:  Period (number of candles) by which short period EMA is calculated

## Crossover Calculation

The `get_crossover_value` method calculates the crossover value based on the inverse crossover of the two EMAs of the closing prices. It uses the `talib.EMA` function from the Talib library to calculate the EMAs. The method then determines the inverse crossover between the two EMAs and returns the corresponding value (-1, 0, or 1).
