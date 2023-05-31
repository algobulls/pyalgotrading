## 1. Initial steps

i. Create a new strategy file with a unique file name.
   eg: strategy_```<developer_initials>```_options_ema_crossover.py

    !!!Note
        * Add the initials of your name after the word strategy in the strategy file name so that it becomes easier to identify the developer who developed the strategy and also helps with a unique strategy name.
        * Make sure that the file name is in lowercase and that each word is separated with an underscore '_' as shown above.

ii. Create a class with the same name as the file name, and make sure the first letter of each word is in uppercase and the initials should be in uppercase as well.
    eg: For the above strategy name the class name would be:
        Strategy```<developer_initials>```OptionsEMACrossover(StrategyOptionsBaseV2)

    !!! Note
            * If the class name includes indicator names like EMA, SMA, and VWAP the name should be in uppercase in the class name but not in the file name.
            * Every strategy class is a child class of the StrategyBase.             

---

## 2. Init method

This method gets called only once when the strategy is started.

i. Strategy info:

In the __init__ method add the ```super().__init__(*args, **kwargs)``` and add the below lines.

```
VERSION = strategy_version 
CLIENT = client_name
STRATEGY_TYPE = 'OPTIONS'

self.logger.info(f'\n{"#" * 40}\nSTRATEGY VERSION: {VERSION}\n{"#" * 40}')
self.logger.debug(f'\n{"#" * 60}\nSTRATEGY TYPE: {STRATEGY_TYPE} | CLIENT: {CLIENT}\n{"#" * 60}')
```

* VERSION: This is the strategy version, the initial version is 3.3.1 as and when there are fixes/updates/changes in the strategy the version should be updated to 3.3.2, and so on.

* CLIENT: Name of the client.

* STRATEGY_TYPE: Whether the strategy is a FUTURES strategy or an OPTIONS strategy.

We print this information in the next line, so whenever we run the strategy this information is displayed in the logs.

We save the parameter string in the parameter_string variable and check if the length of the parameter_string matches the number of parameters in the strategy's YAML file.

eg:

```
parameter_string = '\n(1) FRESH_ORDER_CANDLE \n(1) START_TIME_HOURS \n(1) START_TIME_MINUTES \n(1) END_TIME_HOURS \n(1) END_TIME_MINUTES \n(1) \n(1) STRIKES_DIRECTION_CE' 
                    '\n(1) STRIKES_DIRECTION_PE \n(1) NO_OF_STRIKES_AWAY_CE \n(1) NO_OF_STRIKES_AWAY_PE \n(1) EMA_PERIOD_ONE \n(1) EMA_PERIOD_TWO' 
                    '\n(1) TARGET_PERCENTAGE \n(1) STOPLOSS_PERCENTAGE \n(1) STOPLOSS_RANGE \n(1) STOPLOSS_ORDER_COUNT_ALLOWED'

check_argument(self.strategy_parameters, 'extern_function', lambda x: len(x) >= 15, err_message=f'Need 15 parameters for this strategy: {parameter_string}')
```

* parameter_string: This string contains all the strategy parameters as shown above.

* We check if the number of parameters matches those in the strategy YAML file.

    !!! Note
            * The parameter names and the number of parameters may change for different strategies.

ii. Parameter creation:

Next, we assign the parameter values to the class variables of the same name as the parameters but in the lowercase format as shown below:

eg:
```
self.fresh_order_candle = self.strategy_parameters['FRESH_ORDER_CANDLE']
self.start_time_hours = self.strategy_parameters['START_TIME_HOURS']
self.start_time_minutes = self.strategy_parameters['START_TIME_MINUTES']
self.end_time_hours = self.strategy_parameters['END_TIME_HOURS']
self.end_time_minutes = self.strategy_parameters['END_TIME_MINUTES']
self.no_of_strikes_away_ce = self.strategy_parameters['NO_OF_STRIKES_AWAY_CE']
self.no_of_strikes_away_p = self.strategy_parameters['NO_OF_STRIKES_AWAY_PE']
self._strike_direction_ce = self.strategy_parameters['STRIKES_DIRECTION_CE']
self._strike_direction_pe = self.strategy_parameters['STRIKES_DIRECTION_PE']
self.ema_period_one = self.strategy_parameters['EMA_PERIOD_ONE']
self.ema_period_two = self.strategy_parameters['EMA_PERIOD_TWO']
self.target_percentage = self.strategy_parameters['TARGET_PERCENTAGE']
self.stoploss_percentage = self.strategy_parameters['STOPLOSS_PERCENTAGE']
self.stoploss_range = self.strategy_parameters['STOPLOSS_RANGE']
self.stoploss_order_count_allowed = self.strategy_parameters['STOPLOSS_ORDER_COUNT_ALLOWED']
```

