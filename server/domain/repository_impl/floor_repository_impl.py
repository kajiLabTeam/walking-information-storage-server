from abc import ABCMeta, abstractmethod

from domain.repository_impl.dto.infrastructure_dto import (
    FloorInformationDto,
    FloorRepositoryDto,
)
from psycopg2.extensions import connection


class FloorRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        name: str,
        level: int,
        building_id: str,
    ) -> FloorRepositoryDto:
        pass

    @abstractmethod
    def find_for_id(
        self,
        conn: connection,
        floor_id: str,
    ) -> FloorRepositoryDto | None:
        pass

    @abstractmethod
    def update(
        self,
        conn: connection,
        floor_id: str,
    ) -> None:
        pass


class FloorInformationRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        floor_id: str,
    ) -> FloorInformationDto:
        pass

    @abstractmethod
    def find_for_id(
        self,
        conn: connection,
        floor_information_id: str,
    ) -> FloorInformationDto | None:
        pass

    @abstractmethod
    def find_latest(
        self,
        conn: connection,
    ) -> FloorInformationDto | None:
        pass
