# Frequently Encountered Errors

### Execution time exceeded timeout_duration duration of 60 sec.

#### Possible Causes

 - **Historical Data Fetching Duration:**
    
    Fetching historical data may take longer, especially if the duration is set to a large number of days.

 - **Suboptimal Decision-Making Logic:**
    
    The decision-making logic might be suboptimal, leading to increased processing time.

 - **Sequential Execution Approach:**
    
    A sequential approach of fetching historical data and then making the decisions in case of multiple instruments can contribute to delays.

 - **Real-Time Calculations:**
    
    If there are calculations that could be pre-conditioned or pre-calculated before the market opens, optimizing real-time calculations might help.

#### Solutions

 - **Optimize Historical Data Fetching:**
    
    Consider reducing the number of days for which historical data is fetched. A shorter duration, like 5 days, can be a reasonable compromise.

    ```python
    @staticmethod
    def get_historical_data_duration():
        return 5
    ```

 - **Optimize the Decision-Making logic:**

    Revisit your strategy logic and check if any code block can be optimized.

 - **Batch Processing for Decision-Making:**
    
    In case of multiple instruments, lets say you are fetching the historical data for the instrument, and have implemented the decision-making logic for whether this instrument should get selected for order placement or not. Once this is done, you repeat the same process for the next instrument. Instead of a sequential approach, try fetching historical data for all instruments in one loop and then making decisions for all instruments in another loop.

 - **Pre-Calculate Conditions:**
    
    Identify conditions that can be pre-calculated before the market opens. Adjust the strategy start time to accommodate these pre-calculations. If certain conditions can be chcked before the market starts, set the trading start time of the strategy to a value before the market start time. Add specific checks inside the strategy to ensure that the actual order placement, etc. are executed after the market starts.