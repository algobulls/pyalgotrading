# Prompt Library for Gen AI

## Here are some prompts for Creating Strategy using GenAI

### Moving Averages (EMA or SMA)

```
Create a trading strategy which takes a BUY trade when EMA cuts SMA upwards and a SELL trade when EMA cuts SMA downwards. While placing a trade, if a previous position is open, it should be exited before placing the new trade
```
```
Create a strategy which uses 2 EMAs of different time periods, and it BUYs when EMA of timeperiod 1 crosses the EMA of timeperiod 2 upwards and SELLs when EMA of timeperiod 1 crosses the EMA of timeperiod 2 downwards.
```
```
Develop a strategy that generates a BUY signal when a shorter-term moving average crosses above an intermediate-term moving average, which then crosses above a longer-term moving average. Conversely, generate a SELL signal when the moving averages crossover in the opposite direction.
```

### Relative Strength Index (RSI)
```
Create a strategy that uses RSI indicator to give signals based on over bought or over sold conditions. If RSI is above 70, the strategy should generate a SELL signal and if it's below 30, it should generate a BUY signal
```
```
Create a strategy using RSI of MACD-signal of close with fast MA period as X, slow MA period as Y and signal period as Z, which will SELL on crossing the upper band and BUY on crossing the lower band
```
```
Create a trading strategy using RSI technical indicator
```
```
Create a strategy using RSI of MACD-signal of close with fast MA period as X, slow MA period as Y and signal period as Z, which will SELL on crossing the upper band and BUY on crossing the lower band
```
```
Please help me with a strategy that uses RSI indicator to give signals based on over bought or over sold conditions. If RSI is above 70, the strategy should generate a SELL signal and if it's below 30, it should generate a BUY signal
```
```
Create a trading strategy which takes BUY when RSI crosses lower band and create a SELL when RSI crosses the upward band, set a stop loss of 2% and target to be 15%.
```

### Aroon
```
Create a trading strategy that utilizes the Aroon indicator to generate signals based on overbought or oversold conditions. If the Aroon Up line crosses below the Aroon Down line and falls below 30, the strategy should generate a BUY signal. Conversely, if the Aroon Up line crosses above the Aroon Down line and rises above 70, the strategy should generate a SELL signal
```
### Stochastic
```
Develop a trading strategy that incorporates the stochastic crossover to generate signals. When the %K line crosses above the %D line and both lines are below 30, the strategy should generate a BUY signal. Similarly, when the %K line crosses below the %D line and both lines are above 70, the strategy should generate a SELL signal
```
```
Develop a strategy that generates a BUY signal when the Stochastic RSI indicator crosses above the oversold level (e.g., 20) and a SELL signal when it crosses below the overbought level (e.g., 80).
```
### Bollinger Bands (BB)
```
Develop a strategy that generates a BUY signal when the price breaks above the upper Bollinger Band. Similarly, generate a SELL signal when the price breaks below the lower Bollinger Band
```

### ATR (Volatility)
```
Develop a strategy that generates a BUY signal when the price surpasses a multiple of the ATR above a recent swing high, indicating increased volatility and potential upward momentum. Conversely, generate a SELL signal when the price drops below a multiple of the ATR below a recent swing low, indicating increased volatility and potential downward momentum.
```

### Moving Average Convergence Divergence (MACD)
```
Create a strategy that generates a BUY signal when the MACD histogram bars cross above the zero line and a SELL signal when the histogram bars cross below the zero line.
```

### Volume Weighted Average Price (VWAP)
```
Create a strategy that generates a BUY signal when the price rises above the VWAP line and a SELL signal when the price drops below the VWAP line, indicating potential shifts in supply and demand.
```

### Miscellaneous
```
Create a strategy that generates a BUY signal when the price crosses above the cloud (Span A and Span B) and the cloud changes color from red to green. Conversely, generate a SELL signal when the price crosses below the cloud and the cloud changes color from green to red.
```

```
Develop a strategy that generates a BUY signal when the price crosses above the Parabolic SAR dots and a SELL signal when the price crosses below the dots.
```


```
Implement a gap and go strategy that capitalizes on the momentum created by price gaps at the market open. When the price gaps up significantly and continues to move higher, generate a BUY signal. Similarly, when the price gaps down substantially and continues to move lower, generate a SELL signal.
```