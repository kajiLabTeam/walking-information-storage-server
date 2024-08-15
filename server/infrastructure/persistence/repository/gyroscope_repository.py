from domain.repository_impl.gyroscope_repository_impl import GyroscopeRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class GyroscopeRepository(GyroscopeRepositoryImpl):
    def save(
        self,
        conn: connection,
        realtime_walking_sample_id: str,
    ) -> str:
        with conn as conn:
            print("gyroscope_repository.py: save")
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO gyroscopes (id, realtime_walking_sample_id) VALUES (%s, %s) RETURNING id",
                    (str(ulid), realtime_walking_sample_id),
                )

                result = cursor.fetchone()
                if result is not None:
                    gyroscope_id = result[0]
                else:
                    raise ValueError("Failed to save raw data")

                return gyroscope_id
