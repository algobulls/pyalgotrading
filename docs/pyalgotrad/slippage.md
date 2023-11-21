## Slippage and Brokerage Parameters
In the `algobulls_connection.get_backtesting_report_pnl_table` function, you have the option to specify `slippage` and `brokerage` parameters to account for transaction costs and execution variations. These parameters allow you to fine-tune your backtesting results to better simulate real-world trading conditions.
### Slippage
- **Parameter Name:** `slippage_percent`
- **Type:** float
- **Default Value:** None
- **Definition:** Slippage is the difference between the expected execution price of a trade and the actual execution price. It often occurs due to market volatility and the time it takes to execute an order. Slippage can have a significant impact on trading results, and this parameter allows you to simulate it.
- **Explanation:** Imagine you're trading and placing an order at a specific price, but the market moves quickly. Slippage accounts for the price difference between what you expected and what you actually get. Use this parameter to make your backtesting experience more realistic.

### How to Use
To incorporate slippage into your backtesting, simply pass the desired values for `slippage_percent`, when calling the `algobulls_connection.get_backtesting_report_pnl_table` function. These parameters help you account for real-world trading costs and execution variations, making your backtesting results more realistic.

### Example
```python
import algobulls_connection
# Fetch PnL data for a trading strategy with custom slippage  settings
pnl_table = algobulls_connection.get_backtesting_report_pnl_table(
    strategy_code="your_strategy_code",
    show_all_rows=True,
    force_fetch=True,
    country='USA',
    slippage_percent=4.5,             # Adjust slippage percentage as needed
)
# Print the PnL table with custom slippage  settings
print(pnl_table)
```