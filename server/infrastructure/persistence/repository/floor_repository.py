from typing import Optional

from domain.repository_impl.floor_repository_impl import (
    FloorMapRepositoryImpl,
    FloorRepositoryImpl,
)
from psycopg2.extensions import connection
from ulid import ULID


class FloorRepository(FloorRepositoryImpl):
    def save(self, conn: connection, floor_name) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                floor_id = str(ULID())
                cursor.execute(
                    "INSERT INTO floors (id, floor_name) VALUES (%s, %s)",
                    (floor_id, floor_name),
                )

                return floor_id

    def find_for_id(self, conn: connection, floor_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, floor_name FROM floors WHERE id = %s",
                    (floor_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_id = result[0]
                    # floor_name = result[1]
                else:
                    raise ValueError("Not found")

                return floor_id

    def update(self, conn: connection, floor_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE floors SET floor_name = %s WHERE id = %s",
                    (floor_id),
                )


class FloorMapRepository(FloorMapRepositoryImpl):
    def save(self, conn: connection, floor_id: str, floor_map: bytes) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floor_maps (id, floor_id) VALUES (%s, %s, %s) RETURNING id",
                    (str(ulid), floor_id, floor_map),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_map_image_id = result[0]
                else:
                    raise ValueError("Failed to save floor map image")

                return floor_map_image_id

    def find_for_floor_id(self, conn: connection, floor_id: str) -> Optional[str]:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM floor_maps WHERE floor_id = %s",
                    (floor_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_map_id = result[0]
                else:
                    return None

                return floor_map_id