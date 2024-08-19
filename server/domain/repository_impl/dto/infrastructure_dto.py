from dataclasses import dataclass


@dataclass
class TrajectoryRepositoryDto:
    trajectory_id: str
    floor_information_id: str
