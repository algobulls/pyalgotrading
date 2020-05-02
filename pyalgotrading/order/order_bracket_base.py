from .order_base import OrderBase
from ..constants import BrokerOrderTypeConstants, BrokerOrderTransactionTypeConstants


class OrderBracketBase(OrderBase):
    def __init__(self, instrument, order_transaction_type, order_code, order_variety, quantity, price=None, trigger_price=None, stoploss_trigger=None, target_trigger=None, trailing_stoploss_trigger=None):
        self.instrument = instrument
        self.order_transaction_type = order_transaction_type
        self.order_type = BrokerOrderTypeConstants.BROKER_ORDER_TYPE_BRACKET
        self.order_code = order_code
        self.order_variety = order_variety
        self.quantity = quantity
        self.price = price
        self.trigger_price = trigger_price
        self.target_trigger = target_trigger
        self.stoploss_trigger = stoploss_trigger
        self.trailing_stoploss_trigger = trailing_stoploss_trigger

    def is_closed(self):
        # This is a dummy function with a sole purpose of mimicing the signature of the actual function on the AlgoBulls platform, as described in the documentation.
        pass


class BuyOrderBracket(OrderBracketBase):
    def __init__(self, instrument, order_code, order_variety, quantity, price=None, trigger_price=None, stoploss_trigger=None, target_trigger=None, trailing_stoploss_trigger=None):
        super().__init__(instrument=instrument, order_transaction_type=BrokerOrderTransactionTypeConstants.BROKER_ORDER_TRANSACTION_TYPE_BUY, order_code=order_code, order_variety=order_variety, quantity=quantity, price=price,
                         trigger_price=trigger_price, stoploss_trigger=stoploss_trigger, target_trigger=target_trigger, trailing_stoploss_trigger=trailing_stoploss_trigger)


class SellOrderBracket(OrderBracketBase):
    def __init__(self, instrument, order_code, order_variety, quantity, price=None, trigger_price=None, stoploss_trigger=None, target_trigger=None, trailing_stoploss_trigger=None):
        super().__init__(instrument=instrument, order_transaction_type=BrokerOrderTransactionTypeConstants.BROKER_ORDER_TRANSACTION_TYPE_SELL, order_code=order_code, order_variety=order_variety, quantity=quantity, price=price,
                         trigger_price=trigger_price, stoploss_trigger=stoploss_trigger, target_trigger=target_trigger, trailing_stoploss_trigger=trailing_stoploss_trigger)
