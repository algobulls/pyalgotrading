"""
Module for calculating crossover
"""
from typing import Union, Tuple, List

import pandas as pd


def crossover(val1_hist: Union[Tuple, List, pd.Series], val2_hist: Union[Tuple, List, pd.Series], accuracy_decimals: int = 2) -> int:
    """
    Computes crossover of 2 data series - val1_hist and val2_hist.

    Args:
        val1_hist: Any object which can be converted to a list of data points. (Ex: pandas.Series, tuple, list)
        val2_hist: Any object which can be converted to a list of data points. (Ex: pandas.Series, tuple, list)
        accuracy_decimals: Positive integer, specifying number of decimal places to be looked into until we consider two numbers as equal.
                           Ex: with accuracy_decimals=2, 3.456 and 3.457 are considered equal, but 3.456 and 3.466 are considered unequal.

    Returns:
        - `1` if `val1_hist(OHLC)` cuts `val2_hist` upwards
        - `-1` if `val1_hist` cuts `val2_hist` downwards
        - `0` if there is no cut between `val1_hist` and `val2_hist`

    """
    # This is a dummy function with a sole purpose of mimicing the signature of the actual function on the AlgoBulls platform, as described in the documentation.
    pass
