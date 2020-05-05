import inspect
import json
from datetime import datetime as dt, time

import pandas as pd

from .api import AlgoBullsAPI
from .exceptions import AlgoBullsAPIBadRequest
from ..constants import StrategyMode, TradingType, TradingReportType, AlgoBullsJobStatusEnum, AlgoBullsJobSubmissionResponseEnum, CandleIntervalEnum
from ..strategy.strategy_base import StrategyBase


class AlgoBullsConnection:
    def __init__(self):
        self.api = AlgoBullsAPI()

    def get_authorization_url(self):
        print('This is not implemented YET!!!')
        return 'http://127.0.0.1:8000/login/'

    def set_access_token(self, access_token):
        self.api.set_access_token(access_token)

    def upload_strategy(self, strategy, strategy_code=None):
        """
        Method to upload new strategy (if strategy_code is None) or update existing strategy (if strategy_code is not None)
        """

        # Check for type
        assert issubclass(strategy, StrategyBase), f'strategy should be a subclass of class StrategyBase. Got class of type: type{strategy}'

        # Validate class by creating an instance
        print('Validating Strategy...')
        strategy()

        # Get source code, and upload as new strategy (if strategy_code is None) else edit same strategy
        strategy_name = strategy.name()
        strategy_details = inspect.getsource(strategy)

        if strategy_code is None:
            # If strategy code is None, create a new strategy object
            response = self.api.upload_strategy(strategy_name=strategy_name, strategy_details=strategy_details, abc_version=strategy.versions_supported())
        else:
            # If strategy code is available, update the existing strategy
            response = self.api.update_strategy(strategy_code=strategy_code, strategy_name=strategy_name, strategy_details=strategy_details, abc_version=strategy.versions_supported())
        return response

    def get_all_strategies(self):
        response = self.api.get_all_strategies()
        if isinstance(response['details'], list):
            return pd.DataFrame(response['details'])
        else:
            return response

    def get_strategy_details(self, strategy_code):
        try:
            response = self.api.get_strategy_details(strategy_code)
            strategy_code = response['details']
            return strategy_code
        except AlgoBullsAPIBadRequest:
            print(f'ERROR: No strategy found with ID: {strategy_code}')

    def search_instrument(self, instrument):
        assert (isinstance(instrument, str) is True), f'Argument instrument should be a string'
        response = self.api.search_instrument(instrument)['details']
        return response

    def get_job_status(self, strategy_code, trading_type):
        """
        Gets job status for given strategy_code and trading_type
        """
        response = self.api.get_job_status(strategy_code=strategy_code, trading_type=trading_type)
        if response.get('success') is True:
            return AlgoBullsJobStatusEnum(response['details'])
        else:
            return AlgoBullsJobSubmissionResponseEnum.ERROR, response

    def stop_job(self, strategy_code, trading_type):
        response = self.api.stop_strategy_algotrading(strategy_code=strategy_code, trading_type=trading_type)
        if response.get('success') is True:
            return AlgoBullsJobSubmissionResponseEnum(response['details'])
        else:
            return AlgoBullsJobSubmissionResponseEnum.ERROR, response

    def get_report(self, strategy_code, trading_type, report_type, render_as_dataframe=False, show_all_rows=False):
        response = self.api.get_reports(strategy_code=strategy_code, trading_type=trading_type, report_type=report_type)
        if response.get('success') is True:
            if render_as_dataframe:
                if show_all_rows:
                    pandas_dataframe_all_rows()
                _response = pd.DataFrame(response['detaills'])
            else:
                _response = response['details']
            return _response
        else:
            return AlgoBullsJobSubmissionResponseEnum.ERROR, response

    def backtest(self, strategy_code, start_timestamp, end_timestamp, instrument_id, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY.value):
        # Validate config parameters
        assert (isinstance(strategy_code, str) is True), f'Argument strategy_code should be a string'
        assert (isinstance(start_timestamp, dt) is True), f'Argument start_timestamp should be an instance of type datetime.datetime'
        assert (isinstance(end_timestamp, dt) is True), f'Argument start_timestamp should be an instance of type datetime.datetime'
        assert (isinstance(instrument_id, int) is True), f'Argument instrument_id should be a integer. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(strategy_parameters, dict) is True), f'Argument strategy_parameters should be a dict'
        assert ((strategy_mode in [_strategy_mode.value for _strategy_mode in StrategyMode]) is True), f'Argument strategy_mode should be a string'
        assert (isinstance(candle_interval, CandleIntervalEnum)), f'Argument candle_interval should be an enum of type CandleIntervalEnum'

        # Setup config for backtesting
        strategy_config = {'trading_start_date': start_timestamp.date(), 'trading_start_time': start_timestamp.time(),
                           'trading_end_date': end_timestamp.date(), 'trading_end_time': end_timestamp.time(),
                           'instrument': instrument_id,
                           'parameters': json.dumps(strategy_parameters),
                           'candle_interval': candle_interval.value,
                           'strategy_mode': strategy_mode}
        print('Setting Strategy Config...', end=' ')
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config)
        print('Success.')

        # Submit backtesting job
        print('Submitting Backtesting Job...', end=' ')
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING.value)
        print('Success.')

        if response.get('success') is True:
            return AlgoBullsJobSubmissionResponseEnum(response['details'])
        else:
            return AlgoBullsJobSubmissionResponseEnum.ERROR, response

    def get_backtesting_job_status(self, strategy_code):
        """
        Gets BACKTESTING job status for given strategy_code
        """
        return self.get_job_status(strategy_code, TradingType.BACKTESTING.value)

    def stop_backtesting_job(self, strategy_code):
        """
        Gets BACKTESTING job status for given strategy_code
        """
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING.value)

    def get_backtesting_logs(self, strategy_code):
        return self.get_report(strategy_code, trading_type=TradingType.BACKTESTING.value, report_type=TradingReportType.LOGS)

    def get_backtesting_report_pnl_table(self, strategy_code, show_all_rows=False):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING.value, report_type=TradingReportType.PNL_TABLE.value, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_backtesting_report_statistics(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING.value, report_type=TradingReportType.STATS_TABLE.value, render_as_dataframe=True)

    def get_backtesting_report_order_history(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING.value, report_type=TradingReportType.ORDER_HISTORY.value)

    def papertest(self, strategy_code, start_time, end_time, instrument_id, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY.value):
        # Validate config parameters
        assert (isinstance(strategy_code, str) is True), f'Argument strategy_code should be a string'
        assert (isinstance(start_time, time) is True), f'Argument start_timestamp should be an instance of type datetime.datetime'
        assert (isinstance(end_time, time) is True), f'Argument start_timestamp should be an instance of type datetime.datetime'
        assert (isinstance(instrument_id, int) is True), f'Argument instrument_id should be a integer. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(strategy_parameters, dict) is True), f'Argument strategy_parameters should be a dict'
        assert ((strategy_mode in [_strategy_mode.value for _strategy_mode in StrategyMode]) is True), f'Argument strategy_mode should be a string'
        assert (isinstance(candle_interval, CandleIntervalEnum)), f'Argument candle_interval should be an enum of type CandleIntervalEnum'

        # Setup config for Paper Trading
        strategy_config = {'trading_start_time': start_time,
                           'trading_end_time': end_time,
                           'instrument': instrument_id,
                           'parameters': json.dumps(strategy_parameters),
                           'candle_interval': candle_interval.value,
                           'strategy_mode': strategy_mode}
        print('Setting Strategy Config...', end=' ')
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config)
        print('Success.')

        # Submit Paper Trading job
        print('Submitting Paper Trading Job...', end=' ')
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING.value)
        print('Success.')

        if response.get('success') is True:
            return AlgoBullsJobSubmissionResponseEnum(response['details'])
        else:
            return AlgoBullsJobSubmissionResponseEnum.ERROR, response

    def get_papertrading_job_status(self, strategy_code):
        return self.get_job_status(strategy_code, TradingType.PAPERTRADING.value)

    def stop_papertrading_job(self, strategy_code):
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING.value)

    def get_papertrading_logs(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING.value, report_type=TradingReportType.LOGS.value)

    def get_papertrading_report_pnl_table(self, strategy_code, show_all_rows=False):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING.value, report_type=TradingReportType.PNL_TABLE.value, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_papertrading_report_statistics(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING.value, report_type=TradingReportType.STATS_TABLE.value, render_as_dataframe=True)

    def get_papertrading_report_order_history(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING.value, report_type=TradingReportType.ORDER_HISTORY.value)

    def realtrade(self, strategy_code, start_time, end_time, instrument_id, strategy_parameters, candle_interval, strategy_mode=StrategyMode.INTRADAY.value):
        # Validate config parameters
        assert (isinstance(strategy_code, str) is True), f'Argument strategy_code should be a string'
        assert (isinstance(start_time, time) is True), f'Argument start_time should be an instance of type datetime.time'
        assert (isinstance(end_time, time) is True), f'Argument end_time should be an instance of type datetime.time'
        assert (isinstance(instrument_id, int) is True), f'Argument instrument_id should be a integer. You can find the right id using the \'get_instrument()\' method of AlgoBullsConnection class'
        assert (isinstance(strategy_parameters, dict) is True), f'Argument strategy_parameters should be a dict'
        assert ((strategy_mode in [_strategy_mode.value for _strategy_mode in StrategyMode]) is True), f'Argument strategy_mode should be a string'
        assert (isinstance(candle_interval, CandleIntervalEnum)), f'Argument candle_interval should be an enum of type CandleIntervalEnum'

        # Setup config for backtesting
        strategy_config = {'trading_start_time': start_time,
                           'trading_end_time': end_time,
                           'instrument': instrument_id,
                           'parameters': json.dumps(strategy_parameters),
                           'candle_interval': candle_interval.value,
                           'strategy_mode': strategy_mode}
        print('Setting Strategy Config...', end=' ')
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config)
        print('Success.')

        # Submit Real Trading job
        print('Submitting Real Trading Job...', end=' ')
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, trading_type=TradingType.REALTRADING.value)
        print('Success.')

        if response.get('success') is True:
            return AlgoBullsJobSubmissionResponseEnum(response['details'])
        else:
            return AlgoBullsJobSubmissionResponseEnum.ERROR, response

    def get_realtrading_job_status(self, strategy_code):
        return self.get_job_status(strategy_code, TradingType.REALTRADING.value)

    def stop_realtrading_job(self, strategy_code):
        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.REALTRADING.value)

    def get_realtrading_logs(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING.value, report_type=TradingReportType.LOGS.value)

    def get_realtrading_report_pnl_table(self, strategy_code, show_all_rows=False):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING.value, report_type=TradingReportType.PNL_TABLE.value, render_as_dataframe=True, show_all_rows=show_all_rows)

    def get_realtrading_report_statistics(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING.value, report_type=TradingReportType.STATS_TABLE.value, render_as_dataframe=True)

    def get_realtrading_report_order_history(self, strategy_code):
        return self.get_report(strategy_code=strategy_code, trading_type=TradingType.REALTRADING.value, report_type=TradingReportType.ORDER_HISTORY.value)


def pandas_dataframe_all_rows():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
