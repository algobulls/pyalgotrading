# EMA Regular Order Strategy v2

This strategy, called EMA Regular Order Strategy v2, implements a crossover strategy using Exponential Moving Averages (EMA). It generates entry and exit signals based on the crossover of two EMAs.

## Initialization

The `__init__` method initializes the EMA Regular Order Strategy v2. It retrieves the strategy parameters, including the time periods for the two EMAs. The method performs parameter validation to ensure the time periods are positive integers. The `main_order_map` variable is initialized to `None`.

## Initialization of Variables

The `initialize` method is called at the start of every day to initialize or re-initialize the strategy variables. In this code, it sets the `main_order_map` to an empty dictionary.

## Crossover Calculation

The `get_crossover_value` method calculates the crossover value based on the two EMAs of the closing prices. It uses the `talib.EMA` function from the Talib library to calculate the EMAs. The method then determines the crossover between the two EMAs and returns the corresponding value (-1, 0, or 1).

## Entry Selection

The `strategy_select_instruments_for_entry` method is called every candle time to select instruments for entry. It loops through the instruments provided and uses the `get_crossover_value` method to determine if an instrument meets the entry criteria. If an instrument qualifies, it is added to the `selected_instruments` list along with accompanying meta information indicating the action (BUY or SELL).

## Entry Execution

The `strategy_enter_position` method is called for each instrument selected for entry. It places a buy or sell order for the instrument based on the entry action determined by the crossover. The method returns the order object.

## Exit Selection

The `strategy_select_instruments_for_exit` method is called every candle time to select instruments for exit. It loops through the instruments and checks if the main order for each instrument exists. If a main order is present, it uses the `get_crossover_value` method to determine if an exit order should be placed. If an exit signal is present, the instrument is added to the `selected_instruments` list along with meta information indicating the action (EXIT).

## Exit Execution

The `strategy_exit_position` method is called for each instrument selected for exit. It exits the main order for the instrument and sets the `main_order_map` to `None`. If the exit action is valid (EXIT), the method returns `True` to indicate that the instrument has exited completely. Otherwise, it returns `False`.
