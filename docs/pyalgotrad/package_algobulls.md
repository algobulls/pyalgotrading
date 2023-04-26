# algobulls
Package for interacting with the AlgoBulls backend

## api
Module for handling API calls to the AlgoBulls backend.

## AlgoBullsAPI
AlgoBulls API


__init__(self):
    ```"""
    Init method that is used while creating an object of this class
    """
    self.headers = None
    self.__key_backtesting = None  # cstc id
    self.__key_papertrading = None  # cstc id
    self.__key_realtrading = None  # cstc id```

def create_strategy(self, strategy_name, strategy_details, abc_version) -> dict:
    """
    Create a new strategy for the user on the AlgoBulls platform.

    Parameters:
        strategy_name : str
            name of the strategy
            [required]
        strategy_details : str
            Python code of the strategy
            [required]
        abc_version : str
            value of one of the enums available under AlgoBullsEngineVersion
            [required]
    
    Returns:
        dict
        JSON Response received from AlgoBulls platform after (attempt to) creating a new strategy.

    Warning:
        For every user, the strategy_name should be unique. You cannot create multiple strategies with the same name.
    
    ENDPOINT:
        POST v2/user/strategy/build/python

    """

def get_all_strategies(self) -> dict:
    """
    Get all the Python strategies created by the user on the AlgoBulls platform

    Returns:
        dict
        JSON Response received from AlgoBulls platform with list of all the created strategies.

    Info: ENDPOINT
        `OPTIONS` v2/user/strategy/build/python
    """
    endpoint = f'v2/user/strategy/build/python'
    response = self._send_request(endpoint=endpoint, method='options')
    return response