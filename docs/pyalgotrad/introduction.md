# pyalgotrading

## Introduction

Welcome to the **Pyalgotrading** Documentation – your guide to practising and acquainting yourself with the [pyalgotrading](https://github.com/algobulls/pyalgotrading/){target="_blank"} package. Pyalgotrading, built with Python, is an algorithmic trading library that empowers you to design and implement trading strategies on a variety of financial instruments, such as equities, futures, and options. To embark on your journey with Pyalgotrading, ensure you have an active [AlgoBulls](https://www.algobulls.com/){target="_blank"} account, a platform designed for creating and testing trading strategies.

## Key Features

- Fueled by the **AlgoBulls**
- Comprehensive Support for Algorithmic Trading Strategies:
  - Create & upload strategies seamlessly on the [AlgoBulls Platform](https://algobulls.com)
  - Access a range of strategies from the [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool)
  -  Over 150 Technical Indicators from [TA-Lib](https://pypi.org/project/TA-Lib/) at your disposal
  - Multiple candlestick patterns including Japanese OHLC, Renko, Heikin-Ashi, Linebreak
  - Support for varied candle intervals: 1 minute, 3 minutes, 5 minutes, and more
  - Diverse order types supported: **MARKET**, **LIMIT**, **STOPLOSS-MARKET**, **STOPLOSS-LIMIT**
  - Flexibility for both **INTRADAY** and **DELIVERY** orders
- Full Spectrum of Trading: **Backtesting**, **Paper Trading**, and **Real Trading**:
  - Currently supported with selected [brokers](https://app.algobulls.com/user/brokerlogin)
- Real-time Logs and Reports for Backtesting, Paper Trading, and Real Trading:
  - Detailed Profit and Loss reports (PnL report)
  - Insightful statistics derived from PnL report
  - Order History showcasing state transitions and timestamps
- Generate Candlestick charts using [plotly.py](https://github.com/plotly/plotly.py)

Execute Backtesting, Paper Trading, and Real Trading using the same strategy code base.

!!! Note "Prerequisites"
    Before you commence development, make sure to establish your workspace and gather all prerequisites as outlined [here](prerequisites.md).

## Support / Seeking Assistance

- **Bug Reporting / New Feature Request**: [Create a new issue](https://github.com/algobulls/pyalgotrading/issues/new) on GitHub.
- **Engage in Discussion**: Join fellow developers on the discussion [forum](https://community.algobulls.com/c/github/pyalgotrading/42).
- **Additional Support**: For further help, contact [pushpak@algobulls.com](mailto:pushpak@algobulls.com).

## Overview

1. [Check out the basic structure of a strategy](strategy_guides/structure.md): Before coding your strategy, refer to the basic structure guide provided by the Pyalgotrading package. This will help you understand the trading strategy methods and flow.

2. [Code your own simple strategy using the pyalgotrading package](https://github.com/algobulls/pyalgotrading/): Use your Python IDE to code your trading strategy using the pyalgotrading package. You can also use ready-made strategies from the pyalgostrategypool package if you prefer not to code your own.

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

See [CHANGELOG.md](https://github.com/algobulls/pyalgotrading/blob/master/CHANGELOG.md) for the changelog and [LICENSE](https://github.com/algobulls/pyalgotrading/blob/master/LICENSE) for the license.
