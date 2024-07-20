from psycopg2.extensions import connection
from ulid import ULID

from domain.repository_impl.pedestrian_repository_impl import \
    PedestrianRepositoryImpl


class PedestrianRepository(PedestrianRepositoryImpl):
    def save(self, conn: connection) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute("INSERT INTO pedestrians (id) VALUES (%s)", (str(ulid)))
