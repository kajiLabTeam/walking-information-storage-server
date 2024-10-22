from typing import Literal, list

from domain.dataclasses.coordinate import Pose
from domain.models.reversed_estimated_trajectory.cluster_tracking import ClusterTracking
from domain.models.reversed_estimated_trajectory.reversed_particle_filter import (
    ReversedEstimationParticleFilter,
)
from domain.models.tracking_particle.tracking_particle import TrackingParticle


class ReversedEstimatedTrajectory:
    def __init__(
        self,
        tracking_particle: TrackingParticle,
        method: Literal[
            "cluster",
            "particle_filter",
        ],
    ) -> None:
        self.__tracking_particle = tracking_particle
        self.__reversed_estimated_trajectory: list[Pose] = []

        if method == "cluster":
            self.__cluster_tracking()
        elif method == "particle_filter":
            self.__particle_filter()

        self.__reversed()

    def get_reversed_estimated_trajectory(
        self,
    ) -> list[Pose]:
        return self.__reversed_estimated_trajectory

    def last_position(
        self,
    ) -> Pose:
        return self.__reversed_estimated_trajectory[-1]

    def __cluster_tracking(
        self,
    ):
        self.__reversed_estimated_trajectory = ClusterTracking.run(
            self.__tracking_particle,
        )

    def __particle_filter(
        self,
    ):
        self.__reversed_estimated_trajectory = ReversedEstimationParticleFilter.run(
            self.__tracking_particle,
        )

    def __reversed(
        self,
    ):
        self.__reversed_estimated_trajectory.reverse()

    def __iter__(
        self,
    ):
        return iter(self.__reversed_estimated_trajectory)

    def __len__(
        self,
    ):
        return len(self.__reversed_estimated_trajectory)

    def __getitem__(
        self,
        index,
    ):
        return self.__reversed_estimated_trajectory[index]
