# Introduction

This documentation aims to help users practice and get familiar with the [Pyalgotrading](https://github.com/algobulls/pyalgotrading/) package. Pyalgotrading is a Python-based algorithmic trading library that allows you to create and execute trading strategies on various financial instruments like equities, futures, and options. To start developing with Pyalgotrading, you'll need an active and working [AlgoBulls](https://www.algobulls.com/) account, a platform for creating and testing trading strategies.

## Features

- Powered by the [AlgoBulls Platform](https://algobulls.com)
- Everything related to Algorithmic Trading Strategies:
  - Create & upload strategies on the [AlgoBulls Platform](https://algobulls.com)
  - Free pool of strategies available at [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool)
  - Support for over 150 Technical Indicators from [TA-Lib](https://pypi.org/project/TA-Lib/)
  - Support for various candlestick patterns like Japanese OHLC, Renko, Heikin-Ashi, Linebreak
  - Support for multiple candle intervals - 1 minute, 3 minutes, 5 minutes, and more
  - Support for order types like **MARKET**, **LIMIT**, **STOPLOSS-MARKET**, **STOPLOSS-LIMIT**
  - Support for both **INTRADAY** and **DELIVERY** orders
- Support for **Backtesting**, **Paper Trading**, and **Real Trading**:
  - Currently supported [brokers](https://app.algobulls.com/user/brokerlogin)
- Real-time Logs and Reports for Backtesting, Paper Trading, and Real Trading:
  - Profit and Loss report (PnL report)
  - Statistics of PnL report
  - Order History with state transitions and timestamps
- Plot Candlestick charts using [plotly.py](https://github.com/plotly/plotly.py)

You can perform Backtesting, Paper Trading, and Real Trading on the same strategy code base.

!!! Note "Prerequisites"
    Before you start development, make sure you've set up your workspace and gathered all the prerequisites as described [here](prerequisites.md).

## Support / Getting Help

- **Bug Reporting / New Feature Request**: [Create a new issue](https://github.com/algobulls/pyalgotrading/issues/new) on GitHub.
- **Discussion Forum**: Join the discussion with developers on this [forum](https://community.algobulls.com/c/github/pyalgotrading/42).
- **Additional Support**: If you need further assistance, contact [pushpak@algobulls.com](mailto:pushpak@algobulls.com).

## Overview

1. [Check out the basic structure of a strategy](strategy_guides/structure.md): Before coding your strategy, refer to the basic structure guide provided by the Pyalgotrading package. This will help you understand the trading strategy methods and flow.

2. Code your own simple strategy using the Pyalgotrading package: Use your Python IDE to code your trading strategy using the Pyalgotrading package. You can also use ready-made strategies from the pyalgostrategypool package if you prefer not to code your own.

3. [Upload your strategy to the platform](upload.md): After coding your strategy, upload it to the [AlgoBulls](https://www.algobulls.com/) platform by creating a new strategy and uploading the file.

4. [Run Backtest / Paper Trade / Real Trade using your strategy](testing.md/#submit-a-job): Once your strategy is uploaded, run backtests, paper trades, or real trades on the AlgoBulls platform to evaluate its performance.

5. [Fetch logs during runtime, view reports and statistics, see your order history](testing.md/#fetch-logs): Monitor your strategy's performance by fetching runtime logs, viewing reports and statistics, and checking your order history to see executed trades.

6. Reach out to [AlgoBulls Support](mailto:support@algobulls.com) for any queries: If you encounter issues during the tutorial, contact the [AlgoBulls Support](mailto:support@algobulls.com) team for assistance.

## Conclusion

This documentation helps users get started with the Pyalgotrading package and creating their own trading strategies. It also guides users on uploading, running, and monitoring strategies on the [AlgoBulls](https://www.algobulls.com/) platform. The tutorial aims to equip users with the skills needed to create effective trading strategies using Pyalgotrading.

## Contribution Guidelines

1. [Fork this project][fork]{target=_blank} to your account.
2. [Create a branch][branch]{target=_blank} for the change you intend to make.
3. Make your changes to your fork.
4. [Send a pull request][pr]{target=_blank} from your fork’s branch to our `master` branch.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

See [CHANGELOG.md](https://github.com/algobulls/pyalgotrading/blob/master/CHANGELOG.md) for the changelog and [LICENSE](https://github.com/algobulls/pyalgotrading/blob/master/LICENSE) for the license.
