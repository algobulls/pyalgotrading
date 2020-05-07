class AlgoBullsAPIBaseException(Exception):
    pass


class AlgoBullsAPIAPIBadRequest(AlgoBullsAPIBaseException):
    # HTTP Response Code: 400
    pass


class AlgoBullsAPIAPIUnauthorizedError(AlgoBullsAPIBaseException):
    # HTTP Response Code: 401
    pass


class AlgoBullsAPIAPIResourceNotFoundError(AlgoBullsAPIBaseException):
    # HTTP Response Code: 404
    pass


class AlgoBullsAPIAPIInternalServerErrorException(AlgoBullsAPIBaseException):
    # HTTP Response Code: 500
    pass
