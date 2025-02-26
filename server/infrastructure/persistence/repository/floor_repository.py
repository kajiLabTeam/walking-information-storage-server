from domain.repository_impl import (
    FloorInformationRepositoryImpl,
    FloorRepositoryImpl,
)
from domain.repository_impl.dto.infrastructure_dto import (
    FloorInformationDto,
    FloorRepositoryDto,
)
from infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
)
from psycopg2 import Error as psycopg2Error
from psycopg2.extensions import connection
from ulid import ULID


class FloorRepository(FloorRepositoryImpl):
    def save(
        self,
        conn: connection,
        name: str,
        level: int,
        building_id: str,
    ) -> FloorRepositoryDto:
        with conn:
            try:
                with conn.cursor() as cursor:
                    ulid = str(ULID())
                    cursor.execute(
                        "INSERT INTO floors (id, floor_name, building_id) "
                        "VALUES (%s, %s, %s) RETURNING id",
                        (
                            ulid,
                            name,
                            building_id,
                        ),
                    )

                    return FloorRepositoryDto(
                        id=ulid,
                        name=name,
                        level=level,
                        building_id=building_id,
                    )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.FLOOR_DB_ERROR,
                    detail="Error occurred in floor database",
                    status_code=500,
                ) from e

    def find_for_id(
        self,
        conn: connection,
        floor_id: str,
    ) -> FloorRepositoryDto | None:
        with conn, conn.cursor() as cursor:
            try:
                # クエリを実行
                cursor.execute(
                    "SELECT name, level, building_id FROM floors WHERE id = %s",
                    (floor_id,),
                )
                result = cursor.fetchone()

                if result is None:
                    return None

                # クエリ結果からデータを取得
                floor_name, level, building_id = result

                return FloorRepositoryDto(
                    id=floor_id,
                    name=floor_name,
                    level=level,
                    building_id=building_id,
                )

            except psycopg2Error as db_error:  # psycopg2のエラーを捕捉
                raise InfrastructureError(
                    InfrastructureErrorType.FLOOR_DB_ERROR,
                    detail="Database query failed.",
                    status_code=500,
                ) from db_error

            except Exception as e:  # 他の予期しないエラーを捕捉
                raise InfrastructureError(
                    InfrastructureErrorType.UNKNOWN_ERROR,
                    detail="An unexpected error occurred.",
                    status_code=500,
                ) from e

    def update(
        self,
        conn: connection,
        floor_id: str,
    ) -> None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "UPDATE floors SET floor_name = %s WHERE id = %s",
                    (floor_id),
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.FLOOR_DB_ERROR,
                    detail="Error occurred in floor database",
                    status_code=500,
                ) from e


class FloorInformationRepository(FloorInformationRepositoryImpl):
    def save(
        self,
        conn: connection,
        floor_id: str,
    ) -> FloorInformationDto:
        with conn, conn.cursor() as cursor:
            try:
                floor_information_id = str(ULID())
                cursor.execute(
                    "INSERT INTO floor_information (id, floor_id) VALUES (%s, %s) RETURNING id",
                    (
                        floor_information_id,
                        floor_id,
                    ),
                )

                return FloorInformationDto(
                    id=floor_information_id,
                    floor_id=floor_id,
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.FLOOR_DB_ERROR,
                    detail="Error occurred in floor database",
                    status_code=500,
                ) from e

    def find_for_id(
        self,
        conn: connection,
        floor_information_id: str,
    ) -> FloorInformationDto | None:
        with conn, conn.cursor() as cursor:
            cursor.execute(
                "SELECT floor_id FROM floor_information WHERE id = %s",
                (floor_information_id,),
            )

            result = cursor.fetchone()
            if result is None:
                return None
            floor_id = result[0]

            return FloorInformationDto(
                id=floor_information_id,
                floor_id=floor_id,
            )

    def find_latest(
        self,
        conn: connection,
    ) -> FloorInformationDto | None:
        with conn, conn.cursor() as cursor:
            try:
                cursor.execute(
                    "SELECT id, floor_id FROM floor_information ORDER BY created_at DESC LIMIT 1",
                )

                result = cursor.fetchone()
                if result is None:
                    return None
                floor_information_id = result[0]
                floor_id = result[1]

                return FloorInformationDto(
                    id=floor_information_id,
                    floor_id=floor_id,
                )

            except Exception as e:
                raise InfrastructureError(
                    InfrastructureErrorType.FLOOR_INFORMATION_DB_ERROR,
                    detail="Error occurred in floor database",
                    status_code=500,
                ) from e
