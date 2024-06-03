from typing import List, Optional, Tuple

from config.const.amount import CONVERGENCE_JUDGEMENT_NUMBER
from domain.estimated_particle.estimated_particle import (
    EstimatedParticle, EstimatedParticleFactory)
from domain.estimated_position.estimated_position import EstimatedPosition
from domain.floor_map.floor_map import FloorMap
from domain.walking_parameter.walking_parameter import WalkingParameter
from domain.walking_parameter_collection.walking_parameter_collection import \
    WalkingParameterCollection
from utils.angle import reverse_angle


class TrackingParticle:
    _instance = None

    def __new__(cls, floor_map: FloorMap) -> "TrackingParticle":
        if cls._instance is None:
            cls._instance = super(TrackingParticle, cls).__new__(cls)
            cls._instance.__init__(floor_map)
        return cls._instance

    def __init__(self, floor_map: FloorMap) -> None:
        if hasattr(self, "_initialized") and self._initialized:
            return
        self.__floor_map = floor_map
        self.__tracking_count = 0
        self.__coverage_count = 0
        self.__coverage_position: Optional[EstimatedPosition] = None
        self.__estimation_particles: List[EstimatedParticle] = []
        self.__walking_parameter_collection = WalkingParameterCollection()
        self._initialized = True

    def reset(self) -> None:
        self.__tracking_count = 0
        self.__coverage_count = 0
        self.__coverage_position = None
        self.__estimation_particles = []
        self.__walking_parameter_collection = WalkingParameterCollection()

    @classmethod
    def reset_instance(cls, floor_map: FloorMap) -> None:
        cls._instance = None
        cls._instance = cls(floor_map)

    def get_tracking_count(self) -> int:
        return self.__tracking_count

    def get_coverage_count(self) -> int:
        return self.__coverage_count

    def get_estimation_particles(self) -> List[EstimatedParticle]:
        return self.__estimation_particles

    def get_walking_parameter_reverse(self, index: int) -> List[WalkingParameter]:
        walking_positions = [
            wpc.reverse() for wpc in self.__walking_parameter_collection[:index]
        ]
        walking_positions.reverse()
        return walking_positions

    def get_coverage_position(self) -> Optional[Tuple[EstimatedPosition, int]]:
        if self.__coverage_position is None:
            return None

        return (
            EstimatedPosition(
                x=self.__coverage_position.get_x(),
                y=self.__coverage_position.get_y(),
                direction=reverse_angle(self.__coverage_position.get_direction()),
            ),
            self.__coverage_count,
        )

    def set_estimation_particles(
        self, estimation_particles: List[EstimatedParticle]
    ) -> None:
        self.__estimation_particles = estimation_particles

    def last_estimation_particles(self) -> EstimatedParticle:
        return self.__estimation_particles[-1]

    def last_walking_parameter(self) -> WalkingParameter:
        return self.__walking_parameter_collection[-1]

    def last_estimated_position(self) -> EstimatedPosition:
        return self.last_estimation_particles().estimate_position()

    def reverse(self) -> None:
        self.__estimation_particles.reverse()

    def add(self, estimation_particles: EstimatedParticle) -> None:
        self.__estimation_particles.append(estimation_particles)

    def track(self, walking_parameter: WalkingParameter) -> None:
        if self.__estimation_particles == []:
            estimated_particle = EstimatedParticleFactory().create(
                floor_map=self.__floor_map, initial_walking_parameter=walking_parameter
            )
            self.add(estimated_particle)
            self.__walking_parameter_collection.add(walking_parameter)
            return
        estimation_particles = self.last_estimation_particles()
        estimation_particles.remove_by_floor_map()
        move_estimation_particles = estimation_particles.move(
            current_walking_parameter=walking_parameter
        )
        move_estimation_particles.remove_by_floor_map()
        move_estimation_particles.remove_by_direction(
            step=walking_parameter.get_stride()
        )
        move_estimation_particles.update_weight()
        move_estimation_particles.resampling(step=walking_parameter.get_stride())

        if (
            self.__coverage_position is None
            and self.__tracking_count != 0
            and self.__tracking_count % CONVERGENCE_JUDGEMENT_NUMBER == 0
            and estimation_particles.is_converged()
        ):
            print("収束地点しました")
            self.__coverage_count = self.__tracking_count
            self.__coverage_position = move_estimation_particles.estimate_position()

        self.add(move_estimation_particles)
        self.__walking_parameter_collection.add(walking_parameter)
        self.__tracking_count += 1

    def __iter__(self):
        return iter(self.__estimation_particles)

    def __len__(self):
        return len(self.__estimation_particles)

    def __getitem__(self, index):
        return self.__estimation_particles[index]
