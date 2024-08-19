from enum import Enum


class ApplicationErrorType(Enum):
    NOT_WALKING_START = "NotWalkingStart"
    NOT_FLOOR_INFORMATION = "NotFloorInformation"
    NOT_FLOOR_MAP = "NotFloorMap"
    NOT_FLOOR = "NotFloor"


class ApplicationError(Exception):
    def __init__(self, error_type: ApplicationErrorType, message: str):
        self._type = error_type
        super().__init__(message)

    @property
    def type(self):
        return self._type
