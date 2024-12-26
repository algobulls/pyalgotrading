
# OBV Breakout

This is a trading strategy called "OBV Breakout Strategy" implemented in Python using the PyAlgoTrading library. The strategy relies on On-Balance Volume (OBV) crossovers with its smoothed average to signal potential trades in equities.

!!! Links
    - **[Strategy Code (.py)](https://github.com/algobulls/pyalgostrategypool/blob/master/pyalgostrategypool/obv_breakout/_strategy.py){target=_blank}**
    - **[Strategy Structure (common methods used in a regular and options strategy)](strategy_guides/common_strategy_guide.md){target=_blank}**

!!! Tips "Jupyter Notebooks for US Exchange (NASDAQ)"
    - **[Click here to view a working notebook for NASDAQ exchange in cloud. No installation required. ](https://nbviewer.org/github/algobulls/pyalgotrading/blob/master/jupyter/nasdaq_equity/obv_breakout_us.ipynb){target=_blank}**
    - **[Click here to execute a working notebook for NASDAQ exchange in cloud. No installation required. ](https://mybinder.org/v2/gh/algobulls/pyalgotrading/master?urlpath=lab%2Ftree%2Fjupyter%2Fnasdaq_equity%2Fobv_breakout_us.ipynb){target=_blank}**

## What is OBV
On-Balance Volume (OBV) is a volume-based technical indicator that accumulates or depletes volume depending on whether prices close higher or lower. It can move ahead of price, offering early signals of momentum shifts. A rising OBV usually indicates increased buying pressure, while a falling OBV often signals selling pressure.

## Strategy Overview
This strategy checks for breakouts in the OBV relative to its smoothed average. A bullish breakout occurs when the raw OBV crosses above its smoothed OBV (SMA) over the last `TIME_PERIOD` bars, indicating a potential increase in buying pressure. A bearish breakout occurs when the raw OBV crosses below its smoothed OBV, signaling a potential increase in selling pressure. These breakouts help confirm momentum and signal potential entry for trades.

## Strategy Parameters
The following parameters can be configured for the strategy:

| Name                    | Default Value | Expected Value  | Description                                                                                |
|:------------------------|:------------:|:---------------:|:-------------------------------------------------------------------------------------------|
| **TIME_PERIOD**          |      10      | > 0             | Period used to smooth the raw OBV (e.g., 10 bars).                                         |

## Breakout Calculation
The code computes raw OBV and a smoothed OBV (using `talib.SMA`). A bullish breakout occurs when the raw OBV crosses above its smoothed OBV (SMA), and a bearish breakout occurs when the raw OBV crosses below its smoothed OBV (SMA).