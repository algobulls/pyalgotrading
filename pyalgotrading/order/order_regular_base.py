from .order_base import OrderBase
from ..constants import BrokerOrderTypeConstants, BrokerOrderTransactionTypeConstants


class OrderRegularBase(OrderBase):
    def __init__(self, instrument, order_transaction_type, order_code, order_variety, quantity, price=None, trigger_price=None):
        self.instrument = instrument
        self.order_transaction_type = order_transaction_type
        self.order_type = BrokerOrderTypeConstants.BROKER_ORDER_TYPE_REGULAR
        self.order_code = order_code
        self.order_variety = order_variety
        self.quantity = quantity
        self.price = price
        self.trigger_price = trigger_price


class BuyOrderRegular(OrderRegularBase):
    def __init__(self, instrument, order_code, order_variety, quantity, price=None, trigger_price=None):
        super().__init__(instrument=instrument, order_transaction_type=BrokerOrderTransactionTypeConstants.BROKER_ORDER_TRANSACTION_TYPE_BUY, order_code=order_code, order_variety=order_variety, quantity=quantity, price=price,
                         trigger_price=trigger_price)


class SellOrderRegular(OrderRegularBase):
    def __init__(self, instrument, order_code, order_variety, quantity, price=None, trigger_price=None):
        super().__init__(instrument=instrument, order_transaction_type=BrokerOrderTransactionTypeConstants.BROKER_ORDER_TRANSACTION_TYPE_SELL, order_code=order_code, order_variety=order_variety, quantity=quantity, price=price,
                         trigger_price=trigger_price)
