from collections.abc import Iterator

from app.config.constants.amount import CONVERGENCE_JUDGEMENT_NUMBER
from app.domain.dataclasses import Coordinate, Pose
from app.domain.models.estimated_particle import EstimatedParticle
from app.domain.models.floor_map.floor_map import FloorMap
from app.utils.angle import reverse_angle


class TrackingParticle:
    def __init__(
        self,
        floor_map: FloorMap,
    ) -> None:
        self.__coverage_count = 0
        self.__estimation_particles = EstimatedParticle.initialize(floor_map=floor_map)
        self.__coverage_position: Pose | None = None

    def get_estimation_particles(self) -> list[EstimatedParticle]:
        return self.__estimation_particles

    def get_coverage_position(self) -> tuple[Pose, int] | None:
        """## 収束地点を取得する"""
        if self.__coverage_position is None:
            return None

        return (
            Pose(
                coordinate=Coordinate(
                    x=self.__coverage_position.coordinate.x,
                    y=self.__coverage_position.coordinate.y,
                ),
                direction=reverse_angle(self.__coverage_position.direction),
            ),
            self.__coverage_count,
        )

    def set_estimation_particles(self, estimation_particles: list[EstimatedParticle]) -> None:
        self.__estimation_particles = estimation_particles

    def last_estimation_particles(self) -> EstimatedParticle:
        return self.__estimation_particles[-1]

    def last_estimated_position(self) -> Pose:
        return self.last_estimation_particles().estimate_position()

    def reverse(self) -> None:
        self.__estimation_particles.reverse()

    def add(self, estimation_particles: EstimatedParticle) -> None:
        self.__estimation_particles.append(estimation_particles)

    def track(self) -> None:
        """## パーティクルフィルタによるトラッキングを実行する"""
        for i, position_sample in enumerate(self.__correct_trajectory):
            estimation_particles = self.last_estimation_particles()
            estimation_particles.remove_by_floor_map()
            move_estimation_particles = estimation_particles.move(current_position=position_sample)
            move_estimation_particles.remove_by_floor_map()
            move_estimation_particles.remove_by_direction(step=position_sample.get_step())
            move_estimation_particles.resampling(step=position_sample.get_step(), mode="reversed")

            if i % 10 == 0:
                move_estimation_particles.resampling_by_weight()

            if (
                self.__coverage_position is None
                and i != 0
                and i % CONVERGENCE_JUDGEMENT_NUMBER == 0
                and estimation_particles.is_converged()
            ):
                print("収束しました")  # noqa: T201
                print(i)  # noqa: T201
                self.__coverage_count = i
                self.__coverage_position = move_estimation_particles.estimate_position()

            self.add(move_estimation_particles)

    def __iter__(self) -> Iterator[EstimatedParticle]:
        return iter(self.__estimation_particles)

    def __len__(self) -> int:
        return len(self.__estimation_particles)

    def __getitem__(self, index: int) -> EstimatedParticle:
        return self.__estimation_particles[index]
