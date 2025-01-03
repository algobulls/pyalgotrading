# Options Strategy Structure

!!! Links
    - **[Code Structure of Strategy (workflow of a strategy)](structure.md)**

## 1. Initial steps

1. ### Naming a Class
eg: For the above strategy name the class name would be:
    ```
    StrategyOptionsEMACrossover(StrategyOptionsBaseV2)
    ```

    !!! Tips "Coding Conventions"
            * Make a class with the same name as the file name
            * Make sure the first letter of each word is in uppercase and the initials should be in uppercase as well.
            * If the class name includes indicator names like EMA, SMA, and VWAP the name should be in uppercase in the class name but not in the file name.
            * Every options strategy is a child class of the StrategyOptionsBaseV2 class.

2. ### Naming your Strategy
This name will be displayed in your **My Coded Strategies** in Phoenix Web, and it will also be the **strategy_name** when you are fetching all strategies in pyalgotrading.  
Inside your strategy class, you can write your first parameter as `name`.
    ```
    name = 'options_ema_crossover'
    ```
---

## 2. Init method

This method gets called only once when the strategy is started.

1. ### Strategy info

    In the __init__ method add the line given below
    ```
    super().__init__(*args, **kwargs)
    ``` 

2. ### Parameter creation

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
    !!! Note
          * The parameter names and the number of parameters may change for different strategies.

4. ### Start time and End time creation
Adding Start and End time is useful when you want to define a timerange between which the strategy will be running each day.  
Add the below code to calculate the strategy start time and end time, from the `strategy_parameters`.

    try:
    ```
        self.candle_start_time = time(hour=self.start_time_hours, minute=self.start_time_minutes)
    except ValueError:
        self.logger.fatal('Error converting start hours and minutes... EXITING')
        raise SystemExit
    ```
    try:
    ```
        self.candle_end_time = time(hour=self.end_time_hours, minute=self.end_time_minutes)
    except ValueError:
        self.logger.fatal('Error converting end time hours and minutes... EXITING')
        raise SystemExit
    ```

5. ### Strategy variables

    We create our own strategy variables other than the strategy parameter variables which will be used throughout the strategy.
    
    eg:
    ```
    self.main_order = None            # We save the entry order in this variable
    self.stoploss_order = None        # We save the corresponding stoploss exit order of the entry order in this variable
    ```   
    We initialize the variables with a None value.
        !!! Note
                There could be more strategy variables required as per the strategy requirement. 

---

## 3. Initialize method

Unlike the ```init method```, this method gets called every day at the beginning of the day once the strategy is started.

Here the strategy variables that were initialized as None are again defined as dictionaries/lists except for the ```self.order_tag_manager```. 
Create a reference for ```OrderTagManager``` as shown below:

```
self.order_tag_manager = OrderTagManager
``` 

---

## 4. OrderTagManager

The ```self.order_tag_manager``` is used to store/remove the entry/exit orders. The ```self.order_tag_manager``` has the following methods:

1. ### **add_order**  
    * Stores the order object for the given tags.
    eg:
    
    ```
    self.order_tag_manager.add_order(_order, tags=[base_inst_str, entry_key])
    ```
    
    * Here the ```_order``` is the order object stored inside the ```OrderTagManager``` for the tags ```base_inst_str``` and ```entry_key```.

2. ### **get_orders**
    * Retrieve the order(s) for the given tags.

    eg:
    
    ```
    self.order_tag_manager.get_orders(tags=[base_inst_str, BrokerExistingOrderPositionConstants.ENTER, entry_key], ignore_errors=True)
    ```
    
    * Here the order object retrieved from the ```OrderTagManager``` for the tags ```base_inst_str, BrokerExistingOrderPositionConstants.ENTER``` and ```entry_key```

3. ### **remove_tags**
    * Removes the tags stored in the ```OrderTagManager``` along with the orders related stored in that tag

    eg:
    
    ```
    self.order_tag_manager.remove_tags(tags=entry_key)
    ```
    
    Here the ```entry_key``` tag is removed from the ```OrderTagManager```.

    !!! Note
        When the tag is removed the order objects stored in that tag are also removed but the same order objects would still be present in order tags.

