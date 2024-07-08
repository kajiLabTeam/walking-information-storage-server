from psycopg2.extensions import connection


class WalkingSampleRepository:
    def find_by_id(
        self,
        conn: connection,
        walking_sample_id: str,
    ) -> str:
        with conn as conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT * FROM walking_samples WHERE id = %s", (spot_id,)
                        """,
                        (walking_sample_id),
                    )

                    inserted_data = cursor.fetchone()
                    walking_sample_id = inserted_data[0]

                    if inserted_data is None:
                        return None

                    return walking_sample_id
            except err as err:
                raise err

    def save(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> str:
        with conn as conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO walking_samples (id)
                        VALUES (%s)
                        RETURNING id
                        """,
                        (trajectory_id),
                    )

                    inserted_data = cursor.fetchone()
                    trajectory_id = inserted_data[0]

                    if inserted_data is None:
                        cursor.close()
                        return None

                    cursor.close()

                    return trajectory_id
            except err as err:
                raise err
