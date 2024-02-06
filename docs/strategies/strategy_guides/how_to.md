### Fetch Last Traded Price (LTP) of an Instrument

To fetch the Last Traded Price (LTP) of any instrument, use the following method:

```python
self.broker.get_ltp(instrument)
```

This method retrieves the last traded price of the specified instrument.

---

### Access Attributes of an Instrument Object

An instrument object typically contains various attributes providing information about the instrument:

- `exchange`: Exchange on which the instrument is listed.
- `expiry`: Expiration date of the instrument (applicable for derivatives).
- `lot_size`: Number of units in a single lot of the instrument.
- `strike_price`: Strike price of the instrument (applicable for options).
- `segment`: Trading segment of the instrument.
- `tradingsymbol`: Unique trading symbol of the instrument.
- `tick_size`: Minimum price movement (tick) of the instrument.

To access these attributes, use the following notation:

```python
instrument.exchange
instrument.expiry
instrument.lot_size
instrument.strike_price
instrument.segment
instrument.tradingsymbol
instrument.tick_size
```

---

### Fetch Different Types of Instruments

To fetch different types of instruments, use the `get_instruments_filtered` method:

Method Signature:
```python
self.broker.get_instruments_filtered(segment, tradingsymbol_exact=None, tradingsymbol_prefix=None, tradingsymbol_suffix=None, expiry=None)
```
Example:
```python
instruments = self.broker.get_instruments_filtered(segment='NSE_FO', tradingsymbol_prefix='NIFTY', expiry='2024-01-04')
```

This example fetches equity instruments with a trading symbol prefix of 'NIFTY' and an expiry date of 4th January, 2024.

---
!!! tip "Note"
    The above three subsections are adequate for implementing your own logic for an options strategy.

### Access Attributes of an Order Object

An order object typically contains various attributes providing information about the order:

- `entry_price`: Entry price of the order.
- `id`: AlgoBulls specific alphanumeric order ID.
- `instrument`: Instrument for which the order is placed.
- `order_code`: Code for the order type (INTRADAY/DELIVERY).
- `order_time`: Time at which the order is placed.
- `order_transaction_type`: Type of transaction (BUY/SELL).
- `order_type`: Type of order (REGULAR/BRACKET/COVER).
- `order_variety`: Variety of the order (MARKET, LIMIT, STOPLOSS_MARKET, STOPLOSS_LIMIT).
- `position`: Position (ENTER/EXIT).
- `price`: Price of the order.
- `quantity`: Order quantity.
- `quantity_pending`: Quantity that is currently pending.
- `trigger_price`: Trigger price of the order.

To access these attributes, use the following notation:
```python
order.entry_price
order.id
order.instrument
order.order_code
order.order_time
order.order_transaction_type
order.order_type
order.order_variety
order.position
order.price
order.quantity
order.quantity_pending
order.trigger_price
```


