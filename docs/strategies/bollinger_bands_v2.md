# Bollinger Bands v2

This strategy, called Bollinger Bands v2, is an implementation of the Bollinger Bands indicator. It uses the Bollinger Bands values to generate entry and exit signals for trading instruments.

## Initialization

The `__init__` method initializes the Bollinger Bands v2 strategy. It retrieves the strategy parameters, including the time period and standard deviations for the Bollinger Bands. The method also performs parameter validation to ensure the parameters are positive integers. The `main_order_map` variable is initialized to `None`.

## Initialization of Variables

The `initialize` method is called at the start of every day to initialize or re-initialize the strategy variables. In this code, it sets the `main_order_map` to an empty dictionary.

## Bollinger Bands Calculation

The `get_decision` method calculates the Bollinger Bands values for a given instrument based on the OHLC (Open, High, Low, Close) historical data. It uses the `talib.BBANDS` function from the Talib library to calculate the upper and lower bands. The method compares the previous candle's open, low, and close values with the upper and lower bands to determine the entry or exit action. If the conditions for a buy or sell signal are met, the corresponding action is returned.

## Entry Selection

The `strategy_select_instruments_for_entry` method is called every candle time to select instruments for entry. It loops through the instruments provided and uses the `get_decision` method to determine if an instrument meets the entry criteria. If an instrument qualifies, it is added to the `selected_instruments` list along with accompanying meta information.

## Entry Execution

The `strategy_enter_position` method is called for each instrument selected for entry. It places a buy order for the instrument and returns the order object.

## Exit Selection

The `strategy_select_instruments_for_exit` method is called every candle time to select instruments for exit. It loops through the instruments and checks if the main order for each instrument is complete. If a complete main order is found, it uses the `get_decision` method to determine if an exit order should be placed. If an exit signal is present, the instrument is added to the `selected_instruments` list along with meta information.

## Exit Execution

The `strategy_exit_position` method is called for each instrument selected for exit. It exits the main order for the instrument and sets the `main_order_map` to `None`. If the exit action is valid (EXIT), the method returns `True` to indicate that the instrument has exited completely.

