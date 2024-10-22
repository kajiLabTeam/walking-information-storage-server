from dataclasses import (
    dataclass,
)

from domain.models.estimated_position.estimated_position import (
    EstimatedPosition,
)
from domain.models.walking_parameter.walking_parameter import (
    WalkingParameter,
)


@dataclass
class StartWalkingServiceDto:
    trajectory_id: str
    floor_information_id: str


@dataclass
class MovePedestrianServiceDto:
    estimated_position: EstimatedPosition
    walking_parameter: WalkingParameter


@dataclass
class FinishWalkingServiceDto:
    trajectory_id: str
