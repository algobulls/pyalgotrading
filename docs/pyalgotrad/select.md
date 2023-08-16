# Select your Strategy

---
### Previously...

You have uploaded or saved a strategy by:

[//]: # (* Coding the complete strategy from the [Normal Strategy Guide]&#40;strategies/common_normal_strategy.md&#41; or [Options Strategy Guide]&#40;strategies/common_options_strategy.md&#41; page.)
* Your strategy is already [uploaded](pyalgotrad/upload.md) on the AlgoBulls account and you want to search or select it
    
**OR**

* You have saved the strategy from the AlgoBulls Website



---
### Now...
You are now ready to select or import your strategy from your AlgoBulls account for Backtesting, Paper Trading and/or Real Trading. 

---
### Before you start...
* Make sure you have an active working AlgoBulls account ready to go!
* Open a Jupyter Notebook.
* If you have coded the strategy yourself and not used a ready strategy from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool) package, then make sure your strategy file (.py) and the Jupyter Notebook **are in the same folder**. 

---
### Let's Start...
Run the following code snippets into the Jupyter Notebook one by one (or all together).


---
#### Import statements

```python
import inspect
from pyalgotrading.algobulls import AlgoBullsConnection
```

---
#### Import the strategy class
Perform the below step either to import a ready strategy **OR** to import your own created strategy.

> **Import a ready strategy**
    ```python
    from pyalgostrategypool.strategy_ema_regular_order import StrategyEMARegularOrder
    ```

> **Import your own strategy**
    ```python
    from strategy_sma_regular_order import StrategySMARegularOrder
    ```

---
#### Establish a connection to the AlgoBulls Platform

```python
algobulls_connection = AlgoBullsConnection()
algobulls_connection.get_authorization_url()
```
The output of the above step is:

`Please login to this URL with your AlgoBulls credentials and get your developer access token: https://app.algobulls.com/user/login`

You will need to log in to your AlgoBulls account and fetch the access token from:

Settings -> General -> Developer Options

([See How](https://help.algobulls.com/member/Settings/general-settings/#developer-options))

Once you have the access token, set it in the code as shown here:

```python
algobulls_connection.set_access_token('4365817b795770ea31040a21ad29c8e78b63ad88')
```
Replace the token you have copied with the token in the code above.

---
#### View all the strategies in your AlgoBulls Account
You can view all the strategy saved on your AlgoBulls account.
```python
all_strategies_df = algobulls_connection.get_all_strategies()
print(all_strategies_df)
```

---
#### Search your Strategy
-  Search your strategy using `strategy name`. Make sure you have the strategy with given name in your AlgoBulls Account.
     ```python
         strategy_name = 'Exponential Moving Averages Crossover'
         strategy_code, strategy_name = all_strategies_df.loc[all_strategies_df['strategyName'] == strategy_name].iloc[0]        
     ```
-  Search your strategy using `strategy code`. Make sure you have the strategy with given code in your AlgoBulls Account.
     ```python
     strategy_code = 'afd6214c5db94dbeae7502e861fa4ffc'
     strategycode, strategyname = all_strategies_df.loc[all_strategies_df['strategyCode'] == strategy_code].iloc[0]
     ```

---
### What's Next...
You are now ready to test your uploaded strategy and perform Backtesting, Paper Trading and/or Real Trading with it.

---
