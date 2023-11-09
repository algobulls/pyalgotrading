# pyalgotrading

## Introduction

Welcome to the **Pyalgotrading** Documentation – your guide to practising and acquainting yourself with the [pyalgotrading](https://github.com/algobulls/pyalgotrading/){target="_blank"} package. Pyalgotrading, built with Python, is an algorithmic trading library that empowers you to design and implement trading strategies on a variety of financial instruments, such as equities, futures, and options. To embark on your journey with Pyalgotrading, ensure you have an active [AlgoBulls](https://www.algobulls.com/){target="_blank"} account, a platform designed for creating and testing trading strategies.

## Key Features

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

!!! Note "Prerequisites"
    Before you commence development, make sure to establish your workspace and gather all prerequisites as outlined [here](prerequisites.md).

## Support / Seeking Assistance

- **Bug Reporting / New Feature Request**: [Create a new issue](https://github.com/algobulls/pyalgotrading/issues/new) on GitHub.
- **Engage in Discussion**: Join fellow developers on the discussion [forum](https://community.algobulls.com/c/github/pyalgotrading/42).
- **Additional Support**: For further help, contact [support@algobulls.com](mailto:support@algobulls.com).

## Overview

1. [Check out the basic structure of a strategy](../strategies/strategy_guides/common_strategy_guide.md): Before coding your strategy, refer to the basic structure guide provided by the Pyalgotrading package. This will help you understand the trading strategy methods and flow.

2. [Code your own simple strategy using the pyalgotrading package](prerequisites.md): Use your Python IDE to code your trading strategy using the pyalgotrading package. You can also use ready-made strategies from the pyalgostrategypool package if you prefer not to code your own.

3. [Upload your strategy to the platform](upload.md): Upon coding your strategy, upload it to the AlgoBulls platform by crafting a new strategy and uploading the corresponding file.

4. [Run Backtest / Paper Trade / Real Trade with your strategy](testing.md/#submit-a-job):  Once uploaded, initiate backtests, paper trades, or real trades on the AlgoBulls platform to evaluate its performance.

5. [Retrieve real-time logs, review reports and stats, and inspect order history](testing.md/#fetch-logs):Monitor your strategy's performance by fetching runtime logs, examining reports and statistics, and reviewing your order history to track executed trades.

6. [Reach out to AlgoBulls Support for any queries](mailto:support@algobulls.com): If you encounter issues during the tutorial, contact the AlgoBulls Support team for assistance.

## Conclusion

This documentation serves as your launchpad into the Pyalgotrading package and the creation of your trading strategies. It also steers you through the process of uploading, executing, and monitoring strategies on the AlgoBulls platform. Our goal is to equip you with the expertise needed to craft effective trading strategies using Pyalgotrading.

## Contribution Guidelines

1. [Fork this project][fork]{target=_blank} to your account.
2. [Create a branch][branch]{target=_blank} for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr]{target=_blank} from your fork’s branch to our `master` branch.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

