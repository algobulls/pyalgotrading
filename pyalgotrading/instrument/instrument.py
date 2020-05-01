from datetime import date


class Instrument:

    def __init__(self, segment, tradingsymbol, broker_token, tick_size, lot_size, expiry=None, strike_price=None):
        self.segment = segment
        self.exchange = self.segment.exchange
        self.tradingsymbol = tradingsymbol
        self.broker_token = broker_token
        self.tick_size = tick_size
        self.lot_size = lot_size
        self.expiry = expiry
        self.strike_price = strike_price

    def will_expire(self):
        return self.expiry

    def is_expired(self):
        if self.expiry:
            return date.today() > self.expiry
        else:
            return False