iii. Parameter validation

We validate each parameter's value according to the strategy requirement. The following methods can be used to validate the parameter values:

* check_argument: Checks a single parameter passed in it.

      Syntax:
        check_argument(value to be checked, 'extern_function', validating condition or method, error_message)
        
        eg: 
        check_argument(self.strategy_parameters, 'extern_function', lambda x: len(x) >= 11, err_message=f'Need 11 parameters for this strategy: {parameter_string}')

* check_argument_bulk: Checks multiple parameters passed in a list 
      
      Syntax:
        check_argument_bulk(list of values to be checked, 'extern_function', validating condition or method, error_message)
        
        eg: 
        is_nonnegative_int_arg_list = [self.start_time_hours, self.start_time_minutes, self.end_time_hours, self.end_time_minutes]
        check_argument_bulk(is_nonnegative_int_arg_list, 'extern_function', is_nonnegative_int, 'Value should be >=0')


* is_nonnegative_int: Checks whether the value is greater than or equal to zero.

* is_positive_int_or_float: Checks whether the value is greater than zero and is an integer or a float value.

* is_positive_int: Checks whether the value is greater than zero and is an integer value.

* is_nonnegative_int_or_float: Checks whether the value is greater than or equal to zero and is an integer or a float value.

No of the strikes values are validated as follows:

```
no_of_strikes_list = [(self.no_of_strikes_away_ce, 'NO_OF_STRIKES_AWAY_CE'), (self.no_of_strikes_away_pe, 'NO_OF_STRIKES_AWAY_PE')]

for no_of_strikes, text in no_of_strikes_list:
    check_argument(no_of_strikes, 'extern_function', lambda x: 0 <= x <= 50 and isinstance(x, int), err_message=f'{text} should be an integer with possible values between 0 to 50')
```

Strike direction values are validated as follows:

```
strikes_direction_list = [(self._strike_direction_ce, 'STRIKE_DIRECTION_CE'), (self._strike_direction_pe, 'STRIKE_DIRECTION_PE')]

for strike_direction, text in strikes_direction_list:
    check_argument(strike_direction, 'extern_function', lambda x: x in [0, 1, 2] and isinstance(x, int), err_message=f'{text} should be an integer with possible values - 0: ITM or 1: ATM or 2: OTM')
```

Once all the parameters are validated we calculate the actual value of the strike direction from the strike direction values given in the strategy YAML file.

We define the below dictionary for ```strike_direction```.

```
strike_direction_map = {0: OptionsStrikeDirection.ITM.value, 1: OptionsStrikeDirection.ATM.value, 2: OptionsStrikeDirection.OTM.value}
```

Then we create new variables for strike direction that save the value as ATM, ITM, and OTM based on the YAML parameter value.

```
self.strike_direction_ce = strike_direction_map[self._strike_direction_ce]
self.strike_direction_pe = strike_direction_map[self._strike_direction_pe]
```

iv. Start time and End time creation:

Add the below code to calculate the strategy start time and end time, from the start time and end time parameters in the strategy YAML file.

```
try:
    self.candle_start_time = time(hour=self.start_time_hours, minute=self.start_time_minutes)
except ValueError:
    self.logger.fatal('Error converting start hours and minutes... EXITING')
    raise SystemExit

try:
    self.candle_end_time = time(hour=self.end_time_hours, minute=self.end_time_minutes)
except ValueError:
    self.logger.fatal('Error converting end time hours and minutes... EXITING')
    raise SystemExit
```

v. Strategy variables:

We create our own strategy variables other than the strategy parameter variables which will be used throughout the strategy.

eg:
self.main_order = None            # We save the entry order in this variable
self.stoploss_order = None        # We save the corresponding stoploss exit order of the entry order in this variable

We initialize the variables with a None value.

    !!! Note
            There could be more strategy variables required as per the strategy requirement. 

---

## 3. Initialize method

Unlike the ```init method```, this method gets called every day at the beginning of the day once the strategy is started.

Here the strategy variables that were initialized as None are again defined as dictionaries/lists except for the ```self.order_tag_manager```. 
Create a reference for ```OrderTagManager``` as shown below:

```self.order_tag_manager = OrderTagManager``` 

