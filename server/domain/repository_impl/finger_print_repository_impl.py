from abc import ABCMeta, abstractmethod
from typing import Any

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition
from psycopg2.extensions import connection


class FingerPrintRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass


class AccessPointRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass


class FingerPrintModelRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass
