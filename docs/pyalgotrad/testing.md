# Execute your Strategy

## Previously...
You have uploaded your strategy to the AlgoBulls platform.

---
## Now...
Using the uploaded strategy, you can now try:  

- **Backtesting** 
- **Paper Trading**
- **Real Trading** 

---

## Before you start...
Open a Jupyter Notebook.

The steps you will follow are:

1. Establish a connection to the AlgoBulls Platform.
2. Display all Strategies you have in your account.
3. Select the strategy.
4. Optionally, print the strategy once.
5. Select instrument(s).
6. Submit/Run a Backtest, Paper Trade or Real Trade job.
7. Check Job Status.
8. Fetch Logs (even while the job is running).
9. Fetch Reports. (PnL, Statistics, Order History)

---
## Let's Start...
Run the following code snippets into the Jupyter Notebook one by one (or all together).

### Create a new strategy file
eg: strategy_```<unique_code_if_needed>```_options_ema_crossover.py
Make sure this strategy file is in the same folder as the jupyter notebook.

!!!Tips "Coding Conventions"
    * Keep a unique file name
    * Make sure that the file name is in lowercase and that each word is separated with an underscore '_' as shown above.


!!!Tips "How to Code ?"
    To know more on how to code trading strategies and understand their format, click [here](strategy_guides/structure.md).
    We have in detail explanation for [regular strategies](strategy_guides/common_regular_strategy.md) as well as [options strategies](strategy_guides/common_options_strategy.md)


### Import statements

```python
from pyalgotrading.algobulls import AlgoBullsConnection
from datetime import datetime as dt
from pyalgotrading.constants import *
```

---
### Establish a connection to the AlgoBulls Platform

```python
algobulls_connection = AlgoBullsConnection()
algobulls_connection.get_authorization_url()
```
The output of the above step is:

`Please login to this URL with your AlgoBulls credentials and get your developer access token: https://app.algobulls.com/user/login`

