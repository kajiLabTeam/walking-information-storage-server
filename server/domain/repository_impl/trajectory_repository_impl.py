from abc import ABCMeta, abstractmethod
from typing import Optional

from domain.repository_impl.dto.infrastructure_dto import TrajectoryRepositoryDto
from psycopg2.extensions import connection


class TrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        is_walking: bool,
        pedestrian_id: str,
        floor_information_id: str,
    ) -> str:
        pass

    @abstractmethod
    def find_for_id(
        self, conn: connection, trajectory_id: str
    ) -> Optional[TrajectoryRepositoryDto]:
        pass

    @abstractmethod
    def update(self, conn: connection, is_walking: bool, trajectory_id: str) -> None:
        pass
