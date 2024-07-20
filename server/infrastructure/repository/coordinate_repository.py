from abc import ABCMeta, abstractmethod
from typing import Any

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition
from domain.repository_impl.coordinate_repository_impl import (
    ModifiedCoordinateRepositoryImpl, RealtimeCoordinateRepositoryImpl)
from psycopg2.extensions import connection
from ulid import ULID


class RealtimeCoordinateRepository(RealtimeCoordinateRepositoryImpl):
    def save(
        self,
        conn: connection,
        realtime_walking_sample_id: str,
        estimated_position: EstimatedPosition,
    ) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO realtime_coordinate (id, x, y, realtime_walking_sample_id) VALUES (%s, %s, %s, %s)",
                    (
                        str(ulid),
                        estimated_position.get_x(),
                        estimated_position.get_y(),
                        realtime_walking_sample_id,
                    ),
                )


class ModifiedCoordinateRepository(ModifiedCoordinateRepositoryImpl):
    def save(
        self,
        conn: connection,
        modified_walking_sample_id: str,
        estimated_position: EstimatedPosition,
    ) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO modified_coordinate (id, x, y, modified_walking_sample_id) VALUES (%s, %s, %s, %s)",
                    (
                        str(ulid),
                        estimated_position.get_x(),
                        estimated_position.get_y(),
                        modified_walking_sample_id,
                    ),
                )
