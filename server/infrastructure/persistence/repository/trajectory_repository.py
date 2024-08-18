from domain.repository_impl.trajectory_repository_impl import TrajectoryRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class TrajectoryRepository(TrajectoryRepositoryImpl):
    def save(self, conn: connection, is_walking: bool, floor_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                trajectory_id = str(ULID())
                cursor.execute(
                    "INSERT INTO trajectories (id, is_walking, floor_id) VALUES (%s, %s, %s)",
                    (
                        trajectory_id,
                        is_walking,
                        floor_id,
                    ),
                )

                return trajectory_id

    def find_for_id(self, conn: connection, trajectory_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, floor_id FROM trajectories WHERE id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    trajectory_id = result[0]
                    floor_map_id = result[1]
                else:
                    raise ValueError("Not found")

                return floor_map_id

    def update(self, conn: connection, is_walking: bool, trajectory_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE trajectories SET is_walking = %s WHERE id = %s",
                    (is_walking, trajectory_id),
                )
