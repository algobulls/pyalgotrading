
# OBV Breakout

This is a trading strategy called "OBV Breakout Strategy" implemented in Python using the PyAlgoTrading library. The strategy relies on On-Balance Volume (OBV) breakouts coinciding with price breakouts to signal potential trades in equities.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/obv_breakout/_strategy.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

!!! Tips "Jupyter Notebooks for US Exchange (NASDAQ)"
    - **[Click here to view a working notebook for NASDAQ exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/master/jupyter/nasdaq_equity/obv_breakout_us.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NASDAQ exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/master?urlpath=lab%2Ftree%2Fjupyter%2Fnasdaq_equity%2Fobv_breakout_us.ipynb){target=_blank}**

## What is OBV
On-Balance Volume (OBV) is a volume-based technical indicator that accumulates or depletes volume depending on whether prices close higher or lower. It can move ahead of price, offering early signals of momentum shifts. A rising OBV usually indicates increased buying pressure, while a falling OBV often signals selling pressure.

## Strategy Overview
This strategy checks whether the smoothed OBV (e.g., 10-period moving average) and price both exceed or drop below their respective lookback highs or lows. A bullish setup occurs when OBV moves above its highest level of the last N bars and the closing price simultaneously breaks above its own recent high. A bearish setup occurs when both OBV and price break below their respective lows. These combined breakouts aim to confirm momentum before entering a trade.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                    | Default Value | Expected Value  | Description                                                                                |
|:------------------------|:------------:|:---------------:|:-------------------------------------------------------------------------------------------|
| **OBV_MA_PERIOD**       |      10      | > 0             | Period used to smooth the raw OBV (e.g., 10 bars).                                         |
| **LOOKBACK_PERIOD**     |      10      | > 0             | Number of past bars for OBV and price breakout checks.                                     |
| **TRAILING_STOP_PERIOD**|      10      | > 0             | Lookback window for trailing stops (lowest low for longs, highest high for shorts).        |
| **ATR_PERIOD**          |      14      | > 0             | Period for Average True Range (ATR) calculation used in volatility-based trailing stops.   |
| **ATR_MULTIPLIER**      |      1.5       | > 0             | Multiplier for ATR-based stop, e.g., entry ± (m × ATR).                                    |

## Breakout Calculation
The code computes raw OBV and a smoothed OBV (using `talib.SMA`). A bullish breakout requires `OBV_SMA` to exceed its lookback maximum and the closing price to exceed its own N-bar high; a bearish breakout requires both OBV and price to break below their recent lows. The exit logic considers OBV dips/rises relative to its SMA or trailing stops using both lookback lows/highs and ATR-based thresholds.
