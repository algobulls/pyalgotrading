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

    _1_MINUTE = '1 Minute'
    _1_MINUTES = '1 Minute'
    _3_MINUTES = '3 Minutes'
    _5_MINUTES = '5 Minutes'
    _10_MINUTES = '10 Minutes'
    _15_MINUTES = '15 Minutes'
    _30_MINUTES = '30 Minutes'
    _60_MINUTES = '60 Minutes'
    _1_HOURS = '60 Minutes'
    _1_DAYS = '1 Day'
    _24_HOURS = '1 Day'

    # Alternative names #1
    _3_MINUTE = '3 Minutes'
    _5_MINUTE = '5 Minutes'
    _10_MINUTE = '10 Minutes'
    _15_MINUTE = '15 Minutes'
    _30_MINUTE = '30 Minutes'
    _60_MINUTE = '60 Minutes'
    _1_HOUR = '60 Minutes'
    _24_HOUR = '1 Day'
    _1_DAY = '1 Day'

    # Alternative names #2
    _1MINUTE = '1 Minute'
    _3MINUTE = '3 Minutes'
    _5MINUTE = '5 Minutes'
    _10MINUTE = '10 Minutes'
    _15MINUTE = '15 Minutes'
    _30MINUTE = '30 Minutes'
    _60MINUTE = '60 Minutes'
    _1HOUR = '60 Minutes'
    _24HOUR = '1 Day'
    _1DAY = '1 Day'

    # Alternative names #3
    _1MINUTES = '1 Minute'
    _3MINUTES = '3 Minutes'
    _5MINUTES = '5 Minutes'
    _10MINUTES = '10 Minutes'
    _15MINUTES = '15 Minutes'
    _30MINUTES = '30 Minutes'
    _60MINUTES = '60 Minutes'
    _1HOURS = '60 Minutes'
    _24HOURS = '1 Day'
    _1DAYS = '1 Day'

    # Alternative names #4
    MINUTES_1 = '1 Minute'
    MINUTES_3 = '3 Minutes'
    MINUTES_5 = '5 Minutes'
    MINUTES_10 = '10 Minutes'
    MINUTES_15 = '15 Minutes'
    MINUTES_30 = '30 Minutes'
    MINUTES_60 = '60 Minutes'
    HOURS_1 = '60 Minutes'
    HOURS_24 = '1 Day'
    DAYS_1 = '1 Day'

    # Alternative names #5
    MINUTE_1 = '1 Minute'
    MINUTE_3 = '3 Minutes'
    MINUTE_5 = '5 Minutes'
    MINUTE_10 = '10 Minutes'
    MINUTE_15 = '15 Minutes'
    MINUTE_30 = '30 Minutes'
    MINUTE_60 = '60 Minutes'
    HOUR_1 = '60 Minutes'
    HOUR_24 = '1 Day'
    DAY_1 = '1 Day'

    # Alternative names #6
    MINUTE = '1 Minute'
    HOUR = '60 Minutes'
    DAY = '1 Day'


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


OPTIONS_STRIKE_DIRECTION_NUMERIC_ITM = 0
OPTIONS_STRIKE_DIRECTION_NUMERIC_ATM = 1
OPTIONS_STRIKE_DIRECTION_NUMERIC_OTM = 2

OptionsStrikeDirectionMap = {
    OPTIONS_STRIKE_DIRECTION_NUMERIC_ITM: OptionsStrikeDirection.ITM.value,
    OPTIONS_STRIKE_DIRECTION_NUMERIC_ATM: OptionsStrikeDirection.ATM.value,
    OPTIONS_STRIKE_DIRECTION_NUMERIC_OTM: OptionsStrikeDirection.OTM.value
}


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
    CandleInterval.MINUTE_1.value: 60,
    CandleInterval.MINUTE_3.value: 180,
    CandleInterval.MINUTE_5.value: 300,
    CandleInterval.MINUTE_10.value: 600,
    CandleInterval.MINUTE_15.value: 900,
    CandleInterval.MINUTE_30.value: 1800,
    CandleInterval.MINUTE_60.value: 3600,
    CandleInterval.DAY_1.value: 86400
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


class ABSystemExit(SystemExit):
    # Use this class instead of SystemExit directly for stopping your strategy
    pass
