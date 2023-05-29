# Stochastic Crossover v2

This is a trading strategy called "Stochastic Crossover v2" implemented in Python using the PyAlgoTrading library. The strategy is based on the Stochastic indicator crossover.

## Strategy Overview

The strategy follows a simple rule based on the Stochastic indicator crossover. When the Stochastic indicator's %K line crosses above the %D line, a buy signal is generated. Conversely, when the %K line crosses below the %D line, a sell signal is generated. The strategy aims to capture potential trend reversals.

## Strategy Parameters

The following parameters can be configured for the strategy:

- `FASTK_PERIOD` or `PERIOD`: The period for the fast %K line of the Stochastic indicator.
- `SLOWK_PERIOD` or `SMOOTH_K_PERIOD`: The period for the slow %K line of the Stochastic indicator.
- `SLOWD_PERIOD` or `SMOOTH_D_PERIOD`: The period for the slow %D line of the Stochastic indicator.

## Initialization

The strategy initializes the Stochastic parameters by retrieving them from the strategy parameters. It performs sanity checks to ensure that the parameters are positive integers.

## Entry Decision

The `strategy_select_instruments_for_entry` method is called for each candle to determine the instruments for which entry orders should be placed. It loops over the instruments in the provided bucket and checks if there are no current orders for the instrument. If no orders are present, it calculates the Stochastic crossover value for the instrument. If the crossover value is -1 or 1, indicating a sell or buy signal respectively, the instrument is added to the selected instruments bucket along with additional meta information.

## Entry Order Placement

The `strategy_enter_position` method is called for each selected instrument from the entry decision process. It places a buy or sell order for the instrument based on the sideband information received. The order quantity is determined by multiplying the number of lots by the instrument's lot size.

## Exit Decision

The `strategy_select_instruments_for_exit` method is called for each candle to determine the instruments for which exit orders should be placed. It loops over the instruments in the provided bucket and checks if there is a current order for the instrument that is complete. If a complete order is found, it calculates the Stochastic crossover value for the instrument. If the crossover value is opposite to the order's transaction type (buy or sell), an exit order is placed for the instrument.

## Exit Order Placement

The `strategy_exit_position` method is called for each selected instrument from the exit decision process. It exits the main order for the instrument and sets the main order to None. It returns True to indicate that the instrument has exited completely.

