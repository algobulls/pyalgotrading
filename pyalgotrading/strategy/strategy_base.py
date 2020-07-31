"""

"""
from abc import ABCMeta, abstractmethod
from collections import defaultdict

from pyalgotrading import broker
from ..constants import StrategyMode
from ..order.order_bracket_base import BuyOrderBracket, SellOrderBracket
from ..order.order_regular_base import BuyOrderRegular, SellOrderRegular


class StrategyBase(object, metaclass=ABCMeta):
    """
    Dummy placeholder class. Here to ensure all required methods are implemented and as per requirements.

    Once uploaded, this strategy will be replaced with the real base class strategy
    """

    def __init__(self, *args, **kwargs):
        """
        Init method that is used while creating an object of this class
        Args:
            *args: a variable-length argument list
            **kwargs: a keyworded, variable-length argument list
        """
        # Dummy attributes
        self.strategy_parameters = defaultdict(lambda: 'dummy')
        self.broker = broker.broker_connection_base.BrokerConnectionBase()
        self.utils = broker.utils

        # Dummy Order Attributes
        self.BuyOrderRegular = BuyOrderRegular
        self.SellOrderRegular = SellOrderRegular
        self.BuyOrderBracket = BuyOrderBracket
        self.SellOrderBracket = SellOrderBracket

        # Dummy strategy config attributes
        self.strategy_mode = StrategyMode.INTRADAY  # <Type: Enum of type StrategyMode; This attribute will hold one of the following values - StrategyMode.INTRADAY or StrategyMode.DELIVERY. This value is passed to pyalgotrading.algobulls.connection.backtest/papertest/realtrade methods.>
        self.number_of_lots = 1  # <Type: This attribute will hold one of the following values - StrategyMode.INTRADAY or StrategyMode.DELIVERY. This value is passed to pyalgotrading.algobulls.connection.backtest/papertest/realtrade methods.>

    @staticmethod
    @abstractmethod
    def name():
        """
        Name of the strategy
        Returns: None

        """
        raise NotImplementedError

    def get_historical_data(self, instrument):
        """
        Fetch the historical data of an instrument
        This is a dummy function with a sole purpose of mimicing the signature of the actual function on the AlgoBulls platform, as described in the documentation.
        Args:
            instrument: instrument key

        Returns:
            None
        """
        # This is a dummy function with a sole purpose of mimicing the signature of the actual function on the AlgoBulls platform, as described in the documentation.
        pass

    @staticmethod
    @abstractmethod
    def versions_supported():
        """
        Version of the AlgoBulls platform that this Strategy will run on/tested on
        :return: Should return a single version or list of versions of ABC on which the current strategy has been tested to run successfully
        """
        raise NotImplementedError

    @abstractmethod
    def initialize(self):
        """
        Initialization task for this strategy. Calling this method should initialise/reset the strategy's internal state variables to original state.

        Every Strategy should initialize its internal state variables in this task to reset values.

        Indented to be called by TLS as part of pre market activity & for backtesting mode, at the start of every new backtesting day.
        """
        raise NotImplementedError

    def strategy_select_instruments_for_entry(self, candle, instruments_bucket):
        """
        Select instruments for entry here
        Args:
            candle: the current candle
            instruments_bucket: the list of instruments to be selected from

        Returns:
            selected instruments and sideband (additional) information for each
        """
        raise NotImplementedError

    @abstractmethod
    def strategy_enter_position(self, candle, instrument, sideband_info):
        """
        Enter position for each instrument
        Args:
            candle: the current candle
            instrument: the instrument key
            sideband_info: the additional information regarding the instrument action

        Returns:
            the order, if position is entered
        """
        raise NotImplementedError

    @abstractmethod
    def strategy_select_instruments_for_exit(self, candle, instruments_bucket):
        """
        Select instruments for exit here
        Args:
            candle: the current candle
            instruments_bucket: the list of instruments to be selected from

        Returns:
            selected instruments and sideband (additional) information for each
        """
        raise NotImplementedError

    @abstractmethod
    def strategy_exit_position(self, candle, instrument, sideband_info):
        """
        Exit position for each instrument
        Args:
            candle: the current candle
            instrument: the instrument key
            sideband_info: the additional information regarding the instrument action

        Returns:
            True if order is exited else False
        """
        raise NotImplementedError
