from dataclasses import dataclass


@dataclass
class GenerateTrajectoryServiceDto:
    trajectory_id: str
    walking_information_id: str
    floor_information_id: str
    pedestrian_id: str
    is_walking: bool
