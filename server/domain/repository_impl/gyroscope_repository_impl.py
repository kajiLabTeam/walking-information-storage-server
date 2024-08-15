from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection


class GyroscopeRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(self, conn: connection, realtime_walking_sample_id: str) -> str:
        pass
