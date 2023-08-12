# Welcome to `pyalgotrading` Documentation!

#### **Official Python Package for Algorithmic Trading APIs powered by AlgoBulls!**

### Visit the Tutorial
- Tutorial:
    - [Pyalgotrading Comprehensive Guide](pyalgotrading_comprehensive_guide.md)
    - Setup your workspace
      - [Prerequisites](prerequisites.md)
      - [Requirements](python_packages.md)
    
    - Strategy Execution and Creation:
        - [Basic Structure of a Strategy](structure.md)
        - Create your Strategy
          - [Normal Strategy](../strategies/common_regular_strategy.md)
          - [Options Strategy](../strategies/common_options_strategy.md)
        - [Execute and Test your Strategy](testing.md)

### Features
- Powered by the [AlgoBulls Platform](https://algobulls.com)
- Everything related to Algorithmic Trading Strategies!
    - Create & upload strategies on the [AlgoBulls Platform](https://algobulls.com)
    - Free pool of Strategies are available separately at [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool)!
    - Support for all 150+ Technical Indicators provided by [TA-Lib](https://mrjbq7.github.io/ta-lib/index.html)
    - Support for multiple candlesticks patterns - Japanese OHLC, Renko, Heikin-Ashi, Linebreak
    - Support for multiple candle intervals - 1 minute, 3 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 1 day. 
    - Support for **MARKET**, **LIMIT**, **STOPLOSS-MARKET**, **STOPLOSS-LIMIT** orders
    - Support for **INTRADAY** and **DELIVERY** orders
- Support for **Backtesting**, **Paper Trading** and **Real Trading**

    - Currently supported [brokers](https://app.algobulls.com/user/brokerlogin) 
- Real-time Logs for Backtesting, Paper Trading and Real Trading
- Multiple real-time Reports available for Backtesting, Paper Trading and Real Trading - 
    - Profit-n-Loss report (PnL report)
    - Statistics of (PnL report)
    - Order History for each order with state transitions & timestamps
- Plot Candlestick charts using [plotly.py](https://github.com/plotly/plotly.py)
    
Backtesting, Paper Trading and Real Trading can be performed on the same strategy code base!

### Python 
- Python Support: `Python 3.10+`.
- Python Requirements: See [requirements.txt](https://github.com/algobulls/pyalgotrading/blob/master/requirements.txt).
- We recommend you to use the latest version of Python (v3.10+) to enjoy better performance benefits, especially for pandas (v1.5.3). 

### Installation
Package can be easily installed using `pip` - 
```
pip install pyalgotrading
```

### Support / Getting Help
- *Bug Reporting / New Feature Request*: Please [create a new issue](https://github.com/algobulls/pyalgotrading/issues/new) here on GitHub.
- *Discussion Forum*: Discuss with our developers on this [forum](https://community.algobulls.com/c/github/pyalgotrading/42)
- *Additional Support*: If none of the above help, please contact [pushpak@algobulls.com](mailto:pushpak@algobulls.com).

### Contribution Guidelines
Here’s how we suggest you go about proposing a change to this project:

1. [Fork this project][fork] to your account.
2. [Create a branch][branch] for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr] from your fork’s branch to our `master` branch.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

### Changelog
See [CHANGELOG.md](https://github.com/algobulls/pyalgotrading/blob/master/CHANGELOG.md).

### License
See [LICENSE](https://github.com/algobulls/pyalgotrading/blob/master/LICENSE).
