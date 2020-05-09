from abc import abstractmethod


class BrokerConnectionBase:

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_all_instruments(self):
        raise NotImplementedError

    @abstractmethod
    def get_instrument(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_market_depth(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_circuit_limits(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_ltp(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_ltt(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_ltq(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_total_buy_quantity_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_total_sell_quantity_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_total_volume_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_open_price_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_high_price_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_low_price_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_close_price_last_day(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_historical_data(self, instrument, candle_interval, start_date, end_date):
        raise NotImplementedError

    @abstractmethod
    def get_margins(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_funds(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_profile(self):
        raise NotImplementedError

    @abstractmethod
    def place_order(self, instrument, order_transaction_type, order_type, order_code, order_variety, quantity, price=None, trigger_price=None, stoploss_trigger=None, target_trigger=None, trailing_stoploss_trigger=None):
        raise NotImplementedError

    @abstractmethod
    def get_order_status(self, order_id):
        raise NotImplementedError
