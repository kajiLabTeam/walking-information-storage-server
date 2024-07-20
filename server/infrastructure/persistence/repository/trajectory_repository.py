from abc import ABCMeta, abstractmethod
from typing import Tuple

from domain.repository_impl.trajectory_repository_impl import (
    ModifiedTrajectoryRepositoryImpl, RealtimeTrajectoryRepositoryImpl,
    TrajectoryRepositoryImpl)
from psycopg2.extensions import connection
from ulid import ULID


class TrajectoryRepository(TrajectoryRepositoryImpl):
    def save(self, conn: connection, pedestrian_id: str, floor_map_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO trajectories (pedestrian_id, floor_map_id) VALUES (%s, %s) RETURNING id",
                    (pedestrian_id, floor_map_id),
                )

                result = cursor.fetchone()
                if result is not None:
                    trajectory_id = result[0]
                else:
                    raise ValueError("Not found")

                return trajectory_id


class RealtimeTrajectoryRepository(RealtimeTrajectoryRepositoryImpl):
    def save(self, conn: connection, trajectory_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO id, realtime_trajectories (trajectory_id) VALUES (%s, %s)",
                    (
                        ulid,
                        trajectory_id,
                    ),
                )

    def find_for_trajectory_id(
        self, conn: connection, trajectory_id: str
    ) -> Tuple[str, str]:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, trajectory_id FROM realtime_trajectories WHERE trajectory_id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    realtime_id = result[0]
                    trajectory_id = result[1]
                else:
                    raise ValueError("Not found")

                return realtime_id, trajectory_id


class ModifiedTrajectoryRepository(ModifiedTrajectoryRepositoryImpl):
    def save(self, conn: connection, trajectory_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO modified_trajectories (id, trajectory_id) VALUES (%s, %s)",
                    (
                        ulid,
                        trajectory_id,
                    ),
                )