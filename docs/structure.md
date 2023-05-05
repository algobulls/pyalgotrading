## Previously...
---
You now have the necessary prerequisites installed and ready.

## Now...
---
This page describes the methods you will use to create your strategy. 

## Let's Start...
---
You have the following methods.

### Methods
---
1. `strategy_select_instruments_for_entry()` - You may want to run your strategy for multiple instruments. When you pass those instruments to the strategy, 
the backend core calls this method for each instrument one by one, every candle time. This allows you to write decision-making code for each instrument, 
allowing you to decide whether an order is to be punched for that particular instrument or not.
2. `strategy_enter_position()` - You can now punch your order in this method for each instrument that you have selected for entry in the previous method.
3. `strategy_select_instruments_for_exit()` - Once a position is entered for a particular instrument, the backend core calls this method for those 
instruments one by one, every candle time. This allows you to write decision-making code for each instrument, allowing you to decide whether that 
particular instrument is to be exited or not.
4. `strategy_exit_position()` - You can now exit positions in this method for each instrument that you have selected for exit in the previous method.

### Supporting Methods
---
You have the following supporting methods:

1. `__init__()` - This is the constructor method used in every strategy. You can perform sanity checks here for each parameter passed as an argument to the strategy.
You can also declare the set of variables that you may need for your strategy.   
2. `initialize()` - This method is called every time the strategy starts for the first time as well as the start of every trading day. 
You may set initial values for the set of variables that you have declared in the previous method. 
3. `name()` - This method sets a unique name for your strategy.
4. `versions_supported()` - This method sets the version of AlgoBulls Platform on which this strategy is certified tested successfully by you.

### Utility Functions
---
You have the following utility function to be used in this strategy :

1. `get_crossover_value()` - A utility method available which calculates the crossover value. 

### Flowchart
---
Once you create your own strategy or use a ready strategy from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool) package, this is how it works internally on the AlgoBulls Core Trading Engine.

![Flowchart](flow1.png "How does a Strategy work")

## What's Next...
---
Next, you code the actual strategy taken as an example in this tutorial. Alternatively, you can pick up a ready strategy and directly [upload](upload.md) it.
