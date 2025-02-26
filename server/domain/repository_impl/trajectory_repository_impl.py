from abc import ABCMeta, abstractmethod

from domain.repository_impl.dto.infrastructure_dto import TrajectoryRepositoryDto
from psycopg2.extensions import connection

from server.domain.repository_impl.dto import (
    CorrectPositionRepositoryDto,
    EstimatedPositionRepositoryDto,
)


class TrajectoryRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        is_walking: bool,
        pedestrian_id: str,
        floor_information_id: str,
    ) -> TrajectoryRepositoryDto:
        pass

    @abstractmethod
    def find_for_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> TrajectoryRepositoryDto | None:
        pass

    @abstractmethod
    def update(
        self,
        conn: connection,
        is_walking: bool,
        trajectory_id: str,
    ) -> None:
        pass


class CorrectPositionRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        x: int,
        y: int,
        direction: int,
        trajectory_id: str,
    ) -> None:
        pass

    @abstractmethod
    def find_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> CorrectPositionRepositoryDto | None:
        pass


class EstimatedPositionRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        x: int,
        y: int,
        direction: int,
        is_converged: bool,
        trajectory_id: str,
    ) -> EstimatedPositionRepositoryDto | None:
        pass

    @abstractmethod
    def find_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> EstimatedPositionRepositoryDto | None:
        pass
