from abc import ABCMeta, abstractmethod
from typing import Any

from psycopg2.extensions import connection


class TrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, pedestrian_id: str) -> None:
        pass


class RealtimeTrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, pedestrian_id: str) -> None:
        pass


class ModifiedTrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, pedestrian_id: str) -> None:
        pass
