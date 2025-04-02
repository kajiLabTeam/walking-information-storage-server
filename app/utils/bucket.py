from app.config.constants import (
    ACCELEROMETER_FILE_NAME,
    ATMOSPHERIC_PRESSURE_FILE_NAME,
    FLOOR_BUCKET_NAME,
    FLOOR_INFORMATION_BUCKET_NAME,
    GPS_FILE_NAME,
    GYROSCOPE_FILE_NAME,
    RATIO_WAVE_FILE_NAME,
    WALKING_INFORMATION_BUCKET_NAME,
)
from app.config.constants.bucket import FLOOR_MAP_FILE_NAME


# floors/${floor_id}/floor-information/${floor_information_id}/floor-map.png
def get_floor_map_bucket_name(
    floor_id: str,
    floor_information_id: str,
) -> str:
    return (
        f"{FLOOR_BUCKET_NAME}/{floor_id}/"
        f"{FLOOR_INFORMATION_BUCKET_NAME}/{floor_information_id}/"
        f"{FLOOR_MAP_FILE_NAME}"
    )


# walking-information/${walking_information_id}/gps.csv
def get_gps_bucket_name(
    walking_information_id: str,
) -> str:
    return f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{GPS_FILE_NAME}"


# walking-information/${walking_information_id}/accelerometer.csv
def get_accelerometer_bucket_name(
    walking_information_id: str,
) -> str:
    return f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{ACCELEROMETER_FILE_NAME}"


# walking-information/${walking_information_id}/ratio-wave.csv
def get_ratio_wave_bucket_name(
    walking_information_id: str,
) -> str:
    return f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{RATIO_WAVE_FILE_NAME}"


# walking-information/${walking_information_id}/gyroscopes.csv
def get_gyroscope_bucket_name(
    walking_information_id: str,
) -> str:
    return f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{GYROSCOPE_FILE_NAME}"


# walking-information/${walking_information_id}/atmospheric_pressures.csv
def get_atmospheric_pressure_bucket_name(
    walking_information_id: str,
) -> str:
    return (
        f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/"
        f"{ATMOSPHERIC_PRESSURE_FILE_NAME}"
    )
