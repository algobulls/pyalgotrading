"""
Module for AlgoBulls connection
"""
import inspect
import os
import pprint
import re
import time
from collections import OrderedDict
from datetime import datetime as dt

import pandas as pd
import quantstats as qs
from tabulate import tabulate
from tqdm.auto import tqdm

from .api import AlgoBullsAPI
from .exceptions import AlgoBullsAPIBadRequestException, AlgoBullsAPIGatewayTimeoutErrorException, AlgoBullsAPIUnauthorizedErrorException
from ..constants import StrategyMode, TradingType, TradingReportType, CandleInterval, AlgoBullsEngineVersion, Country, ExecutionStatus, EXCHANGE_LOCALE_MAP, Locale, CandleIntervalSecondsMap
from ..strategy.strategy_base import StrategyBase
from ..utils.func import get_valid_enum_names, get_datetime_with_tz, calculate_brokerage, calculate_slippage


class AlgoBullsConnection:
    """
    Class for AlgoBulls connection
    """

    def __init__(self):
        """
        Init method that is used while creating an object of this class
        """
        self.api = AlgoBullsAPI(self)

        self.saved_parameters = {
            'start_timestamp_map': {},
            'end_timestamp_map': {}
        }

        self.strategy_country_map = {
            TradingType.BACKTESTING: {},
            TradingType.PAPERTRADING: {},
            TradingType.REALTRADING: {},
        }

        self.backtesting_pnl_data = None
        self.papertrade_pnl_data = None
        self.realtrade_pnl_data = None

    @staticmethod
    def get_authorization_url():
        """
        Fetch the authorization URL

        Returns:
            Authorization URL
        """
        url = 'https://app.algobulls.com/user/login'
        print(f'Please login to this URL with your AlgoBulls credentials and get your developer access token: {url}')

    @staticmethod
    def get_token_url():
        """
        Fetch the token URL

        Returns:
            Token URL
        """
        url = 'https://app.algobulls.com/settings?section=developerOptions'
        print(f'Please login to this URL to get your unique token: {url}')

    def set_access_token(self, access_token, validate_token=True):
        """
        Set the access token

        Args:
            access_token: access token
            validate_token: whether you want to validate the access-token
        Returns:
            None
        """
        assert isinstance(access_token, str), f'Argument "access_token" should be a string'
        self.api.set_access_token(access_token)

        if validate_token:
            try:
                _ = self.api.get_all_strategies()
                print("Access token is valid.")
            except AlgoBullsAPIUnauthorizedErrorException:
                print(f"Access token is invalid. ", end='')
                self.get_token_url()

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

    def get_strategy_name(self, strategy_code):
        """
        Fetch the name of the strategy using strategy-code

        Args:
            strategy_code: strategy code

        Returns:
            name of the strategy
        """
        strategy_name = None
        try:
            # TODO: Currently fetching strategy name over API everytime. Will be optimized in future to avoid repeated API calls.
            all_strategies_df = self.get_all_strategies()
            strategy_name = all_strategies_df.loc[all_strategies_df['strategyCode'] == strategy_code].iloc[0]['strategyName']

        except Exception as ex:
            print(f'Error while fetching strategy name of strategy code {strategy_code}. Error: {ex}')
        return strategy_name

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
        except AlgoBullsAPIBadRequestException:
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

    def delete_previous_trades(self, strategy):
        """
        Delete all the previous trades and clear the pnl table

        Args:
            strategy: Strategy code
        """

        response = {}
        for _ in range(30):
            try:
                response = self.api.delete_previous_trades(strategy)
                print(response.get('message'))
                break
            except AlgoBullsAPIGatewayTimeoutErrorException as ex:
                print(f'Deleting previous trades... in process... (attempt {_})\n{ex}')
                time.sleep(1)

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

        self.api.stop_strategy_algotrading(strategy_code=strategy_code, trading_type=trading_type)

    def get_logs(self, strategy_code, trading_type, display_progress_bar=True, print_live_logs=False):
        """
        Fetch logs for a strategy

        Args:
            strategy_code: strategy code
            trading_type: trading type
            display_progress_bar: to track the execution progress bar as your strategy is executed
            print_live_logs: to print the logs as they are fetched
        Returns:
            Execution logs
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(trading_type, TradingType), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'

        # TODO: to extract timestamp from a different source which will be independent of whether save parameters are present in the object
        start_timestamp_map = self.saved_parameters.get('start_timestamp_map')
        end_timestamp_map = self.saved_parameters.get('end_timestamp_map')
        sleep_time = 1
        total_seconds = 1

        # calculate the sleep time for RT and PT
        if trading_type is not TradingType.BACKTESTING:
            try:
                sleep_time = CandleIntervalSecondsMap[self.saved_parameters.get('candle_interval').value]
                print(f"Your candle interval is {self.saved_parameters.get('candle_interval').value}, therefore logs will be fetched every {sleep_time} seconds.")
            except AttributeError:
                print("WARNING: Could not fetch the candle interval from saved parameters. Logs will be fetched every 60 seconds.")
                sleep_time = 60

        # initialize the parameters required for displaying progress bar
        if display_progress_bar:
            if start_timestamp_map.get(trading_type) and end_timestamp_map.get(trading_type):
                start_timestamp = start_timestamp_map.get(trading_type).replace(tzinfo=None)
                end_timestamp = end_timestamp_map.get(trading_type).replace(tzinfo=None)
                total_seconds = (end_timestamp - start_timestamp).total_seconds()
            else:
                display_progress_bar = False

        # initialize all the variables
        all_logs = ''
        tqdm_progress_bar = None
        initial_next_token = None
        error_counter = 0
        status = None
        count_starting_status = 0
        response = {}
        logs = []

        while True:
            # if logs are in starting phase, we wait until it changes
            if status is None or status == ExecutionStatus.STARTING.value:
                status = self.get_job_status(strategy_code, trading_type)["message"]
                time.sleep(5)

                # log the counting for "STARTING" phase of execution
                if status == ExecutionStatus.STARTING.value:
                    count_starting_status += 1
                    print('\r', end=f'Looking for a dedicated virtual server to execute your strategy... ({count_starting_status})')
                continue

            # if logs get in started phase, we initialize the tqdm object for progress tracking
            if display_progress_bar:
                if tqdm_progress_bar is None and status == ExecutionStatus.STARTED.value:
                    tqdm_progress_bar = tqdm(desc='Execution Progress', total=total_seconds, position=0, leave=True, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]')

            # try the logs API 5 times or until it succeeds
            for i in range(5):
                try:
                    response = self.api.get_logs(strategy_code=strategy_code, trading_type=trading_type, initial_next_token=initial_next_token)
                    logs = response.get('data')
                    if logs:
                        break
                except AlgoBullsAPIGatewayTimeoutErrorException:
                    tqdm.write(f"\n{'----' * 10}\nFaced an error while fetching logs.\n{'----' * 10}\n")
                    time.sleep(5)

            initial_next_token = response.get('nextForwardToken')

            # if logs are empty we validate the status of execution
            if not logs:
                status = self.get_job_status(strategy_code, trading_type)["message"]

                # if status is stopped we break the while loop
                if status in [ExecutionStatus.STOPPED.value, ExecutionStatus.STOPPING.value]:

                    # tqdm.write(f"INFO: Got status as {status}, strategy execution completed.")    # for debug
                    if display_progress_bar:
                        if tqdm_progress_bar is not None:
                            tqdm_progress_bar.close()
                    break

                # continue if logs are not fetched
                else:
                    time.sleep(5)

                    # tqdm.write(f"WARNING: got no data, current status is {status}...")      # for debug
                    continue

            else:
                # incoming logs are in list, merge them to string
                if type(logs) is list and initial_next_token:
                    all_logs += ''.join(logs)

                # print the logs below progressbar
                if print_live_logs:
                    tqdm.write(''.join(logs))

                # iterate in reverse order
                if display_progress_bar:
                    for log in logs[::-1]:
                        try:
                            # extract log terms inside square brackets
                            _ = re.findall(r'\[(.*?)\]', log)

                            # extract datetime from logs
                            if tqdm_progress_bar is not None and _[0] in ['BT', 'PT', 'RT']:
                                current_timestamp = dt.strptime(_[1].split(',')[0], '%Y-%m-%d %H:%M:%S')
                                total_completion = (current_timestamp - start_timestamp).total_seconds()
                                tqdm_progress_bar.update(total_completion - tqdm_progress_bar.n)
                                break

                        except Exception as ex:
                            tqdm.write(f'WARNING: faced an error while updating logs process. Error: {ex}')
                            error_counter += 1

                    # avoid infinite loop in case of error
                    if error_counter > 5:
                        break

                if len(logs) >= self.api.page_size:
                    # tqdm.write(f"\n{'-----' * 5}\nWaiting {sleep_time} seconds for fetching next logs ...\n{'-----' * 5}\n")  # for debug
                    time.sleep(sleep_time)
                else:
                    time.sleep(1)

        return all_logs

    def get_report_order_history(self, strategy_code, trading_type, render_as_dataframe=False, show_all_rows=True, country=None):
        """
        Fetch report for a strategy

        Args:
            strategy_code: Strategy code
            trading_type: Value of TradingType Enum
            render_as_dataframe: True or False
            show_all_rows: True or False
            country: country of the Exchange

        Returns:
            report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(trading_type, TradingType), f'Argument "trading_type" should be an enum of type {TradingType.__name__}'
        assert isinstance(render_as_dataframe, bool), f'Argument "render_as_dataframe" should be a bool'
        assert isinstance(show_all_rows, bool), f'Argument "show_all_rows" should be a bool'
        # assert (broker is None or isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be None or an enum of type {AlgoBullsSupportedBrokers.__name__}'

        main_data = []
        total_data = 0
        _total = 0
        i = 1

        if country is None:
            country = self.strategy_country_map[trading_type].get(strategy_code, Country.DEFAULT.value)

        while True:
            for _ in range(5):
                try:
                    response = self.api.get_reports(strategy_code=strategy_code, trading_type=trading_type, report_type=TradingReportType.ORDER_HISTORY, country=country, current_page=i)
                    _total = response.get("totalTrades")
                    _data = response.get("data")

                    # if data is retrieved as a list then update the main data
                    if _data and isinstance(_data, list):
                        main_data.extend(_data)
                        total_data += self.api.page_size
                        i += 1
                        break

                except AlgoBullsAPIGatewayTimeoutErrorException:
                    time.sleep(5)

            # break if total requested data is more than total data
            if total_data > _total:
                break

        if main_data:

            # for rendering as dataframe
            if render_as_dataframe:
                pandas_dataframe_all_rows()

                # explode the "customer_tradebook_states" column to get separate rows for every state
                _response = pd.DataFrame(main_data)
                df = _response.explode('customer_tradebook_states').reset_index(drop=True)
                df = df.join(pd.json_normalize(df.pop('customer_tradebook_states')))
                _response = df.set_index("orderId").sort_values("timestamp_created")[["timestamp_created", "transaction_type", "state", "instrument", "quantity", "currency", "price"]]

            # for rendering as string or json
            else:
                _response = main_data
                main_order_string = ""

                for i in range(len(main_data)):
                    # tables for displaying order details and order stats
                    order_detail = [
                        ["Order ID", main_data[i]["orderId"]],
                        ["Transaction Type", main_data[i]["transaction_type"]],
                        ["Instrument", main_data[i]["instrument"]],
                        ["Quantity", main_data[i]["quantity"]],
                        ["Price", str(main_data[i]["currency"]) + str(main_data[i]["price"])]
                    ]
                    main_order_string += tabulate(order_detail, tablefmt="psql") + "\n"
                    main_order_string += tabulate(main_data[i]["customer_tradebook_states"], headers="keys", tablefmt="psql") + "\n"
                    main_order_string += '\n' + '======' * 15 + '\n'

                _response = main_order_string
            return _response
        else:
            print("Report not available yet. Please retry in sometime")

    def get_report_pnl_table(self, strategy_code, trading_type, country, brokerage_percentage=None, brokerage_flat_price=None, slippage_percent=None, show_all_rows=True):
        """
            Fetch BT/PT/RT Profit & Loss details

            Args:
                strategy_code: strategy code
                trading_type: type of trades : Backtesting, Papertrading, Realtrading
                country: country of the exchange
                brokerage_percentage: Percentage of broker commission per trade
                brokerage_flat_price: Broker fee per trade
                slippage_percent: percentage of slippage per order
                show_all_rows: show all rows of the dataframe returned

            Returns:
                Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        # Set the country code
        if country is None:
            country = self.strategy_country_map[trading_type].get(strategy_code, Country.DEFAULT.value)

        # Fetch the data
        response = self.api.get_reports(strategy_code=strategy_code, trading_type=trading_type, report_type=TradingReportType.PNL_TABLE, country=country, current_page=1)
        data = response.get("data")

        if show_all_rows:
            pandas_dataframe_all_rows()

        # Post-processing: Cleanup & converting data to dataframe
        column_rename_map = OrderedDict([
            ('strategy.instrument.segment', 'instrument_segment'),
            ('strategy.instrument.tradingsymbol', 'instrument_tradingsymbol'),
            ('entry.timestamp', 'entry_timestamp'),
            ('entry.isBuy', 'entry_transaction_type'),
            ('entry.quantity', 'entry_quantity'),
            ('entry.prefix', 'entry_currency'),
            ('entry.price', 'entry_price'),
            ('exit.timestamp', 'exit_timestamp'),
            ('exit.isBuy', 'exit_transaction_type'),
            ('exit.quantity', 'exit_quantity'),
            ('exit.prefix', 'exit_currency'),
            ('exit.price', 'exit_price'),
            ('pnlAbsolute.value', 'pnl_absolute')
        ])

        if data:
            # Generate df from json data & perform cleanups
            _df = pd.json_normalize(data[::-1])[list(column_rename_map.keys())].rename(columns=column_rename_map)
            _df[['entry_timestamp', 'exit_timestamp']] = _df[['entry_timestamp', 'exit_timestamp']].apply(pd.to_datetime, format="%Y-%m-%d | %H:%M %z", errors="coerce")
            _df['entry_transaction_type'] = _df['entry_transaction_type'].apply(lambda _: 'BUY' if _ else 'SELL')
            _df['exit_transaction_type'] = _df['exit_transaction_type'].apply(lambda _: 'BUY' if _ else 'SELL')
            _df["pnl_cumulative_absolute"] = _df["pnl_absolute"].cumsum(axis=0, skipna=True)

            # generate slippage data
            if slippage_percent:
                _df = calculate_slippage(pnl_df=_df, slippage_percent=slippage_percent)

            _df = calculate_brokerage(pnl_df=_df, brokerage_percentage=brokerage_percentage, brokerage_flat_price=brokerage_flat_price)
        else:
            # No data available, send back an empty dataframe
            _df = pd.DataFrame(columns=list(column_rename_map.values()))
            _df['net_pnl'] = None

        return _df

    def get_report_statistics(self, strategy_code=None, initial_funds=None, report="full", html_dump=True, pnl_df=None, file_path="None", date_time_format="%Y-%m-%d %H:%M:%S%z"):
        """
            Fetch BT/PT/RT report statistics

            Args:
                strategy_code: strategy code
                report: format and content of the report
                html_dump: save it as a html file
                pnl_df: dataframe containing pnl reports; this parameter will be ignored if file_path is provided
                initial_funds: initial funds to before starting the job
                file_path: file path of the csv or xlsx containing pnl data for statistics; if provided, pnl_df would be ignored
                date_time_format: datetime format of the column inside the "entry_timestamp" column in the csv or xlxs file
            Returns:
                Report details
        """

        # read and validate the csv given in path file
        if os.path.isfile(file_path):
            # only accept csv or xlxs files
            _, _ext = os.path.splitext(file_path)
            if _ext == '.csv':
                pnl_df = pd.read_csv(file_path)
            elif _ext == '.xlxs':
                pnl_df = pd.read_excel(file_path)
            else:
                raise Exception(f'ERROR: File with extension {_ext} is not supported.\n Please provide path to files with extension as ".csv" or ".xlxs"')

            # handle the exceptions gracefully, check the validity of the input file
            if "entry_timestamp" not in pnl_df.columns or "net_pnl" not in pnl_df.columns:
                raise Exception(f"ERROR: Given  {_ext} file does not have the required columns 'entry_timestamp' and 'net_pnl'.")
            try:
                dt.strptime(pnl_df.iloc[0]["entry_timestamp"], date_time_format)
            except ValueError:
                raise ValueError(f"ERROR: Datetime strings inside 'entry_timestamp' column should be of the format {date_time_format}.")

            # cleanup dataframe generated from read files
            pnl_df[['entry_timestamp']] = pnl_df[['entry_timestamp']].apply(pd.to_datetime, format=date_time_format, errors="coerce")

        order_report = None
        if initial_funds is None:
            initial_funds = self.saved_parameters.get("initial_funds_virtual") or 1e9

        # get pnl data and cleanup as per quantstats format
        _returns_df = pnl_df[['entry_timestamp', 'net_pnl']]
        _returns_df['entry_timestamp'] = _returns_df['entry_timestamp'].dt.tz_localize(None)  # Note: Quantstats has a bug. It doesn't accept the df index, which is set below, with timezone. Hence, we have to drop the timezone info
        _returns_df = _returns_df.set_index('entry_timestamp')
        _returns_df["total_funds"] = _returns_df.net_pnl.cumsum() + initial_funds
        _returns_df = _returns_df.dropna()

        # Note: Quantstats has a potential bug. It cannot work with multiple entries having the same timestamp. For now, we are dropping multiple entries with the same entry_timestamp (else the quantstats code below would throw an error)
        # Suggestion for workaround: For entries with same entry timestamps, we can slightly modify the entry timestamps by adding single-digit microseconds to make them unique
        _returns_df = _returns_df[~_returns_df.index.duplicated(keep='first')]

        # Extract the final column; note: timestamp is the index so that is available too
        total_funds_series = _returns_df.total_funds

        # select report type
        try:
            if report == "metrics":
                order_report = qs.reports.metrics(total_funds_series)
            elif report == "full":
                order_report = qs.reports.full(total_funds_series)
        except ZeroDivisionError:
            raise Exception("ERROR: PnL data generated is too less to perform statistical analysis")

        # save as html file
        if html_dump:
            # if there is an error in calling the API, give a default name to html file.
            try:
                all_strategies = self.get_all_strategies()
                strategy_name = all_strategies.loc[all_strategies['strategyCode'] == strategy_code]['strategyName'].iloc[0]
            except Exception:
                strategy_name = 'strategy_results'
            qs.reports.html(total_funds_series, title=strategy_name, output='', download_filename=f'report_{strategy_name}_{time.time():.0f}.html')

        return order_report

    def print_strategy_config(self, trading_type):
        _ = self.saved_parameters
        strategy_name = self.get_strategy_name(_['strategy_code'])

        data = [
            ['Strategy Name', strategy_name],
            # ['Strategy Code', _['strategy_code']],    # not required as of now
            ['Trading Type', trading_type.name],
            ['Instrument(s)', pprint.pformat(_['instruments'])],
            ['Quantity/Lots', _['lots']],
            ['Start Timestamp', _['start_timestamp_map'][trading_type]],
            ['End Timestamp', _['end_timestamp_map'][trading_type]],
            ['Parameters', pprint.pformat(_['strategy_parameters'])],
            ['Candle', _['candle_interval'].value],
            ['Mode', _['strategy_mode'].name],
        ]

        if trading_type in [TradingType.BACKTESTING, TradingType.PAPERTRADING]:
            data.append(['Initial Funds (Virtual)', _['initial_funds_virtual']])
        elif trading_type in [TradingType.REALTRADING]:
            data.insert(0, ["Broker Name", _['vendor_details']['brokerName']])  # Note, key is still 'vendor_details' even for broking purpose

        if _.get('vendor_details') is not None:
            data.insert(0, ["Vendor Name", _['vendor_details']['brokerName']])

        _msg = tabulate(data, headers=['Config', 'Value'], tablefmt="fancy_grid")
        print(f"\nStarting the strategy '{strategy_name}' in {trading_type.name} mode...\n{_msg}\n")

    def start_job(self, strategy_code=None, start_timestamp=None, end_timestamp=None, instruments=None, lots=None, strategy_parameters=None, candle_interval=None, strategy_mode=None, initial_funds_virtual=None, delete_previous_trades=True,
                  trading_type=None, broking_details=None, **kwargs):
        """
        Submit a BT/PT/RT job for a strategy on the AlgoBulls Platform

        Args:
            strategy_code: Strategy code
            start_timestamp: Start date-time/time
            end_timestamp: End date-time/time
            instruments: Instrument key
            lots: Number of lots of the passed instrument to trade on
            strategy_parameters: Parameters
            candle_interval: Candle interval
            strategy_mode: Intraday or delivery
            delete_previous_trades: Delete data for previous trades
            initial_funds_virtual: virtual funds allotted before the backtesting starts
            trading_type: type of trading : PT/BT/RT
            broking_details: details of client's broker

        Legacy args (will be deprecated in future release):
            'strategy_code' behaves same as 'strategy'
            'start_timestamp' behaves same as 'start'
            'end_timestamp' behaves same as 'end'
            'instrument' behaves same as 'instruments'
            'strategy_parameters' behaves same as 'parameters'
            'candle_interval' behaves same as 'candle'
            'strategy_mode' behaves same as 'mode'

        Returns:
            job submission status
        """

        # check if values received by new parameter names, else extract from old parameter names, else extract from saved parameters
        saved_params = self.saved_parameters
        start_timestamp_map = saved_params.get('start_timestamp_map')
        end_timestamp_map = saved_params.get('end_timestamp_map')
        strategy_code = strategy_code or kwargs.get('strategy_code') or saved_params.get('strategy_code')
        start_timestamp = start_timestamp or kwargs.get('start_timestamp') or start_timestamp_map.get(trading_type)
        end_timestamp = end_timestamp or kwargs.get('end_timestamp') or end_timestamp_map.get(trading_type)
        strategy_parameters = strategy_parameters or kwargs.get('strategy_parameters') or saved_params.get('strategy_parameters')
        candle_interval = candle_interval or kwargs.get('candle_interval') or saved_params.get('candle_interval')
        instruments = instruments or kwargs.get('instrument') or saved_params.get('instruments')
        strategy_mode = strategy_mode or kwargs.get('strategy_mode') or saved_params.get('strategy_mode') or StrategyMode.INTRADAY
        lots = lots or saved_params.get('lots')
        initial_funds_virtual = initial_funds_virtual or saved_params.get('initial_funds_virtual') or 1e9
        broking_details = broking_details or saved_params.get('vendor_details')

        # Sanity checks - Convert config parameters
        _error_msg_candle = f'Argument "candle" should be a valid string or an enum of type CandleInterval. Possible string values can be: {get_valid_enum_names(CandleInterval)}'
        _error_msg_timestamps = f'\nString Format (YYYY-MM-DD HH:MM z) or an instance of type datetime.datetime for Back Testing \nString Format (HH:MM z) or an instance of type datetime.time for Real trading or Paper Trading'
        _error_msg_instruments = f'Argument "instruments" should be a valid instrument string or a list of valid instruments strings. You can use the \'get_instrument()\' method of AlgoBullsConnection class to search for instruments'
        _error_msg_mode = f'Argument "mode" should be a valid string or an enum of type StrategyMode. Possible string values can be: {get_valid_enum_names(StrategyMode)}'
        _error_msg_broking_details = 'Argument "broking_details" should be a valid dict with valid keys. Expected keys "brokerName" and "credentialParameters" '

        initial_funds_virtual = float(initial_funds_virtual)
        if isinstance(start_timestamp, str):
            start_timestamp = get_datetime_with_tz(start_timestamp, trading_type)
        if isinstance(end_timestamp, str):
            end_timestamp = get_datetime_with_tz(end_timestamp, trading_type)
        if isinstance(strategy_mode, str):
            _ = strategy_mode.upper()
            assert _ in StrategyMode.__members__, _error_msg_candle
            strategy_mode = StrategyMode[_]
        if isinstance(candle_interval, str):
            _ = f"{'_' if candle_interval[0].isdigit() else ''}{candle_interval.strip().upper().replace(' ', '_')}"
            assert _ in CandleInterval.__members__, _error_msg_candle
            candle_interval = CandleInterval[_]
        if isinstance(instruments, str):
            instruments = [instruments]
        if strategy_parameters == {} or strategy_parameters is None:
            strategy_parameters = dict()

        # Sanity checks - Validate config parameters
        assert isinstance(strategy_code, str), f'Argument "strategy" should be a valid string'
        assert isinstance(start_timestamp, dt), 'Argument "start" should be a valid timestamp string\n' + _error_msg_timestamps
        assert isinstance(end_timestamp, dt), 'Argument "end" should be a valid timestamp string\n' + _error_msg_timestamps
        assert isinstance(instruments, list), _error_msg_instruments
        assert len(instruments) > 0, _error_msg_instruments
        assert (isinstance(lots, int) and lots > 0), f'Argument "lots" should be a positive integer.'
        assert isinstance(strategy_parameters, dict), f'Argument "parameters" should be a dict'
        assert isinstance(strategy_mode, StrategyMode), _error_msg_mode
        assert isinstance(candle_interval, CandleInterval), _error_msg_candle
        assert isinstance(initial_funds_virtual, float), 'Argument "initial_funds_virtual" should be a float'
        assert isinstance(delete_previous_trades, bool), 'Argument "delete_previous_trades" should be a boolean'

        if broking_details is not None:
            assert isinstance(broking_details, dict), f'Argument "broking_details" should be a dict'
            assert 'brokerName' in broking_details, f'Argument "broking_details" should be a dict with "brokerName" key'
            assert 'credentialParameters' in broking_details, f'Argument "broking_details" should be a dict with "credentialParameters" key'

        if trading_type is not TradingType.BACKTESTING:
            start_timestamp = dt.combine(dt.now().astimezone(start_timestamp.tzinfo).date(), start_timestamp.time(), tzinfo=start_timestamp.tzinfo)
            end_timestamp = dt.combine(dt.now().astimezone(end_timestamp.tzinfo).date(), end_timestamp.time(), tzinfo=end_timestamp.tzinfo)

            start_timestamp_map[TradingType.REALTRADING] = start_timestamp
            start_timestamp_map[TradingType.PAPERTRADING] = start_timestamp
            end_timestamp_map[TradingType.REALTRADING] = end_timestamp
            end_timestamp_map[TradingType.PAPERTRADING] = end_timestamp

        else:
            start_timestamp_map[TradingType.BACKTESTING] = start_timestamp
            end_timestamp_map[TradingType.BACKTESTING] = end_timestamp

        # Restructuring strategy params
        restructured_strategy_parameters = []
        for parameter_name in strategy_parameters:
            restructured_strategy_parameters.append({
                'paramName': parameter_name,
                'paramValue': strategy_parameters[parameter_name]
            })

        # get exchange location
        _ = instruments[0].split(':')
        if len(_) == 2 and EXCHANGE_LOCALE_MAP.get(_[0]) is not None:
            location = EXCHANGE_LOCALE_MAP[_[0]]
        else:
            print('Warning: Valid exchange not given, assuming exchange as "NSE_EQ".\n Expected format for giving an instrument "<EXCHANGE>:<TRADING_SYMBOL>"\nPossible exchange values include: {EXCHANGE_LOCALE_MAP.keys()}')
            location = EXCHANGE_LOCALE_MAP[Locale.DEFAULT.value]

        # generate instruments' id list
        instrument_list = []
        for _instrument in instruments:
            exchange, tradingsymbol = _instrument.split(':')
            instrument_results = self.search_instrument(instrument=tradingsymbol, exchange=exchange)
            for _ in instrument_results:
                if _["value"] == _instrument:
                    instrument_list.append({'id': _["id"]})
                    break

        # save BT/PT/RT parameters
        self.saved_parameters = {
            'strategy_code': strategy_code,
            'start_timestamp_map': start_timestamp_map,
            'end_timestamp_map': end_timestamp_map,
            'strategy_parameters': strategy_parameters,
            'candle_interval': candle_interval,
            'instruments': instruments,
            'strategy_mode': strategy_mode,
            'lots': lots,
            'initial_funds_virtual': initial_funds_virtual,
            'vendor_details': broking_details  # Note: key name is saved as vendor_details for logging purpose
        }

        self.print_strategy_config(trading_type)

        # delete previous trades
        if delete_previous_trades and trading_type in [TradingType.BACKTESTING, TradingType.PAPERTRADING]:
            self.delete_previous_trades(strategy_code)

        # Setup config for starting the job
        strategy_config = {
            'instruments': {
                'instruments': instrument_list
            },
            'lots': lots,
            'userParams': restructured_strategy_parameters,
            'candleDuration': candle_interval.value,
            'strategyMode': strategy_mode.value
        }
        self.api.set_strategy_config(strategy_code=strategy_code, strategy_config=strategy_config, trading_type=trading_type)

        # Submit trading job
        response = self.api.start_strategy_algotrading(strategy_code=strategy_code, start_timestamp=start_timestamp, end_timestamp=end_timestamp, trading_type=trading_type,
                                                       lots=lots, initial_funds_virtual=initial_funds_virtual, broker_details=broking_details, location=location)

        self.strategy_country_map[trading_type][strategy_code] = Country[Locale(location).name].value
        return response

    def backtest(self, strategy=None, start=None, end=None, instruments=None, lots=None, parameters=None, candle=None, mode=None, delete_previous_trades=True, initial_funds_virtual=None, vendor_details=None, **kwargs):
        """
        Submit a backtesting job for a strategy on the AlgoBulls Platform

        Args:
            strategy: Strategy code
            start: Start date-time/time
            end: End date-time/time
            instruments: Instrument key
            lots: Number of lots of the passed instrument to trade on
            parameters: Parameters
            candle: Candle interval
            mode: Intraday or delivery
            delete_previous_trades: Delete data for previous trades
            initial_funds_virtual: virtual funds allotted before the backtesting starts
            vendor_details: vendor's details for authentication and verification

        Legacy args (will be deprecated in future release):
            'strategy_code' behaves same as 'strategy'
            'start_timestamp' behaves same as 'start'
            'end_timestamp' behaves same as 'end'
            'instrument' behaves same as 'instruments'
            'strategy_parameters' behaves same as 'parameters'
            'candle_interval' behaves same as 'candle'
            'strategy_mode' behaves same as 'mode'

        Returns:
            backtest job submission status
        """

        # start backtesting job
        _ = self.start_job(
            strategy_code=strategy, start_timestamp=start, end_timestamp=end, instruments=instruments, lots=lots, strategy_parameters=parameters, candle_interval=candle, strategy_mode=mode,
            initial_funds_virtual=initial_funds_virtual, delete_previous_trades=delete_previous_trades, trading_type=TradingType.BACKTESTING, broking_details=vendor_details, **kwargs
        )

        # Update previously saved pnl data and exchange location
        self.backtesting_pnl_data = None

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
            stop job status
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING)

    def get_backtesting_logs(self, strategy_code, display_progress_bar=True, print_live_logs=False):
        """
        Fetch Back Testing logs

        Args:
            strategy_code: Strategy code
            display_progress_bar: to track the execution on progress bar as your strategy is executed
            print_live_logs: to print the live logs as your strategy is executed

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(display_progress_bar, bool), f'Argument "display_progress_bar" should be a boolean'
        assert isinstance(print_live_logs, bool), f'Argument "print_live_logs" should be a boolean'

        return self.get_logs(strategy_code, trading_type=TradingType.BACKTESTING, display_progress_bar=display_progress_bar, print_live_logs=print_live_logs)

    def get_backtesting_report_pnl_table(self, strategy_code, country=None, force_fetch=False, broker_commission_percentage=None, broker_commission_price=None, slippage_percent=None):
        """
        Fetch Back Testing Profit & Loss details

        Args:
            strategy_code: strategy code
            country: country of Exchange
            force_fetch: Forcefully fetch PnL data
            broker_commission_percentage: Percentage of broker commission per trade
            broker_commission_price: Broker fee per trade
            slippage_percent: Slippage percentage value

        Returns:
            Report details
        """

        if self.backtesting_pnl_data is None or country is not None or force_fetch:
            self.backtesting_pnl_data = self.get_report_pnl_table(strategy_code, TradingType.BACKTESTING, country, broker_commission_percentage, broker_commission_price, slippage_percent)

        return self.backtesting_pnl_data

    def get_backtesting_report_statistics(self, strategy_code, initial_funds=None, report='metrics', html_dump=False):
        """
        Fetch Back Testing report statistics

        Args:
            strategy_code: strategy code
            initial_funds: initial funds that were set before backtesting
            report: format and content of the report
            html_dump: save it as a html file

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        if self.backtesting_pnl_data is None:
            self.get_backtesting_report_pnl_table(strategy_code)
        else:
            print('Generating Statistics for already fetched P&L data...')

        order_report = self.get_report_statistics(strategy_code, initial_funds, report, html_dump, self.backtesting_pnl_data)

        return order_report

    def get_backtesting_report_order_history(self, strategy_code, country=None, render_as_dataframe=False):
        """
        Fetch Back Testing order history

        Args:
            strategy_code: strategy code
            country: country of the segment
            render_as_dataframe: return order history as dataframe or pretty string
        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_report_order_history(strategy_code=strategy_code, trading_type=TradingType.BACKTESTING, render_as_dataframe=render_as_dataframe, country=country)

    def papertrade(self, strategy=None, start=None, end=None, instruments=None, lots=None, parameters=None, candle=None, mode=None, delete_previous_trades=True, initial_funds_virtual=None, vendor_details=None, **kwargs):
        """
        Submit a papertrade job for a strategy on the AlgoBulls Platform

        Args:
            strategy: Strategy code
            start: Start date-time/time
            end: End date-time/time
            instruments: Instrument key
            lots: Number of lots of the passed instrument to trade on
            parameters: Parameters
            candle: Candle interval
            mode: Intraday or delivery
            delete_previous_trades: Delete data of all previous trades
            initial_funds_virtual: virtual funds allotted before the paper trading starts
            vendor_details: vendor's details for authentication and verification

        Legacy args (will be deprecated in future release):
            'strategy_code' behaves same as 'strategy'
            'start_timestamp' behaves same as 'start'
            'end_timestamp' behaves same as 'end'
            'instrument' behaves same as 'instruments'
            'strategy_parameters' behaves same as 'parameters'
            'candle_interval' behaves same as 'candle'
            'strategy_mode' behaves same as 'mode'

        Returns:
            papertrade job submission status
        """

        # start papertrading job
        _ = self.start_job(
            strategy_code=strategy, start_timestamp=start, end_timestamp=end, instruments=instruments, lots=lots, strategy_parameters=parameters, candle_interval=candle, strategy_mode=mode,
            initial_funds_virtual=initial_funds_virtual, delete_previous_trades=delete_previous_trades, trading_type=TradingType.PAPERTRADING, broking_details=vendor_details, **kwargs
        )

        # Update previously saved pnl data and exchange location
        self.papertrade_pnl_data = None

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
            stop job status
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING)

    def get_papertrading_logs(self, strategy_code, display_progress_bar=True, print_live_logs=True):
        """
        Fetch Paper Trading logs

        Args:
            strategy_code: Strategy code
            display_progress_bar: to track the execution on progress bar as your strategy is executed
            print_live_logs: to print the live logs as your strategy is executed

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(display_progress_bar, bool), f'Argument "display_progress_bar" should be a boolean'
        assert isinstance(print_live_logs, bool), f'Argument "print_live_logs" should be a boolean'

        return self.get_logs(strategy_code, trading_type=TradingType.PAPERTRADING, display_progress_bar=display_progress_bar, print_live_logs=print_live_logs)

    def get_papertrading_report_pnl_table(self, strategy_code, country=None, force_fetch=False, broker_commission_percentage=None, broker_commission_price=None, slippage_percent=None):
        """
        Fetch Paper Trading Profit & Loss details

        Args:
            strategy_code: strategy code
            country: country of the exchange
            force_fetch: Forcefully fetch PnL data
            broker_commission_percentage: Percentage of broker commission per trade
            broker_commission_price: Broker fee per trade
            slippage_percent: Slippage percentage value

        Returns:
            Report details
        """

        if self.papertrade_pnl_data is None or country is not None or force_fetch:
            self.papertrade_pnl_data = self.get_report_pnl_table(strategy_code, TradingType.PAPERTRADING, country, broker_commission_percentage, broker_commission_price, slippage_percent)

        return self.papertrade_pnl_data

    def get_papertrading_report_statistics(self, strategy_code, initial_funds=None, report='metrics', html_dump=False):
        """
        Fetch Paper Trading report statistics

        Args:
            strategy_code: strategy code
            initial_funds: initial funds allotted before papertrading
            report: format and content of the report
            html_dump: save it as a html file

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        if self.papertrade_pnl_data is None:
            self.get_papertrading_report_pnl_table(strategy_code)
        else:
            print('Generating Statistics for already fetched P&L data...')

        order_report = self.get_report_statistics(strategy_code, initial_funds, report, html_dump, self.papertrade_pnl_data)

        return order_report

    def get_papertrading_report_order_history(self, strategy_code, country=None, render_as_dataframe=False):
        """
        Fetch Paper Trading order history

        Args:
            strategy_code: strategy code
            country: country of the segment
            render_as_dataframe: return order history as dataframe or pretty string

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_report_order_history(strategy_code=strategy_code, trading_type=TradingType.PAPERTRADING, render_as_dataframe=render_as_dataframe, country=country)

    def realtrade(self, strategy=None, start=None, end=None, instruments=None, lots=None, parameters=None, candle=None, mode=None, broking_details=None, **kwargs):
        """
        Start a Real Trading session.
        Update: This requires an approval process which is currently on request basis.

        Start a realtrading job for a strategy on the AlgoBulls Platform

        Args:
            strategy: Strategy code
            start: Start date-time/time
            end: End date-time/time
            instruments: Instrument key
            lots: Number of lots of the passed instrument to trade on
            parameters: Parameters
            candle: Candle interval
            mode: Intraday or delivery
            broking_details: client's broking details

        Legacy args (will be deprecated in future release):
            'strategy_code' behaves same as 'strategy'
            'start_timestamp' behaves same as 'start'
            'end_timestamp' behaves same as 'end'
            'instrument' behaves same as 'instruments'
            'strategy_parameters' behaves same as 'parameters'
            'candle_interval' behaves same as 'candle'
            'strategy_mode' behaves same as 'mode'

        Returns:
            realtrade job submission status
        """

        # start realtrading job
        _ = self.start_job(strategy_code=strategy, start_timestamp=start, end_timestamp=end, instruments=instruments, lots=lots, strategy_parameters=parameters, candle_interval=candle, strategy_mode=mode, trading_type=TradingType.REALTRADING,
                           broking_details=broking_details, **kwargs)

        # Update previously saved pnl data and exchange location
        self.realtrade_pnl_data = None

    def livetrade(self, *args, **kwargs):
        self.realtrade(*args, **kwargs)

    def get_realtrading_job_status(self, strategy_code):
        """
        Fetch Real Trading job status

        Args:
            strategy_code: Strategy code

        Returns:
            Job status
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_job_status(strategy_code, TradingType.REALTRADING)

    def stop_realtrading_job(self, strategy_code):
        """
        Stop the Real Trading session

        Args:
            strategy_code: Strategy code

        Returns:
            stop job status
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.stop_job(strategy_code=strategy_code, trading_type=TradingType.REALTRADING)

    def get_realtrading_logs(self, strategy_code, display_progress_bar=True, print_live_logs=True):
        """
        Fetch Real Trading logs

        Args:
            strategy_code: Strategy code
            display_progress_bar: to track the execution on progress bar as your strategy is executed
            print_live_logs: to print the live logs as your strategy is executed

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'
        assert isinstance(display_progress_bar, bool), f'Argument "display_progress_bar" should be a boolean'
        assert isinstance(print_live_logs, bool), f'Argument "print_live_logs" should be a boolean'

        return self.get_logs(strategy_code, trading_type=TradingType.REALTRADING, display_progress_bar=display_progress_bar, print_live_logs=print_live_logs)

    def get_realtrading_report_pnl_table(self, strategy_code, country=None, force_fetch=False, broker_commission_percentage=None, broker_commission_price=None):
        """
        Fetch Real Trading Profit & Loss details

        Args:
            strategy_code: strategy code
            country: country of the Exchange
            force_fetch: Forcefully fetch PnL data
            broker_commission_percentage: Percentage of broker commission per trade
            broker_commission_price: Broker fee per trade

        Returns:
            Report details
        """

        if self.realtrade_pnl_data is None or country is not None or force_fetch:
            self.realtrade_pnl_data = self.get_report_pnl_table(strategy_code, TradingType.REALTRADING, country, broker_commission_percentage, broker_commission_price)

        return self.realtrade_pnl_data

    def get_realtrading_report_statistics(self, strategy_code, initial_funds=None, report='metrics', html_dump=False):
        """
        Fetch Real Trading report statistics

        Args:
            strategy_code: strategy code
            initial_funds: initial funds allotted before realtrading
            report: format and content of the report
            html_dump: save it as a html file

        Returns:
            Report details
        """

        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        if self.realtrade_pnl_data is None:
            self.get_realtrading_report_pnl_table(strategy_code)
        else:
            print('Generating Statistics for already fetched P&L data...')

        order_report = self.get_report_statistics(strategy_code, initial_funds, report, html_dump, self.realtrade_pnl_data)

        return order_report

    def get_realtrading_report_order_history(self, strategy_code, country=None, render_as_dataframe=False):
        """
        Fetch Real Trading order history
        Args:
            strategy_code: strategy code
            country: country of the segment
            render_as_dataframe: return order history as dataframe or pretty string

        Returns:
            Report details
        """
        # assert (isinstance(broker, AlgoBullsSupportedBrokers) is True), f'Argument broker should be an enum of type {AlgoBullsSupportedBrokers.__name__}'
        assert isinstance(strategy_code, str), f'Argument "strategy_code" should be a string'

        return self.get_report_order_history(strategy_code=strategy_code, trading_type=TradingType.REALTRADING, render_as_dataframe=render_as_dataframe, country=country)


def pandas_dataframe_all_rows():
    """
    Enable printing of all rows in a dataframe.

    Returns: None
    """

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
