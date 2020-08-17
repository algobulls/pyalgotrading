"""
Module for AlgoBulls connection
"""
import inspect
from datetime import datetime as dt, time

import pandas as pd

from .api import AlgoBullsAPI
from .exceptions import AlgoBullsAPIBadRequest
from ..constants import StrategyMode, TradingType, TradingReportType, CandleInterval
from ..strategy.strategy_base import StrategyBase



class AlgoBullsConnection:
    """
    Class for AlgoBulls connection
    """

    def __init__(self):
        """
        Init method that is used while creating an object of this class
        """
        self.api = AlgoBullsAPI()

    @staticmethod
    def get_authorization_url():
        """
        Fetches the authorization URL
        Returns:
            authorization URL
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
        assert (isinstance(access_token, str) is True), f'Argument "access_token" should be a string'
        self.api.set_access_token(access_token)

    def create_strategy(self, strategy, overwrite=False):
        """
        Method to upload new strategy.

        All strategies are unique by name, per customer.
        If customer tries to upload strategy with the same name as an already existing strategy -
        if overwrite is False:
            - AlgoBullsAPIBadRequest Exception will be thrown. No change would be done in the backend database.
        If overwrite is True,
            - Existing strategy with strategy_name would be overwritten. No exception will be thrown.
        """

        # Sanity checks
        assert issubclass(strategy, StrategyBase), f'strategy should be a subclass of class StrategyBase. Got class of type: type{strategy}'

        # Validate class by creating an instance
        print('Validating Strategy...')
        strategy()

        # Get source code, and upload as new strategy (if strategy_code is None) else edit same strategy
        strategy_name = strategy.name()
        strategy_details = inspect.getsource(strategy)
        abc_version = strategy.versions_supported().value

        # If strategy code is None, create a new strategy object
        try:
            response = self.api.create_strategy(strategy_name=strategy_name, strategy_details=strategy_details, abc_version=abc_version)
        except AlgoBullsAPIBadRequest as ex:
            if overwrite is True:
                # If strategy code is available, update the existing strategy
                response = self.api.update_strategy(strategy_name=strategy_name, strategy_details=strategy_details, abc_version=abc_version)
            else:
                print(f'Error uploading strategy. Details:\n{ex}')
                return

        return response

    def get_all_strategies(self):
        """
        Fetch all available strategies
        Returns:
            list of available strategies
        """
        response = self.api.get_all_strategies()
        if isinstance(response['data'], list):
            return pd.DataFrame(response['data'])
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
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'

        try:
            response = self.api.get_strategy_details(strategy_code)
            strategy_code = response['data']
            return strategy_code
        except AlgoBullsAPIBadRequest:
            print(f'ERROR: No strategy found with ID: {strategy_code}')

    def search_instrument(self, instrument):
        """
        Search for an instrument
        Args:
            instrument: instrument key

        Returns:
            True or False
        """
        assert (isinstance(instrument, str) is True), f'Argument "instrument" should be a string'
        response = self.api.search_instrument(instrument).get('data')
        return response

    def get_job_status(self, strategy_code, trading_type):
        """
        Gets job status for given strategy_code and trading_type
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(trading_type, TradingType) is True), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

        response = self.api.get_job_status(strategy_code=strategy_code, trading_type=trading_type)
        return response

    def stop_job(self, strategy_code, trading_type):
        """
        Stops a job
        Args:
            strategy_code: strategy code
            trading_type: trading type

        Returns:
            job status
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(trading_type, TradingType) is True), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

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
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(trading_type, TradingType) is True), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

        return self.api.get_logs(strategy_code=strategy_code, trading_type=trading_type).get('data')

    def get_report(self, strategy_code, trading_type, report_type, render_as_dataframe=False, show_all_rows=False):
        """
        Fetch report for a strategy

        Args:
            strategy_code: strategy code
            trading_type: trading type
            report_type: report type
            render_as_dataframe: True or False
            show_all_rows: True or False

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(trading_type, TradingType) is True), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'
        assert (isinstance(report_type, TradingReportType) is True), f'Argument "report_type" should be an enum of type {TradingReportType.__name__}'
        assert (isinstance(render_as_dataframe, bool) is True), f'Argument "render_as_dataframe" should be a bool'
        assert (isinstance(show_all_rows, bool) is True), f'Argument "show_all_rows" should be a bool'
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
            strategy_code: strategy code
            start_timestamp: start date/time
            end_timestamp: end date/time
            instrument: instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: parameters
            candle_interval: candle interval
            strategy_mode: intraday or delivery

        Returns:
            backtest job submission status
        """
        # Sanity checks - Validate config parameters
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(start_timestamp, dt) is True), f'Argument "start_timestamp" should be an instance of type datetime.datetime'
        assert (isinstance(end_timestamp, dt) is True), f'Argument "start_timestamp" should be an instance of type datetime.datetime'
        assert (isinstance(instrument, str) is True), f'Argument "instrument" should be a string. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(lots, int) is True and lots > 0), f'Argument "lots" should be a positive integer.'
        assert (isinstance(strategy_parameters, dict) is True), f'Argument "strategy_parameters" should be a dict'
        assert (isinstance(strategy_mode, StrategyMode) is True), f'Argument "strategy_mode" should be enum of type StrategyMode'
        assert (isinstance(candle_interval, CandleInterval)), f'Argument "candle_interval" should be an enum of type CandleInterval'

        # Setup config for Backtesting
        strategy_config = {'tradingTime': [start_timestamp.strftime('%d-%m-%Y %H:%M'), end_timestamp.strftime('%d-%m-%Y %H:%M')],
                           'instruments': [instrument],
                           'lots': lots,
                           'parameters': strategy_parameters,
                           'candle': candle_interval.value,
                           'strategyMode': strategy_mode.value}
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config, trading_type=TradingType.BACKTESTING)

        # Submit Backtesting job
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING)

    def get_backtesting_job_status(self, strategy_code):
        """
        Gets BACKTESTING job status for given strategy_code
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_job_status(strategy_code, TradingType.BACKTESTING)

    def stop_backtesting_job(self, strategy_code):
        """
        Stops the BACKTESTING job
        Args:
            strategy_code: Strategy Code / ID

        Returns:
            None
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING)

    def get_backtesting_logs(self, strategy_code):
        """
        Fetch backtesting logs
        Args:
            strategy_code:

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_logs(strategy_code, trading_type=TradingType.BACKTESTING)

    def get_backtesting_report_pnl_table(self, strategy_code, show_all_rows=False):
        """
        Fetch backtesting Profit / Loss details
        Args:
            strategy_code: strategy code
            show_all_rows: True or False

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING, report_type=TradingReportType.PNL_TABLE, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_backtesting_report_statistics(self, strategy_code):
        """
        Fetch backtesting report statistics
        Args:
            strategy_code: strategy code

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING, report_type=TradingReportType.STATS_TABLE, render_as_dataframe=True)

    def get_backtesting_report_order_history(self, strategy_code):
        """
        Fetch backtesting order history
        Args:
            strategy_code: strategy code

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING, report_type=TradingReportType.ORDER_HISTORY)

    def papertrade(self, strategy_code, start_time, end_time, instrument, lots, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY):
        """
        Start a paper trading session
        Args:
            strategy_code: strategy code
            start_time: start time
            end_time: end time
            instrument: instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: parameters
            candle_interval: candle interval
            strategy_mode: intraday or delivery

        Returns:
            job status
        """
        # Sanity checks - Validate config parameters
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(start_time, time) is True), f'Argument "start_timestamp" should be an instance of type datetime.datetime'
        assert (isinstance(end_time, time) is True), f'Argument "start_timestamp" should be an instance of type datetime.datetime'
        assert (isinstance(instrument, str) is True), f'Argument "instrument" should be a string. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(lots, int) is True and lots > 0), f'Argument "lots" should be a positive integer.'
        assert (isinstance(strategy_parameters, dict) is True), f'Argument "strategy_parameters" should be a dict'
        assert (isinstance(strategy_mode, StrategyMode) is True), f'Argument "strategy_mode" should be enum of type StrategyMode'
        assert (isinstance(candle_interval, CandleInterval)), f'Argument "candle_interval" should be an enum of type CandleInterval'

        # Setup config for Paper Trading
        strategy_config = {'tradingTime': [start_time.strftime('%H:%M'), end_time.strftime('%H:%M')],
                           'instruments': [instrument],
                           'lots': lots,
                           'parameters': strategy_parameters,
                           'candle': candle_interval.value,
                           'strategyMode': strategy_mode.value}
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config, trading_type=TradingType.PAPERTRADING)

        # Submit Paper Trading job
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING)

    def get_papertrading_job_status(self, strategy_code):
        """
        Get papertrading job status
        Args:
            strategy_code:

        Returns:
            job status
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_job_status(strategy_code, TradingType.PAPERTRADING)

    def stop_papertrading_job(self, strategy_code):
        """
        Stop the papertrading session
        Args:
            strategy_code: strategy code

        Returns:
            None
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING)

    def get_papertrading_logs(self, strategy_code):
        """
        Fetch papertrading logs
        Args:
            strategy_code: strategy code

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_logs(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING)

    def get_papertrading_report_pnl_table(self, strategy_code, show_all_rows=False):
        """
        Fetch papertrading Profit / Loss details
        Args:
            strategy_code: strategy code
            show_all_rows: True or False

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, report_type=TradingReportType.PNL_TABLE, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_papertrading_report_statistics(self, strategy_code):
        """
        Fetch papertrading report statistics
        Args:
            strategy_code: strategy code

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, report_type=TradingReportType.STATS_TABLE, render_as_dataframe=True)

    def get_papertrading_report_order_history(self, strategy_code):
        """
        Fetch papertrading order history
        Args:
            strategy_code: strategy code

        Returns:
            report details
        """
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, report_type=TradingReportType.ORDER_HISTORY)

    def realtrade(self, strategy_code, start_time, end_time, instrument, lots, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY):
        """
        Start a realtrading session
        Args:
            strategy_code: strategy code
            start_time: start time
            end_time: end time
            instrument: instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: parameters
            candle_interval: candle interval
            strategy_mode: intraday or delivery

        Returns:
            job status
        """
        # Sanity checks - Validate config parameters
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        assert (isinstance(start_time, time) is True), f'Argument "start_time" should be an instance of type datetime.time'
        assert (isinstance(end_time, time) is True), f'Argument "end_time" should be an instance of type datetime.time'
        assert (isinstance(instrument, str) is True), f'Argument "instrument" should be a string. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(lots, int) is True and lots > 0), f'Argument "lots" should be a positive integer.'
        assert (isinstance(strategy_parameters, dict) is True), f'Argument "strategy_parameters" should be a dict'
        assert (isinstance(strategy_mode, StrategyMode) is True), f'Argument "strategy_mode" should be enum of type StrategyMode'
        assert (isinstance(candle_interval, CandleInterval)), f'Argument "candle_interval" should be an enum of type CandleInterval'

        # Setup config for backtesting
        strategy_config = {'tradingTime': [start_time.strftime('%H:%M'), end_time.strftime('%H:%M')],
                           'instruments': [instrument],
                           'lots': lots,
                           'parameters': strategy_parameters,
                           'candle': candle_interval.value,
                           'strategyMode': strategy_mode.value}
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config, trading_type=TradingType.REALTRADING)

        # Submit Real Trading job
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, trading_type=TradingType.REALTRADING)

    def get_realtrading_job_status(self, strategy_code):
        """
        Fetch realtrading job status
        Args:
            strategy_code: strategy code

        Returns:
            job status
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'

        return self.get_job_status(strategy_code, TradingType.REALTRADING)

    def stop_realtrading_job(self, strategy_code):
        """
        Stop the realtrading session
        Args:
            strategy_code: strategy code

        Returns:
            None
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.REALTRADING)

    def get_realtrading_logs(self, strategy_code):
        """
        Fetch realtrading logs
        Args:
            strategy_code: strategy code

        Returns:
            report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'

        return self.get_logs(strategy_code=strategy_code, trading_type=TradingType.REALTRADING)

    def get_realtrading_report_pnl_table(self, strategy_code, show_all_rows=False):
        """
        Fetch realtrading Profit / Loss table
        Args:
            # broker: broker name
            strategy_code: strategy code
            show_all_rows: True or False

        Returns:
            report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, report_type=TradingReportType.PNL_TABLE, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_realtrading_report_statistics(self, strategy_code):
        """
        Fetch realtrading report statistics
        Args:
            # broker: broker name
            strategy_code: strategy code

        Returns:
            report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'

        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, report_type=TradingReportType.STATS_TABLE, render_as_dataframe=True)

    def get_realtrading_report_order_history(self, strategy_code):
        """
        Fetch realtrading order history
        Args:
            # broker: broker name
            strategy_code: strategy code

        Returns:
            report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert (isinstance(strategy_code, str) is True), f'Argument "strategy_code" should be a string'

        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, report_type=TradingReportType.ORDER_HISTORY)


def pandas_dataframe_all_rows():
    """

    Returns: None

    """
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
