from enum import Enum


class InfrastructureErrorType(Enum):
    NOT_FOUND_FLOOR_INFORMATION = "NOT_FOUND_FLOOR_INFORMATION"
    NOT_FOUND_FLOOR_MAP = "NOT_FOUND_FLOOR_MAP"
    NOT_FOUND_FLOOR = "NOT_FOUND_FLOOR"
    NOT_FOUND_TRAJECTORY = "NOT_FOUND_TRAJECTORY"
    NOT_FOUND_WALKING_SAMPLE = "NOT_FOUND_WALKING_SAMPLE"
    BUILDING_DB_ERROR = "BUILDING_DB_ERROR"
    FLOOR_DB_ERROR = "FLOOR_DB_ERROR"
    FLOOR_INFORMATION_DB_ERROR = "FLOOR_INFORMATION_DB_ERROR"
    FLOOR_MAP_DB_ERROR = "FLOOR_MAP_DB_ERROR"
    TRAJECTORY_DB_ERROR = "TRAJECTORY_DB_ERROR"
    WALKING_SAMPLE_DB_ERROR = "WALKING_SAMPLE_DB_ERROR"
    PEDESTRIAN_DB_ERROR = "PEDESTRIAN_DB_ERROR"
    WALKING_INFORMATION_DB_ERROR = "WALKING_INFORMATION_DB_ERROR"
    GYROSCOPE_DB_ERROR = "GYROSCOPE_DB_ERROR"
    ACCELEROMETER_DB_ERROR = "ACCELEROMETER_DB_ERROR"
    RATIO_WAVE_DB_ERROR = "RATIO_WAVE_DB_ERROR"
    ATMOSPHERIC_PRESSURE_DB_ERROR = "ATMOSPHERIC_PRESSURE_DB_ERROR"


class InfrastructureError(Exception):
    def __init__(
        self, error_type: InfrastructureErrorType, message: str, status_code: int
    ):
        self._type = error_type
        self._status_code = status_code
        super().__init__(message)

    @property
    def type(self):
        return self._type

    @property
    def status_code(self):
        return self._status_code
