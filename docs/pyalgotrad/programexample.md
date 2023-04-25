# Create your Strategy

### **Previously...**

You have covered the basic code structure of a strategy.

---
### **Now...**

You can either follow this page to create a strategy, or you can pickup a ready strategy (shown below) and move to the next page. 

---
### **Before you start...**

If you want to use a ready strategy from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool) package, then you can directly jump to the [Upload](upload.md) section. 

---
### **Let's Start...**

Follow the steps given below to create a new strategy of your own.

Create a python file called `strategy_sma_regular_order.py`.

You will add the following code snippets into the file and then save it.

---
#### Import statements

```python
from pyalgotrading.strategy.strategy_base import StrategyBase
from pyalgotrading.constants import *
```

---
#### Create the class `StrategySMARegularOrder` and subclass it from `StrategyBase`

```python
class StrategySMARegularOrder(StrategyBase):
```
Now you can add the methods mentioned in the [structure](structure.md) inside the class. First you can add the `__init__` and the `initialize` methods.

---
#### Constructor: `def __init__()`

```python
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.timeperiod_x = self.strategy_parameters['timeperiod1']
    self.timeperiod_y = self.strategy_parameters['timeperiod2']

    self.main_order = None
```

The `init` method does the following:

1. `super()` - Calls the constructor of the superclass.
2. `self.strategy_parameters` - Catches the parameters and saves them for local use - When you will submit a testing job for your SMA strategy, 
you will pass parameters that will be used inside the strategy. 
For SMA, we are calculating crossover for 2 SMA timeperiod values, example 5 and 12.  These 2 parameters will be caught by `self.strategy_parameters` and stored for local use in `self.timeperiod1` and `self.timeperiod2`.
3. `self.main_order` - Create an object that manages orders for you throughout the strategy.

The `init` method is specific to Python's internal workings and it is preceded and succeeded by double underscores ( _ _ ) joined together.

---
#### `def initialize()`

```python
def initialize(self):
    self.main_order = {}
```

The `initialize` method sets the `self.main_order` as an empty dictionary. This method is called at the start of every trading day.

For instance, say you are submitting a backtesting job for 5 previous days starting at 10:30 every day, then the `initialize` method will be called every day for 5 days at 10:30.

Now add the two static methods, `name` and `versions_supprted`.

---
#### `def name()`

```python
@staticmethod
def name():
    return 'SMA Regular Order Strategy'
```
The name should be unique in your collection of strategies.

---
#### `def versions_supported()`

```python
@staticmethod
def versions_supported():
    return AlgoBullsEngineVersion.VERSION_3_2_0
```
Mark both the above methods as `@staticmethod`.

The `versions_supported` method does the following:

1. It notifies the AlgoBulls platform that the strategy is working correctly for the platform version 3.2.0
2. Since the platform will be constantly upgraded to incorporate new features and improve efficiency, the verion may change.
3. If the version changes, and if you submit a job for this strategy, then the AlgoBulls platform will spawn a server having version 3.2.0 for your strategy.
4. Having this method ensures that the AlgoBulls platform always provides the correct environment for your strategy.

---
#### `def strategy_select_instruments_for_entry()`

```python
def strategy_select_instruments_for_entry(self, candle, instruments_bucket):

    selected_instruments_bucket = []
    sideband_info_bucket = []

    for instrument in instruments_bucket:
        crossover_value = self.get_crossover_value(instrument)
        if crossover_value == 1:
            selected_instruments_bucket.append(instrument)
            sideband_info_bucket.append({'action': 'BUY'})
        elif crossover_value == -1:
            if self.strategy_mode is StrategyMode.INTRADAY:
                selected_instruments_bucket.append(instrument)
                sideband_info_bucket.append({'action': 'SELL'})

    return selected_instruments_bucket, sideband_info_bucket
```

The `strategy_select_instruments_for_entry` method does the following:

1. `selected_instruments_bucket` and `sideband_info_bucket` - Creates 2 empty lists that will be used to pass the selected instruments and additional information about them respectively.
2. The Loop - The loop will iterate over each instrument name passed (while submitting the job) and will decide whether to set an entry position or not for it.
3. `crossover_value` - The crossover value is calculated and stored here. Crossover values are interpreted as:
    1. Value 1 - Cut upwards
    2. Value -1 - Cut downwards
    3. Value 0 - No crossover
4. If conditions - If the crossover value is 1, then the instrument is selected for entry position, with the position as 'BUY'. If the crossover value is -1, then the instrument is selected for entry position, with the position as 'SELL'. The selected instrument is appended to the `selected_instruments_bucket`, and the associated action (BUY/SELL) is appended to the `sideband_info_bucket`.
5. `selected_instruments_bucket` and `sideband_info_bucket` - Both the lists (whether populated or empty) are returned to the platform for further actions.

