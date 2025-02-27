def check_order_placed_successfully(self, _order):
    """
        This method checks whether --
        -- order is not None
        -- broker_order_id exists for this order
        -- order status is not REJECTED
        Returns True if all of the above are True, else False.
        """
    return _order is not None and _order.broker_order_id is not None and _order.get_order_status() != BrokerOrderStatusConstants.REJECTED


def check_order_complete_status(self, _order):
    """
    This method checks whether --
    -- order is not None
    -- broker_order_id exists for this order
    -- order status is COMPLETE

    Returns True if all of the above are True, else False
    """
    return _order is not None and _order.broker_order_id is not None and _order.get_order_status() == BrokerOrderStatusConstants.COMPLETE