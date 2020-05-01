import requests

from .exceptions import AlgoBullsBaseException, AlgoBullsAPIUnauthorizedError, AlgoBullsAPINotFoundError, AlgoBullsAPIBadRequest
from ..constants import StrategyType


class AlgoBullsAPI:
    SERVER_ENDPOINT = 'http://127.0.0.1:8000/'

    def __init__(self):
        self.headers = None

    def set_access_token(self, access_token):
        """Sets access token to the headers attribute for accessing APIs requiring authorization"""
        self.headers = {
            'Authorization': f'Token {access_token}'
        }

    def _send_request(self, method='get', endpoint='', base_url=SERVER_ENDPOINT, params=None, form_data=None, requires_authorization=True):
        url = f'{base_url}{endpoint}'
        headers = self.headers if requires_authorization else None
        response = requests.request(method=method, headers=headers, url=url, params=params, data=form_data)

        if response.status_code == 200:
            response_json = response.json()
            return response_json
        elif response.status_code == 401:
            raise AlgoBullsAPIUnauthorizedError(f'Unauthorized Error --> Method: {method} | URL: {url} | Response: {response.json()}')
        elif response.status_code == 404:
            raise AlgoBullsAPINotFoundError(f'API Not Found --> Method: {method} | URL: {url} | Response: {response.json()}')
        elif response.status_code == 400:
            raise AlgoBullsAPIBadRequest(f'Bad Request --> Method: {method} | URL: {url} | Response: {response.json()}')
        else:
            response.raw.decode_content = True
            raise AlgoBullsBaseException(f'Unknown non-200 status code --> Method: {method} | URL: {url} | Response: {response.json()} | Response code: {response.status_code}')

    def upload_strategy(self, strategy_name, strategy_details, abc_version):
        """
        Upload a new strategy
        """
        form_data = {'strategy_name': strategy_name, 'strategy_details': strategy_details, 'abc_version': abc_version}
        endpoint = f'v1/build_python_strategy'
        response = self._send_request(endpoint=endpoint, method='post', form_data=form_data)
        return response

    def update_strategy(self, strategy_code, strategy_name, strategy_details, abc_version):
        """
        Update existing strategy
        """
        form_data = {'strategy_code': strategy_code, 'build_strategy_name': strategy_name, 'strategy_details': strategy_details, 'abc_version': abc_version}
        endpoint = f'v1/build_python_strategy'
        response = self._send_request(endpoint=endpoint, method='put', form_data=form_data)
        return response

    def get_all_strategies(self):
        """
        Get all Python Build Strategies
        """
        endpoint = f'v1/build_python_strategy_get_all'
        response = self._send_request(endpoint=endpoint)
        return response

    def get_strategy_details(self, strategy_code):
        """
        Get Strategy from strategy_code
        """
        params = {'strategy_code': strategy_code}
        endpoint = f'v1/build_python_strategy'
        response = self._send_request(endpoint=endpoint, params=params)
        return response

    def search_instrument(self, instrument):
        params = {'instrument': instrument}
        endpoint = f'v1/instrument_search'
        response = self._send_request(endpoint=endpoint, params=params, requires_authorization=False)
        return response

    def set_strategy_config(self, strategy_code, strategy_config):
        params = {'strategy_code': strategy_code, 'strategy_type': StrategyType.STRATEGY_TYPE_CUSTOMER_PYTHON.value}
        form_data = strategy_config
        endpoint = f'v1/customer_strategy_tweak'
        response = self._send_request(method='patch', endpoint=endpoint, params=params, form_data=form_data)
        return response

    def start_strategy_algotrading(self, strategy_code, trading_type):
        """
        Submit backtesting job for strategy with code strategy_code & return the job ID.
        """
        params = {'strategy_code': strategy_code, 'strategy_type': StrategyType.STRATEGY_TYPE_CUSTOMER_PYTHON.value, 'trading_type': trading_type}
        endpoint = f'v1/customer_strategy_algotrading'
        form_data = {'action': 'start'}
        response = self._send_request(method='post', endpoint=endpoint, params=params, form_data=form_data)
        return response

    def stop_strategy_algotrading(self, strategy_code, trading_type):
        """
        Submit backtesting job for strategy with code strategy_code & return the job ID.
        """
        params = {'strategy_code': strategy_code, 'strategy_type': StrategyType.STRATEGY_TYPE_CUSTOMER_PYTHON.value, 'trading_type': trading_type}
        endpoint = f'v1/customer_strategy_algotrading'
        form_data = {'action': 'stop'}
        response = self._send_request(method='post', endpoint=endpoint, params=params, form_data=form_data)
        return response

    def get_job_status(self, strategy_code, trading_type):
        """
        Get JOB status for a given strategy_code and given trading_type
        """
        params = {'strategy_code': strategy_code, 'strategy_type': StrategyType.STRATEGY_TYPE_CUSTOMER_PYTHON.value, 'trading_type': trading_type}
        endpoint = f'v1/customer_strategy_algotrading'
        response = self._send_request(endpoint=endpoint, params=params)
        return response

    def get_reports(self, strategy_code, trading_type, report_type):
        params = {'strategy_code': strategy_code, 'strategy_type': StrategyType.STRATEGY_TYPE_CUSTOMER_PYTHON.value, 'trading_type': trading_type, 'report_type': report_type}
        endpoint = f'v1/customer_strategy_algotrading_reports'
        response = self._send_request(endpoint=endpoint, params=params)
        return response
