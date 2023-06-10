class AlgoBullsAPIBaseException(Exception):
    """
    Base exception class for all API related exceptions
    """

    def __init__(self, method, url, response, status_code):
        self.method = method
        self.url = url
        self.response = response

        message = f'{self.get_error_type()} | Method: {self.method} | URL: {self.url} | Response: {self.response} | status code: {status_code}'

        super().__init__(message)

    def get_error_type(self):
        return 'Unknown non-200 status code'


class AlgoBullsAPIBadRequestException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 400 (Bad Request)
    """

    def get_error_type(self):
        return 'Bad Request'


class AlgoBullsAPIUnauthorizedErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 401 (Unauthorized)
    """

    def get_error_type(self):
        return 'Unauthorized Error'


class AlgoBullsAPIInsufficientBalanceErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 402 (Insufficient Balance)
    """

    def get_error_type(self):
        return 'Insufficient Balance'


class AlgoBullsAPIForbiddenErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 403 (Operation not permitted)
    Use case: Trying to START or STOP a strategy when it is in intermediate state.
    """

    def get_error_type(self):
        return 'Forbidden'


class AlgoBullsAPIResourceNotFoundErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 404 (Resource Not Found)
    """

    def get_error_type(self):
        return 'Resource Not Found'


class AlgoBullsAPIInternalServerErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 500 (Internal Server Error)
    """

    def get_error_type(self):
        return 'Internal Server Error'


class AlgoBullsAPIGatewayTimeoutErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 504 (Gateway Timeout Error)
    """

    def get_error_type(self):
        return 'Gateway Timeout Error'
