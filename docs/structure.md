You have the following methods:

1. `strategy_select_instruments_for_entry(self, candle, instruments_bucket)` - A method to select instruments for entry
2. `strategy_enter_position(self, candle, instrument, sideband_info)` - A method to set enter positions for each selected instrument
3. `strategy_select_instruments_for_exit(self, candle, instruments_bucket)` - A method to select instruments for exit
4. `strategy_exit_position(self, candle, instrument, sideband_info)` - A method to set exit positions for each selected instrument

You have the following supporting methods:

1. `__init__(self, *args, **kwargs)` - A method called init which is called when the strategy starts for the first time
2. `initialize(self)` - A method called initialise which is called when the strategy starts for the first time as well as the start of every trading day
3. `name()` - A method which sets a unique name for your strategy
4. `versions_supported()` - A method which sets the version of Algobulls Platform on which this strategy is certified tested successfully by you

You have the following strategy specific method:

1. `get_crossover_value(self, instrument)` - A method which calculates the crossover value 

The flowchart is as follows:

![Flowchart](flow1.png "How does a Strategy work")