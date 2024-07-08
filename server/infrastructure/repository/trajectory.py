from psycopg2.extensions import connection


class TrajectoryRepository:
    def save(
        self,
        conn: connection,
        id: str,
    ) -> str:
        with conn as conn:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO trajectories (id)
                        VALUES (%s)
                        RETURNING id
                        """,
                        (id),
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
