from io import BytesIO
from typing import List

import numpy as np
import pandas as pd

from domain.models.trajectory.trajectory import Trajectory


class AngleConverter:
    def __init__(self, raw_data_file: bytes):
        self.__raw_data_df = pd.read_csv(BytesIO(raw_data_file))

    def generate_correct_trajectory(self, time_unit: float = 0.7) -> Trajectory:
        """
        ## 角速度積分して角度の変化量を計算し、正しい軌跡を生成する
        """
        angle = self.__calculate_cumulative_angle(
            self.__raw_data_df, time_unit=time_unit
        )

        return angle

      
      

    def __calculate_cumulative_angle(
        self, gyro_df: pd.DataFrame, time_unit: float = 0.7
    ) -> float:
        sample_freq = 100
        window_gayo = 10
        gyro_df["time_unit"] = (gyro_df["t"] / time_unit).astype(int)

        # print(gyro_df["time_unit"])

        gyro_df["norm"] = (
            gyro_df["x"] ** 2 + gyro_df["y"] ** 2 + gyro_df["z"] ** 2
        ) ** (1 / 2)
        gyro_df["angle"] = np.cumsum(gyro_df["x"]) / sample_freq
        gyro_df["low_x"] = gyro_df["x"].rolling(window=window_gayo).mean()
        gyro_df["angle_x"] = gyro_df["angle"].rolling(
            window=window_gayo, center=True
        ).mean() * (180 / np.pi)

      

        angle_df = (
            gyro_df.groupby("time_unit")
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

        return gyro_df["angle_x"].max()

     