from domain.repository_impl.raw_data_repository_impl import RawDataRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class RawDataRepository(RawDataRepositoryImpl):
    def save(
        self,
        conn: connection,
        realtime_walking_sample_id: str,
    ) -> str:
        print("RawDataRepository.save")
        print("realtime_walking_sample_id: ", realtime_walking_sample_id)

        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO raw_data (id, realtime_walking_sample_id) VALUES (%s, %s) RETURNING id",
                    (str(ulid), realtime_walking_sample_id),
                )

                result = cursor.fetchone()
                if result is not None:
                    raw_data_id = result[0]
                else:
                    raise ValueError("Failed to save raw data")

                return raw_data_id
