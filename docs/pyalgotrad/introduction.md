# Introduction

---

This tutorial aims to help users practice and get familiar with the [Pyalgotrading](https://github.com/algobulls/pyalgotrading/) package, which is a Python-based algorithmic trading library. It allows you to create and execute your trading strategies on various financial instruments such as equities, futures, options, and more. To follow this tutorial, you will need to have an active and working [AlgoBulls](https://www.algobulls.com/) account, which is a platform for creating and testing trading strategies.

---
## [Prerequisites](prerequisites.md)

Before starting the tutorial, ensure that you have the following setup:

- An active and working [AlgoBulls](https://www.algobulls.com/) account
- Python IDE of your choice (if you want to code your own strategy)
- Jupyter Notebook (for points 2,3, and 4)

---

## Features
- Powered by the [AlgoBulls Platform](https://algobulls.com){target=_blank}
- Everything related to Algorithmic Trading Strategies!
    - Create & upload strategies on the [AlgoBulls Platform](https://algobulls.com){target=_blank}
    - Free pool of Strategies are available separately at [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool){target=_blank}!
    - Support for all 150+ Technical Indicators provided by [TA-Lib](https://pypi.org/project/TA-Lib/){target=_blank}
    - Support for multiple candlesticks patterns - Japanese OHLC, Renko, Heikin-Ashi, Linebreak
    - Support for multiple candle intervals - 1 minute, 3 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 1 day. 
    - Support for **MARKET**, **LIMIT**, **STOPLOSS-MARKET**, **STOPLOSS-LIMIT** orders
    - Support for **INTRADAY** and **DELIVERY** orders
- Support for **Backtesting**, **Paper Trading** and **Real Trading**

    - Currently supported [brokers](https://app.algobulls.com/user/brokerlogin){target=_blank} 
- Real-time Logs for Backtesting, Paper Trading and Real Trading
- Multiple real-time Reports available for Backtesting, Paper Trading and Real Trading - 
    - Profit-n-Loss report (PnL report)
    - Statistics of (PnL report)
    - Order History for each order with state transitions & timestamps
- Plot Candlestick charts using [plotly.py](https://github.com/plotly/plotly.py){target=_blank}
    
Backtesting, Paper Trading and Real Trading can be performed on the same strategy code base!

### Python 
- Python Support: `Python 3.10+`.
- Python Requirements: See [requirements.txt](https://github.com/algobulls/pyalgotrading/blob/master/requirements.txt){target=_blank}.
- We recommend you to use the latest version of Python (v3.10+) to enjoy better performance benefits, especially for pandas (v1.5.3). 

### Installation
Package can be easily installed using `pip` - 
```
pip install pyalgotrading
```

## Support / Getting Help
- *Bug Reporting / New Feature Request*: Please [create a new issue](https://github.com/algobulls/pyalgotrading/issues/new){target=_blank} here on GitHub.
- *Discussion Forum*: Discuss with our developers on this [forum](https://community.algobulls.com/c/github/pyalgotrading/42){target=_blank}
- *Additional Support*: If none of the above help, please contact [pushpak@algobulls.com](mailto:pushpak@algobulls.com){target=_blank}.


---
## Tutorial Steps

1. Code your own simple strategy using the Pyalgotrading package: In this step, you will use your Python IDE to code your own trading strategy using Pyalgotrading package. You can also use the ready-made strategy provided by the pyalgostrategypool package if you don't want to code your own.  

    ---

2. Upload your strategy to the [AlgoBulls](https://www.algobulls.com/) platform: After coding your strategy, you will need to upload it to the [AlgoBulls](https://www.algobulls.com/) platform. This can be done by creating a new strategy on the platform and then uploading your strategy file.  
    
    ---

3. Run Backtest / Paper Trade / Real Trade using your strategy: Once you have uploaded your strategy, you can run backtests, paper trades or real trades to see how your strategy performs. These can be done from the AlgoBulls platform itself.  
    
    ---

4. Fetch logs during runtime, see reports, view statistics, and see your order history: You can fetch the logs during runtime to monitor your strategy's performance and view reports and statistics to analyze its effectiveness. You can also view your order history to see the trades executed by your strategy.  
    
    ---

5. Check out the basic [structure](structure.md) of a strategy: Before coding your strategy, you can refer to the basic structure of a strategy provided by the Pyalgotrading package. This will give you an idea of the methods involved in the trading strategy and their flow.  
    
    ---

6. Reach out to [AlgoBulls Support](mailto:support@algobulls.com) for any queries: If you face any issues during the tutorial, you can reach out to the [AlgoBulls Support](mailto:support@algobulls.com)(mailto:support@algobulls.com) team for help.  

---

## Conclusion

In conclusion, this tutorial helps users get started with the Pyalgotrading package and create their own trading strategies. It also provides information on how to upload, run and monitor the strategies on the [AlgoBulls](https://www.algobulls.com/) platform. The tutorial aims to equip users with the necessary skills to create effective trading strategies using the Pyalgotrading package.

---

## Contribution Guidelines
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
