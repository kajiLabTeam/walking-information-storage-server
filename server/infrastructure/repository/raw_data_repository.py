from abc import ABCMeta, abstractmethod

from domain.repository_impl.raw_data_repository_impl import \
    RawDataRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class RawDataRepository(RawDataRepositoryImpl):
    def save(
        self, conn: connection, realtime_walking_sample_id: str, raw_data_file: bytes
    ) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO raw_data (id, realtime_walking_sample_id, data) VALUES (%s, %s, %s)",
                    (str(ulid), realtime_walking_sample_id, raw_data_file),
                )

                # TODO : ファイルの保存処理を追加する
