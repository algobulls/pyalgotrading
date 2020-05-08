class AlgoBullsAPIBaseException(Exception):
    pass


class AlgoBullsAPIBadRequest(AlgoBullsAPIBaseException):
    # HTTP Response Code: 400
    pass


class AlgoBullsAPIUnauthorizedError(AlgoBullsAPIBaseException):
    # HTTP Response Code: 401
    pass


class AlgoBullsAPIResourceNotFoundError(AlgoBullsAPIBaseException):
    # HTTP Response Code: 404
    pass


class AlgoBullsAPIInternalServerErrorException(AlgoBullsAPIBaseException):
    # HTTP Response Code: 500
    pass
