from domain.repository_impl.raw_data_repository_impl import \
    RawDataRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class RawDataRepository(RawDataRepositoryImpl):
    def save(
        self, conn: connection, realtime_walking_sample_id: str, raw_data_file: bytes
    ) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO raw_data (id, realtime_walking_sample_id, data) VALUES (%s, %s, %s) RETURNING id",
                    (str(ulid), realtime_walking_sample_id, raw_data_file),
                )

                result = cursor.fetchone()
                if result is not None:
                    raw_data_id = result[0]
                else:
                    raise ValueError("Failed to save raw data")

                return raw_data_id
