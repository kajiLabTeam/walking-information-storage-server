from app.config.const import (
    ACCELEROMETER_BUCKET_NAME,
    ACCELEROMETER_EXTENSION,
    ATMOSPHERIC_PRESSURE_BUCKET_NAME,
    ATMOSPHERIC_PRESSURE_EXTENSION,
    FLOOR_BUCKET_NAME,
    FLOOR_INFORMATION_BUCKET_NAME,
    FLOOR_MAP_BUCKET_NAME,
    FLOOR_MAP_EXTENSION,
    GPS_BUCKET_NAME,
    GPS_EXTENSION,
    GYROSCOPE_BUCKET_NAME,
    GYROSCOPE_EXTENSION,
    RATIO_WAVE_BUCKET_NAME,
    RATIO_WAVE_EXTENSION,
    WALKING_INFORMATION_BUCKET_NAME,
)


# floors/${floor_id}/floor-information/${floor_information_id}/floor-map.png
def get_floor_map_bucket_name(
    floor_id: str,
    floor_information_id: str,
) -> str:
    return (
        f"{FLOOR_BUCKET_NAME}/{floor_id}/"
        f"{FLOOR_INFORMATION_BUCKET_NAME}/{floor_information_id}/"
        f"{FLOOR_MAP_BUCKET_NAME}."
        f"{FLOOR_MAP_EXTENSION}"
    )


# walking-information/${walking_information_id}/gps.csv
def get_gps_bucket_name(
    walking_information_id: str,
) -> str:
    return (
        f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/"
        f"{GPS_BUCKET_NAME}."
        f"{GPS_EXTENSION}"
    )


# walking-information/${walking_information_id}/accelerometer.csv
def get_accelerometer_bucket_name(
    walking_information_id: str,
) -> str:
    return (
        f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/"
        f"{ACCELEROMETER_BUCKET_NAME}."
        f"{ACCELEROMETER_EXTENSION}"
    )


# walking-information/${walking_information_id}/ratio-wave.csv
def get_ratio_wave_bucket_name(
    walking_information_id: str,
) -> str:
    return (
        f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/"
        f"{RATIO_WAVE_BUCKET_NAME}."
        f"{RATIO_WAVE_EXTENSION}"
    )


# walking-information/${walking_information_id}/gyroscopes.csv
def get_gyroscope_bucket_name(
    walking_information_id: str,
) -> str:
    return (
        f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/"
        f"{GYROSCOPE_BUCKET_NAME}."
        f"{GYROSCOPE_EXTENSION}"
    )


# walking-information/${walking_information_id}/atmospheric_pressures.csv
def get_atmospheric_pressure_bucket_name(
    walking_information_id: str,
) -> str:
    return (
        f"{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/"
        f"{ATMOSPHERIC_PRESSURE_BUCKET_NAME}."
        f"{ATMOSPHERIC_PRESSURE_EXTENSION}"
    )
