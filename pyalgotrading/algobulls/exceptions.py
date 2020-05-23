class AlgoBullsAPIBaseException(Exception):
    """
    Base exception class for all API related exceptions
    """
    pass


class AlgoBullsAPIBadRequest(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 400 (Bad Request)
    """
    pass


class AlgoBullsAPIUnauthorizedError(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 401 (Unauthorized)
    """
    pass


class AlgoBullsAPIResourceNotFoundError(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 404 (Resource Not Found)
    """
    pass


class AlgoBullsAPIInternalServerErrorException(AlgoBullsAPIBaseException):
    """
    Exception class for HTTP status code of 500 (Internal Server Error)
    """
    pass
