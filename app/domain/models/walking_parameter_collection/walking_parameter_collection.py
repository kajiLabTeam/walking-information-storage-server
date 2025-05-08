from collections.abc import Iterator
from io import BytesIO

import numpy as np
import pandas as pd
from scipy.signal import find_peaks

from app.domain.models.walking_parameter.walking_parameter import WalkingParameter


class WalkingParameterCollection:
    def __init__(
        self,
        gyroscope_file: bytes,
        accelerometer_file: bytes,
    ) -> None:
        self.__walking_parameters: list[WalkingParameter] = self.__separate_gyroscope_file_by_step(
            gyroscope_file=gyroscope_file,
            accelerometer_file=accelerometer_file,
        )

    def __separate_gyroscope_file_by_step(
        self,
        gyroscope_file: bytes,
        accelerometer_file: bytes,
    ) -> list[WalkingParameter]:
        walking_parameters: list[WalkingParameter] = []
        acc_df = pd.read_csv(BytesIO(accelerometer_file))
        start_unix = 1743498000
        acc_df["t"] = start_unix + acc_df["t"]

        # ベクトル長の計算
        acc_df["omega_norm"] = np.sqrt(acc_df["x"] ** 2 + acc_df["y"] ** 2 + acc_df["z"] ** 2)

        # ステップ検出
        peaks_norm, _ = find_peaks(acc_df["omega_norm"], height=0.3, distance=25)
        step_times = acc_df["t"].iloc[peaks_norm].to_numpy()

        step_segments = []
        if len(step_times) > 0:
            threshold = 0.5
            start_time = step_times[0]
            for i in range(1, len(step_times)):
                if step_times[i] - step_times[i - 1] > threshold:
                    start_time = step_times[i]
                    step_segments.append([step_times[i - 1], step_times[i]])

            step_segments.append([start_time, step_times[-1]])

        gyro_df = pd.read_csv(BytesIO(gyroscope_file))
        gyro_df["t"] = start_unix + gyro_df["t"]

        for idx, (seg_start, seg_end) in enumerate(step_segments):
            gyro_seg_data = gyro_df[(gyro_df["t"] >= seg_start) & (gyro_df["t"] <= seg_end)].copy()

            if not gyro_seg_data.empty:
                gyro_seg_data["t"] = gyro_seg_data["t"] - start_unix
                gyro_seg_data = gyro_seg_data[["t", "x", "y", "z"]]
                walking_parameters.append(
                    WalkingParameter(
                        step=idx,
                        walking_period=(seg_start, seg_end),
                        gyroscope_file=gyro_seg_data.to_csv(index=False).encode("utf-8"),
                    )
                )

        return walking_parameters

    def get_walking_parameters(
        self,
    ) -> list[WalkingParameter]:
        return self.__walking_parameters

    def add(
        self,
        walking_parameter: WalkingParameter,
    ) -> None:
        self.__walking_parameters.append(walking_parameter)

    def remove(
        self,
        walking_parameter: WalkingParameter,
    ) -> None:
        self.__walking_parameters.remove(walking_parameter)

    def __iter__(
        self,
    ) -> Iterator[WalkingParameter]:
        return iter(self.__walking_parameters)

    def __len__(
        self,
    ) -> int:
        return len(self.__walking_parameters)

    def __getitem__(
        self,
        index: int,
    ) -> WalkingParameter:
        return self.__walking_parameters[index]