4. ### **remove_order**

    * Remove the order(s) from the ```OrderTagManager``` for the given tag(s).
    
    eg:
    
    ```
    self.order_tag_manager.remove_order(main_order)
    ```
    Here the ```main_order``` order object is removed from the ```OrderTagManager```.

    !!! Note
        The order object will be removed from all the tags ta

5. ### **get_internals**
    Returns the values i.e. both the entry and exit orders stored inside the tags list.

---

## 5. Child instruments calculation

1. ### **get_ltp** 
    Fetch the ltp of the base instrument (instrument set while executing strategy)
    ```
    ltp = self.broker.get_ltp(self.underlying_instrument)
    ```

2. ### **options_instruments_set_up_local**
   Get the ATM ITM and OTM lists of the child instrument based on the LTP
    ```
    self.options_instruments_set_up_local(self.underlying_instrument, tradingsymbol_suffix, ltp)
    ```

3. ### **get_child_instrument_details**
   Select a child instrument from the lists of ATM, ITM, and OTM based on the strike direction and no of strikes given for the child instrument
    ```
    child_instrument = self.get_child_instrument_details(self.underlying_instrument, tradingsymbol_suffix, strike_direction, no_of_strikes)
    ```

---

## 6. Entry Methods

1. ### **strategy_select_instruments_for_entry**
    * In this method we process each instrument in the instruments bucket, if there is some entry condition to be checked then we create a ```get_entry_decision``` method 
    that calculates the entry condition like a crossover or compares the latest value of the OHLC data or indicator data.

    * When the order has to be placed we add the ```instrument``` to ```selectd_instruments_bucket``` and additional data related to the instrument that will be required while placing to the ```sideband_info```. This information is passed to the ```strategy_enter_position``` method

2. ### **strategy_enter_position**

    * Here is where we actually place the entry order for which we calculate the quantity for the order to be placed. If the order is placed successfully we save the order in a class variable such that we can access the order object via the variable in the exit methods.

---

## 7. Exit Methods

1. ### **strategy_select_instruments_for_exit**
    * This method is called before the entry methods because in the case of delivery strategy we want to resume and exit previous day orders before we can place new entry orders.
    * Here we place stoploss exit orders, target exit orders, and check for exit conditions for the open entry orders.

2. ### **strategy_exit_position**
    * Here is where we actually place the exit order for where we exit the order which was placed during entry. If the order is placed successfully we clear the order in a class variable such that we can add new orders to the vacant place in variable in the entry methods.

---

## 8. Other common methods

There are other methods that are used in the strategy:

1. ### **check_and_place_stoploss_order**

    This method is called in the ```strategy_select_instruments_for_exit``` when our entry order is open, and we want to place a stoploss exit order for the same.

2. ### **set_all_none**

    This method is called in the ```strategy_exit_position``` when our entry order has exited, and we want to remove the order object from the ```self.main_order``` variable.

3. ### **options_instruments_set_up_local**

    This method is called in the ```strategy_select_instruments_for_entry``` to fetch the ATM, ITM, and OTM lists of the child instruments based on the LTP of the base instrument. 

4. ### **get_child_instrument_details**

    This method is called in the ```strategy_select_instruments_for_entry``` to fetch a single child instrument based on the no of strikes and strike direction.
        
---

## 9. Cleanup

1. Add comments and docstrings wherever possible to improve code readability.
2. Once the strategy is completed you can optimize imports, give proper indentation and proper formatting to the strategy code and remove unwanted imports, variables, and methods before delivering the code.

---

## 10. Check out our docs for developed **Options** strategies 
- [Options Bear Call Ladder](../../strategies/options_bear_call_ladder.md){target=_blank}
- [Options Bear Put Ladder](../../strategies/options_bear_put_ladder.md){target=_blank}
- [Options Bull Call Ladder](../../strategies/options_bull_call_ladder.md){target=_blank}
- [Options Bull Put Ladder](../../strategies/options_bull_put_ladder.md){target=_blank}
- [Options Long Iron Butterfly](../../strategies/options_long_iron_butterfly.md){target=_blank}
- [Options Straddle](../../strategies/options_straddle.md){target=_blank}
- [Options Strangle](../../strategies/options_strangle.md){target=_blank}



!!! Tip 
     To know more about a strategy from our given template, simply **check the first line of comment** in the code of that specific strategy.  


