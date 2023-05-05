"""
Module for AlgoBulls connection
"""
import inspect
import time
from datetime import datetime as dt

import pandas as pd
import quantstats as qs

from .api import AlgoBullsAPI
from .exceptions import AlgoBullsAPIBadRequest
from ..constants import StrategyMode, TradingType, TradingReportType, CandleInterval, MESSAGE_REALTRADING_FORBIDDEN, AlgoBullsEngineVersion
from ..strategy.strategy_base import StrategyBase


class AlgoBullsConnection:
    """
    Class for AlgoBulls connection
    """

    def __init__(self):
        """
        Init method that is used while creating an object of this class
        """
        self.api = AlgoBullsAPI(self)
        self.pnl_data = None

    @staticmethod
    def get_authorization_url():
        """
        Fetch the authorization URL

        Returns:
            Authorization URL
        """
        url = 'https://app.algobulls.com/user/login'
        print(f'Please login to this URL with your AlgoBulls credentials and get your developer access token: {url}')
        return url

    def set_access_token(self, access_token):
        """
        Set the access token

        Args:
            access_token: access token

        Returns:
            None
        """
        assert isinstance(access_token, str), f'Argument "access_token" should be a string'
        self.api.set_access_token(access_token)

    def create_strategy(self, strategy, overwrite=False, strategy_code=None, abc_version=None):
        """
        Method to upload new strategy.

        All strategies are unique by name, per customer.
        If customer tries to upload strategy with the same name as an already existing strategy -
        if overwrite is False:
            - AlgoBullsAPIBadRequest Exception will be thrown. No change would be done in the backend database.
        If overwrite is True,
            - Existing strategy with strategy_name would be overwritten. No exception will be thrown.
        If abc_version is not None,
            - Create strategy for specific version
        else:
            - Create strategy for latest version

        Args:
            strategy: A strategy
            overwrite: A boolean variable
            strategy_code: Strategy code
            abc_version: ABC version
        """

        # Sanity checks
        assert issubclass(strategy, StrategyBase), f'strategy should be a subclass of class StrategyBase. Got class of type: type{strategy}'
        assert hasattr(strategy, 'name'), f'Strategy name not defined'

        # Validate class by creating an instance
        # Todo: Temporarily disabling strategy validation for this bug fix: Validating strategy which has assert checks for strategy parameters to be of specific type (say 'int') fails with TypeError.
        #       In future, if assert checks can be taken care of dynamically, turn this validation ON.
        # print('Validating Strategy...')
        # strategy()

        # Get source code, and upload as new strategy (if strategy_code is None) else edit same strategy
        strategy_name = strategy.name if isinstance(strategy.name, str) else strategy.name()
        strategy_details = inspect.getsource(strategy)
        versions_supported = strategy.versions_supported() if hasattr(strategy, 'versions_supported') else AlgoBullsEngineVersion.VERSION_3_3_0

        if abc_version is None:
            if isinstance(versions_supported, list):
                _abc_version = versions_supported[0].value  # Take the first version
            else:
                _abc_version = versions_supported.value
        else:
            _abc_version = abc_version.value

        if overwrite is False:
            response = self.api.create_strategy(strategy_name=strategy_name, strategy_details=strategy_details, abc_version=_abc_version)
        else:
            response = None
            if strategy_code:
                _strategy_code = strategy_code
            else:
                _ = self.get_all_strategies(return_as_dataframe=False)
                try:
                    _strategy_code = {_dict['strategyName']: _dict['strategyCode'] for _dict in _}[strategy_name]
                    response = self.api.update_strategy(strategy_code=_strategy_code, strategy_name=strategy_name, strategy_details=strategy_details, abc_version=_abc_version)

                except KeyError:
                    response = self.api.create_strategy(strategy_name=strategy_name, strategy_details=strategy_details,
                                                        abc_version=_abc_version)
        return response

    def get_all_strategies(self, return_as_dataframe=True):
        """
        Fetch all available strategies

        Args:
            return_as_dataframe: If true, strategies returned as a Dataframe else returned as JSON

        Returns:
            list of available strategies
        """
        response = self.api.get_all_strategies()
        if isinstance(response['data'], list):
            _ = response['data']
            return pd.DataFrame(_) if return_as_dataframe else _
        else:
            return response

    def get_strategy_details(self, strategy_code):
        """
        Fetch the strategy details of a particular strategy

        Args:
            strategy_code: strategy code

        Returns:
            strategy program / code
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        try:
            response = self.api.get_strategy_details(strategy_code)
            strategy_code = response['data']
            return strategy_code
        except AlgoBullsAPIBadRequest:
            print(f'ERROR: No strategy found with ID: {strategy_code}')

    def search_instrument(self, instrument, exchange='NSE'):
        """
        Search for an instrument

        Args:
            instrument: instrument key
            exchange: exchange, default is 'NSE'

        Returns:
            A list of matching instruments
        """
        assert isinstance(instrument, str), f'Argument "instrument" should be a string'
        response = self.api.search_instrument(instrument, exchange=exchange).get('data')
        return response

    def get_job_status(self, strategy_code, trading_type):
        """
        Get status for a Back Testing / Paper Trading / Real Trading Job

        Args:
            strategy_code: Strategy code
            trading_type: Trading type

        Returns:
            Job status
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(trading_type, TradingType), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

        response = self.api.get_job_status(strategy_code=strategy_code, trading_type=trading_type)
        return response

    def stop_job(self, strategy_code, trading_type):
        """
        Stop a running job

        Args:
            strategy_code: strategy code
            trading_type: trading type

        Returns:
            Job status
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(trading_type, TradingType), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

        response = self.api.stop_strategy_algotrading(strategy_code=strategy_code, trading_type=trading_type)

    def get_logs(self, strategy_code, trading_type):
        """
        Fetch logs for a strategy

        Args:
            strategy_code: strategy code
            trading_type: trading type

        Returns:
            Execution logs
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(trading_type, TradingType), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

        return self.api.get_logs(strategy_code=strategy_code, trading_type=trading_type).get('data')

    def get_report(self, strategy_code, trading_type, report_type, render_as_dataframe=False, show_all_rows=False):
        """
        Fetch report for a strategy

        Args:
            strategy_code: Strategy code
            trading_type: Value of TradingType Enum
            report_type: Value of TradingReportType Enum
            render_as_dataframe: True or False
            show_all_rows: True or False

        Returns:
            report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(trading_type, TradingType), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'
        assert isinstance(report_type, TradingReportType), f'Argument "report_type" should be an enum of type {TradingReportType.__name__}'
        assert isinstance(render_as_dataframe, bool), f'Argument "render_as_dataframe" should be a bool'
        assert isinstance(show_all_rows, bool), f'Argument "show_all_rows" should be a bool'
        # assert (broker is None or isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be None or an enum of type {AlgoBullsSupportedBrokers.__name__}'

        response = self.api.get_reports(strategy_code=strategy_code, trading_type=trading_type, report_type=report_type)
        if response.get('data'):
            if render_as_dataframe:
                if show_all_rows:
                    pandas_dataframe_all_rows()
                _response = pd.DataFrame(response['data'])
            else:
                _response = response['data']
            return _response
        else:
            print('Report not available yet. Please retry in sometime')
            # return response

    def backtest(self, strategy_code, start_timestamp, end_timestamp, instrument, lots, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY):
        """
        Submit a backtesting job for a strategy on the AlgoBulls Platform

        Args:
            strategy_code: Strategy code
            start_timestamp: Start date/time
            end_timestamp: End date/time
            instrument: Instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: Parameters
            candle_interval: Candle interval
            strategy_mode: Intraday or delivery

        Returns:
            backtest job submission status
        """
        # Sanity checks - Validate config parameters
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(start_timestamp, dt), f'Argument "start_timestamp" should be an instance of type datetime.datetime'
        assert isinstance(end_timestamp, dt), f'Argument "end_timestamp" should be an instance of type datetime.datetime'
        assert isinstance(instrument, str), f'Argument "instrument" should be a string. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(lots, int) and lots > 0), f'Argument "lots" should be a positive integer.'
        assert isinstance(strategy_parameters, dict), f'Argument "strategy_parameters" should be a dict'
        assert isinstance(strategy_mode, StrategyMode), f'Argument "strategy_mode" should be enum of type StrategyMode'
        assert isinstance(candle_interval, CandleInterval), f'Argument "candle_interval" should be an enum of type CandleInterval'

        # Restructuring strategy params
        restructured_strategy_parameters = []
        for _ in strategy_parameters:
            restructured_strategy_parameters.append({
                'paramName': _,
                'paramValue': strategy_parameters[_]
            })

        instrument_id = None
        instrument_results = self.search_instrument(instrument.split(':')[-1])
        for _ in instrument_results:
            if _["value"] == instrument:
                instrument_id = _["id"]
                break

        # Setup config for Backtesting
        strategy_config = {
            'instruments': {
                'instruments': [{'id': instrument_id}]
            },
            'lots': lots,
            'userParams': restructured_strategy_parameters,
            'candleDuration': candle_interval.value,
            'strategyMode': strategy_mode.value}
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config, trading_type=TradingType.BACKTESTING)

        # Submit Backtesting job
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, start_timestamp=start_timestamp, end_timestamp=end_timestamp, trading_type=TradingType.BACKTESTING, lots=lots)

    def get_backtesting_job_status(self, strategy_code):
        """
        Get Back Testing job status for given strategy_code

        Args:
            strategy_code: Strategy code

        Returns:
            Job status
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_job_status(strategy_code, TradingType.BACKTESTING)

    def stop_backtesting_job(self, strategy_code):
        """
        Stop a running Back Testing job

        Args:
            strategy_code: Strategy Code

        Returns:
            Job status
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING)

    def get_backtesting_logs(self, strategy_code):
        """
        Fetch Back Testing logs

        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_logs(strategy_code, trading_type=TradingType.BACKTESTING)

    def get_backtesting_report_pnl_table(self, strategy_code, show_all_rows=False):
        """
        Fetch Back Testing Profit & Loss details

        Args:
            strategy_code: strategy code
            show_all_rows: True or False

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        data = self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING, report_type=TradingReportType.PNL_TABLE)

        columns_required = [
            'strategy.instrument.segment', 'strategy.instrument.tradingsymbol',
            'entry.timestamp', 'entry.isBuy', 'entry.quantity', 'entry.prefix', 'entry.price',
            'exit.timestamp', 'exit.isBuy', 'exit.quantity', 'exit.prefix', 'exit.price',
            'pnlAbsolute.value'
        ]
        column_rename_map = {
            'strategy.instrument.segment': 'instrument_segment',
            'strategy.instrument.tradingsymbol': 'instrument_tradingsymbol',
            'entry.timestamp': 'entry_timestamp',
            'entry.isBuy': 'entry_transaction_type',
            'entry.quantity': 'entry_quantity',
            'entry.prefix': 'entry_currency',
            'entry.price': 'entry_price',
            'exit.timestamp': 'exit_timestamp',
            'exit.isBuy': 'exit_transaction_type',
            'exit.quantity': 'exit_quantity',
            'exit.prefix': 'exit_currency',
            'exit.price': 'exit_price',
            'pnlAbsolute.value': 'pnl_absolute',
        }

        # Generate df from json data & perform cleanups
        _df = pd.json_normalize(data[::-1])[columns_required].rename(columns=column_rename_map)
        _df[['entry_timestamp', 'exit_timestamp']] = _df[['entry_timestamp', 'exit_timestamp']].apply(pd.to_datetime, format="%Y-%m-%d | %H:%M", errors="coerce")
        _df['entry_transaction_type'] = _df['entry_transaction_type'].apply(lambda _: 'BUY' if _ else 'SELL')
        _df['exit_transaction_type'] = _df['exit_transaction_type'].apply(lambda _: 'BUY' if _ else 'SELL')
        _df["pnl_cumulative_absolute"] = _df["pnl_absolute"].cumsum(axis=0, skipna=True)

        self.pnl_data = _df
        return self.pnl_data

    def get_backtesting_report_statistics(self, strategy_code, mode='quantstats', report='metrics', html_dump=False):
        """
        Fetch Back Testing report statistics

        Args:
            strategy_code: strategy code

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        order_report = None
        initial_funds = 1e9         # TODO: Allow this to be customized by the user

        if self.pnl_data is None:
            self.get_backtesting_report_pnl_table(strategy_code)
        else:
            print('Generating Statistics for already fetched P&L data...')

        # get pnl data and cleanup as per quantstats format
        _returns_df = self.pnl_data[['entry_timestamp', 'pnl_absolute']]
        _returns_df = _returns_df.set_index('entry_timestamp')
        _returns_df["total_funds"] = _returns_df.pnl_absolute.cumsum() + initial_funds
        _returns_df = _returns_df.dropna()

        # Note: Quantstats has a potential bug. It cannot work with multiple entries having the same timestamp. For now, we are dropping multiple entries with the same entry_timestamp (else the quantstats code below would throw an error)
        # Suggestion for workaround: For entries with same entry timestamps, we can slightly modify the entry timestamps by adding single-digit microseconds to make them unique
        _returns_df = _returns_df[~_returns_df.index.duplicated(keep='first')]

        # Extract the final column; note: timestamp is the index so that is available too
        total_funds_series = _returns_df.total_funds

        # select report type
        if report == "metrics":
            order_report = qs.reports.metrics(total_funds_series)
        elif report == "full":
            order_report = qs.reports.full(total_funds_series)

        # save as html file
        if html_dump:
            all_strategies = self.get_all_strategies()
            strategy_name = all_strategies.loc[all_strategies['strategyCode'] == strategy_code]['strategyName'].iloc[0]
            qs.reports.html(total_funds_series, title=strategy_name, output='', download_filename=f'report_{strategy_name}_{time.time():.0f}.html')

        return order_report

    def get_backtesting_report_order_history(self, strategy_code):
        """
        Fetch Back Testing order history

        Args:
            strategy_code: strategy code

        Returns:
            Report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING, report_type=TradingReportType.ORDER_HISTORY)

    def papertrade(self, strategy_code, start_time, end_time, instrument, lots, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY):
        """
        Start a paper trading session

        Args:
            strategy_code: Strategy code
            start_time: Start time
            end_time: End time
            instrument: Instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: Parameters
            candle_interval: Candle interval
            strategy_mode: Intraday or delivery

        Returns:
            job status
        """
        # Sanity checks - Validate config parameters
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(start_time, dt), f'Argument "start_time" should be an instance of type datetime.datetime'
        assert isinstance(end_time, dt), f'Argument "end_time" should be an instance of type datetime.datetime'
        assert isinstance(instrument, str), f'Argument "instrument" should be a string. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(lots, int) and lots > 0), f'Argument "lots" should be a positive integer.'
        assert isinstance(strategy_parameters, dict), f'Argument "strategy_parameters" should be a dict'
        assert isinstance(strategy_mode, StrategyMode), f'Argument "strategy_mode" should be enum of type StrategyMode'
        assert isinstance(candle_interval, CandleInterval), f'Argument "candle_interval" should be an enum of type CandleInterval'

        # Restructuring strategy params
        restructured_strategy_parameters = []
        for _ in strategy_parameters:
            restructured_strategy_parameters.append({
                'paramName': _,
                'paramValue': strategy_parameters[_]
            })

        instrument_id = None
        instrument_results = self.search_instrument(instrument.split(':')[-1])
        for _ in instrument_results:
            if _["value"] == instrument:
                instrument_id = _["id"]
                break

        # Setup config for Paper Trading
        strategy_config = {
            'instruments': {
                'instruments': [{'id': instrument_id}]
            },
            'lots': lots,
            'userParams': restructured_strategy_parameters,
            'candleDuration': candle_interval.value,
            'strategyMode': strategy_mode.value}
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config, trading_type=TradingType.PAPERTRADING)

        # Submit Paper Trading job
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, start_timestamp=start_time, end_timestamp=end_time, trading_type=TradingType.PAPERTRADING, lots=lots)

    def get_papertrading_job_status(self, strategy_code):
        """
        Get Paper Trading job status

        Args:
            strategy_code: Strategy code

        Returns:
            Job status
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_job_status(strategy_code, TradingType.PAPERTRADING)

    def stop_papertrading_job(self, strategy_code):
        """
        Stop the Paper Trading session

        Args:
            strategy_code: Strategy code

        Returns:
            None
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING)

    def get_papertrading_logs(self, strategy_code):
        """
        Fetch Paper Trading logs

        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_logs(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING)

    def get_papertrading_report_pnl_table(self, strategy_code, show_all_rows=False):
        """
        Fetch Paper Trading Profit & Loss details

        Args:
            strategy_code: Strategy code
            show_all_rows: True or False

        Returns:
            Report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, report_type=TradingReportType.PNL_TABLE, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_papertrading_report_statistics(self, strategy_code):
        """
        Fetch Paper Trading report statistics

        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, report_type=TradingReportType.STATS_TABLE, render_as_dataframe=True)

    def get_papertrading_report_order_history(self, strategy_code):
        """
        Fetch Paper Trading order history

        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, report_type=TradingReportType.ORDER_HISTORY)

    def realtrade(self, strategy_code, start_time, end_time, instrument, lots, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY):
        """
        Start a Real Trading session

        Args:
            strategy_code: Strategy code
            start_time: Start time
            end_time: End time
            instrument: Instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: Parameters
            candle_interval: Candle interval
            strategy_mode: Intraday or delivery

        Returns:
            job status
        """
        print(MESSAGE_REALTRADING_FORBIDDEN)

    def get_realtrading_job_status(self, strategy_code):
        """
        Fetch Real Trading job status

        Args:
            strategy_code: Strategy code

        Returns:
            Job status
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_job_status(strategy_code, TradingType.REALTRADING)

    def stop_realtrading_job(self, strategy_code):
        """
        Stop the Real Trading session

        Args:
            strategy_code: Strategy code

        Returns:
            None
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.REALTRADING)

    def get_realtrading_logs(self, strategy_code):
        """
        Fetch Real Trading logs

        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_logs(strategy_code=strategy_code, trading_type=TradingType.REALTRADING)

    def get_realtrading_report_pnl_table(self, strategy_code, show_all_rows=False):
        """
        Fetch Real Trading Profit & Loss table
        Args:
            strategy_code: Strategy code
            show_all_rows: True or False

        Returns:
            Report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, report_type=TradingReportType.PNL_TABLE, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_realtrading_report_statistics(self, strategy_code):
        """
        Fetch Real Trading report statistics
        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, report_type=TradingReportType.STATS_TABLE, render_as_dataframe=True)

    def get_realtrading_report_order_history(self, strategy_code):
        """
        Fetch Real Trading order history
        Args:
            strategy_code: Strategy code

        Returns:
            Report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, report_type=TradingReportType.ORDER_HISTORY)


def pandas_dataframe_all_rows():
    """

    Returns: None

    """
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
