"""
Class for Regular Order
"""
from .order_base import OrderBase
from ..constants import BrokerOrderTypeConstants, BrokerOrderTransactionTypeConstants


class OrderRegularBase(OrderBase):
    """
    Class for Regular Order
    """
    def __init__(self, instrument, order_transaction_type, order_code, order_variety, quantity, price=None, trigger_price=None):
        """
        Init method that is used while creating an object of this class
        Args:
            instrument: instrument key
            order_transaction_type: order transaction type
            order_code: regular order
            order_variety: market / limit / stoploss market / stoploss limit
            quantity: order quantity
            price: amount / value
            trigger_price: trigger amount / value
        """
        self.instrument = instrument
        self.order_transaction_type = order_transaction_type
        self.order_type = BrokerOrderTypeConstants.BROKER_ORDER_TYPE_REGULAR
        self.order_code = order_code
        self.order_variety = order_variety
        self.quantity = quantity
        self.price = price
        self.trigger_price = trigger_price


class BuyOrderRegular(OrderRegularBase):
    """
    Class for Regular Order Buy
    """
    def __init__(self, instrument, order_code, order_variety, quantity, price=None, trigger_price=None):
        """
        Init method that is used while creating an object of this class
        """
        super().__init__(instrument=instrument, order_transaction_type=BrokerOrderTransactionTypeConstants.BROKER_ORDER_TRANSACTION_TYPE_BUY, order_code=order_code, order_variety=order_variety, quantity=quantity, price=price,
                         trigger_price=trigger_price)


class SellOrderRegular(OrderRegularBase):
    """
    Class for Regular Order Buy
    """
    def __init__(self, instrument, order_code, order_variety, quantity, price=None, trigger_price=None):
        """
        Init method that is used while creating an object of this class
        """
        super().__init__(instrument=instrument, order_transaction_type=BrokerOrderTransactionTypeConstants.BROKER_ORDER_TRANSACTION_TYPE_SELL, order_code=order_code, order_variety=order_variety, quantity=quantity, price=price,
                         trigger_price=trigger_price)
