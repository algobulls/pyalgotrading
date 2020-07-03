"""
Module for class BrokerConnectionZerodha
"""
import pandas as pd

from pyalgotrading.broker.broker_connection_base import BrokerConnectionBase
from pyalgotrading.constants import *
from pyalgotrading.utils.func import import_with_install


class BrokerConnectionZerodha(BrokerConnectionBase):
    """
    class for Broker Connection Zerodha

    """
    # Initializing constants. They will be populated correctly by the populate_constants() method
    ORDER_TRANSACTION_TYPE_MAP = {}
    ORDER_TYPE_MAP = {}
    ORDER_CODE_MAP = {}
    ORDER_VARIETY_MAP = {}

    def __init__(self, api_key, api_secret):
        """
        Init method that is used while creating an object of this class
        Args:
            api_key: api key given by the broker
            api_secret: api secret to be used for making an authenticated connection with the broker
        """
        self.api_key = api_key
        self.api_secret = api_secret

        # Create kiteconnect instance
        kiteconnect = import_with_install(package_import_name='kiteconnect', package_install_name='kiteconnect', package_version='3.8.2')
        self.api = kiteconnect.KiteConnect(api_key=self.api_key)

        # Print the login url. User will use this to login to broker site and get access token
        print(f'Please login to this link to generate your request token: {self.api.login_url()}')

        # Create other attributes
        self.all_instruments = None
        self.populate_constants()

    def get_name(self):
        """
        Fetch the name of the broker
        Returns:
            name of the broker
        """
        return 'ZERODHA'

    def populate_constants(self):
        """
        Map pyalgotrading constants to broker constants
        :return: None
        """
        _ = import_with_install(package_import_name='kiteconnect', package_install_name='kiteconnect', package_version='3.8.2').KiteConnect

        BrokerConnectionZerodha.ORDER_TRANSACTION_TYPE_MAP = {BrokerOrderTransactionTypeConstants.BUY: _.TRANSACTION_TYPE_BUY,
                                                              BrokerOrderTransactionTypeConstants.SELL: _.TRANSACTION_TYPE_SELL}

        BrokerConnectionZerodha.ORDER_TYPE_MAP = {BrokerOrderTypeConstants.REGULAR: _.VARIETY_REGULAR,
                                                  BrokerOrderTypeConstants.BRACKET: _.VARIETY_BO,
                                                  BrokerOrderTypeConstants.COVER: _.VARIETY_CO,
                                                  BrokerOrderTypeConstants.AMO: _.VARIETY_AMO}

        BrokerConnectionZerodha.ORDER_CODE_MAP = {BrokerOrderCodeConstants.INTRADAY: _.PRODUCT_MIS,
                                                  BrokerOrderCodeConstants.DELIVERY: _.PRODUCT_CNC}

        BrokerConnectionZerodha.ORDER_VARIETY_MAP = {BrokerOrderVarietyConstants.MARKET: _.ORDER_TYPE_MARKET,
                                                     BrokerOrderVarietyConstants.LIMIT: _.ORDER_TYPE_LIMIT,
                                                     BrokerOrderVarietyConstants.STOPLOSS_LIMIT: _.ORDER_TYPE_SL,
                                                     BrokerOrderVarietyConstants.STOPLOSS_MARKET: _.ORDER_TYPE_SLM}

    def set_access_token(self, request_token):
        """
        Sets the access token
        Args:
            request_token: the request token

        Returns:
            None
        """
        data = self.api.generate_session(request_token, api_secret=self.api_secret)
        self.api.set_access_token(data["access_token"])

    def get_all_instruments(self):
        """
        Fetches all instruments
        Returns:
            list of all instruments
        """
        self.all_instruments = pd.DataFrame(self.api.instruments())
        return self.all_instruments

    def get_instrument(self, segment, tradingsymbol):
        """
        Fetch an instrument
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            instrument
        """
        if self.all_instruments is None:
            self.all_instruments = self.get_all_instruments()
        return self.all_instruments[(self.all_instruments.segment == segment) & (self.all_instruments.tradingsymbol == tradingsymbol)].iloc[0]

    def get_quote(self, segment, tradingsymbol):
        """
        Fetch the quote
        Args:
            segment:
            tradingsymbol:

        Returns:
            quote value
        """
        instrument = f'{segment}:{tradingsymbol}'
        quote = self.api.quote([instrument])[instrument]
        return quote

    def get_market_depth(self, segment, tradingsymbol):
        """
        Fetch the market depth
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            market depth value
        """
        quote = self.get_quote(segment, tradingsymbol)
        buy_market_depth = pd.DataFrame(quote['depth']['buy'])
        sell_market_depth = pd.DataFrame(quote['depth']['sell'])
        return buy_market_depth, sell_market_depth

    def get_circuit_limits(self, segment, tradingsymbol):
        """
        Fetch the circuit limits
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            circuit limit value
        """
        quote = self.get_quote(segment, tradingsymbol)
        lower_circuit_limit = quote['lower_circuit_limit']
        upper_circuit_limit = quote['upper_circuit_limit']
        return lower_circuit_limit, upper_circuit_limit

    def get_ltp(self, segment, tradingsymbol):
        """
        Fetch the Last Trading Price (LTP)
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            ltp value
        """
        quote = self.get_quote(segment, tradingsymbol)
        ltp = quote['last_price']
        return ltp

    def get_ltt(self, segment, tradingsymbol):
        """
        Fetch the Last Trading Time (LTT)
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            ltt value
        """
        quote = self.get_quote(segment, tradingsymbol)
        ltt = quote['last_trade_time']
        return ltt

    def get_ltq(self, segment, tradingsymbol):
        """
        Fetch the Last Trading Quantity (LTQ)
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            ltq value
        """
        quote = self.get_quote(segment, tradingsymbol)
        ltq = quote['last_quantity']
        return ltq

    def get_total_buy_quantity_day(self, segment, tradingsymbol):
        """
        Fetch the total buy quantity for the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            total quantity value
        """
        quote = self.get_quote(segment, tradingsymbol)
        total_buy_quantity_day = quote['buy_quantity']
        return total_buy_quantity_day

    def get_total_sell_quantity_day(self, segment, tradingsymbol):
        """
        Fetch the total sell quantity for the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            total quantity value
        """
        quote = self.get_quote(segment, tradingsymbol)
        total_sell_quantity_day = quote['sell_quantity']
        return total_sell_quantity_day

    def get_total_volume_day(self, segment, tradingsymbol):
        """
        Fetch the total volume for the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            total volume value
        """
        quote = self.get_quote(segment, tradingsymbol)
        total_volume_day = quote['volume']
        return total_volume_day

    def get_open_price_day(self, segment, tradingsymbol):
        """
        Fetch the open price of the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            open price value
        """
        quote = self.get_quote(segment, tradingsymbol)
        open_price_day = quote['ohlc']['open']
        return open_price_day

    def get_high_price_day(self, segment, tradingsymbol):
        """
        Fetch the high price of the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            high price value
        """
        quote = self.get_quote(segment, tradingsymbol)
        high_price_day = quote['ohlc']['high']
        return high_price_day

    def get_low_price_day(self, segment, tradingsymbol):
        """
        Fetch the low price of the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            low price value
        """
        quote = self.get_quote(segment, tradingsymbol)
        low_price_day = quote['ohlc']['low']
        return low_price_day

    def get_close_price_last_day(self, segment, tradingsymbol):
        """
        Fetch the closed price of the day
        Args:
            segment: segment
            tradingsymbol: trading symbol

        Returns:
            closed price value
        """
        quote = self.get_quote(segment, tradingsymbol)
        close_price_day = quote['ohlc']['close']
        return close_price_day

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
        return pd.DataFrame(self.api.historical_data(instrument['instrument_token'], from_date=start_date, to_date=end_date, interval=candle_interval)) \
            .reindex(['date', 'open', 'high', 'low', 'close', 'volume'], axis="columns").rename(columns={'date': 'timestamp'})

    def get_margins(self, segment):
        """
        Fetch the margins
        Args:
            segment: segment

        Returns:
            margin value
        """
        list_permissible_segments = ['equity', 'commodity']
        assert (segment in list_permissible_segments), f'segment should be one of {list_permissible_segments}'
        return self.api.margins(segment=segment)

    def get_funds(self, segment):
        """
        Fetch the available funds
        Args:
            segment: segment

        Returns:
            available funds value
        """
        list_permissible_segments = ['equity', 'commodity']
        assert (segment in list_permissible_segments), f'segment should be one of {list_permissible_segments}'
        return self.api.margins(segment=segment)['net']

    def get_profile(self):
        """
        Fetch the profile
        Returns:
            profile information
        """
        return self.api.profile()

    def place_order(self, instrument, order_transaction_type, order_type, order_code, order_variety, quantity, price=None, trigger_price=None, stoploss=None, target=None, trailing_stoploss=None):
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
            stoploss: stoploss amount / value
            target: target amount / value
            trailing_stoploss: trailing stoploss amount / value

        Returns:
            Order status
        """
        _variety = BrokerConnectionZerodha.ORDER_TYPE_MAP[order_type]  # what we call as 'Order Type', Zerodha calls it as 'variety'
        _transaction_type = BrokerConnectionZerodha.ORDER_TRANSACTION_TYPE_MAP[order_transaction_type]
        _product = BrokerConnectionZerodha.ORDER_CODE_MAP[order_code]  # what we call as 'Order Code', Zerodha calls it as 'product'
        _order_type = BrokerConnectionZerodha.ORDER_VARIETY_MAP[order_variety]  # What we call as 'Order Variety', Zerodha calls it as 'order_type'
        return self.api.place_order(variety=_variety, exchange=instrument.exchange, tradingsymbol=instrument.tradingsymbol, transaction_type=_transaction_type, quantity=quantity, product=_product, order_type=_order_type, price=price,
                                    trigger_price=trigger_price, squareoff=target, stoploss=stoploss, trailing_stoploss=trailing_stoploss)

    def get_order_status(self, order_id):
        """
        Fetch the status of the order
        Args:
            order_id: order id

        Returns:
            the status of the order
        """
        return self.api.order_history(order_id)[-1]['status']

    def cancel_order(self, order_id, order_type):
        """
        Cancel an order
        Args:
            order_id: order id
            order_type: order type

        Returns:
            Order Status
        """
        _variety = BrokerConnectionZerodha.ORDER_TYPE_MAP[order_type]  # What we call as 'Order Type', Zerodha calls it as 'variety'
        return self.api.cancel_order(variety=_variety, order_id=order_id)
