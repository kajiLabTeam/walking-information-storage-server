from abc import ABCMeta, abstractmethod
from typing import Any

from psycopg2.extensions import connection

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition


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
