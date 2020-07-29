class AlgoBullsAPIBaseException(Exception):
    """
    Base exception class for all API related exceptions
    """

    def __init__(self, method, url, response):
        self.method = method
        self.url = url
        self.response = response

        message = f'{self.get_error_type()} | Method: {self.method} | URL: {self.url} | Response: {self.response}'
        super().__init__(message)

    def get_error_type(self):
        return 'Unknown non-200 status code'


class AlgoBullsAPIBadRequest(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 400 (Bad Request)
    """

    def get_error_type(self):
        return 'Bad Request'


class AlgoBullsAPIUnauthorizedError(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 401 (Unauthorized)
    """

    def get_error_type(self):
        return 'Unauthorized Error'


class AlgoBullsAPIInsufficientBalanceError(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 402 (Insufficient Balance)
    """

    def get_error_type(self):
        return 'Insufficient Balance'


class AlgoBullsAPIForbiddenError(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 403 (Operation not permitted)
    Use case: Trying to START or STOP a strategy when it is in intermediate state.
    """

    def get_error_type(self):
        return 'Forbidden'


class AlgoBullsAPIResourceNotFoundError(AlgoBullsAPIBaseException):
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
