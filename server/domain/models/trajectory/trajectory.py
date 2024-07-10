from typing import List

from domain.models.walking_parameter.walking_parameter import WalkingParameter


class Trajectory:
    def __init__(self, trajectory: List[WalkingParameter]):
        self.__trajectory: WalkingParameter = trajectory

    def get_trajectory(self) -> WalkingParameter:
        return self.__trajectory

    def last_trajectory(self) -> WalkingParameter:
        return self.__trajectory[-1]
