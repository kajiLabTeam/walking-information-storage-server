from io import BytesIO

import numpy as np
import pandas as pd


class WalkingParameter:
    def __init__(
        self,
        step: int,
        walking_period: tuple[float, float],
        gyroscope_file: bytes,
    ) -> None:
        self.__walking_period = walking_period
        self.__step = step
        self.__angle_change = self.__calculate_cumulative_angle(gyroscope_file)

    def get_step(
        self,
    ) -> int:
        return self.__step

    def get_angle_change(
        self,
    ) -> int:
        return self.__angle_change

    def __calculate_cumulative_angle(
        self,
        gyroscope_file: bytes,
    ) -> int:
        gyro_df = pd.read_csv(BytesIO(gyroscope_file))
        gyro_df = gyro_df.copy()
        gyro_df["dt"] = gyro_df["t"].diff().fillna(0)

        gyro_df["delta_yaw_rad"] = gyro_df["z"] * gyro_df["dt"]

        total_yaw_rad = gyro_df["delta_yaw_rad"].sum()

        return np.degrees(total_yaw_rad)
