"""

"""
import pandas as pd


def HeikinAshi(japanese_data: pd.DataFrame, ohlc: tuple = ('timestamp', 'open', 'high', 'low', 'close')):
    """
    Computes HeikinAshi Candlesticks Pattern data from Japanese candlesticks pattern data.

    Args:
        japanese_data: Pandas DataFrame holding Japanese Candlesticks Pattern Data
        ohlc: Column names corresponding to 'timestamp', 'open', 'high', 'low' and 'close' data respectively

    Returns:
        HeikinAshi Candlesticks Pattern data

    """
    if not len(ohlc) >= 5:
        print("Argument 'ohlc' should be a tuple of 5 values corresponding to the column names in 'japanese_data' pandas DataFrame, for 'timestamp', 'open', 'high', 'low' and 'close' data respectively.")

    ha_open = 'ha_' + ohlc[1]
    ha_high = 'ha_' + ohlc[2]
    ha_low = 'ha_' + ohlc[3]
    ha_close = 'ha_' + ohlc[4]

    japanese_data = japanese_data.copy()  # make sure we don't modify the original DataFrame
    japanese_data[ha_close] = (japanese_data[ohlc[1]] + japanese_data[ohlc[2]] + japanese_data[ohlc[3]] + japanese_data[ohlc[4]]) / 4

    japanese_data[ha_open] = 0.0
    for i in range(0, len(japanese_data)):
        if i == 0:
            japanese_data[ha_open].iat[i] = (japanese_data[ohlc[1]].iat[i] + japanese_data[ohlc[4]].iat[i]) / 2
        else:
            japanese_data[ha_open].iat[i] = (japanese_data[ha_open].iat[i - 1] + japanese_data[ha_close].iat[i - 1]) / 2

    japanese_data[ha_high] = japanese_data[[ha_open, ha_close, ohlc[2]]].max(axis=1)
    japanese_data[ha_low] = japanese_data[[ha_open, ha_close, ohlc[3]]].min(axis=1)

    # Create separate DataFrame with the required columns only
    heikinashi_data = pd.DataFrame()
    heikinashi_data['timestamp'] = japanese_data['timestamp']
    heikinashi_data['open'] = japanese_data[ha_open]
    heikinashi_data['high'] = japanese_data[ha_high]
    heikinashi_data['low'] = japanese_data[ha_low]
    heikinashi_data['close'] = japanese_data[ha_close]

    return heikinashi_data
