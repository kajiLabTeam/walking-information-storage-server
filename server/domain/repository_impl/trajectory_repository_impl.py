from abc import ABCMeta, abstractmethod
from typing import Dict

from psycopg2.extensions import connection


class TrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, pedestrian_id: str, floor_map_id: str) -> str:
        pass


class RealtimeTrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, trajectory_id: str) -> None:
        pass

    @abstractmethod
    def find_for_trajectory_id(
        self, conn: connection, trajectory_id: str
    ) -> Dict[str, str]:
        pass


class ModifiedTrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, trajectory_id: str) -> None:
        pass
