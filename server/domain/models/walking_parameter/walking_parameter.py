from io import BytesIO
from typing import Optional

import numpy as np
import pandas as pd


class WalkingParameter:
    def __init__(self, id: Optional[str], step: int, gyroscope_file: bytes):
        self.__id = id
        self.__step = step
        self.__angle_changed = self.__calculate_cumulative_angle(gyroscope_file)

    def get_id(self) -> str:
        if self.__id is None:
            raise ValueError("Not")

        return self.__id

    def get_step(self) -> int:
        return self.__step

    def get_angle_changed(self) -> int:
        return self.__angle_changed

    def __calculate_cumulative_angle(
        self, gyroscope_file: bytes, time_unit: float = 0.7
    ) -> int:
        sample_freq = 100
        window_gayo = 10
        gyro_df = pd.read_csv(BytesIO(gyroscope_file))
        gyro_df["time_unit"] = (gyro_df["t"] / time_unit).astype(int)

        gyro_df["norm"] = (
            gyro_df["x"] ** 2 + gyro_df["y"] ** 2 + gyro_df["z"] ** 2
        ) ** (1 / 2)
        gyro_df["angle"] = np.cumsum(gyro_df["x"]) / sample_freq
        gyro_df["low_x"] = gyro_df["x"].rolling(window=window_gayo).mean()
        gyro_df["angle_x"] = gyro_df["angle"].rolling(
            window=window_gayo, center=True
        ).mean() * (180 / np.pi)

        return int(gyro_df["angle_x"].max())
