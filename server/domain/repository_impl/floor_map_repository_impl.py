from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection


class FloorMapRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection) -> None:
        pass


class FloorMapImageRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, pedestrian_id: str) -> None:
        pass

    @abstractmethod
    def find_for_floor_map_id(self, conn: connection, floor_map_id: str) -> bytes:
        pass
