import pandas as pd

def VWAP(hist_data_df):

    # Disable this warning: A value is trying to be set on a copy of a slice from a DataFrame.
    pd.options.mode.chained_assignment = None  # default='warn'

    # VWAP behaves specially as compared to other indicators
    # It uses only current day's historical data
    hist_data_df['date'] = hist_data_df['timestamp'].apply(lambda x: x.date())
    unique_dates = sorted(set(hist_data_df['date']))
    vwap = []

    # Compute vwap for each day's data & append it to vwap variable
    for i, date in enumerate(unique_dates):
        day_df = hist_data_df.loc[hist_data_df['date'] == date]
        typical_price_day_df = (day_df.high + day_df.low + day_df.close) / 3
        vwap_day = list(((typical_price_day_df * day_df.volume).cumsum()) / day_df.volume.cumsum())
        vwap += vwap_day

    vwap = pd.Series(vwap) 

    return vwap
