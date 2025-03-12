from dataclasses import dataclass

from app.domain.dataclasses import Pose
from app.domain.models.walking_parameter.walking_parameter import WalkingParameter


@dataclass
class StartWalkingServiceDto:
    trajectory_id: str
    floor_information_id: str


@dataclass
class MovePedestrianServiceDto:
    pose: Pose
    walking_parameter: WalkingParameter


@dataclass
class FinishWalkingServiceDto:
    trajectory_id: str


@dataclass
class GenerateTrajectoryServiceDto:
    trajectory_id: str
    walking_information_id: str
    floor_information_id: str
    pedestrian_id: str
    is_walking: bool
