You can open a Jupyter Notebook.

You will run the following code snippets into the notebook one by one (or all together).

## Import the following
---
```python
import inspect
from pyalgotrading.algobulls import AlgoBullsConnection
```

## Import your own strategy / a readymade strategy
---

Now perform either of these steps:

1) You can now upload your own created strategy.

2) As an example, you can also upload the `StrategyEMARegularOrder` strategy from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool) package. 

=== "Import your own strategy"
    ```python
    from strategy_sma_regular_order import StrategySMARegularOrder
    ```
    
=== "Import a readymade strategy"
    ```python
    from pyalgostrategypool.strategy_ema_regular_order import StrategyEMARegularOrder
    ```

Now you will establish a connection to the Algobulls Platform.

You will need to login to your AlgoBulls account and fetch the access token from:

Settings -> General -> Developer Options 

## Establish a connection to the AlgoBulls Platform
---
```python
algobulls_connection = AlgoBullsConnection()
algobulls_connection.get_authorization_url()
# The output of the above step is:
# Please login to this URL with your AlgoBulls credentials and get your developer access token: https://app.algobulls.com/user/login
# Set the access token in the next line of code as shown here:
algobulls_connection.set_access_token('4365817b795770ea31040a21ad29c8e78b63ad88')
```

You can print your strategy code once to verify if this is the correct code before uploading it to the platform.
## Print your Strategy code
--- 
```python
print(inspect.getsource(StrategySMARegularOrder))
```

## Upload your Strategy
---
```python
algobulls_connection.create_strategy(StrategySMARegularOrder)
# If you are re-uploading your strategy after some changes, then use the overwrite switch as shown here:
# algobulls_connection.create_strategy(StrategySMARegularOrder, overwrite=True)
```


