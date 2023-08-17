# Python Packages and Requirements

---

### Once your Prerequisites are ready, you need to make sure all the below packages are installed properly in your environment

- **[Pyalgotrading Package](https://pypi.org/project/pyalgotrading/){target=_blank}** (version: latest):  
   This package has all the necessary classes to create strategies. For the SMA strategy, you will subclass your class from the StrategyBase class which is present in this package.
   ``` 
      pip3 install pyalgotrading
   ```
  
    ---

- **[TA-Lib Package](https://pypi.org/project/TA-Lib/){target=_blank}** (version: 0.4.27):  
   This package encompasses all Technical Indicators used in Technical Analysis by strategists. You will need this package to compute Moving Average (SMA) for the example.

    ```
       python -m pip install TA-Lib
    ```
    !!! warning
         * If you face any error while installing this package, I recommend you to check their [documentation](https://pypi.org/project/TA-Lib/){target=_blank} and follow their steps for installation.
  
   ---

- **[Pandas Package](https://pandas.pydata.org/pandas-docs/version/1.5.3/getting_started/index.html){target=_blank}** (version: 1.5.3):    
   This is a package used for data-manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series. This will help you to operate on the profit and loss data, it will also assist you to operate on historical data which will be fetched inside the strategy.  
   ```
    pip3 install pandas==1.5.3
   ```

   ---

- **[QuantStats Package](https://github.com/ranaroussi/quantstats){target=_blank}** (version: 0.0.59):  
   This library performs portfolio profiling, allowing quants and portfolio managers to understand their performance better by providing them with in-depth analytics and risk metrics. It is used to generate the plots to visualize and generate analytics of your returns.
   ```
    pip3 install quantstats==0.0.59
   ```
