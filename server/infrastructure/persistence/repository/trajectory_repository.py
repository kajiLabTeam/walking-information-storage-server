from psycopg2.extensions import connection
from ulid import ULID

from server.domain.repository_impl import (
    CorrectPositionRepositoryImpl,
    EstimatedPositionRepositoryImpl,
    TrajectoryRepositoryImpl,
)
from server.domain.repository_impl.dto.infrastructure_dto import (
    CorrectPositionRepositoryDto,
    EstimatedPositionRepositoryDto,
    TrajectoryRepositoryDto,
)
from server.infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
)


class TrajectoryRepository(TrajectoryRepositoryImpl):
    def save(
        self,
        conn: connection,
        is_walking: bool,
        pedestrian_id: str,
        floor_information_id: str,
    ) -> TrajectoryRepositoryDto:
        with conn, conn.cursor() as cursor:
            try:
                trajectory_id = str(ULID())
                cursor.execute(
                    "INSERT INTO trajectories (id, is_walking, pedestrian_id, floor_information_id)"
                    "VALUES (%s, %s, %s, %s)",
                    (
                        trajectory_id,
                        is_walking,
                        pedestrian_id,
                        floor_information_id,
                    ),
                )

                return TrajectoryRepositoryDto(
                    id=trajectory_id,
                    is_walking=is_walking,
                    pedestrian_id=pedestrian_id,
                    floor_information_id=floor_information_id,
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                    500,
                    "Failed to save trajectory",
                ) from e

    def find_for_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> TrajectoryRepositoryDto | None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT is_walking, pedestrian_id, floor_information_id "
                    "FROM trajectories WHERE id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is None:
                    return None

                is_walking = result[0]
                pedestrian_id = result[1]
                floor_information_id = result[2]

                return TrajectoryRepositoryDto(
                    id=trajectory_id,
                    is_walking=is_walking,
                    pedestrian_id=pedestrian_id,
                    floor_information_id=floor_information_id,
                )
            except InfrastructureError as e:
                if e.type == InfrastructureErrorType.NOT_FOUND_TRAJECTORY:
                    raise
                raise InfrastructureError(
                    InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                    500,
                    "Failed to find trajectory",
                ) from e
            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                    500,
                    "Failed to find trajectory",
                ) from e

    def update(
        self,
        conn: connection,
        is_walking: bool,
        trajectory_id: str,
    ) -> None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "UPDATE trajectories SET is_walking = %s WHERE id = %s",
                    (
                        is_walking,
                        trajectory_id,
                    ),
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.TRAJECTORY_DB_ERROR,
                    500,
                    "Failed to update trajectory",
                ) from e


class CorrectPositionRepository(CorrectPositionRepositoryImpl):
    def save(
        self,
        conn: connection,
        x: int,
        y: int,
        direction: int,
        trajectory_id: str,
    ) -> None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO correct_positions (x, y, direction, trajectory_id)"
                    "VALUES (%s, %s, %s, %s)",
                    (
                        x,
                        y,
                        direction,
                        trajectory_id,
                    ),
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.CORRECT_POSITION_DB_ERROR,
                    500,
                    "Failed to save correct position",
                ) from e

    def find_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> CorrectPositionRepositoryDto | None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT id, x, y, direction FROM correct_positions WHERE trajectory_id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is None:
                    return None

                correct_position_id, x, y, direction = result

                return CorrectPositionRepositoryDto(
                    id=correct_position_id,
                    x=x,
                    y=y,
                    direction=direction,
                    trajectory_id=trajectory_id,
                )
            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.CORRECT_POSITION_DB_ERROR,
                    500,
                    "Failed to find correct position",
                ) from e


class EstimatedPositionRepository(EstimatedPositionRepositoryImpl):
    def save(
        self,
        conn: connection,
        x: int,
        y: int,
        direction: int,
        is_converged: bool,
        trajectory_id: str,
    ) -> None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO estimated_positions (x, y, direction, is_converged, trajectory_id)"
                    "VALUES (%s, %s, %s, %s, %s)",
                    (
                        x,
                        y,
                        direction,
                        is_converged,
                        trajectory_id,
                    ),
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.ESTIMATED_POSITION_DB_ERROR,
                    500,
                    "Failed to save estimated position",
                ) from e

    def find_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> EstimatedPositionRepositoryDto | None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT id, x, y, direction, is_converged, walking_information_id "
                    "FROM estimated_positions WHERE trajectory_id = %s",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is None:
                    return None

                estimated_position_id, x, y, direction, is_converged, walking_information_id = (
                    result
                )

                return EstimatedPositionRepositoryDto(
                    id=estimated_position_id,
                    x=x,
                    y=y,
                    direction=direction,
                    is_converged=is_converged,
                    trajectory_id=trajectory_id,
                    walking_information_id=walking_information_id,
                )
            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.ESTIMATED_POSITION_DB_ERROR,
                    500,
                    "Failed to find estimated position",
                ) from e
