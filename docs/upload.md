# Upload your Strategy

## Previously...
---
You have created a strategy by:

* Coding the complete strategy from the [Create](programexample.md) page.

**OR**

* Picking up a ready strategy from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool) package.

## Now...
---
You are now ready to upload your strategy into your AlgoBulls account for Backtesting, Paper Trading and/or Real Trading.

## Before you start...
---

* Make sure you have an active working AlgoBulls account ready to go!
* Open a Jupyter Notebook.
* If you have coded the strategy yourself and not used a ready strategy from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool) package, then make sure your strategy file (.py) and the Jupyter Notebook **are in the same folder
  **.

## Let's Start...
---
Run the following code snippets into the Jupyter Notebook one by one (or all together).

### Import statements
---

```python
import inspect
from pyalgotrading.algobulls import AlgoBullsConnection
```

### Import the strategy class
---
Perform the below step either to import a ready strategy **OR** to import your own created strategy.

=== "Import a ready strategy"

```python
from pyalgostrategypool.strategy_ema_regular_order import StrategyEMARegularOrder
```

=== "Import your own strategy"

```python
from strategy_sma_regular_order import StrategySMARegularOrder
```

### Establish a connection to the AlgoBulls Platform
---

```python
algobulls_connection = AlgoBullsConnection()
algobulls_connection.get_authorization_url()
```

The output of the above step is:

`Please login to this URL with your AlgoBulls credentials and get your developer access token: https://app.algobulls.com/user/login`

You will need to login to your AlgoBulls account and fetch the access token from:

Settings -> General -> Developer Options

([See How](https://help.algobulls.com/member/Settings/general-settings/#developer-options))

Once you have the access token, set it in the code as shown here:

```python
algobulls_connection.set_access_token('4365817b795770ea31040a21ad29c8e78b63ad88')
```

Replace the token you have copied with the token in the code above.

### Print your Strategy code
--- 
You can print your strategy code once to verify if this is the correct code before uploading it to the platform. This step is optional.

```python
print(inspect.getsource(StrategySMARegularOrder))
```

### Upload your Strategy
---
Upload your strategy as shown in the code below.

```python
algobulls_connection.create_strategy(StrategySMARegularOrder)
```

### Re-upload your Strategy after modifications
---
If you are re-uploading your strategy after some changes, then use the overwrite switch as shown here.

```python
algobulls_connection.create_strategy(StrategySMARegularOrder, overwrite=True)
```

## What's Next...
---
You are now ready to test your uploaded strategy and perform Backtesting, Paper Trading and/or Real Trading with it.
