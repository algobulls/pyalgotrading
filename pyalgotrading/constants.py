from enum import Enum


class AlgoBullsEngineVersion:
    VERSION_3_1_0 = '3.1.0'


class AlgoBullsJobStatusEnum(Enum):
    JOB_RUNNING = 'RUNNING'
    JOB_STOPPED = 'STOPPED'


class AlgoBullsJobSubmissionResponseEnum(Enum):
    SUCCESS = 'Success'
    ERROR = 'Error'
    JOB_NOT_RUNNING = 'Job not running'


class BrokerOrderTransactionTypeConstants(Enum):
    BUY = 'BUY'
    SELL = 'SELL'


class BrokerOrderTypeConstants(Enum):
    REGULAR = 'ORDER_TYPE_REGULAR'
    BRACKET = 'ORDER_TYPE_BRACKET'
    COVER = 'ORDER_TYPE_COVER'
    AMO = 'ORDER_TYPE_AFTER_MARKET_ORDER'


class BrokerOrderCodeConstants(Enum):
    INTRADAY = 'ORDER_CODE_INTRADAY'
    DELIVERY = 'ORDER_CODE_DELIVERY_T0'
    DELIVERY_T1 = 'ORDER_CODE_DELIVERY_T1'
    DELIVERY_T2 = 'ORDER_CODE_DELIVERY_T2'


class BrokerOrderVarietyConstants(Enum):
    MARKET = 'ORDER_VARIETY_MARKET'
    LIMIT = 'ORDER_VARIETY_LIMIT'
    STOPLOSS_MARKET = 'ORDER_VARIETY_STOPLOSS_MARKET'
    STOPLOSS_LIMIT = 'ORDER_VARIETY_STOPLOSS_LIMIT'


class CandleIntervalEnum(Enum):
    MINUTE = 'minute'
    MINUTE_1 = 'minute'
    MINUTES = 'minute'
    MINUTES_1 = 'minute'
    MINUTES_3 = '3minutes'
    MINUTES_5 = '5minutes'
    MINUTES_10 = '10minutes'
    MINUTES_15 = '15minutes'
    MINUTES_30 = '30minutes'
    MINUTES_60 = '60minutes'
    HOUR = '60minutes'
    HOUR_1 = '60minutes'
    HOURS_1 = '60minutes'
    HOURS_24 = 'day'
    DAY = 'day'


class StrategyMode(Enum):
    INTRADAY = 0
    DELIVERY = 1


class StrategyType(Enum):
    PYTHON = 1


class TradingType(Enum):
    BACKTESTING = 0
    PAPERTRADING = 1
    REALTRADING = 2


class TradingReportType(Enum):
    PNL_TABLE = 0
    STATS_TABLE = 1
    ORDER_HISTORY = 2
    LOGS = 3
