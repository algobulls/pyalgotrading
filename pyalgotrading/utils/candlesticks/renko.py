"""

"""
import math

import pandas as pd


def Renko(japanese_candles, brick_count=2, initial_open=None, initial_close=None):
    """

    Args:
        japanese_candles:
        brick_count:
        initial_open:
        initial_close:

    Returns:

    """
    if not initial_close:
        initial_open = japanese_candles.iloc[0]['open']
        initial_close = japanese_candles.iloc[0]['close']
    else:
        initial_open = japanese_candles.iloc[0]['open'] + (brick_count - ((japanese_candles.iloc[0]['open'] - initial_open) % brick_count))
        initial_close = japanese_candles.iloc[0]['close'] + (brick_count - ((japanese_candles.iloc[0]['close'] - initial_close) % brick_count))

    renko_candles = [{'timestamp': japanese_candles.iloc[0]['timestamp'], 'open': initial_open, 'close': initial_close}]
    prev_renko_candle = renko_candles[-1]

    for _, candle in japanese_candles.iloc[1:].iterrows():
        max_open_close = max(prev_renko_candle['open'], prev_renko_candle['close'])
        min_open_close = min(prev_renko_candle['open'], prev_renko_candle['close'])

        if candle['close'] > max_open_close:
            number_of_renko_candles = math.floor((candle['close'] - max_open_close) / brick_count)
            for i in range(number_of_renko_candles):
                renko_candles.append({'timestamp': candle['timestamp'], 'open': max_open_close, 'close': max_open_close + brick_count})
                prev_renko_candle = renko_candles[-1]
                max_open_close = max(prev_renko_candle['open'], prev_renko_candle['close'])

        elif candle['close'] < min_open_close:
            number_of_renko_candles = math.floor((min_open_close - candle['close']) / brick_count)
            for i in range(number_of_renko_candles):
                renko_candles.append({'timestamp': candle['timestamp'], 'open': min_open_close, 'close': min_open_close - brick_count})
                prev_renko_candle = renko_candles[-1]
                min_open_close = min(prev_renko_candle['open'], prev_renko_candle['close'])

    return pd.DataFrame(renko_candles)
