# Aroon Crossover v2

This strategy, called Aroon Crossover v2, implements a crossover strategy using the Aroon indicator. It generates entry and exit signals based on the crossover of Aroon Up and Aroon Down values.

## Strategy Overview
add here

## Strategy Parameters
add here

## Initialization

The `__init__` method initializes the Aroon Crossover v2 strategy. It retrieves the strategy parameters, including the time period for the Aroon indicator. The method also performs parameter validation to ensure the time period is a positive integer. The `main_order_map` variable is initialized to `None`.

## Initialization of Variables

The `initialize` method is called at the start of every day to initialize or re-initialize the strategy variables. In this code, it sets the `main_order_map` to an empty dictionary.

## Crossover Calculation

The `get_crossover_value` method calculates the Aroon Up and Aroon Down values for a given instrument based on the historical data. It uses the `talib.AROON` function from the Talib library to calculate the values. The method then determines the crossover of Aroon Up and Aroon Down and returns the corresponding entry or exit action.

## Entry Selection

The `strategy_select_instruments_for_entry` method is called every candle time to select instruments for entry. It loops through the instruments provided and uses the `get_crossover_value` method to determine if an instrument meets the entry criteria. If an instrument qualifies, it is added to the `selected_instruments` list along with accompanying meta information.

## Entry Execution

The `strategy_enter_position` method is called for each instrument selected for entry. It places a buy or sell order for the instrument based on the entry action determined by the crossover. The method returns the order object.

## Exit Selection

The `strategy_select_instruments_for_exit` method is called every candle time to select instruments for exit. It loops through the instruments and checks if the main order for each instrument is complete. If a complete main order is found, it uses the `get_crossover_value` method to determine if an exit order should be placed. If an exit signal is present, the instrument is added to the `selected_instruments` list along with meta information.

## Exit Execution

The `strategy_exit_position` method is called for each instrument selected for exit. It exits the main order for the instrument and sets the `main_order_map` to `None`. If the exit action is valid (EXIT_BUY or EXIT_SELL), the method returns `True` to indicate that the instrument has exited completely. Otherwise, it returns `False`.