!!! Note
    * SELL Entry positions are allowed only if the strategy is running for INTRADAY. DELIVERY strategies do not allow SELL as entry positions. This is taken care of in the `elif` part.
    * The `strategy_select_instruments_for_entry` method is called once for every candle time. For Instance, if you submit a job with the candle time as 15 minutes, then this method will be called once for every 15 minute candle.
    * The actual Entry position (BUY/SELL) is not entered here. Here, only the instrument is selected based on the crossover value with the proper action mentioned in the `sideband_info_bucket`. The Entry position will be taken in the next method below.
    * The `sideband_info_bucket` contains a very versatile dictionary object. You may use it to pass any other additional information that you wish. 

---
#### `def strategy_enter_position()`

```python
def strategy_enter_position(self, candle, instrument, sideband_info):
    if sideband_info['action'] == 'BUY':
        qty = self.number_of_lots * instrument.lot_size
        self.main_order[instrument] = \
            self.broker.BuyOrderRegular(instrument=instrument,
                order_code=BrokerOrderCodeConstants.INTRADAY,
                order_variety=BrokerOrderVarietyConstants.MARKET,
                quantity=qty)
    elif sideband_info['action'] == 'SELL':
        qty = self.number_of_lots * instrument.lot_size
        self.main_order[instrument] = \
            self.broker.SellOrderRegular(instrument=instrument,
                 order_code=BrokerOrderCodeConstants.INTRADAY,
                 order_variety=BrokerOrderVarietyConstants.MARKET,
                 quantity=qty)
    else:
        raise SystemExit(f'Got invalid sideband_info value: {sideband_info}')

    return self.main_order[instrument]
```

The `strategy_enter_position` method does the following:

1. If conditions - The conditions read the action from the `sideband_info` and perform the required action (BUY/SELL).
2. `qty` - The quantity is calculated and stored here. The number of lots will be passed by you as a parameter while submitting a job. The parameter will be caught in `self.number_of_lots`. The instrument object has the 'lot size', which you can retrieve using `instrument.lot_size`. You can then use the formula as shown in the code to calculate the quantity.
3. `BuyOrderRegular` and `SellOrderRegular` - These execute the required action. You need to pass the instrument, order code, order variety and the quantity values.
    * `instrument` - the instrument on which the BUY/SELL action will be performed.
    * `order_code` - whether the order is for INTRADAY or DELIVERY. Possible values are:
        + `BrokerOrderCodeConstants.INTRADAY`
        + `BrokerOrderCodeConstants.DELIVERY`
        + `BrokerOrderCodeConstants.DELIVERY_T1`
        + `BrokerOrderCodeConstants.DELIVERY_T2`
    * `order_variety` - the type of order variety. Possible values are:
        + `BrokerOrderVarietyConstants.MARKET`
        + `BrokerOrderVarietyConstants.LIMIT`
        + `BrokerOrderVarietyConstants.STOPLOSS_MARKET`
        + `BrokerOrderVarietyConstants.STOPLOSS_LIMIT`
    * `qty` - the quantity to BUY/SELL.
4. `self.main_order` - The main order (for that particular instrument) is now populated (BUY OR SELL) and is returned to the platform for further actions.

You can also punch Bracket Orders instead of Regular Orders. A typical BUY Bracket Order will look like this:
```python
qty = self.number_of_lots * instrument.lot_size
ltp = self.broker.get_ltp(instrument)
self.main_order[instrument] = \
            self.broker.BuyOrderBracket(instrument=instrument,
                order_code=BrokerOrderCodeConstants.INTRADAY,
                order_variety=BrokerOrderVarietyConstants.LIMIT,
                quantity=qty,
                price=ltp,
                stoploss_trigger=ltp - (ltp * self.stoploss),
                target_trigger=ltp + (ltp * self.target),
                trailing_stoploss_trigger=ltp * self.trailing_stoploss)
```

The additional parameters are:

* `price` - If you want to BUY at the market price (Last Traded Price) or LTP, then just fetch the LTP using `get_ltp` as shown in the code above. Store the value in `ltp` and pass it to `price`.
* `stoploss_trigger`, `target_trigger` and `trailing_stoploss_trigger` - You can calculate these using the `ltp` and the values you will pass through 
the job that you will submit. The parameters will be caught as `self.stoploss`, `self.target` and `self.trailing_stoploss`.

!!! Note
    * If you plan to use Bracket Order instead of Regular Orders, then create a separate Python file for it, say `strategy_sma_bracket_order.py`.
     You can also change the class name as `StrategySMABracketOrder`. There will be changes in the entry and exit methods also.
    * The `strategy_enter_position` method is called once for every instrument. For instance, you want to run this strategy for 5 instruments. Say that the `strategy_select_instruments_for_entry` method selects 3 instruments for ENTRY positions (BUY/SELL). Then, the `strategy_enter_position` method will be called thrice, once for each instrument respectively within the candle time frame (say, 15 minutes). 

---
#### `def strategy_select_instruments_for_exit()`

