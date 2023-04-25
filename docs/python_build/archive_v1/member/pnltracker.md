# P&L Tracker
The P&L Tracker feature enables you to grab profits or limit your loss at (close to) predefined values for your strategy.

`Profit Desired` - Give the desired profit amount here. This is the maximum profit that you would like to gain from this strategy, after which you would like the strategy to stop. As soon the strategy breaches this amount, all positions will be squared off and the strategy will stop its execution.

`Risk Appetite` - Give the risk appetite amount here. This is the most loss that you would like to bear in this strategy, after which you would like the strategy to stop. As soon the strategy breaches this amount, all positions will be squared off and the strategy will stop its execution.

This feature is available and live for:

|  Trading Type | Available |
|:-------------:|:-------:|
| Real Trading  |    <font size=4>✅</font>    |
| Paper Trading |    <font size=4>✅</font>    |
| Backtesting   |    <font size=4>✅</font>    |

AlgoBulls Risk Management System will try its best to book your P&L at the given Profit Desired or limit it at the given Risk Appetite.

[ ![Portfolio](imgs/PnL_tracker.gif "Click to Enlarge or Ctrl+Click to open in a new Tab") ](imgs/PnL_tracker.gif)

You can either give both values or keep both values blank. Giving one of the values and keeping the other value blank is not allowed.

In other words:

* This feature can be turned ON by giving both values.
  
* This feature can be turned OFF by keeping both values blank.

Currently, The P&L Scan Frequency for Real Trading and Paper Trading is 1 minute (i.e. 60 seconds). This may change in the future.

!!! note
        * This feature is currently in Beta mode, so if you are not sure, keep both values blank (Turn OFF this feature).

        * For Real Trading - These values are not guaranteed as there are various factors into play outside the control of AlgoBulls systems, like market liquidity, momentum, delays introduced due to network, and so on.

        * For Real Trading - For P&L tracker to function effectively, please do not run multiple strategies on the same instrument(s).         
