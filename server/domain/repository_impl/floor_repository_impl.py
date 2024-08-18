from abc import ABCMeta, abstractmethod
from typing import Optional

from psycopg2.extensions import connection


class FloorRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, floor_name: str) -> str:
        pass

    @abstractmethod
    def find_for_id(self, conn: connection, floor_id: str) -> str:
        pass

    @abstractmethod
    def update(self, conn: connection, floor_id: str) -> None:
        pass


class FloorMapRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, floor_id: str, floor_map: bytes) -> str:
        pass

    @abstractmethod
    def find_for_floor_id(self, conn: connection, floor_id: str) -> Optional[str]:
        pass


class FpModelRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, floor_id: str, fp_model: bytes) -> str:
        pass

    @abstractmethod
    def find_for_floor_id(self, conn: connection, floor_id: str) -> Optional[str]:
        pass


class AccessPointRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, floor_id: str, ap_mac: str) -> str:
        pass

    @abstractmethod
    def find_for_floor_id(self, conn: connection, floor_id: str) -> Optional[str]:
        pass
