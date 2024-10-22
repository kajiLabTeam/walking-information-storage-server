from abc import (
    ABCMeta,
    abstractmethod,
)

from domain.models.estimated_position.estimated_position import (
    EstimatedPosition,
)
from domain.models.particle_collection.particle_collection import (
    ParticleCollection,
)
from domain.repository_impl.dto.infrastructure_dto import (
    WalkingSampleRepositoryDto,
)
from psycopg2.extensions import (
    connection,
)


class WalkingSampleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        is_converged: bool,
        trajectory_id: str,
        walking_information_id: str,
    ) -> WalkingSampleRepositoryDto:
        pass

    @abstractmethod
    def find_latest_for_trajectory_id(
        self,
        conn: connection,
        trajectory_id: str,
    ) -> WalkingSampleRepositoryDto:
        pass


class ParticleRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save_all(
        self,
        conn: connection,
        walking_sample_id: str,
        particle_collection: ParticleCollection,
    ) -> None:
        pass

    @abstractmethod
    def find_for_walking_sample_id(
        self,
        conn: connection,
        walking_sample_id: str,
    ) -> ParticleCollection:
        pass


class EstimatedPositionRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def save(
        self,
        conn: connection,
        estimated_position: EstimatedPosition,
        walking_sample_id: str,
    ) -> str:
        pass
