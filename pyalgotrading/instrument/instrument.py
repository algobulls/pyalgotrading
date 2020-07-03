"""
Instrument Class
"""
from datetime import date


class Instrument:
    """
    Instrument Class
    """
    def __init__(self, segment, tradingsymbol, broker_token, tick_size, lot_size, expiry=None, strike_price=None):
        """
        Init method that is used while creating an object of this class
        Args:
            segment: segment
            tradingsymbol: trading symbol
            broker_token: alphnumeric token
            tick_size: tick size
            lot_size: lot size
            expiry: expiry date
            strike_price: strike amount / value
        """
        self.segment = segment
        self.exchange = self.segment.exchange
        self.tradingsymbol = tradingsymbol
        self.broker_token = broker_token
        self.tick_size = tick_size
        self.lot_size = lot_size
        self.expiry = expiry
        self.strike_price = strike_price

    def will_expire(self):
        """
        Returns expiry details
        Returns:
            a value containing the expiry date
        """
        return self.expiry

    def is_expired(self):
        """
        Returns whether expired or not
        Returns:
            True or False
        """
        if self.expiry:
            return date.today() > self.expiry
        else:
            return False
