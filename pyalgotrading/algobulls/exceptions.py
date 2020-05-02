class AlgoBullsBaseException(Exception):
    pass


class AlgoBullsAPIUnauthorizedError(AlgoBullsBaseException):
    pass


class AlgoBullsIncorrectParamsError(AlgoBullsBaseException):
    pass


class AlgoBullsAPICallFailedError(AlgoBullsBaseException):
    pass


class AlgoBullsAPINotFoundError(AlgoBullsBaseException):
    pass


class AlgoBullsAPIBadRequest(AlgoBullsBaseException):
    pass


class AlgoBullsIncorrectUsernameException(AlgoBullsBaseException):
    pass


class AlgoBullsIncorrectPasswordException(AlgoBullsBaseException):
    pass


class AlgoBullsIncorrectApiSecretException(AlgoBullsBaseException):
    pass


class AlgoBullsInternalServerErrorException(AlgoBullsBaseException):
    pass


class AlgoBullsLoginErrorException(AlgoBullsBaseException):
    pass


class AlgoBullsAccessTokenNotFound(AlgoBullsBaseException):
    pass
