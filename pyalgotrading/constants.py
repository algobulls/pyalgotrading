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
    # We have added multiple enums, to take care of all practical combinations in which a user may input a candle interval as a string.
    # (Note: Before applying a user input to this enum, it is cleaned up - leading/trailing spaces removed, cases converted to caps, internal spaces converted to _.
    # That way a user has lot of flexibility in entering the candle interval as a string)

    _1_MINUTE = 'minute'
    _1_MINUTES = 'minute'
    _3_MINUTES = '3minutes'
    _5_MINUTES = '5minutes'
    _10_MINUTES = '10minutes'
    _15_MINUTES = '15minutes'
    _30_MINUTES = '30minutes'
    _60_MINUTES = '60minutes'
    _1_HOURS = '60minutes'
    _1_DAYS = 'day'
    _24_HOURS = 'day'

    # Alternative names #1
    _3_MINUTE = '3minutes'
    _5_MINUTE = '5minutes'
    _10_MINUTE = '10minutes'
    _15_MINUTE = '15minutes'
    _30_MINUTE = '30minutes'
    _60_MINUTE = '60minutes'
    _1_HOUR = '60minutes'
    _24_HOUR = 'day'
    _1_DAY = 'day'

    # Alternative names #2
    _1MINUTE = 'minute'
    _3MINUTE = '3minutes'
    _5MINUTE = '5minutes'
    _10MINUTE = '10minutes'
    _15MINUTE = '15minutes'
    _30MINUTE = '30minutes'
    _60MINUTE = '60minutes'
    _1HOUR = '60minutes'
    _24HOUR = 'day'
    _1DAY = 'day'

    # Alternative names #3
    _1MINUTES = 'minute'
    _3MINUTES = '3minutes'
    _5MINUTES = '5minutes'
    _10MINUTES = '10minutes'
    _15MINUTES = '15minutes'
    _30MINUTES = '30minutes'
    _60MINUTES = '60minutes'
    _1HOURS = '60minutes'
    _24HOURS = 'day'
    _1DAYS = 'day'

    # Alternative names #4
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

    # Alternative names #5
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

    # Alternative names #6
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


class ActionConstants(Enum):
    """
    A class of Action Types
    """
    ENTRY_BUY = 'ENTRY_BUY'
    ENTRY_SELL = 'ENTRY_SELL'
    EXIT_BUY = 'EXIT_BUY'
    EXIT_SELL = 'EXIT_SELL'
    NO_ACTION = 'NO_ACTION'


class Locale(Enum):
    """
    A class of locale
    """
    DEFAULT = 'en-US'
    INDIA = 'en-IN'
    USA = 'en-US'


class Country(Enum):
    """
    A class of countries
    """
    DEFAULT = 'USA'
    INDIA = 'India'
    USA = 'USA'


class ExecutionStatus(Enum):
    """
    A class of status values of execution
    """
    STARTING = 'STARTING'
    STARTED = 'STARTED'
    STOPPING = 'STOPPING'
    STOPPED = 'STOPPED'


class OptionsStrikeDirection(Enum):
    ITM = 'ITM'
    ATM = 'ATM'
    OTM = 'OTM'


class OptionsTradingsymbolSuffix(Enum):
    CE = 'CE'
    PE = 'PE'


class OptionsExpiryKey(Enum):
    WEEKLY_CURRENT = 'WEEKLY_CURRENT'
    WEEKLY_NEXT = 'WEEKLY_NEXT'
    MONTHLY_CURRENT = 'MONTHLY_CURRENT'
    MONTHLY_NEXT = 'MONTHLY_NEXT'


class OptionsInstrumentDirection(Enum):
    EXACT = 'EXACT'
    ROUNDUP = 'ROUNDUP'
    ROUNDDOWN = 'ROUNDDOWN'


CandleIntervalSecondsMap = {
    'minute': 60,
    '3minutes': 180,
    '5minutes': 300,
    '10minutes': 600,
    '15minutes': 900,
    '30minutes': 1800,
    '60minutes': 3600,
    'day': 86400
}

KEY_DT_FORMAT_WITH_TIMEZONE = 0
KEY_DT_FORMAT_WITHOUT_TIMEZONE = 1

TRADING_TYPE_DT_FORMAT_MAP = {
    TradingType.BACKTESTING: {KEY_DT_FORMAT_WITH_TIMEZONE: '%Y-%m-%d %H:%M %z', KEY_DT_FORMAT_WITHOUT_TIMEZONE: '%Y-%m-%d %H:%M'},
    TradingType.PAPERTRADING: {KEY_DT_FORMAT_WITH_TIMEZONE: '%H:%M %z', KEY_DT_FORMAT_WITHOUT_TIMEZONE: '%H:%M'},
    TradingType.REALTRADING: {KEY_DT_FORMAT_WITH_TIMEZONE: '%H:%M %z', KEY_DT_FORMAT_WITHOUT_TIMEZONE: '%H:%M'},
}

EXCHANGE_LOCALE_MAP = {
    'NSE': Locale.INDIA.value,
    'BSE': Locale.INDIA.value,
    'NASDAQ': Locale.USA.value,
    'NYSE': Locale.USA.value,
}

