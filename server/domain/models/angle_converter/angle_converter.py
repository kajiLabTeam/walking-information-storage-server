from io import BytesIO
from typing import List

import numpy as np
import pandas as pd
from domain.models.trajectory.trajectory import Trajectory


class AngleConverter:
    def __init__(self, raw_data_file: bytes):
        self.__gyro_df = pd.read_csv(BytesIO(raw_data_file))

    def calculate_cumulative_angle(self, time_unit: float = 0.7) -> int:

        sample_freq = 100
        window_gayo = 10
        self.__gyro_df["time_unit"] = (self.__gyro_df["t"] / time_unit).astype(int)

        self.__gyro_df["norm"] = (
            self.__gyro_df["x"] ** 2
            + self.__gyro_df["y"] ** 2
            + self.__gyro_df["z"] ** 2
        ) ** (1 / 2)
        self.__gyro_df["angle"] = np.cumsum(self.__gyro_df["x"]) / sample_freq
        self.__gyro_df["low_x"] = self.__gyro_df["x"].rolling(window=window_gayo).mean()
        self.__gyro_df["angle_x"] = self.__gyro_df["angle"].rolling(
            window=window_gayo, center=True
        ).mean() * (180 / np.pi)

        angle_df = (
            self.__gyro_df.groupby("time_unit")
            .apply(
                lambda df: pd.Series(
                    {
                        "t": df["t"].iloc[0],  # 各グループの開始時間
                        "angle_x": np.trapz(df[f"angle_x"], df["t"]),
                    }
                )
            )
            .reset_index(drop=True)
        )

        return int(self.__gyro_df["angle_x"].max())
