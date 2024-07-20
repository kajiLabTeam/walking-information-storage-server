from abc import ABCMeta, abstractmethod

from domain.repository_impl.floor_map_repository_impl import (
    FloorMapImageRepositoryImpl, FloorMapRepositoryImpl)
from psycopg2.extensions import connection
from ulid import ULID


class FloorMapRepository(FloorMapRepositoryImpl):

    def save(self, conn: connection) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute("INSERT INTO floor_map (id) VALUES (%s)", (str(ulid)))


class FloorMapImageRepository(FloorMapImageRepositoryImpl):

    def save(self, conn: connection, floor_map_id: str, floor_map_image: bytes) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floor_map_image (id, floor_map_id) VALUES (%s, %s, %s)",
                    (floor_map_id, floor_map_image),
                )
                # TODO : 画像の保存処理を追加する

    def find_for_floor_map_id(self, conn: connection, floor_map_id: str) -> bytes:
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

                return bytes
