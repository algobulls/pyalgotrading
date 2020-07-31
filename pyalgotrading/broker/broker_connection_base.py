"""
Base class for Broker Connection
"""
from abc import abstractmethod


class BrokerConnectionBase:
    """
    Base class for Broker Connection
    """
    @abstractmethod
    def get_name(self):
        """
        Name of the broker
        Returns:
            broker name
        """
        raise NotImplementedError

    @abstractmethod
    def get_all_instruments(self):
        """
        All instruments enlisted by the broker
        Returns:
            list of all instruments
        """
        raise NotImplementedError

    @abstractmethod
    def get_instrument(self, *args, **kwargs):
        """
        Fetch a single instrument
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            a single instrument
        """
        raise NotImplementedError

    @abstractmethod
    def get_market_depth(self, *args, **kwargs):
        """
        Fetch the market depth
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            market depth value
        """
        raise NotImplementedError

    @abstractmethod
    def get_circuit_limits(self, *args, **kwargs):
        """
        Fetch the circuit limits
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            circuit limit value
        """
        raise NotImplementedError

    @abstractmethod
    def get_ltp(self, *args, **kwargs):
        """
        Fetch the Last Trading Price (LTP)
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            ltp value
        """
        raise NotImplementedError

    @abstractmethod
    def get_ltt(self, *args, **kwargs):
        """
        Fetch the Last Trading Time (LTT)
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            ltt value
        """
        raise NotImplementedError

    @abstractmethod
    def get_ltq(self, *args, **kwargs):
        """
        Fetch the Last Trading Quantity (LTQ)
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            ltq value
        """
        raise NotImplementedError

    @abstractmethod
    def get_total_pending_buy_quantity(self, *args, **kwargs):
        """
        Fetch the total pending buy quantity for instrument
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            total quantity value
        """
        raise NotImplementedError

    @abstractmethod
    def get_total_pending_sell_quantity(self, *args, **kwargs):
        """
        Fetch the total pending sell quantity for the instrument
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            total quantity value
        """
        raise NotImplementedError

    @abstractmethod
    def get_total_volume_day(self, *args, **kwargs):
        """
        Fetch the total volume for the day
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            total volume value
        """
        raise NotImplementedError

    @abstractmethod
    def get_open_price_day(self, *args, **kwargs):
        """
        Fetch the open price of the day
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            open price value
        """
        raise NotImplementedError

    @abstractmethod
    def get_high_price_day(self, *args, **kwargs):
        """
        Fetch the high price of the day
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            high price value
        """
        raise NotImplementedError

    @abstractmethod
    def get_low_price_day(self, *args, **kwargs):
        """
        Fetch the low price of the day
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            low price value
        """
        raise NotImplementedError

    @abstractmethod
    def get_close_price_last_day(self, *args, **kwargs):
        """
        Fetch the closed price of the day
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            closed price value
        """
        raise NotImplementedError

    @abstractmethod
    def get_historical_data(self, instrument, candle_interval, start_date, end_date):
        """
        Fetch the historical data
        Args:
            instrument: instrument key
            candle_interval: candle interval
            start_date: date from which to fetch the historical data
            end_date: date till which to fetch the historical data

        Returns:
            historical data
        """
        raise NotImplementedError

    @abstractmethod
    def get_margins(self, *args, **kwargs):
        """
        Fetch the margins
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            margin value
        """
        raise NotImplementedError

    @abstractmethod
    def get_funds(self, *args, **kwargs):
        """
        Fetch the available funds
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list

        Returns:
            available funds value
        """
        raise NotImplementedError

    @abstractmethod
    def get_profile(self):
        """
        Fetch the profile
        Returns:
            profile information
        """
        raise NotImplementedError

    @abstractmethod
    def place_order(self, instrument, order_transaction_type, order_type, order_code, order_variety, quantity, price=None, trigger_price=None, stoploss_trigger=None, target_trigger=None, trailing_stoploss_trigger=None):
        """
        Place an order
        Args:
            instrument: instrument key
            order_transaction_type: buy or sell
            order_type: regular or bracket
            order_code: orde code
            order_variety: market / limit / stoploss market / stoploss limit
            quantity: quantity
            price: amount / value
            trigger_price: trigger price amount / value
            stoploss_trigger: stoploss trigger amount / value
            target_trigger: target trigger amount / value
            trailing_stoploss_trigger: trailing stoploss trigger amount / value

        Returns:
            order id
        """
        raise NotImplementedError

    @abstractmethod
    def get_order_status(self, order_id):
        """
        Fetch the status of the order
        Args:
            order_id: order id

        Returns:
            the status of the order
        """
        raise NotImplementedError