!!! info "Get Developer Key"
    You will need to log in to your AlgoBulls account and fetch the access token from:  ([See How](prerequisites.md/#algobulls-account){target="_blank"})  
    **Settings** -> **General** -> **Developer Options**  
    

Once you have the access token, set it in the code as shown here:

```python
algobulls_connection.set_access_token('4365817b795770ea31040a21ad29c8e78b63ad88')
```

Replace the token you have copied with the token in the code above.

---
#### Display all strategies in your account
---

```python
all_strategies = algobulls_connection.get_all_strategies()
all_strategies
```

An example of the output will be:
![Output](output.png "Sample Output")

### Select the strategy

Select the last entry of the `strategyCode` column and display it.
```python
strategy_code = all_strategies.iloc[-1]['strategyCode']
strategy_code
```

---
### Print your Strategy code

You can print your strategy code once to verify if this is the correct code. This step is optional.

```python
strategy_details1 = algobulls_connection.get_strategy_details(strategy_code)
print(strategy_details1)
```

---
### Search for instruments (based on a search query)

Now display a few instruments with some keyword. The example below uses 'SBIN' as the keyword.

```python
instruments = algobulls_connection.search_instrument('SBIN')
instruments
```

--- 
### Select an instrument

From the output, select the instrument on which you wish to test your strategy. For this example, select the first one.
```python
instrument = instruments[0]['value']
instrument
```

---
### Submit a Job

Delete previous trades
```python
algobulls_connection.delete_previous_trades(strategy=strategy)
```

Set the **parameters** for the strategy
```python

parameters={
    'timeperiod1': 5,
    'timeperiod2': 12
}
```

```python
vendor_details = {
    'brokerName': '<VENDOR_NAME>',
    'credentialParameters': {
        'api_key': '<API_KEY>',
        'secret_key': '<SECRET_KEY>'
    }
}
```

```python
broking_details = {
    'brokerName': '<BROKER_NAME>',
    'credentialParameters': {
        'user_id': '<USER_ID>',
        'api_key': '<API_KEY>',
        'password': '<PASSWORD>'
    }
}
```

Click on each of the tabs to see the relevant code snippet.

=== "**Backtesting**"
    ```python
    algobulls_connection.backtest(
            strategy=strategy_code,         # strategy code
            start='2020-7-1 09:15 +0530',   # start date-time of strategy ('YYYY-MM-DD HH:MM z')
            end='2020-7-7 15:30 +0530',     # end date-time of strategy ('YYYY-MM-DD HH:MM z')
            instruments='NSE:SBIN',         # name of the instrument
            lots=1,                         # number of lots per trade
            parameters=parameters,          # parameters required for the strategy
            candle='15 minutes',            # candle size eg : '1 Day', '1 hour', '3 minutes'
            delete_previous_trades=True,    # delete the previous trades for papertrading (default is true),
            initial_funds_virtual=10000,    # virtual funds allotted before the paper trading starts (default is 1e9)
            vendor_details=vendor_details   # vendor's details for authentication and verification 
    )
    ```


=== "**Paper Trading**"
    ```python
    algobulls_connection.papertrade(
            strategy=strategy_code,         # strategy code
            start='09:15 +0530',            # start time of strategy (HH:MM z)     
            end='15:30 +0530',              # end time of strategy (HH:MM z)
            instruments='NSE:SBIN',         # name of the instrument
            lots=1,                         # number of lots per trade
            parameters=parameters,          # parameters required for the strategy
            candle='15 minutes',            # candle size eg : '1 Day', '1 hour', '3 minutes'
            delete_previous_trades=True,    # delete the previous trades for papertrading (default is true)
            initial_funds_virtual=10000,    # virtual funds allotted before the paper trading starts (default is 1e9)
            vendor_details=vendor_details   # vendor's details for authentication and verification 
    )
    ```

=== "**Real Trading**"
    ```python
    algobulls_connection.realtrade(
            strategy=strategy_code,          # strategy code
            start='09:15 +0530',             # start time of strategy (HH:MM z)     
            end='15:30 +0530',               # end time of strategy (HH:MM z)
            instruments='NSE:SBIN',          # name of the instrument
            lots=1,                          # number of lots per trade
            parameters=parameters,           # parameters required for the strategy
            candle='15 minutes',             # candle size eg : '1 Day', '1 hour', '3 minutes'
            broking_details=broking_details  # broker's details for authentication and verification 
    )
    ```


---
### Fetch Job Status

Click on each of the tabs to see the relevant code snippet.
There are 4 stages of your strategy execution : **STARTING**, **STARTED**, **STOPPING** and **STOPPED**  

=== "**Backtesting**"
    ```python
    algobulls_connection.get_backtesting_job_status(strategy_code)
    ```
    
=== "**Paper Trading**"
    ```python
    algobulls_connection.get_papertrading_job_status(strategy_code)
    ```
    
=== "**Real Trading**"
    ```python
    algobulls_connection.get_realtrading_job_status(strategy_code)
    ```
    
You can stop a submitted job anytime.

---
### Stop a Job

Click on each of the tabs to see the relevant code snippet.  

=== "**Backtesting**"
    ```python
    algobulls_connection.stop_backtesting_job(strategy_code)
    ```
    
=== "**Paper Trading**"
    ```python
    algobulls_connection.stop_papertrading_job(strategy_code)
    ```
    
=== "**Real Trading**"
    ```python
    algobulls_connection.stop_realtrading_job(strategy_code)
    ```

You can fetch the logs in the middle of a job to monitor the progress.

---
### Fetch logs

!!! Tip "Logging Tip"
    - There are 2 variations when fetching logs:  
        - Progressive Logs (`auto_update` = True):  will show progress bar and update the latest logs as the strategy is executed
        - Complete Logs (`auto_update` = False): will fetch logs only till the point where strategy is currently executing.(It wont update the latest logs, unless called manually again)

Click on each of the tabs to see the relevant code snippet.  

=== "**Backtesting**"
    ```python
    logs = algobulls_connection.get_backtesting_logs(
                strategy_code,                              # strategy code 
                auto_update=True,                           # (default=True)update the logs and show your strategy progress. If False, will only fetch logs from start to the current stage of execution
                display_logs_in_auto_update_mode=True       # only if auto_update is also True, will print logs as the progress is tracked
            )
    print(logs)
    ```
    
=== "**Paper Trading**"
    ```python
    logs = algobulls_connection.get_papertrading_logs(
                strategy_code,                              # strategy code 
                auto_update=True,                           # (default=True)update the logs and show your strategy progress. If False, will only fetch logs from start to the current stage of execution
                display_logs_in_auto_update_mode=True       # only if auto_update is also True, will print logs as the progress is tracked
            )
    print(logs)
    ```
    
=== "**Real Trading**"
    ```python
    logs = algobulls_connection.get_realtrading_logs(
                strategy_code,                              # strategy code 
                auto_update=True,                           # (default=True)update the logs and show your strategy progress. If False, will only fetch logs from start to the current stage of execution
                display_logs_in_auto_update_mode=True       # only if auto_update is also True, will print logs as the progress is tracked
            )
    print(logs)
    ```
    
You can fetch the PnL report, statistics and order history for a job.
    
---
### Fetch PnL Reports

Click on each of the tabs to see the relevant code snippet.

!!! Warning "Please Note"
     Make sure that  strategy's execution **status** is at **STOPPED** stage before generating **PnL reports**

=== "**Backtesting**"
    ```python
    algobulls_connection.get_backtesting_report_pnl_table(
            strategy_code,              # strategy code
            show_all_rows=True,         # default=True         
            force_fetch=True,           # pnl data is saved locally once fetched, to update the locally fetched data, make this parameter True
            country='USA',              # country of the exchange that was used while starting the job ('India' or 'USA')
    )
    ```
    
=== "**Paper Trading**"
    ```python
    algobulls_connection.get_papertrading_report_pnl_table(
            strategy_code,              # strategy code
            show_all_rows=True,         # default=True         
            force_fetch=True,           # pnl data is saved locally once fetched, to update the locally fetched data, make this parameter True
            country='USA',              # country of the exchange that was used while starting the job ('India' or 'USA')
    )
    ```
    
=== "**Real Trading**"
    ```python
    algobulls_connection.get_realtrading_report_pnl_table(
            strategy_code,              # strategy code
            show_all_rows=True,         # default=True         
            force_fetch=True,           # pnl data is saved locally once fetched, to update the locally fetched data, make this parameter True
            country='USA',              # country of the exchange that was used while starting the job ('India' or 'USA')
    )
    ```

---
### Fetch Report Statistics

Click on each of the tabs to see the relevant code snippet.

!!! Tip "Analytics Tips"
    You can view your analytics on the python build page as well, simply log inside your AlgoBulls Account, and look for your Strategy in **Python Build** -> **My Coded Strategies**

=== "**Backtesting**"
    ```python
    algobulls_connection.get_backtesting_report_statistics(
        strategy_code,          # strategy code
        mode='quantstats',      # package used to generate statistics
        report='full',          # format of the report
        html_dump=True          # save report as html file
    )
    ```
    
=== "**Paper Trading**"
    ```python
    algobulls_connection.get_papertrading_report_statistics(
        strategy_code,          # strategy code
        mode='quantstats',      # package used to generate statistics
        report='full',          # format of the report
        html_dump=True          # save report as html file
    )
    ```
    
=== "**Real Trading**"
    ```python
    algobulls_connection.get_realtrading_report_statistics(
        strategy_code,          # strategy code
        mode='quantstats',      # package used to generate statistics
        report='full',          # format of the report
        html_dump=True          # save report as html file
    )
    ```
   
--- 
### Fetch Order History

Click on each of the tabs to see the relevant code snippet.

=== "**Backtesting**"
    ```python
    order_history = algobulls_connection.get_backtesting_report_order_history(strategy_code)
    print(order_history)
    ```
    
=== "**Paper Trading**"
    ```python
    order_history = algobulls_connection.get_papertrading_report_order_history(strategy_code)
    print(order_history)
    ```

=== "**Real Trading**"
    ```python
    order_history = algobulls_connection.get_realtrading_report_order_history(strategy_code)
    print(order_history)
    ```

!!! Note
    - Order History for Real Trading is not supported by brokers.
    - Order History for Backtesting, Paper Trading and Real Trading is supported by the **AlgoBulls Virtual Brokers**.

---
## What's Next...

You can now explore more by creating and uploading more complex strategies.

You can also check out the [Analytics](pyalgotrading_analytics.md), to understand more about the returns and analyze your strategy based on the analytics report.
