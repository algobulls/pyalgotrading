# Reverse RSI v2

This is a trading strategy called "Reverse RSI v2" implemented in Python using the PyAlgoTrading library. The strategy is based on the relative strength index indicator.

## Strategy Overview
The Reverse RSI v2 strategy is a trading strategy based on the Relative Strength Index (RSI) indicator. It generates entry and exit signals based on the reverse crossover of the RSI values from specified overbought and oversold levels.

## Strategy Parameters
The following parameters can be configured for the strategy:

 - `TIME_PERIOD`: Period (number of candles) by which RSI is calculated
 - `OVERBOUGHT_VALUE`: RSI value above which stocks are considered over-bought
 - `OVERSOLD_VALUE`:  RSI value below which stocks are considered over-sold

## Initialization

The `__init__` method initializes the Reverse RSI v2 strategy. It retrieves the strategy parameters, including the time period for RSI calculation, overbought value, and oversold value. The method performs parameter validation to ensure the values are positive integers. The `main_order_map` variable is initialized to `None`.

## Initialization of Variables

The `initialize` method is called at the start of every day to initialize or re-initialize the strategy variables. In this code, it sets the `main_order_map` to an empty dictionary.

## Decision Calculation

The `get_crossover_value` method calculates the crossover values for the RSI indicator using historical data of the instrument. It compares the RSI values with the overbought and oversold levels to determine the entry and exit actions. The method returns the crossover values for oversold and overbought levels.

## Entry Selection

The `strategy_select_instruments_for_entry` method is called every candle time to select instruments for entry. It loops through the instruments provided and checks if the main order for each instrument is None. If a main order doesn't exist, it calls the `get_crossover_value` method to determine if an entry order should be placed based on the oversold and overbought crossover values. If an entry signal is present, the instrument is added to the `selected_instruments` list along with accompanying meta information indicating the action (BUY or SELL).

## Entry Execution

The `strategy_enter_position` method is called for each instrument selected for entry. It places a buy or sell order for the instrument based on the entry action determined by the oversold and overbought crossover values. The method returns the order object.

## Exit Selection

The `strategy_select_instruments_for_exit` method is called every candle time to select instruments for exit. It loops through the instruments and checks if the main order for each instrument exists. If a main order is present, it calls the `get_crossover_value` method to determine if an exit order should be placed based on the oversold and overbought crossover values. If an exit signal is present, the instrument is added to the `instruments` list along with meta information indicating the action (EXIT).

## Exit Execution

The `strategy_exit_position` method is called for each instrument selected for exit. It exits the main order for the instrument and sets the `main_order_map` to `None`. If the exit action is valid (EXIT), the method returns `True` to indicate that the instrument has exited completely. Otherwise, it returns `False`.

