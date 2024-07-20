from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition


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
    def save(
        self,
        conn: connection,
        modified_walking_sample_id: str,
        estimated_position: EstimatedPosition,
    ) -> None:
        pass
