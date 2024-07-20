from abc import ABCMeta, abstractmethod
from typing import Any

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition
from psycopg2.extensions import connection


class RealtimeCoordinateRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        realtime_walking_sample_id: str,
        estimated_position: EstimatedPosition,
    ) -> None:
        pass


class ModifiedCoordinateRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, estimated_position: EstimatedPosition) -> None:
        pass
