from enum import Enum


class InfrastructureErrorType(Enum):
    NOT_FOUND_FLOOR_INFORMATION = "NOT_FOUND_FLOOR_INFORMATION"
    NOT_FOUND_FLOOR_MAP = "NOT_FOUND_FLOOR_MAP"
    NOT_FOUND_FLOOR = "NOT_FOUND_FLOOR"
    NOT_FOUND_TRAJECTORY = "NOT_FOUND_TRAJECTORY"
    NOT_FOUND_WALKING_SAMPLE = "NOT_FOUND_WALKING_SAMPLE"


class InfrastructureError(Exception):
    def __init__(self, error_type: InfrastructureErrorType, message: str):
        self._type = error_type
        super().__init__(message)

    @property
    def type(self):
        return self._type
