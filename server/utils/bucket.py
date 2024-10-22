from config.const import (
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
    PEDESTRIAN_BUCKET_NAME,
    RATIO_WAVE_BUCKET_NAME,
    RATIO_WAVE_EXTENSION,
    WALKING_INFORMATION_BUCKET_NAME,
)


# floors/${floor_id}/floor-information/${floor_information_id}/floor-maps/${floor_map_id}.png
def get_floor_map_bucket_name(
    floor_id: str,
    floor_information_id: str,
    floor_map_id: str,
) -> str:
    return f"{FLOOR_BUCKET_NAME}/{floor_id}/{FLOOR_INFORMATION_BUCKET_NAME}/{floor_information_id}/{FLOOR_MAP_BUCKET_NAME}/{floor_map_id}.{FLOOR_MAP_EXTENSION}"


# pedestrian/${pedestrian_id}/walking-information/${walking_information_id}/gps/${gps_id}.csv
def get_gps_bucket_name(
    pedestrian_id: str,
    walking_information_id: str,
    gps_id: str,
) -> str:
    return f"{PEDESTRIAN_BUCKET_NAME}/{pedestrian_id}/{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{GPS_BUCKET_NAME}/{gps_id}.{GPS_EXTENSION}"


# pedestrian/${pedestrian_id}/walking-information/${walking_information_id}/accelerometers/${accelerometer_id}.csv
def get_accelerometer_bucket_name(
    pedestrian_id: str,
    walking_information_id: str,
    accelerometer_id: str,
) -> str:
    return f"{PEDESTRIAN_BUCKET_NAME}/{pedestrian_id}/{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{ACCELEROMETER_BUCKET_NAME}/{accelerometer_id}.{ACCELEROMETER_EXTENSION}"


# pedestrian/${pedestrian_id}/walking-information/${walking_information_id}/ratio-waves/${ratio_wave_id}.csv
def get_ratio_wave_bucket_name(
    pedestrian_id: str,
    walking_information_id: str,
    ratio_wave_id: str,
) -> str:
    return f"{PEDESTRIAN_BUCKET_NAME}/{pedestrian_id}/{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{RATIO_WAVE_BUCKET_NAME}/{ratio_wave_id}.{RATIO_WAVE_EXTENSION}"


# pedestrian/${pedestrian_id}/walking-information/${walking_information_id}/gyroscopes/${gyroscope_id}.csv
def get_gyroscope_bucket_name(
    pedestrian_id: str,
    walking_information_id: str,
    gyroscope_id: str,
) -> str:
    return f"{PEDESTRIAN_BUCKET_NAME}/{pedestrian_id}/{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{GYROSCOPE_BUCKET_NAME}/{gyroscope_id}.{GYROSCOPE_EXTENSION}"


# pedestrian/${pedestrian_id}/walking-information/${walking_information_id}/atmospheric_pressures/${atmospheric_pressure_id}.csv
def get_atmospheric_pressure_bucket_name(
    pedestrian_id: str,
    walking_information_id: str,
    atmospheric_pressure_id: str,
) -> str:
    return f"{PEDESTRIAN_BUCKET_NAME}/{pedestrian_id}/{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{ATMOSPHERIC_PRESSURE_BUCKET_NAME}/{atmospheric_pressure_id}.{ATMOSPHERIC_PRESSURE_EXTENSION}"
