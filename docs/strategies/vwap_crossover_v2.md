# VWAP Crossover v2

This is a trading strategy called "VWAP Crossover v2" implemented in Python using the PyAlgoTrading library. The strategy is based on the crossover of the VWAP (Volume Weighted Average Price) indicator.

## Strategy Overview

The strategy follows a simple rule based on the crossover of the VWAP indicator. When the price crosses above the VWAP, a buy signal is generated, and when the price crosses below the VWAP, a sell signal is generated. The strategy aims to capture potential trend reversals based on the VWAP.

## Strategy Parameters

No specific strategy parameters are mentioned in the code. 

The strategy may utilize the following parameters from the base `StrategyBase` class:

- `number_of_lots`: The number of lots to be used for each trade.

## Initialization

The strategy initializes the `main_order_map` variable to keep track of the main order for each instrument.

## Entry Decision

The `strategy_select_instruments_for_entry` method is called for each candle to determine the instruments for which entry orders should be placed. It loops over the instruments in the provided bucket and checks if there are no current orders for the instrument. If no orders are present, it calculates the VWAP crossover value for the instrument. If the crossover value is -1 or 1, indicating a sell or buy signal respectively, the instrument is added to the selected instruments bucket along with additional meta information.

## Entry Order Placement

The `strategy_enter_position` method is called for each selected instrument from the entry decision process. It places a buy or sell order for the instrument based on the sideband information received. The order quantity is determined by multiplying the number of lots by the instrument's lot size.

## Exit Decision

The `strategy_select_instruments_for_exit` method is called for each candle to determine the instruments for which exit orders should be placed. It loops over the instruments in the provided bucket and checks if there is a current order for the instrument that is complete. If a complete order is found, it calculates the VWAP crossover value for the instrument. If the crossover value is opposite to the order's transaction type (buy or sell), an exit order is placed for the instrument.

## Exit Order Placement

The `strategy_exit_position` method is called for each selected instrument from the exit decision process. It exits the main order for the instrument, sets the main order to None, and returns `True` to indicate that the instrument has exited completely.

