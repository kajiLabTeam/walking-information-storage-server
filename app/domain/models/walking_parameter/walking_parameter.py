from io import BytesIO

import numpy as np
import pandas as pd

from app.domain.errors import DomainError, DomainErrorType


class WalkingParameter:
    def __init__(
        self,
        step: int,
        walking_period: tuple[int, int],
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
        try:
            sample_freq = 100
            window_gayo = 10
            gyro_df = pd.read_csv(BytesIO(gyroscope_file))
            gyro_df["time_unit"] = gyro_df["t"]

            gyro_df["norm"] = (gyro_df["x"] ** 2 + gyro_df["y"] ** 2 + gyro_df["z"] ** 2) ** (1 / 2)
            gyro_df["angle"] = np.cumsum(gyro_df["x"]) / sample_freq
            gyro_df["low_x"] = gyro_df["x"].rolling(window=window_gayo).mean()
            gyro_df["angle_x"] = gyro_df["angle"].rolling(
                window=window_gayo,
                center=True,
            ).mean() * (180 / np.pi)

            return int(gyro_df["angle_x"].max())
        except Exception as err:
            raise DomainError(
                error_type=DomainErrorType.INVALID_GYROSCOPE_DATA,
                status_code=400,
                detail="gyroscope data is invalid",
            ) from err
