from abc import ABCMeta, abstractmethod
from typing import Optional

from psycopg2.extensions import connection


class TrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self, conn: connection, is_walking: bool, floor_id: str, pedestrian_id: str
    ) -> str:
        pass

    @abstractmethod
    def find_for_id(self, conn: connection, trajectory_id: str) -> Optional[str]:
        pass

    @abstractmethod
    def update(self, conn: connection, is_walking: bool, trajectory_id: str) -> None:
        pass
