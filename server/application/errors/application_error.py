from enum import Enum


class ApplicationErrorType(Enum):
    NOT_WALKING_START = "NotWalkingStart"


class ApplicationError(Exception):
    def __init__(self, error_type: ApplicationErrorType, message: str):
        self._type = error_type
        super().__init__(message)

    @property
    def type(self):
        return self._type
