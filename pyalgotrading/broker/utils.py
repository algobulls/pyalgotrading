def crossover(val1_hist, val2_hist, accuracy_decimals=2):
    """
    Computes crossover of 2 data series - val1_hist and val2_hist.

    :param val1_hist: Any object which can be converted to a list of data points. (Ex: pandas.Series, tuple, list)
    :param val2_hist: Any object which can be converted to a list of data points. (Ex: pandas.Series, tuple, list)
    :param accuracy_decimals: Positive integer, specifying number of decimal places to be looked into until we consider 2 numbers as same. Ex: with accuracy_decimals=2, 3.456 and 3.457 are considered equal, but 3.456 and 3.466 are considered unequal.

    :return: 1 if val1_hist cuts val2_hist upwards, -1 if cut is downwards and 0 if there is no cut
    """
    # This is a dummy function with a sole purpose of mimicing the signature of the actual function on the AlgoBulls platform, as described in the documentation.
    pass
