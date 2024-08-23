from domain.repository_impl.dto.infrastructure_dto import TrajectoryRepositoryDto
from domain.repository_impl.trajectory_repository_impl import TrajectoryRepositoryImpl
from infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
)
from psycopg2.extensions import connection
from ulid import ULID


class TrajectoryRepository(TrajectoryRepositoryImpl):
    def save(
        self,
        conn: connection,
        is_walking: bool,
        pedestrian_id: str,
        floor_information_id: str,
    ) -> TrajectoryRepositoryDto:
        with conn:
            with conn.cursor() as cursor:
                try:
                    trajectory_id = str(ULID())
                    cursor.execute(
                        "INSERT INTO trajectories (id, is_walking, pedestrian_id, floor_information_id) VALUES (%s, %s, %s, %s)",
                        (
                            trajectory_id,
                            is_walking,
                            pedestrian_id,
                            floor_information_id,
                        ),
                    )

                    return TrajectoryRepositoryDto(
                        trajectory_id=trajectory_id,
                        is_walking=is_walking,
                        pedestrian_id=pedestrian_id,
                        floor_information_id=floor_information_id,
                    )

                except Exception as e:
                    raise InfrastructureError(
                        InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                        "Failed to save trajectory",
                        500,
                    ) from e

    def find_for_id(
        self, conn: connection, trajectory_id: str
    ) -> TrajectoryRepositoryDto:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(
                        "SELECT is_walking, pedestrian_id, floor_information_id FROM trajectories WHERE id = %s",
                        (trajectory_id,),
                    )

                    result = cursor.fetchone()
                    if result is not None:
                        is_walking = result[0]
                        pedestrian_id = result[1]
                        floor_information_id = result[2]
                    else:
                        raise InfrastructureError(
                            InfrastructureErrorType.NOT_FOUND_TRAJECTORY,
                            message="Trajectory not found",
                            status_code=404,
                        )

                    return TrajectoryRepositoryDto(
                        trajectory_id=trajectory_id,
                        is_walking=is_walking,
                        pedestrian_id=pedestrian_id,
                        floor_information_id=floor_information_id,
                    )

                except Exception as e:
                    raise InfrastructureError(
                        InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                        "Failed to find trajectory",
                        500,
                    ) from e

    def update(self, conn: connection, is_walking: bool, trajectory_id: str) -> None:
        with conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute(
                        "UPDATE trajectories SET is_walking = %s WHERE id = %s",
                        (is_walking, trajectory_id),
                    )

                except Exception as e:
                    raise InfrastructureError(
                        InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                        "Failed to update trajectory",
                        500,
                    ) from e
