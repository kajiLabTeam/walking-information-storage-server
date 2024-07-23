from psycopg2.extensions import connection
from ulid import ULID

from domain.repository_impl.floor_map_repository_impl import (
    FloorMapImageRepositoryImpl,
    FloorMapRepositoryImpl,
)


class FloorMapRepository(FloorMapRepositoryImpl):
    def save(self, conn: connection) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute("INSERT INTO floor_map (id) VALUES (%s)", (str(ulid)))


class FloorMapImageRepository(FloorMapImageRepositoryImpl):
    def save(self, conn: connection, floor_map_id: str, floor_map_image: bytes) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floor_map_image (id, floor_map_id) VALUES (%s, %s, %s) RETURNING id",
                    (ulid, floor_map_id, floor_map_image),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_map_image_id = result[0]
                else:
                    raise ValueError("Failed to save floor map image")

                return floor_map_image_id

    def find_for_floor_map_id(self, conn: connection, floor_map_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM floor_map_image WHERE floor_map_id = %s",
                    (floor_map_id,),
                )

                # TODO : 画像の取得処理を追加する
                result = cursor.fetchone()
                if result is not None:
                    floor_map_image_id = result[0]
                else:
                    floor_map_image_id = None

                return floor_map_id
