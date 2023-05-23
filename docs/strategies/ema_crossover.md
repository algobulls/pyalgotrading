# **EMA Crossover Strategy :**

The **EMA (Exponential Moving Average)** crossover strategy is a popular technical analysis approach used by traders to identify potential buying and selling signals in financial markets. It involves the use of two or more exponential moving averages of different time periods.

In this strategy, traders look for the crossover of two moving averages to determine entry and exit points for trades. Typically, a shorter-term EMA (such as the 20-day EMA) and a longer-term EMA (such as the 50-day EMA) are used. When the shorter-term EMA crosses above the longer-term EMA, it is considered a bullish signal and suggests a potential buying opportunity. Conversely, when the shorter-term EMA crosses below the longer-term EMA, it is seen as a bearish signal and indicates a potential selling opportunity.

![Flowchart](images/FlowChart.png "How does a Strategy work")

## **DECISION**

## **Initialise the Variables:**

1. The method begins by calling the **\_\_init\_\_** method of the parent class using **super().\_\_init\_\_(\*args, \*\*kwargs)**. This ensures that any initialization code in the parent class is executed.
2. The code retrieves the values of two strategy parameters, **TIMEPERIOD1** and **TIMEPERIOD2** , from the **strategy\_parameters** dictionary which are defined as strategy parameters section in strategy settings.
3. It performs assertions to validate the retrieved parameter values. It checks that both **timeperiod1** and **timeperiod2** are positive integers greater than zero. If any of these conditions fail, an assertion error is raised with an appropriate error message.
4. The code initializes the **main\_order** variable to None. This variable is likely used to store information about the main order of the strategy, such as the current position or status.

Overall, this code snippet sets up the initial state of the strategy object by retrieving and validating the required strategy parameters and initializing the **main\_order** variable.

## **Get the Crossover:**

The given code snippet presents a function named **get\_crossover\_value(self, instrument)** that calculates and returns a crossover value for a given instrument. Here is a summary of what the function does:

1. The function starts by calling the **get\_historical\_data()** method (a function called to retrieve the historical candle data of a given instrument and of given candle size) to retrieve historical data for the specified instrument. This data is used to calculate the exponential moving averages (EMAs) and perform the crossover analysis.
2. Using the historical data, the function computes two EMAs: **ema\_x** and **ema\_y**. The **ema\_x** is calculated based on the closing prices from the historical data using the time period specified by **self.timeperiod1**. Similarly, the **ema\_y** is calculated using the closing prices and the time period specified by **self.timeperiod2**. These EMAs are calculated using the **talib.EMA()** function, which is from a technical analysis library like **TA-Lib**.
3. The function then calls the **crossover()** method of the utils object (returns whether value\_1 has crossed value\_2 in upward direction or downward direction thus return 1, -1 or 0 if it is crossing upward, downward or no crossing respectively) with **ema\_x** and **ema\_y** as inputs. This method is a custom implementation that compares the two EMAs and determines if a crossover event has occurred. The **crossover\_value** variable is assigned the value returned by this method.
4. Finally, the function returns the **crossover\_value** , which represents the result of the crossover analysis between the two EMAs for the specified instrument.

In summary, the **get\_crossover\_value()** function retrieves historical data for a given instrument, calculates the EMAs based on the specified time periods, and determines the crossover value by comparing the EMAs. This function is an essential part of the strategy as it provides the crossover information used for making entry and exit decisions.

## **EXIT :**

## **Select Instruments for Exit:**

**strategy\_select\_instruments\_for\_exit(self, candle,**  **instruments\_bucket**** ):**

This function is responsible for selecting instruments from a given **instruments\_bucket** for which an exit action should be triggered. It iterates over each instrument in the **instruments\_bucket** and checks if there is a corresponding order in the **main\_order** dictionary for that instrument. If an order exists, it retrieves the crossover value for that instrument using the **get\_crossover\_value()** method. If the crossover value is either 1 or -1, indicating a specific condition for exiting the position, the instrument is added to the **selected\_instruments\_bucket** list, and a corresponding dictionary with the action set to 'EXIT' is added to the **sideband\_info\_bucket**. Finally, the function returns the **selected\_instruments\_bucket** and **sideband\_info\_bucket**.

## **Exit Position of Selected Instruments:**

**strategy\_exit\_position(self, candle, instrument,**  **sideband\_info**** ):**

This function is called for each instrument that requires an exit action, as determined by the **sideband\_info** received from the **strategy\_select\_instruments\_for\_exit()** function. If the action specified in **sideband\_info** is ' **EXIT**', it calls the **exit\_position()** method of the **main\_order** object associated with the instrument, indicating the exit of the position. It then sets the **main\_order** entry for that instrument to None, indicating that the position has been closed. Finally, the function returns True to indicate a successful exit. If the action is not 'EXIT', the function returns False to indicate that no exit was performed for the instrument.

In summary, these functions work together to identify instruments for which an exit action should be triggered based on certain conditions, and then execute the exit action by calling the appropriate methods and updating the **main\_order** dictionary.

## **ENTRY:**

## **Select Instruments for Entry:**

**strategy_select_instruments_for_entry(self, candle, instruments_bucket):**

This function is responsible for selecting instruments from a given **instruments\_bucket** for which an entry action should be triggered. It iterates over each instrument in the **instruments\_bucket** and retrieves the crossover value for that instrument using the **get\_crossover\_value()** method. If the crossover value is 1, indicating a specific condition for entering a long position, the instrument is added to the **selected\_instruments\_bucket** list, and a corresponding dictionary with the action set to 'BUY' is added to the **sideband\_info** \_bucket. If the crossover value is -1 and the strategy mode is set to **StrategyMode.INTRADAY** , indicating a condition for entering a short position in an intraday strategy, the instrument is added to the **selected\_instruments\_bucket** list, and a dictionary with the action set to ' **SELL**' is added to the **sideband\_info**** \_bucket **. Finally, the function returns the** selected\_instruments\_bucket **and** sideband\_info ****\_bucket**.

## **Enter Position of the Selected Instrument:**

**strategy\_enter\_position(self, candle, instrument, sideband\_info ):**

This function is called for each instrument that requires an entry action, as determined by the **sideband\_info** received from the **strategy\_select\_instruments\_for\_entry()** function. If the action specified in **sideband\_info** is 'BUY', it calculates the quantity (qty) for the order based on the number of lots and the instrument's lot size. It then creates a buy order using the **BuyOrderRegular()** method of the broker object, passing in the necessary parameters such as the instrument, order code, order variety, and quantity. The resulting order object is stored in the **main\_order** dictionary with the instrument as the key. Similarly, if the action is 'SELL' and the strategy mode is intraday, it calculates the quantity and creates a sell order using the **SellOrderRegular()** method. If the action is neither 'BUY' nor 'SELL', it raises a **SystemExit** exception with an error message indicating an invalid **sideband\_info** value. Finally, the function returns the order object associated with the instrument in the **main\_order** dictionary.

In summary, these functions work together to identify instruments for which an entry action should be triggered based on certain conditions, and then execute the entry action by creating the appropriate buy or sell order using the broker object and updating the **main\_order** dictionary with the resulting order object.