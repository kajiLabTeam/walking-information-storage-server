from abc import ABCMeta, abstractmethod

from domain.repository_impl.pedestrian_repository_impl import \
    PedestrianRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class PedestrianRepository(PedestrianRepositoryImpl):
    def save(self, conn: connection) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute("INSERT INTO pedestrians (id) VALUES (%s)", (str(ulid)))
