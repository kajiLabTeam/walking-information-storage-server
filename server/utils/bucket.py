from config.const.bucket import (
    FLOOR_BUCKET_NAME,
    FLOOR_INFORMATION_BUCKET_NAME,
    FLOOR_MAP_BUCKET_NAME,
    GYROSCOPE_BUCKET_NAME,
    PEDESTRIAN_BUCKET_NAME,
    WALKING_INFORMATION_BUCKET_NAME,
)
from config.const.extension import FLOOR_MAP_EXTENSION, GYROSCOPE_EXTENSION


# floors/01F8VYXK67BGC1F9RP1E4S9YTV/floor-information/01J5MT4907RHS5Q8QT583YXB96/floor-maps
def get_floor_map_bucket_name(
    floor_id: str, floor_information_id: str, floor_map_id: str
) -> str:
    return f"{FLOOR_BUCKET_NAME}/{floor_id}/{FLOOR_INFORMATION_BUCKET_NAME}/{floor_information_id}/{FLOOR_MAP_BUCKET_NAME}/{floor_map_id}.{FLOOR_MAP_EXTENSION}"


# pedestrian/${pedestrian_id}/walking-information/${walking_information_id}/gyroscope/${gyroscope_id}.csv
def get_gyroscope_bucket_name(
    pedestrian_id: str, walking_information_id: str, gyroscope_id: str
) -> str:
    return f"{PEDESTRIAN_BUCKET_NAME}/{pedestrian_id}/{WALKING_INFORMATION_BUCKET_NAME}/{walking_information_id}/{GYROSCOPE_BUCKET_NAME}/{gyroscope_id}.{GYROSCOPE_EXTENSION}"
