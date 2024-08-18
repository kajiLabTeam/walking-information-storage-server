from typing import Optional

from domain.models.estimated_position.estimated_position import EstimatedPosition
from domain.models.particle.particle import Particle
from domain.models.particle_collection.particle_collection import ParticleCollection
from domain.repository_impl.walking_sample_repository_impl import (
    EstimatedPositionRepositoryImpl,
    ParticleRepositoryImpl,
    WalkingSampleRepositoryImpl,
)
from psycopg2.extensions import connection
from ulid import ULID


class WalkingSampleRepository(WalkingSampleRepositoryImpl):
    def save(
        self,
        conn: connection,
        is_converged: bool,
        trajectory_id: str,
        walking_information_id: str,
    ) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                walking_sample_id = str(ULID())
                cursor.execute(
                    "INSERT INTO walking_samples (id, is_converged, trajectory_id, walking_information_id) VALUES (%s, %s, %s, %s)",
                    (
                        walking_sample_id,
                        is_converged,
                        trajectory_id,
                        walking_information_id,
                    ),
                )

                return walking_sample_id

    def find_latest_id_for_trajectory_id(
        self, conn: connection, trajectory_id: str
    ) -> Optional[str]:
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM walking_samples WHERE trajectory_id = %s ORDER BY created_at DESC LIMIT 1",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    walking_sample_id = result[0]
                else:
                    return None

                return walking_sample_id


class ParticleRepository(ParticleRepositoryImpl):
    def save_all(
        self,
        conn: connection,
        walking_sample_id: str,
        particle_collection: ParticleCollection,
    ) -> None:
        with conn as conn:
            with conn.cursor() as cursor:
                for particle in particle_collection.get_particles():
                    particle_id = str(ULID())
                    cursor.execute(
                        "INSERT INTO particles (id, x, y, weight, direction, walking_sample_id) VALUES (%s, %s, %s, %s, %s, %s)",
                        (
                            particle_id,
                            particle.get_x(),
                            particle.get_y(),
                            particle.get_weight(),
                            particle.get_direction(),
                            walking_sample_id,
                        ),
                    )

    def find_for_walking_sample_id(
        self, conn: connection, walking_sample_id: str
    ) -> ParticleCollection:
        particle_collection = ParticleCollection()
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT x, y, weight, direction FROM particles WHERE walking_sample_id = %s",
                    (walking_sample_id,),
                )
                for x, y, weight, direction in cursor.fetchall():
                    particle = Particle(x, y, weight, direction)
                    particle_collection.add(particle=particle)

        return particle_collection

    def find_latest_for_walking_sample_id(
        self, conn: connection, walking_sample_id: str
    ) -> ParticleCollection:
        particle_collection = ParticleCollection()
        with conn as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT x, y, weight, direction FROM particles WHERE walking_sample_id = %s ORDER BY created_at DESC LIMIT 1",
                    (walking_sample_id,),
                )
                for x, y, weight, direction in cursor.fetchall():
                    particle = Particle(x, y, weight, direction)
                    particle_collection.add(particle=particle)

        return particle_collection


class EstimatedPositionRepository(EstimatedPositionRepositoryImpl):
    def save(
        self,
        conn: connection,
        estimated_position: EstimatedPosition,
        walking_sample_id: str,
    ) -> str:
        with conn as conn:
            with conn.cursor() as cursor:
                estimated_position_id = str(ULID())
                cursor.execute(
                    "INSERT INTO estimated_positions (id, x, y, direction, walking_sample_id) VALUES (%s, %s, %s, %s, %s)",
                    (
                        estimated_position_id,
                        estimated_position.get_x(),
                        estimated_position.get_y(),
                        estimated_position.get_direction(),
                        walking_sample_id,
                    ),
                )

                return estimated_position_id
