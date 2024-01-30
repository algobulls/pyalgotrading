### Fetch Last Traded Price (LTP) of an Instrument

To fetch the Last Traded Price (LTP) of any instrument, use the following method:

```python
self.broker.get_ltp(instrument)
```

This method retrieves the last traded price of the specified instrument.

---

### Access Attributes of an Instrument Object

An instrument object typically contains various attributes providing information about the instrument:

- `segment`: Trading segment of the instrument.
- `exchange`: Exchange on which the instrument is listed.
- `tradingsymbol`: Unique trading symbol of the instrument.
- `tick_size`: Minimum price movement (tick) of the instrument.
- `lot_size`: Number of units in a single lot of the instrument.
- `expiry`: Expiration date of the instrument (applicable for derivatives).
- `strike_price`: Strike price of the instrument (applicable for options).

To access these attributes, use the following notation:

```python
instrument.segment
instrument.exchange
instrument.tradingsymbol
instrument.tick_size
instrument.lot_size
instrument.expiry
instrument.strike_price
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


