from domain.repository_impl.trajectory_repository_impl import (
    ModifiedTrajectoryRepositoryImpl,
    RealtimeTrajectoryRepositoryImpl,
    TrajectoryRepositoryImpl,
)
from psycopg2.extensions import connection
from ulid import ULID


class TrajectoryRepository(TrajectoryRepositoryImpl):
    def save(self, conn: connection, pedestrian_id: str, floor_map_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO trajectories (id, is_walking, pedestrian_id, floor_map_id) VALUES (%s, %s, %s, %s) RETURNING id",
                    (str(ulid), True, pedestrian_id, floor_map_id),
                )

                result = cursor.fetchone()
                if result is not None:
                    trajectory_id = result[0]
                else:
                    raise ValueError("Not found")

                return trajectory_id

    def find_for_id(self, conn: connection, trajectory_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, floor_map_id FROM trajectories WHERE id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    trajectory_id = result[0]
                    floor_map_id = result[1]
                else:
                    raise ValueError("Not found")

                return floor_map_id

    def update(self, conn: connection, trajectory_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE trajectories SET is_walking = %s WHERE id = %s",
                    (False, trajectory_id),
                )


class RealtimeTrajectoryRepository(RealtimeTrajectoryRepositoryImpl):
    def save(self, conn: connection, trajectory_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO realtime (id, trajectory_id) VALUES (%s, %s)",
                    (
                        str(ulid),
                        trajectory_id,
                    ),
                )

    def find_for_trajectory_id(self, conn: connection, trajectory_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, trajectory_id FROM realtime WHERE trajectory_id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    realtime_id = result[0]
                    trajectory_id = result[1]
                else:
                    raise ValueError("Not found")

                return realtime_id


class ModifiedTrajectoryRepository(ModifiedTrajectoryRepositoryImpl):
    def save(self, conn: connection, trajectory_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO modified (id, trajectory_id) VALUES (%s, %s)",
                    (
                        str(ulid),
                        trajectory_id,
                    ),
                )