---

## 4. OrderTagManager

The ```self.order_tag_manager``` is used to store/remove the entry/exit orders. The ```self.order_tag_manager``` has following methods:

**i. add_order**: 

* Stores the order object for the given tags.

eg:

```self.order_tag_manager.add_order(_order, tags=[base_inst_str, entry_key])```

Here the ```_order``` is the order object stored inside the ```OrderTagManager``` for the tags ```base_inst_str``` and ```entry_key```.

**ii. get_orders**: 

* Retrieve the order(s) for the given tags.

eg:

```self.order_tag_manager.get_orders(tags=[base_inst_str, BrokerExistingOrderPositionConstants.ENTER, entry_key], ignore_errors=True)```

Here the order object retrieved from the ```OrderTagManager``` for the tags ```base_inst_str, BrokerExistingOrderPositionConstants.ENTER``` and ```entry_key```

**iii. remove_tags**: 

* Removes the tags stored in the ```OrderTagManager``` along with the orders related stored in that tag

eg:

```self.order_tag_manager.remove_tags(tags=entry_key)```

Here the ```entry_key``` tag is removed from the ```OrderTagManager```.

!!! Note

When the tag is removed the order objects stored in that tag are also removed but the same order objects would still be present in order tags.

**iv. remove_order**: 

* Remove the order(s) from the ```OrderTagManager``` for the given tag(s).

eg:

```self.order_tag_manager.remove_order(main_order)```

Here the ```main_order``` order object is removed from the ```OrderTagManager```.

!!! Note

The order object will be removed from all the tags ta

**v. get_internals**: 

* Returns the values i.e both the entry and exit orders stored inside the tags list.

---

## 5. Child instruments calculation

i. Fetch the LTP of the base instrument (instrument in the YAML).

```ltp = self.broker.get_ltp(self.underlying_instrument)```

ii. Get the ATM ITM and OTM lists of the child instrument based on the LTP:

```self.options_instruments_set_up_local(self.underlying_instrument, tradingsymbol_suffix, ltp)```

iii. Select a child instrument from the lists of ATM, ITM, and OTM based on the strike direction and no of strikes given for the child instrument. 

```child_instrument = self.get_child_instrument_details(self.underlying_instrument, tradingsymbol_suffix, strike_direction, no_of_strikes)```

---

## 6. Entry Methods

**i. strategy_select_instruments_for_entry:**

* In this method we process each instrument in the instruments bucket, if there is some entry condition to be checked then we create a ```get_entry_decision``` method 
that calculates the entry condition like a crossover or compares the latest value of the OHLC data or indicator data.


* When the order has to be placed we add the ```instrument``` to ```selectd_instruments_bucket``` and additional data related to the instrument that will be required while placing to the ```sideband_info```. This information is passed to the ```strategy_enter_position``` method

**ii. strategy_enter_position:**

* Here is where we actually place the entry order for which we calculate the quantity for the order to be placed. If the order is placed successfully we save the order in a class variable such that we can access the order object via the variable in the exit methods.

---

## 7. Exit Methods

**i. strategy_select_instruments_for_exit:**

* This method is called before the entry methods because in the case of delivery strategy we want to resume and exit previous day orders before we can place new entry orders.

* Here we place stoploss exit orders, target exit orders, and check for exit conditions for the open entry orders.

---

## 8. Other common methods

There are other methods that are used in the strategy:

**i. check_and_place_stoploss_order:**

This method is called in the ```strategy_select_instruments_for_exit``` when our entry order is open and we want to place a stoploss exit order for the same.

**ii. set_all_none:**

This method is called in the ```strategy_exit_position``` when our entry order has exited and we want to remove the order object from the ```self.main_order``` variable.

**iii. options_instruments_set_up_local**

This method is called in the ```strategy_select_instruments_for_entry``` to fetch the ATM, ITM, and OTM lists of the child instruments based on the LTP of the base instrument. 

**iv. get_child_instrument_details**

This method is called in the ```strategy_select_instruments_for_entry``` to fetch a single child instrument based on the no of strikes and strike direction.
        
---

## 9. Cleanup

i. Add comments and docstrings wherever possible to improve code readability.

ii. Once the strategy is completed perform O-I-L on the strategy code and remove unwanted imports, variables, and methods before delivering the code.**

---

To know more about a strategy from our given template, simply **check the first line of comment** in the code of that specific strategy.
You can even access them [here](https://algobulls.github.io/pyalgotrading/) in `Strategies` Section