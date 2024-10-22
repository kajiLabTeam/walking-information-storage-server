from __future__ import annotations

from config.const import CONVERGENCE_JUDGEMENT_NUMBER, RSSI_MODEL_PATH
from domain.dataclasses.coordinate import Coordinate, Pose
from domain.errors.domain_error import DomainError, DomainErrorType
from domain.models.estimated_particle.estimated_particle import EstimatedParticle
from domain.models.floor_map.floor_map import FloorMap
from domain.models.walking_parameter.walking_parameter import WalkingParameter
from domain.models.walking_parameter_collection.walking_parameter_collection import (
    WalkingParameterCollection,
)
from utils import reverse_angle


class TrackingParticle:
    def __init__(
        self,
        floor_map: FloorMap,
        model_path: str = RSSI_MODEL_PATH,
    ) -> None:
        self.__floor_map = floor_map
        self.__tracking_count = 0
        self.__coverage_count = 0
        self.__coverage_pose: Pose | None = None
        self.__estimation_particles: list[EstimatedParticle] = []
        self.__walking_parameter_collection = WalkingParameterCollection()
        self._initialized = True

    def get_tracking_count(
        self,
    ) -> int:
        return self.__tracking_count

    def get_coverage_count(
        self,
    ) -> int:
        return self.__coverage_count

    def get_estimation_particles(
        self,
    ) -> list[EstimatedParticle]:
        return self.__estimation_particles

    def get_walking_parameter_reverse(
        self,
        index: int,
    ) -> list[WalkingParameter]:
        walking_positions = [
            wpc.reverse() for wpc in self.__walking_parameter_collection[:index]
        ]
        walking_positions.reverse()
        return walking_positions

    def get_coverage_position(
        self,
    ) -> Tuple[
        Pose,
        int,
    ]:
        if self.__coverage_pose is None:
            raise DomainError(
                error_type=DomainErrorType.COVERAGE_POSITION_IS_NONE,
                status_code=500,
                detail="収束地点が存在しません",
            )

        return (
            Pose(
                coordinate=Coordinate(
                    x=self.__coverage_pose.get_x(),
                    y=self.__coverage_pose.get_y(),
                ),
                direction=reverse_angle(
                    self.__coverage_pose.get_direction(),
                ),
            ),
            self.__coverage_count,
        )

    def set_estimation_particles(
        self,
        estimation_particles: list[EstimatedParticle],
    ) -> None:
        self.__estimation_particles = estimation_particles

    def last_estimation_particles(
        self,
    ) -> EstimatedParticle:
        return self.__estimation_particles[-1]

    def last_walking_parameter(
        self,
    ) -> WalkingParameter:
        return self.__walking_parameter_collection[-1]

    def last_estimated_pose(
        self,
    ) -> Pose:
        return self.last_estimation_particles().get_estimated_pose()

    def reverse(
        self,
    ) -> None:
        self.__estimation_particles.reverse()

    def add(
        self,
        estimation_particles: EstimatedParticle,
    ) -> None:
        self.__estimation_particles.append(estimation_particles)

    def track(
        self,
        walking_parameter: WalkingParameter,
    ) -> None:
        if self.__estimation_particles == []:
            estimated_particle = EstimatedParticle.initialize(
                floor_map=self.__floor_map,
                initial_walking_parameter=walking_parameter,
            )
            self.add(estimated_particle)
            self.__walking_parameter_collection.add(walking_parameter)
            return
        estimation_particles = self.last_estimation_particles()
        estimation_particles.remove_by_floor_map()
        move_estimation_particles = estimation_particles.move(
            current_walking_parameter=walking_parameter,
        )
        move_estimation_particles.remove_by_floor_map()
        move_estimation_particles.remove_by_direction(
            step=walking_parameter.get_step(),
        )
        move_estimation_particles.resampling(step=walking_parameter.get_step())

        if (
            self.__coverage_pose is None
            and self.__tracking_count != 0
            and self.__tracking_count % CONVERGENCE_JUDGEMENT_NUMBER == 0
            and estimation_particles.is_converged()
        ):
            print("収束しました")
            self.__coverage_count = self.__tracking_count
            self.__coverage_pose = move_estimation_particles.get_estimated_pose()

        self.add(move_estimation_particles)
        self.__walking_parameter_collection.add(walking_parameter)
        self.__tracking_count += 1

    def __iter__(
        self,
    ):
        return iter(self.__estimation_particles)

    def __len__(
        self,
    ):
        return len(self.__estimation_particles)

    def __getitem__(
        self,
        index,
    ):
        return self.__estimation_particles[index]
