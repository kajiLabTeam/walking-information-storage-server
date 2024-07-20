from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection


class RawDataRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self, conn: connection, realtime_walking_sample_id: str, raw_data_file: bytes
    ) -> None:
        pass
