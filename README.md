# pyalgotrading

Official Python Package for Algorithmic Trading APIs powered by AlgoBulls!

### Features

- Powered by the [AlgoBulls Platform]([https://app.algobulls.com](https://algobulls.com/build/))
- Everything related to Algorithmic Trading Strategies!
    - Free pool of Strategies are available at [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool)!
    - Create & upload strategies easily on the cloud
    - Support for all 150+ Technical Indicators provided by [TA-Lib](https://pypi.org/project/TA-Lib/)
    - Support for multiple candlesticks patterns - Japanese OHLC, Renko, Heikin-Ashi, Linebreak
    - Support for multiple candle intervals - 1 minute, 3 minutes, 5 minutes, 10 minutes, 15 minutes, 30 minutes, 1 hour, 1 day.
    - Support for **Regular Orders**, **Bracket Orders** and **Cover Orders**
    - Support for **MARKET**, **LIMIT**, **STOPLOSS-LIMIT**, **STOPLOSS-MARKET** orders
    - Support for **INTRADAY** and **DELIVERY** orders
- Support for **Backtesting**
- Support for **Paper Trading**
- Support for **Live Trading** / **Real Trading**
- Support for multiple brokers for Live Trading. Check list of supported brokers [here](https://app.algobulls.com/user/brokerlogin).
- Real-time Logs for Backtesting, Paper Trading, Live Trading
- Multiple real-time Reports available for Backtesting, Paper Trading and Live Trading:
    - Profit-&-Loss report (P&L report)
    - Statistics Report
    - Order History Log for each order with state transitions & timestamps
    - Detailed analytics with charts
- Support for calculating Slippage
- Support for calculating Brokerage
- Support for importing external P&L table and generating analytics on the same
- Plot Candlestick charts using [plotly.py](https://github.com/plotly/plotly.py)

Backtesting, Paper Trading and Real Trading can be performed on the same strategy code base!

### Documentation

You can find the docs [here](https://algobulls.github.io/pyalgotrading/).

### Jupyter Notebooks

Easily access and use complete Jupyter Notebook for NASDSAQ and NSE markets [here](https://github.com/algobulls/pyalgotrading/tree/master/jupyter).
You can:
- Easily view them on the web using [nbviewer](https://nbviewer.org/), without installing Python or Jupyter Notebooks.
- Easily execute them on the web using [Binder](https://mybinder.org/), without installing Python or Jupyter Notebooks.
- Download and use them on your local machine, and installing Python & Jupyter Notebooks

### Python

- Python Support: `Python 3.8+`.
- Python Requirements: See [requirements.txt](https://github.com/algobulls/pyalgotrading/blob/master/requirements.txt).
- We recommend you to use the latest version of Python (v3.8+) to enjoy better performance benefits, especially for pandas.

### Installation

Package can be easily installed using `pip` -

```
pip install pyalgotrading
```

### Support / Getting Help

- *Bug Reporting / New Feature Request*: Please [create a new issue](https://github.com/algobulls/pyalgotrading/issues/new) here on GitHub.
- *Discussion Community*: [Slack](https://join.slack.com/t/algotradingninjas/shared_invite/zt-234npz3lu-A1f55maTr~j0tOIoxWA5hA) 
- *Additional Support*: If none of the above help, please contact [pushpak@algobulls.com](mailto:pushpak@algobulls.com).

### Contribution Guidelines

Here’s how we suggest you go about proposing a change to this project:

1. [Fork this project][fork] to your account.
2. [Create a branch][branch] for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr] from your fork’s branch to our `master` branch.

### Rewards

If you are interested in contributing to this repo, **pyalgotrading** or [**pyalgostrategypool**](https://github.com/algobulls/pyalgostrategypool), our official pool of FREE algorithmic trading strategies, please join our official [Slack](https://join.slack.com/t/algotradingninjas/shared_invite/zt-234npz3lu-A1f55maTr~j0tOIoxWA5hA) community.
You would be provided with credits for unlimited trading access on the AlgoBulls platform.


[fork]: https://help.github.com/articles/fork-a-repo/

[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository

[pr]: https://help.github.com/articles/using-pull-requests/

### Changelog

See [CHANGELOG.md](https://github.com/algobulls/pyalgotrading/blob/master/CHANGELOG.md).

### License

See [LICENSE](https://github.com/algobulls/pyalgotrading/blob/master/LICENSE).
