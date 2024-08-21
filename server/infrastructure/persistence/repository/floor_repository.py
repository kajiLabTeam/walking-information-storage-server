from domain.repository_impl.dto.infrastructure_dto import (
    FloorInformationDto,
    FloorMapRepositoryDto,
    FloorRepositoryDto,
)
from domain.repository_impl.floor_repository_impl import (
    FloorInformationRepositoryImpl,
    FloorMapRepositoryImpl,
    FloorRepositoryImpl,
)
from infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
)
from psycopg2.extensions import connection
from ulid import ULID


class FloorRepository(FloorRepositoryImpl):
    def save(
        self, conn: connection, floor_name: str, building_id
    ) -> FloorRepositoryDto:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floors (id, floor_name, building_id) VALUES (%s, %s, %s) RETURNING id",
                    (str(ulid), floor_name, building_id),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_id = result[0]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR,
                        message="Floor not found",
                    )

                return FloorRepositoryDto(
                    floor_id=floor_id, floor_name=floor_name, building_id=building_id
                )

    def find_for_id(self, conn: connection, floor_id: str) -> FloorRepositoryDto:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT floor_name, building_id FROM floors WHERE id = %s",
                    (floor_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_name = result[0]
                    building_id = result[1]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR,
                        message="Floor not found",
                    )

                return FloorRepositoryDto(
                    floor_id=floor_id, floor_name=floor_name, building_id=building_id
                )

    def update(self, conn: connection, floor_id: str) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE floors SET floor_name = %s WHERE id = %s",
                    (floor_id),
                )


class FloorInformationRepository(FloorInformationRepositoryImpl):
    def save(self, conn: connection, floor_id: str) -> FloorInformationDto:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floor_information (id, floor_id) VALUES (%s, %s) RETURNING id",
                    (str(ulid), floor_id),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_information_id = result[0]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR_INFORMATION,
                        message="Floor information not found",
                    )

                return FloorInformationDto(
                    floor_information_id=floor_information_id, floor_id=floor_id
                )

    def find_for_id(
        self, conn: connection, floor_information_id: str
    ) -> FloorInformationDto:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT floor_id FROM floor_information WHERE id = %s",
                    (floor_information_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_id = result[0]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR_INFORMATION,
                        message="Floor information not found",
                    )

                return FloorInformationDto(
                    floor_information_id=floor_information_id, floor_id=floor_id
                )

    def find_latest(self, conn: connection) -> FloorInformationDto:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, floor_id FROM floor_information ORDER BY created_at DESC LIMIT 1"
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_information_id = result[0]
                    floor_id = result[1]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR_INFORMATION,
                        message="Floor information not found",
                    )

                return FloorInformationDto(
                    floor_information_id=floor_information_id, floor_id=floor_id
                )


class FloorMapRepository(FloorMapRepositoryImpl):
    def save(
        self, conn: connection, floor_information_id: str, floor_map: bytes
    ) -> FloorMapRepositoryDto:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO floor_maps (id, floor_information_id, floor_map) VALUES (%s, %s, %s) RETURNING id",
                    (str(ulid), floor_information_id, floor_map),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_map_id = result[0]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR_MAP,
                        message="Floor map not found",
                    )

                return FloorMapRepositoryDto(
                    floor_map_id=floor_map_id, floor_information_id=floor_information_id
                )

    def find_for_floor_information_id(
        self, conn: connection, floor_information_id: str
    ) -> FloorMapRepositoryDto:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM floor_maps WHERE floor_information_id = %s",
                    (floor_information_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    floor_id = result[0]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_FLOOR_MAP,
                        message="Floor map not found",
                    )

                return FloorMapRepositoryDto(
                    floor_map_id=floor_id, floor_information_id=floor_information_id
                )
