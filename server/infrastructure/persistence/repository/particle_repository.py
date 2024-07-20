from typing import Any

from domain.models.estimated_position.estimated_position import \
    EstimatedPosition
from domain.models.particle.particle import Particle
from domain.models.particle_collection.particle_collection import \
    ParticleCollection
from domain.repository_impl.particle_repository_impl import \
    ParticleRepositoryImpl
from psycopg2.extensions import connection
from ulid import ULID


class ParticleRepository(ParticleRepositoryImpl):
    def save_all(
        self,
        conn: connection,
        realtime_walking_sample_id: str,
        particle_collection: ParticleCollection,
    ) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                for particle in particle_collection.get_particles():
                    ulid = ULID()
                    cursor.execute(
                        "INSERT INTO particle (id, x, y, weight, direction, realtime_walking_sample_id) VALUES (%s, %s, %s, %s, %s, %s)",
                        (
                            str(ulid),
                            particle.get_x(),
                            particle.get_y(),
                            particle.get_weight(),
                            particle.get_direction(),
                            realtime_walking_sample_id,
                        ),
                    )

    def find_for_realtime_walking_sample_id(
        self, conn: connection, realtime_walking_sample_id: str
    ) -> ParticleCollection:
        particle_collection = ParticleCollection()
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT x, y, weight, direction FROM particle WHERE realtime_walking_sample_id = %s",
                    (realtime_walking_sample_id,),
                )
                for x, y, weight, direction in cursor.fetchall():
                    particle = Particle(x, y, weight, direction)
                    particle_collection.add(particle=particle)

        return particle_collection
