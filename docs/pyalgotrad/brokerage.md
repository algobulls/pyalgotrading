### Brokerage

- **Parameter Name:** `broker_commission_percentage`
- **Type:** float
- **Default Value:** None
- **Definition:** Brokerage is the fee charged by your broker for executing a trade. It's usually a percentage of the trade value. The `broker_commission_percentage` parameter lets you specify the brokerage fee as a percentage.
- **Explanation:** Brokers charge a fee for executing your trades, and this fee is often a percentage of your trade amount. You can adjust this parameter to match the fees your broker charges.

- **Parameter Name:** `broker_commission_price`
- **Type:** float
- **Default Value:** None
- **Definition:** The `broker_commission_price` parameter allows you to specify a fixed broker fee per trade. This fee is added on top of the percentage-based brokerage. It accounts for any flat fees associated with your trades.
- **Explanation:** In addition to the percentage-based fees, some brokers charge a fixed fee for every trade. Use this parameter to include those fixed fees in your backtesting calculations.

### How to Use
To incorporate slippage and brokerage into your backtesting, simply pass the desired values for `slippage_percent`, `broker_commission_percentage`, and `broker_commission_price` when calling the `algobulls_connection.get_backtesting_report_pnl_table` function. These parameters help you account for real-world trading costs and execution variations, making your backtesting results more realistic.

- **Note:** When both `broker_commission_percentage` and `broker_commission_price` are provided, the function will automatically calculate the brokerage cost using both parameters and select the option that results in the lower brokerage cost. This ensures that you pay the minimum brokerage fees for your trades.

### Example
```python
import algobulls_connection
# Fetch PnL data for a trading strategy with custom slippage and brokerage settings
pnl_table = algobulls_connection.get_backtesting_report_pnl_table(
    strategy_code="your_strategy_code",
    show_all_rows=True,
    force_fetch=True,
    country='USA',
    broker_commission_percentage=1.5,  # Adjust brokerage percentage as needed
    broker_commission_price=0.3,      # Adjust fixed brokerage cost as needed
    slippage_percent=4.5,             # Adjust slippage percentage as needed
)
# Print the PnL table with custom slippage and brokerage settings
print(pnl_table)
```