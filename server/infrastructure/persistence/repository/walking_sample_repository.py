from domain.models.walking_parameter.walking_parameter import WalkingParameter
from domain.repository_impl.walking_sample_repository_impl import (
    ModifiedWalkingSampleRepositoryImpl,
    RealtimeWalkingSampleRepositoryImpl,
)
from psycopg2.extensions import connection
from ulid import ULID


class RealtimeWalkingSampleRepository(RealtimeWalkingSampleRepositoryImpl):
    def save(
        self, conn: connection, realtime_id: str, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO id, step, angle_changed, realtime_id VALUES (%s, %s, %s, %s)",
                    (
                        str(ulid),
                        walking_sample.get_step(),
                        walking_sample.get_angle_changed(),
                        realtime_id,
                    ),
                )
                return walking_sample

    def find_latest_for_realtime_id(
        self, conn: connection, realtime_id: str
    ) -> WalkingParameter:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, step, angle_changed FROM realtime_walking_sample WHERE realtime_id = %s ORDER BY created_at DESC LIMIT 1",
                    (realtime_id,),
                )
                row = cursor.fetchone()
                if row is None:
                    raise ValueError("Not found")

                return WalkingParameter(id=row[0], step=row[1], angle_changed=row[2])

    def find_latest_id_for_realtime_id(self, conn: connection, realtime_id: str) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM realtime_walking_sample WHERE realtime_id = %s ORDER BY created_at DESC LIMIT 1",
                    (realtime_id,),
                )
                row = cursor.fetchone()
                if row is None:
                    raise ValueError("Not found")

                return row[0]


class ModifiedWalkingSampleRepository(ModifiedWalkingSampleRepositoryImpl):
    def save(
        self, conn: connection, modified_id: str, walking_sample: WalkingParameter
    ) -> WalkingParameter:
        with conn as conn:
            with conn.cursor() as cursor:
                ulid = ULID()
                cursor.execute(
                    "INSERT INTO id, step, angle_changed, modified_id VALUES (%s, %s, %s, %s)",
                    (
                        str(ulid),
                        walking_sample.get_step(),
                        walking_sample.get_angle_changed(),
                        modified_id,
                    ),
                )

                return walking_sample
