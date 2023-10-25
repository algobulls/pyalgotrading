# Volatility Trends with Average True Range (ATR)
This is a trading strategy called "Volatility Trends ATR" implemented in Python using the PyAlgoTrading library. The strategy is based on the ATR indicator crossover.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/volatility_trend_atr.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

!!! Tips "Jupyter Notebook for Indian Exchange (NSE)"
    - **[Click here to view a working notebook for NSE exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/master/jupyter/nse_equity/volatility_trend_atr.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NSE exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/fe289cc5d5df69e7b87b930cce110326645cd99d?urlpath=lab%2Ftree%2Fjupyter%2Fnse_equity%2Fvolatility_trend_atr.ipynb){target=_blank}**

# Volatility Trends with Average True Range (ATR) Indicator
In the ever-changing realm of stock trading, market volatility can be both an opportunity and a challenge. Traders and investors require a reliable instrument to gauge price fluctuations and devise informed strategies. The Average True Range (ATR) steps in as a robust technical indicator to fulfill this role. ATR delivers valuable insights into market volatility trends, equipping traders with the necessary tools to make calculated decisions in the stock market.

Here is a summary of ATR in the stock market:
- The Average True Range (ATR), is a technical gauge designed to quantify a security's trading range over a specific time frame. Rather than simply tracking daily price changes, ATR calculates the "true range," accounting for gaps between trading sessions.

- ATR serves as a reliable volatility indicator. It quantifies the market's propensity for price movement. Elevated ATR values indicate significant price fluctuations, while lower values suggest relative price stability.

- ATR is adaptable to individual trading preferences. Traders can tailor the ATR period to match their specific trading style. For daily charts, a typical choice is the 14-day period, but adjustments can be made for shorter or longer timeframes, allowing for versatile application.

- ATR provides a numerical value, and its magnitude corresponds to the extent of market volatility. Larger ATR values signal more significant trading opportunities, much like a roller coaster promising an exhilarating ride.

- However, ATR isn't solely focused on turbulence. It effectively identifies periods of low volatility or consolidation in the market, signaling a need for caution or a potential shift in trading strategies.


## Strategy Overview
The Average True Range (ATR) steps in as a robust technical indicator to fulfill this role. ATR delivers valuable insights into market volatility trends, equipping traders with the necessary tools to make calculated decisions in the stock market.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                   |  Default Value  | Expected Value   | Description                                                                    |
|:-----------------------|:---------------:|:-----------------|:-------------------------------------------------------------------------------|
| **TIME_PERIOD**        |      None       | greater than 0   | Period (number of candles) by which ATR is calculated             |
| **ATR_PREV_CANDLES_NUM** |      None       | greater than 0  | nth Previous candle ATR  |

## Decision Calculation
The `get_trend_direction` method calculates the ATR values for the volatility trend atr indicator using historical data of the instrument. It uses the `talib.AROON` function from the Talib library to calculate the values. It compares the ATR values with the atr of previous specified candle and determine the entry and exit actions. The method returns the ATR values for current candle.
 