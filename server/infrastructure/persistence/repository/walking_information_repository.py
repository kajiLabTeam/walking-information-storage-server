from infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
)
from psycopg2.extensions import connection
from ulid import ULID

from server.domain.repository_impl import (
    WalkingInformationRepositoryImpl,
)
from server.domain.repository_impl.dto.infrastructure_dto import (
    WalkingInformationRepositoryDto,
)


class WalkingInformationRepository(WalkingInformationRepositoryImpl):
    def save(
        self,
        conn: connection,
        pedestrian_id: str,
    ) -> WalkingInformationRepositoryDto:
        with conn, conn.cursor() as cursor:
            try:
                walking_information_id = str(ULID())

                cursor.execute(
                    ("INSERT INTO walking_information (id, pedestrian_id) VALUES (%s, %s)"),
                    (
                        (walking_information_id),
                        pedestrian_id,
                    ),
                )

                return WalkingInformationRepositoryDto(
                    id=walking_information_id,
                    pedestrian_id=pedestrian_id,
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.WALKING_INFORMATION_DB_ERROR,
                    500,
                    "Failed to save walking information",
                ) from e

    def find_for_id(
        self,
        conn: connection,
        walking_information_id: str,
    ) -> WalkingInformationRepositoryDto | None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT * FROM walking_information WHERE id = %s",
                    (walking_information_id,),
                )
                record = cursor.fetchone()

                if record is None:
                    return None

                return WalkingInformationRepositoryDto(
                    id=record[0],
                    pedestrian_id=record[1],
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.WALKING_INFORMATION_DB_ERROR,
                    500,
                    "Failed to find walking information",
                ) from e

    def find_for_pedestrian_id(
        self,
        conn: connection,
        pedestrian_id: str,
    ) -> WalkingInformationRepositoryDto | None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT * FROM walking_information WHERE pedestrian_id = %s",
                    (pedestrian_id,),
                )
                record = cursor.fetchone()

                if record is None:
                    return None

                return WalkingInformationRepositoryDto(
                    id=record[0],
                    pedestrian_id=record[1],
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.WALKING_INFORMATION_DB_ERROR,
                    500,
                    "Failed to find walking information",
                ) from e