```python
def strategy_select_instruments_for_exit(self, candle, instruments_bucket):
    selected_instruments_bucket = []
    sideband_info_bucket = []

    for instrument in instruments_bucket:
        if self.main_order.get(instrument) is not None:
            crossover_value = self.get_crossover_value(instrument)
            if crossover_value in [1, -1]:
                selected_instruments_bucket.append(instrument)
                sideband_info_bucket.append({'action': 'EXIT'})
    return selected_instruments_bucket, sideband_info_bucket
```

The `strategy_select_instruments_for_exit` method does the following:

1. `selected_instruments_bucket` and `sideband_info_bucket` - Creates 2 empty lists that will be used to pass the selected instruments and additional information about them respectively.
2. The Loop - The loop will iterate over each instrument name passed (which are in Entry position (BUY/SELL)) and will decide whether to set an exit position or not for it.
3. If condition - The exit steps are executed only if the instrument is holding at an ENTRY position (BUY/SELL). You can do this by checking if the `self.main_order` object is `None` or not, and proceed only if it is not `None`. 
3. `crossover_value` - The crossover value is calculated and stored here. Crossover values are interpreted as:
    1. Value 1 - Cut upwards
    2. Value -1 - Cut downwards
    3. Value 0 - No crossover
4. If condition - If the crossover value is 1 or -1, then the instrument is selected for exit position. The selected instrument is appended to the `selected_instruments_bucket`, and the associated action (EXIT) is appended to the `sideband_info_bucket`.
5. `selected_instruments_bucket` and `sideband_info_bucket` - Both the lists (whether populated or empty) are returned to the platform for further actions.

!!! Note
    * The actual Exit position (BUY/SELL) is not entered here. Here, only the instrument is selected based on the crossover value with the proper action mentioned in the `sideband_info_bucket`. The Exit position will be taken in the next method below.
    * The `sideband_info_bucket` contains a very versatile dictionary object. You may use it to pass any other additional information that you wish.
    * Whenever a new trading day starts, the `strategy_select_instruments_for_exit` is called first. This is very important for DELIVERY strategies. Many instruments might be holding in an Entry Position at the end of the previous trading day, and they might be eligible for exit at the start of the new trading day.  

---
#### `def strategy_exit_position()`

```python
def strategy_exit_position(self, candle, instrument, sideband_info):
    if sideband_info['action'] == 'EXIT':
        self.main_order[instrument].exit_position()
        self.main_order[instrument] = None
        return True

    return False
```

The `strategy_exit_position` method does the following:

1. If condition - checks whether the appropriate action is set in the `sideband_info`.
2. `self.main_order` - calls `exit_position` method for the particular main order of the instrument. If the Entry Position was BUY, then the exit position is automatically taken as SELL and vice versa. The platform takes care of this automatically.
3. `self.main_order` - set it to `None`, as the order has been exited and no longer holds anything.
4. Return values - returns `True` to the platform if the exit steps were performed, else return `False`.

---
#### `def get_crossover_value()`

```python
def get_crossover_value(self, instrument):
    hist_data = self.get_historical_data(instrument)
    sma_x = talib.SMA(hist_data['close'], timeperiod=self.timeperiod_x)
    sma_y = talib.SMA(hist_data['close'], timeperiod=self.timeperiod_y)
    crossover_value = self.utils.crossover(sma_x, sma_y)
    return crossover_value
```

The `get_crossover_value` method does the following:

1. `hist_data` - The historical data for the instrument is fetched using the `get_historical_data` method and stored here. The data is in the form of a table (Pandas DataFrame) having the following columns:
    * `timestamp` - the data and time when the data was measured
    * `volume` - the volume of that instrument
    * `open`, `high`, `low` and `close` - the OHLC values of the instrument
    * `oi` - the Open Interest of that instrument
2. `sma_x` and `sma_y` - the SMA function from the `talib` package is used to calculate the Moving Average for both SMA timeperiods. The candle close value is used for calculations, i.e. `hist_data['close']`.
3. `crossover_value` - calculates the crossover value using the `crossover` method from the `utils` package.
4. Return value - return the crossover value to the caller method.

!!! Note
    * The order of values passed to the `crossover` method of the `utils` package is very important.
    * Example: you have 2 SMA values, 5 and 12. The strategy describes that there should be an BUY Entry Position when SMA(5) cuts SMA(12) upwards (crossover value should be 1).
    * In this case, if you mistakenly pass SMA(12) value first and SMA(5) value next to the `crossover` function, the answer you will get is -1 (Cut downwards).
    * Though, the crossover value is correct, the strategy is expecting to BUY at crossover 1 as per the code, which will not work now.
    * Therefore, the strategy will work correctly only if you pass SMA(5) first and then SMA(12) to the `crossover` function, thus making the order of parameters passed an important point to be aware of, while coding the strategy.

### **What's Next...**
---
Next, you upload the strategy into your AlgoBulls account.
