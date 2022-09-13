"""
A collection of classes of type Enumeration use while programming a new strategy
"""
from enum import Enum


class AlgoBullsEngineVersion(Enum):
    """
    A class of Versioning Constants
    """
    VERSION_3_3_0 = '3.3.0'


class AlgoBullsJobStatus(Enum):
    """
    A class of job status Constants
    """
    JOB_RUNNING = 'RUNNING'
    JOB_STOPPED = 'STOPPED'
    JOB_STATUS_UNKNOWN = 'JOB STATUS UNKNOWN'


class AlgoBullsJobSubmissionResponse(Enum):
    """
    A class of responses when querying the job status
    """
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'
    JOB_ALREADY_RUNNING = 'ALREADY RUNNING'
    JOB_NOT_RUNNING = 'JOB NOT RUNNING'


class AlgoBullsSupportedBrokers(Enum):
    """
    A class of supported brokers
    """
    ZERODHA = 'ZERODHA'


class BrokerOrderTransactionTypeConstants(Enum):
    """
    A class of Order Transaction Type Constants
    """
    BUY = 'BUY'
    SELL = 'SELL'


class BrokerOrderTypeConstants(Enum):
    """
    A class of Order Type Constants
    """
    REGULAR = 'ORDER_TYPE_REGULAR'
    BRACKET = 'ORDER_TYPE_BRACKET'
    COVER = 'ORDER_TYPE_COVER'
    AMO = 'ORDER_TYPE_AFTER_MARKET_ORDER'


class BrokerOrderCodeConstants(Enum):
    """
    A class of Order Code Constants
    """
    INTRADAY = 'ORDER_CODE_INTRADAY'
    DELIVERY = 'ORDER_CODE_DELIVERY_T0'
    DELIVERY_T1 = 'ORDER_CODE_DELIVERY_T1'
    DELIVERY_T2 = 'ORDER_CODE_DELIVERY_T2'


class BrokerOrderVarietyConstants(Enum):
    """
    A class of Order Variety Constants
    """
    MARKET = 'ORDER_VARIETY_MARKET'
    LIMIT = 'ORDER_VARIETY_LIMIT'
    STOPLOSS_MARKET = 'ORDER_VARIETY_STOPLOSS_MARKET'
    STOPLOSS_LIMIT = 'ORDER_VARIETY_STOPLOSS_LIMIT'


class BrokerExistingOrderPositionConstants(Enum):
    """
    A class of Order Position Constants
    """
    ENTER = 'ORDER_POSITION_ENTER'
    EXIT = 'ORDER_POSITION_EXIT'


class BrokerOrderStatusConstants(Enum):
    """
    A class of Order Status Constants
    """
    PUT_ORDER_REQ_RECEIVED = 'PUT ORDER REQ RECEIVED'
    VALIDATION_PENDING = 'VALIDATION PENDING'
    OPEN_PENDING = 'OPEN PENDING'
    TRIGGER_PENDING = 'TRIGGER PENDING'
    CANCEL_PENDING = 'CANCEL PENDING'
    COMPLETE = 'COMPLETE'
    CANCELLED = 'CANCELLED'
    OPEN = 'OPEN'
    REJECTED = 'REJECTED'


class CandleInterval(Enum):
    """
    A class of Candle Intervals with their Alternate names
    """
    # MINUTES_1 = 0
    # MINUTES_3 = 1
    # MINUTES_5 = 2
    # MINUTES_10 = 3
    # MINUTES_15 = 4
    # MINUTES_30 = 5
    # MINUTES_60 = 6
    # HOURS_1 = 6
    # HOURS_24 = 7
    # DAYS_1 = 7
    #
    # # Alternative names
    # MINUTE_1 = 0
    # MINUTE_3 = 1
    # MINUTE_5 = 2
    # MINUTE_10 = 3
    # MINUTE_15 = 4
    # MINUTE_30 = 5
    # MINUTE_60 = 6
    # HOUR_1 = 6
    # HOUR_24 = 7
    # DAY_1 = 7
    #
    # MINUTE = 0
    # HOUR = 6
    # DAY = 7

    MINUTES_1 = 'minute'
    MINUTES_3 = '3minutes'
    MINUTES_5 = '5minutes'
    MINUTES_10 = '10minutes'
    MINUTES_15 = '15minutes'
    MINUTES_30 = '30minutes'
    MINUTES_60 = '60minutes'
    HOURS_1 = '60minutes'
    HOURS_24 = 'day'
    DAYS_1 = 'day'

    # Alternative names
    MINUTE_1 = 'minute'
    MINUTE_3 = '3minutes'
    MINUTE_5 = '5minutes'
    MINUTE_10 = '10minutes'
    MINUTE_15 = '15minutes'
    MINUTE_30 = '30minutes'
    MINUTE_60 = '60minutes'
    HOUR_1 = '60minutes'
    HOUR_24 = 'day'
    DAY_1 = 'day'

    MINUTE = 'minute'
    HOUR = '60minutes'
    DAY = 'day'


class StrategyMode(Enum):
    """
    A class of Strategy Modes
    """
    INTRADAY = "INTRADAY"
    DELIVERY = "DELIVERY"


class StrategyType(Enum):
    """
    A class of Strategy Type
    """
    PYTHON = 1


class TradingType(Enum):
    """
    A class of Trading Types
    """
    BACKTESTING = 0
    PAPERTRADING = 1
    REALTRADING = 2


class TradingReportType(Enum):
    """
    A class of Trading Report Types
    """
    PNL_TABLE = 1
    STATS_TABLE = 2
    ORDER_HISTORY = 3


class PlotType(Enum):
    """
    A class of Plot Types
    """
    JAPANESE = 'JAPANESE'
    LINEBREAK = 'Linebreak'
    RENKO = 'Renko'
    HEIKINASHI = 'HeikinAshi'
    QUANDL_JAPANESE = 'Quandl JAPANESE'


class DecisionConstants(Enum):
    """
    A class of Decision Types
    """
    ENTRY_POSITION = 'ENTRY_POSITION'
    EXIT_POSITION = 'EXIT_POSITION'


MESSAGE_REALTRADING_FORBIDDEN = 'Forbidden. This strategy is not approved for RT mode. Email us on support@algobulls.com to get your strategy approved. ' \
                                'The AlgoBulls support team will guide you with the approval process. Once your strategy is approved, you can run it for RT directly from your AlgoBulls account.'
