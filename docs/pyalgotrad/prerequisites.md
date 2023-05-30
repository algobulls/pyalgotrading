# Prerequisites

---
You will need the following to perform this tutorial:

1. **AlgoBulls Account ([Link](https://www.algobulls.com/))** - You will need this account to upload and test your strategies. The account needs to be setup with the proper risk management values and a bound broker before any trades can be executed. Make sure the account is properly setup or contact [AlgoBulls Support](mailto:support@algobulls.com) for any help.

    ---

2. **Python 3.7+ ([Link](https://www.python.org/downloads/))** - The AlgoBulls platform can run all strategies that conform to Python 3.7 and above. 

    ---

3. **A Python IDE of your choice, like Pycharm ([Link](https://www.jetbrains.com/pycharm/download/))** - As mentioned in the [Introduction], this tutorial will demonstrate the pyalgotrading package by implementing the Simple Moving Average Crossover Strategy for Regular Orders. You will make this strategy as a separate python file, and the PyCharm Community Edition IDE is enough for this purpose. If you are already using a Python IDE of your choice, you may skip this step. 

    ---

4. **TA-Lib Package ([Link](https://mrjbq7.github.io/ta-lib/install.html))** - This package encompasses all Technical Indicators used in Technical Analysis by strategists. You will need this package to compute Moving Average (SMA) for the example.

    ---

5. **pyalgotrading Package ([Link](https://pypi.org/project/pyalgotrading/))** - This package has all the necessary classes to create strategies. For the SMA strategy, you will subclass your class from the StrategyBase class which is present in this package.

    ---

6. **Jupyter Notebook ([Link](https://jupyter.org/install))** - You will use a Jupyter Notebook to connect to the AlgoBulls platform. You will upload the strategy, test your strategy (Backtesting, Paper Trading or Real Trading), and fetch logs using the notebook.

    ---

!!! Tips
    * It is a good idea to set up a virtual environment first
    * Install Python 3.7+
    * Once Python is installed, most packages are easily installed in your venv using `pip install` command
    * `pip install TA-Lib`
    * `pip install pyalgotrading`
    * `pip install jupyterlab`

---