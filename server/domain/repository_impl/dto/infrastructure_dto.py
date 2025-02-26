from dataclasses import dataclass


@dataclass
class PedestrianRepositoryDto:
    id: str


@dataclass
class BuildingRepositoryDto:
    id: str
    latitude: float
    longitude: float
    building_name: str


@dataclass
class FloorRepositoryDto:
    id: str
    name: str
    level: int
    building_id: str


@dataclass
class FloorInformationDto:
    id: str
    floor_id: str


@dataclass
class TrajectoryRepositoryDto:
    id: str
    is_walking: bool
    pedestrian_id: str
    floor_information_id: str


@dataclass
class WalkingInformationRepositoryDto:
    id: str
    pedestrian_id: str


@dataclass
class CoordinateRepositoryDto:
    coordinate_id: str
    x: int
    y: int
    is_walkable: bool
    floor_id: str


@dataclass
class CoordinateInformationRepositoryDto:
    id: str
    coordinate_id: str


@dataclass
class CorrectPositionRepositoryDto:
    id: str
    x: int
    y: int
    direction: int
    trajectory_id: str


@dataclass
class EstimatedPositionRepositoryDto:
    id: str
    x: int
    y: int
    direction: int
    is_converged: bool
    trajectory_id: str
    walking_information_id: str
