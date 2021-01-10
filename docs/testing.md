# Test your Strategy

## Previously...
---
You have uploaded your strategy to the AlgoBulls platform.
## Now...
---
Using the uploaded strategy, you can now try:

* Backtesting
* Paper Trading
* Real Trading 

## Before you start...
---
Open a Jupyter Notebook.

The steps you will follow are:

1. Establish a connection to the AlgoBulls Platform.
2. Display all Strategies you have in your account.
3. Select the SMA strategy.
4. Optionally, print the strategy once.
5. Select instrument(s).
6. Submit/Run a Backtest, Paper Trade or Real Trade job.
7. Check Job Status.
8. Fetch Logs (even while the job is running).
9. Fetch Reports. (PnL, Statistics, Order History)

## Let's Start...
---
Run the following code snippets into the Jupyter Notebook one by one (or all together).

### Import statements
---
```python
from pyalgotrading.algobulls import AlgoBullsConnection
from datetime import datetime as dt
from pyalgotrading.constants import *
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

### Display all strategies in your account
---
```python
all_strategies = algobulls_connection.get_all_strategies()
all_strategies
```

An example of the output wil be:
![Output](output.png "Sample Output")

### Select the SMA strategy
---
Select the last entry of the `strategyCode` column and display it.
```python
strategy_code1 = all_strategies.iloc[-1]['strategyCode']
strategy_code1
```

### Print your Strategy code
--- 
You can print your strategy code once to verify if this is the correct code. This step is optional.

```python
strategy_details1 = algobulls_connection.get_strategy_details(strategy_code1)
print(strategy_details1)
```

### Search for instruments (based on a search query)
---
Now display a few instruments with some keyword. The example below uses 'SBIN' as the keyword.

```python
instruments = algobulls_connection.search_instrument('SBIN')
instruments
```

### Select an instrument
---
From the output, select the instrument on which you wish to test your strategy. For this example, select the first one.
```python
instrument = instruments[0]['value']
instrument
```

### Submit a Job
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    algobulls_connection.backtest(strategy_code=strategy_code1, 
            start_timestamp=dt(year=2020, month=7, day=1, hour=9, minute=15), 
            end_timestamp=dt(year=2020, month=7, day=7, hour=15, minute=30), 
            instrument=instrument, 
            lots=1,
            strategy_parameters={
              'timeperiod1': 5,
              'timeperiod2': 12
            }, 
            candle_interval=CandleInterval.MINUTES_15)
    ```
    
=== "Paper Trading"
    ```python
    algobulls_connection.papertrade(strategy_code=strategy_code1, 
            start_time=time(hour=9, minute=15), 
            end_time=time(hour=23, minute=30), 
            instrument=instrument, 
            lots=1,
            strategy_parameters={
                'timeperiod1': 5,
                'timeperiod2': 12
            }, 
            candle_interval=CandleInterval.MINUTES_15)
    ```
    
=== "Real Trading"
    ```python
    algobulls_connection.realtrade(strategy_code=strategy_code1, 
            start_time=time(hour=9, minute=15), 
            end_time=time(hour=15, minute=30), 
            instrument=instrument, 
            lots=1,
            strategy_parameters={
               'timeperiod1': 5, 
                'timeperiod2': 12
            },
            candle_interval=CandleInterval.MINUTES_1)
    ```
    
### Fetch Job Status
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    algobulls_connection.get_backtesting_job_status(strategy_code1)
    ```
    
=== "Paper Trading"
    ```python
    algobulls_connection.get_papertrading_job_status(strategy_code1)
    ```
    
=== "Real Trading"
    ```python
    algobulls_connection.get_realtrading_job_status(strategy_code=strategy_code1)
    ```
    
You can stop a submitted job anytime.

### Stop a Job
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    algobulls_connection.stop_backtesting_job(strategy_code1)
    ```
    
=== "Paper Trading"
    ```python
    algobulls_connection.stop_papertrading_job(strategy_code1)
    ```
    
=== "Real Trading"
    ```python
    algobulls_connection.stop_realtrading_job(strategy_code=strategy_code1)
    ```

You can fetch the logs in the middle of a job to mnoitor the progress.

### Fetch logs of an ongoing/stopped/completed job
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    logs = algobulls_connection.get_backtesting_logs(strategy_code1)
    print(logs)
    ```
    
=== "Paper Trading"
    ```python
    logs = algobulls_connection.get_papertrading_logs(strategy_code1)
    print(logs)
    ```
    
=== "Real Trading"
    ```python
    logs = algobulls_connection.get_realtrading_logs(strategy_code=strategy_code1)
    print(logs)
    ```
    
You can fetch the PnL report, statistics and order history for a job.
    
### Fetch PnL Reports
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    algobulls_connection.get_backtesting_report_pnl_table(strategy_code1, show_all_rows=True)
    ```
    
=== "Paper Trading"
    ```python
    algobulls_connection.get_papertrading_report_pnl_table(strategy_code1)
    ```
    
=== "Real Trading"
    ```python
    algobulls_connection.get_realtrading_report_pnl_table(strategy_code=strategy_code1)
    ```

### Fetch Report Statistics
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    algobulls_connection.get_backtesting_report_statistics(strategy_code1)
    ```
    
=== "Paper Trading"
    ```python
    algobulls_connection.get_papertrading_report_statistics(strategy_code1)
    ```
    
=== "Real Trading"
    ```python
    algobulls_connection.get_realtrading_report_statistics(strategy_code=strategy_code1)
    ```
    
### Fetch Order History
---
Click on each of the tabs to see the relevant code snippet.

=== "Backtesting"
    ```python
    order_history = algobulls_connection.get_backtesting_report_order_history(strategy_code1)
    print(order_history)
    ```
    
=== "Paper Trading"
    ```python
    order_history = algobulls_connection.get_papertrading_report_order_history(strategy_code1)
    print(order_history)
    ```

!!! Note
    * Order History for Real Trading is not supported by brokers.
    * Order History for Backtesting and Paper Trading is supported by the AlgoBulls Virtual Brokers.

## What's Next...
---
You can now explore more by creating and uploading more complex strategies.

You can also check out the [Strategy Coding Guidelines](codeguide.md).
