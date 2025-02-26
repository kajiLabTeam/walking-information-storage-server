from abc import ABCMeta, abstractmethod

from domain.repository_impl.dto.infrastructure_dto import (
    CoordinateRepositoryDto,
)
from psycopg2.extensions import connection


class CoordinateRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        floor_name: str,
        building_id: str,
    ) -> CoordinateRepositoryDto:
        pass

    @abstractmethod
    def find_for_id(
        self,
        conn: connection,
        floor_id: str,
    ) -> CoordinateRepositoryDto | None:
        pass
