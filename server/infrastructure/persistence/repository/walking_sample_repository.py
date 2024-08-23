from domain.models.estimated_position.estimated_position import EstimatedPosition
from domain.models.particle.particle import Particle
from domain.models.particle_collection.particle_collection import ParticleCollection
from domain.repository_impl.dto.infrastructure_dto import WalkingSampleRepositoryDto
from domain.repository_impl.walking_sample_repository_impl import (
    EstimatedPositionRepositoryImpl,
    ParticleRepositoryImpl,
    WalkingSampleRepositoryImpl,
)
from infrastructure.errors.infrastructure_error import (
    InfrastructureError,
    InfrastructureErrorType,
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
    ) -> WalkingSampleRepositoryDto:
        with conn:
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

                return WalkingSampleRepositoryDto(
                    walking_sample_id=walking_sample_id,
                    is_converged=is_converged,
                    trajectory_id=trajectory_id,
                    walking_information_id=walking_information_id,
                )

    def find_latest_for_trajectory_id(
        self, conn: connection, trajectory_id: str
    ) -> WalkingSampleRepositoryDto:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, is_converged, trajectory_id, walking_information_id FROM walking_samples WHERE trajectory_id = %s ORDER BY created_at DESC LIMIT 1",
                    (trajectory_id,),
                )

                result = cursor.fetchone()
                if result is not None:
                    walking_sample_id = result[0]
                    is_converged = result[1]
                    trajectory_id = result[2]
                    walking_information_id = result[3]
                else:
                    raise InfrastructureError(
                        InfrastructureErrorType.NOT_FOUND_WALKING_SAMPLE,
                        message="Walking sample not found",
                    )

                return WalkingSampleRepositoryDto(
                    walking_sample_id=walking_sample_id,
                    is_converged=is_converged,
                    trajectory_id=trajectory_id,
                    walking_information_id=walking_information_id,
                )


class ParticleRepository(ParticleRepositoryImpl):
    def save_all(
        self,
        conn: connection,
        walking_sample_id: str,
        particle_collection: ParticleCollection,
    ) -> None:
        with conn:
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
        with conn:
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
        with conn:
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
        with conn:
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
