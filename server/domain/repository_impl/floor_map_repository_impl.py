from abc import ABCMeta, abstractmethod
from typing import Optional

from psycopg2.extensions import connection


class FloorMapRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection) -> None:
        pass


class FloorMapImageRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, floor_map_id: str, floor_map_image: bytes) -> str:
        pass

    @abstractmethod
    def find_for_floor_map_id(
        self, conn: connection, floor_map_id: str
    ) -> Optional[str]:
        pass
