"""

"""
import pandas as pd


def Linebreak(japanese_candles):
    """

    Args:
        japanese_candles:

    Returns:

    """
    linebreak_candles = [{'close': candle['close'], 'open': candle['open'], 'timestamp': candle['timestamp']} for _, candle in japanese_candles.iloc[:3].iterrows()]

    for _, candle in japanese_candles.iloc[3:].iterrows():
        all_greater = all(candle['close'] > _ for _ in [max(_linebreakcandle['open'], _linebreakcandle['close']) for _linebreakcandle in linebreak_candles[-3:]])
        all_lesser = all(candle['close'] < _ for _ in [min(_linebreakcandle['open'], _linebreakcandle['close']) for _linebreakcandle in linebreak_candles[-3:]])

        prev_linebreak_candle = linebreak_candles[-1]
        if all_greater:
            new_linebreak_candle = {'open': max(prev_linebreak_candle['open'], prev_linebreak_candle['close']),
                                    'close': candle['close'],
                                    'timestamp': candle['timestamp']}
            linebreak_candles.append(new_linebreak_candle)
        elif all_lesser:
            new_linebreak_candle = {'open': min(prev_linebreak_candle['open'], prev_linebreak_candle['close']),
                                    'close': candle['close'],
                                    'timestamp': candle['timestamp']}
            linebreak_candles.append(new_linebreak_candle)

    return pd.DataFrame(linebreak_candles)
